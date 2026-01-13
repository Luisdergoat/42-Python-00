def ft_harvest_total():
    """Calculate and print the total harvest over three days."""
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total_harvest = day1 + day2
    total_harvest = total_harvest + day3
    print(f"Total harvest: {total_harvest}")
    pass
