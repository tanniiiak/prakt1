"""
Эмулятор оболочки ОС. Этап 1: REPL.
Вариант №14.

Реализует минимальный прототип командной строки UNIX-подобной ОС:
- приглашение вида user@host:~$
- парсер команд по пробелам
- заглушки ls и cd
- обработка ошибок (неизвестная команда, неверные аргументы)
- команда exit
"""

import getpass
import socket


def get_prompt():
    """
    Формируем приглашение вида user@host:~$.
    Использует реальные данные ОС: имя пользователя и имя хоста.
    """
    user = getpass.getuser()
    host = socket.gethostname()
    return f"{user}@{host}:~$ "


def execute_command(command, args):
    """
    Выполняет одну команду.
    Возвращает строку 'exit', если нужно завершить работу эмулятора.
    Иначе возвращает None.
    """
    if command == "exit":
        print("Выход из эмулятора...")
        return "exit"

    elif command == "ls":
        # Заглушка ls. Принимает 0 или больше аргументов.
        print(f"Команда: {command}")
        if args:
            print(f"Аргументы: {args}")
        else:
            print("Аргументы: нет")

    elif command == "cd":
        # Заглушка cd. Должна принимать ровно 1 аргумент (путь).
        print(f"Команда: {command}")
        if len(args) == 0:
            print("Ошибка: cd требует один аргумент (путь)")
        elif len(args) > 1:
            print(f"Ошибка: cd принимает один аргумент, получено {len(args)}")
        else:
            print(f"Аргументы: {args}")

    else:
        print(f"Ошибка: команда '{command}' не найдена.")

    return None


def main():
    """Точка входа. Запускает REPL-цикл."""
    print("--- Запуск эмулятора оболочки (Вариант 14) ---")
    print("Введите 'exit' для выхода.\n")

    while True:
        try:
            user_input = input(get_prompt())

            # Пропускаем пустые строки (только пробелы/Enter)
            if not user_input.strip():
                continue

            # Парсер: разделяем по пробелам
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            # Выполняем команду
            result = execute_command(command, args)
            if result == "exit":
                break

        except KeyboardInterrupt:
            # Ctrl+C — корректный выход
            print("\nЗавершение работы (Ctrl+C).")
            break
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
