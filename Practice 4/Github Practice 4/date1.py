from datetime import datetime, timedelta

current_date = datetime.now()
result = current_date - timedelta(days=5)
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("5 days ago:", result.strftime("%Y-%m-%d"))