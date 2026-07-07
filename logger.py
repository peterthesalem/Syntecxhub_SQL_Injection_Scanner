from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/scan.log", "a") as logfile:
        logfile.write(f"[{timestamp}] {message}\n")
