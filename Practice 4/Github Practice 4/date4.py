from datetime import datetime

# Пример двух дат
date1 = datetime(2023, 10, 1, 12, 0, 0)
date2 = datetime(2023, 10, 2, 12, 0, 0)

difference = date2 - date1
seconds_diff = int(difference.total_seconds())

print(f"Difference in seconds: {seconds_diff}")