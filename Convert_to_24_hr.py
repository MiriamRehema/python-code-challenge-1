def convert_to_24_hour(hour, minute, period):
    #This is to show that the time is in a 12hr system
    if period == "am":
        if hour == 12:
            hour = 0
            #This shows that if the time is not in a 12hr system
    else:
        if hour != 12:
            hour += 12
    #should return in a 24hr system
    return "{:02d}{:02d}".format(hour, minute)
#example
print(convert_to_24_hour(8, 30, "am")) 
print(convert_to_24_hour(10,45, "pm")) 