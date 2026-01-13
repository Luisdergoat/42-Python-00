def ft_count_harvest_iterative():
    """Count days until harvest iteratively."""
    days = int(input("Days until harvest: "))
    for counter in range(1, days + 2):
        if (counter > days):
            print("Harvest time!")
        else:
            print(f"Day {counter}")
    pass
