

def convertSecondsSinceMidnight(secondsSinceMidnight):

    if secondsSinceMidnight < 0 or secondsSinceMidnight >= 86400:
        return "Invalid input"

    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60

    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    if hours == 0:
        hours = 12
    elif hours > 12:
        hours = hours - 12

    return f"{hours}:{minutes:02d}:{seconds:02d} {period}"

