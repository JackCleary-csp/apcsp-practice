minutes_available = int(input("Minutes available"))
breaks = int(input("Number of breaks: "))
break_minutes = int(input("Minutes per break: "))
lunch = int(input("Lunch break minutes: "))

work_minutes = minutes_available - (lunch + breaks)

print("locked in minutes: ", work_minutes)