def ft_water_reminder():
    """Remind user to water the plants based on days since last watering."""
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
    pass
