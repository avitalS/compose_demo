import sys
sys.path.insert(0, '/app')

from app import get_message, run_devops_task

def test_message():
    assert get_message() == "Hello from app"

def test_run_devops_task(capsys):
    run_devops_task()
    captured = capsys.readouterr()
    assert "DevOps task started successfully" in captured.out


