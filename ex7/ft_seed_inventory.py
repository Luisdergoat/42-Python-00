def ft_seed_inventory(seed, amount, type):
    """Print the inventory of seeds based on type."""
    test = 0
    if (type == "packets"):
        end_type = "packets available"
        test = 1
    if (type == "grams"):
        end_type = "grams total"
        test = 2
    if (type == "area"):
        end_type = "square meters"
        test = 3
    if (test == 0):
        print("Unknown unit type")
        return
    if (end_type == "square meters"):
        print(f"{seed.capitalize()} seeds: covers {amount} {end_type}")
        return
    print(f"{seed.capitalize()} seeds: {amount} {end_type}")
    pass
