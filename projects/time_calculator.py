def add_time(start, duration, start_day=''):
    # Separte the start into hours and minutes
    times = start.split()
    time = times[0].split(":")
    period = times[1]

    # Calculate 24-hour clock format
    if period == "PM" :
        hour = int(time[0]) + 12
        time[0] = str(hour)
    
    # Separate the duration into hours and minutes
    dur_time = duration.split(":")

    # Add hours and minutes
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])

    if new_minutes >= 60 :
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    days_add = 0
    if new_hour > 24 :
        days_add = new_hour // 24
        new_hour -= days_add * 24
    
    # Find AM and PM
    # Return to 12-hour clock format
    if new_hour > 0 and new_hour < 12 :
        period = "AM"
    elif new_hour == 12 :
        period = "PM"
    elif new_hour > 12 :
        period = "PM"
        new_hour -= 12
    else : # new_hour == 0
        period = "AM"
        new_hour += 12

    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""
    
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if start_day :
        weeks = days_add // 7
        i = week_days.index(start_day.lower().capitalize()) + (days_add - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time = str(new_hour) + ":" + (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + " " + period + day + days_later
    
    return new_time

print(add_time('11:43 PM', '24:20', 'tueSday'))
