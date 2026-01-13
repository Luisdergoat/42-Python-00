def ft_count_harvest_recursive(current=1, days=None):
    """Count days until harvest recursively."""
    if (days is None):
        days = int(input("Enter number of days until harvest: "))
    print(f"Day {current}")
    if (current >= days):
        print("Harvest time!")
        return
    ft_count_harvest_recursive(current + 1, days)
    pass
