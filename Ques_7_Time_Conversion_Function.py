def convertSecondsSinceMidnight(secondsSinceMidnight):
    # Check for valid input (must be within one day)
    if secondsSinceMidnight < 0 or secondsSinceMidnight >= 86400:
        return "Invalid input"

    # Convert total seconds into hours, minutes, and seconds
    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60

    # Determine AM or PM
    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    # Convert from 24-hour time to 12-hour time
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours = hours - 12

    # Return formatted time string
    return f"{hours}:{minutes:02d}:{seconds:02d} {period}"

print(convertSecondsSinceMidnight(1926))
