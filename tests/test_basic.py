
import subprocess
import sys
import os


def test_shell_launches():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(root, "startup.txt")
    
    if not os.path.exists(script_path):
        assert os.path.exists(os.path.join(root, "src", "shell.py"))
        return
    
    result = subprocess.run(
        [sys.executable, os.path.join(root, "src", "shell.py"),
         "--script", script_path],
        capture_output=True,
        text=True,
        timeout=10,
        cwd=root,
    )
    assert "Запуск эмулятора" in result.stdout