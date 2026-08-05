from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_time(timezone: str):
    try:
        current_time = datetime.now(
            ZoneInfo(timezone)
        )
        return current_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    except Exception:
        return "Invalid timezone"

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return str(e)