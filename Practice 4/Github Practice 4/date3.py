from datetime import datetime

now = datetime.now()
# Метод replace позволяет обнулить микросекунды
now_without_ms = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", now_without_ms)