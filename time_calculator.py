def get_days(days):
  if days == 1:
    return "(next day)"
  elif days > 1:
    return f"({days} days left)"

def add_time(start, duration, day = False):
  hours_in_a_day = 24
  hours_in_half_day = 12
  week_days = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
  ]

  days_later = 0
  hours, minus = start.split(":")
  minus, period = minus.split(" ")
  ending_hours , ending_minus = duration.split(":")

  hours = int(hours)
  minus = int(minus)
  ending_hours = int(ending_hours)
  ending_minus = int(ending_minus)
  period = period.strip().lower()

  total_hours = hours + ending_hours
  total_minus = minus + ending_minus

  if total_minus >= 60:
    total_hours += int(total_minus / 60)
    total_minus = int(total_minus % 60)

  if ending_hours or ending_minus:
    if period == "pm" and total_hours > hours_in_half_day:
      if total_hours % hours_in_a_day >= 1.0:
        days_later += 1

    if total_hours >= hours_in_half_day:
      hours_left = total_hours / hours_in_a_day
      days_later += int(hours_left)

    temp_hours = total_hours
    while True:
      if temp_hours < hours_in_half_day:
        break;
      if period == "pm":
        period = "am"
      else:
        period = "am"
        temp_hours -= hours_in_half_day

  remaining_hours = int(total_hours % hours_in_half_day) or hours + 1
  remaining_minus = int(total_minus % 60)

  new_time = f"{remaining_hours}:{remaining_minus} {period.upper()}"
  if day:
    day = day.strip().lower()
    selected_day = int((week_days.index(day) + days_later) % 7)
    current_day = week_days[selected_day]
    new_time += f"{current_day.title()} {get_days(days_later)}"
  else :
    new_time = " ".join((new_time, get_days(days_later)))
    
    return new_time