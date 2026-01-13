def ft_count_harvest_recursive(current, days):
    """Count days until harvest recursively."""
    if (current > days):
        print("Harvest time!")
        return
    else:
        print(f"Day {current}")
    ft_count_harvest_recursive(current + 1, days)
    pass
