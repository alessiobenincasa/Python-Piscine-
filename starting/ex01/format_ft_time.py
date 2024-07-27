import time
from datetime import datetime


current_time_seconds = time.time()


current_datetime = datetime.now()


print(f"Seconds since January 1, 1970: {current_time_seconds:.4f} or {current_time_seconds:.2e} in scientific notation")


formatted_date = current_datetime.strftime("%b %d %Y")
print(formatted_date)
