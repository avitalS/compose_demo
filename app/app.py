import os
from datetime import datetime

def get_message():
    return "Hello from app_homeWork"

def run_devops_task():
    # שליפת משתני סביבה
    user = os.getenv("USER_NAME", "Student")
    env = os.getenv("APP_ENV", "Dev")
    
    # יצירת חותמת זמן
    now = datetime.now().strftime("%H:%M:%S")
    
    # הדפסת הודעות הלוג
    print(f"[{now}] [ENV: {env}] Hello {user}!")
    print(f"[{now}] [ENV: {env}] DevOps task started successfully.")

if __name__ == "__main__":
    print(get_message())
    run_devops_task()
