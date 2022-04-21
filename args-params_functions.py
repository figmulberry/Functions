"""Arguments and Parameters"""
"""Positional Arguments"""
def describe_animal(animal_type, horse_name):
    """Display information about a horse"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {horse_name.title()}.")

describe_animal('horse', 'senior mustang')