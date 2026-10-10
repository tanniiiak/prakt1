"""
Эмулятор оболочки ОС. Вариант №14.
Этап 1: REPL.
Этап 2: конфигурация (CLI: --vfs и --script).
"""

import os
import getpass
import socket
import argparse
import json



def parse_args():
    """Парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Эмулятор оболочки ОС. Вариант №14."
    )
    parser.add_argument("--vfs", type=str, default=None,
                        help="Путь к файлу VFS (JSON)")
    parser.add_argument("--script", type=str, default=None,
                        help="Путь к стартовому скрипту")
    return parser.parse_args()



def load_vfs(path):
    """Загружает VFS из JSON. При ошибке — None."""
    if path is None:
        return None
    if not os.path.exists(path):
        print(f"Ошибка: файл VFS '{path}' не найден.")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Ошибка: неверный формат JSON в VFS: {e}")
        return None



def get_prompt():
    """Приглашение вида user@host:~$."""
    user = getpass.getuser()
    host = socket.gethostname()
    return f"{user}@{host}:~$ "



def execute_command(command, args, vfs):
    """Выполняет команду. Возвращает 'exit' для выхода."""
    if command == "exit":
        print("Выход из эмулятора...")
        return "exit"

    elif command == "ls":
        print(f"Команда: {command}")
        print(f"Аргументы: {args}" if args else "Аргументы: нет")

    elif command == "cd":
        print(f"Команда: {command}")
        if len(args) == 0:
            print("Ошибка: cd требует один аргумент (путь)")
        elif len(args) > 1:
            print(f"Ошибка: cd принимает один аргумент, получено {len(args)}")
        else:
            print(f"Аргументы: {args}")

    elif command == "vfs":
        if vfs is None:
            print("VFS не загружена.")
        else:
            print(json.dumps(vfs, ensure_ascii=False, indent=2))

    else:
        print(f"Ошибка: команда '{command}' не найдена.")

    return None


def run_interactive(vfs):
    """Интерактивный режим REPL."""
    print("Введите 'exit' для выхода.\n")
    while True:
        try:
            user_input = input(get_prompt())
            if not user_input.strip():
                continue
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]
            result = execute_command(command, args, vfs)
            if result == "exit":
                break
        except KeyboardInterrupt:
            print("\nЗавершение работы (Ctrl+C).")
            break


def run_script(script_path, vfs):
    """Запускает стартовый скрипт. Ошибочные строки пропускает."""
    if not os.path.exists(script_path):
        print(f"Ошибка: скрипт '{script_path}' не найден.")
        return

    try:
        with open(script_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка чтения скрипта: {e}")
        return

    print(f"Выполнение стартового скрипта: {script_path}")
    print("-" * 40)

    prompt = get_prompt()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Эхо: показываем приглашение + команду
        print(f"{prompt}{stripped}")

        parts = stripped.split()
        command = parts[0]
        args = parts[1:]

        result = execute_command(command, args, vfs)
        if result == "exit":
            break


def main():
    args = parse_args()

    print("--- Запуск эмулятора оболочки (Вариант 14) ---")
    print("Параметры запуска:")
    print(f"  VFS:    {args.vfs if args.vfs else '(не задан)'}")
    print(f"  Script: {args.script if args.script else '(не задан)'}")
    print()

    vfs = load_vfs(args.vfs)

    if args.script:
        run_script(args.script, vfs)
    else:
        run_interactive(vfs)


if __name__ == "__main__":
    main()