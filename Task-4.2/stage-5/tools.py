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


# print("Tools module loaded successfully.")
# print("Available tools:")
# a = get_current_time("Asia/Karachi")
# print("Current time in Asia/Karachi:", a)

# b = calculator("25 * 10")
# print("Result of 25 * 10:", b)