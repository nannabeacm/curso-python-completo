def introduce(hero: str, alias: str):
    print(f"I am {hero}, also known as {alias}.")


def calculate_force(mass: float, acceleration: float) -> float:
    force = mass * acceleration
    return force


def attack(villain: str):
    """
    Attack a villain using punches.

    Params:
        villain (str): Villain name.

    Returns:
        none
    """
    print(f"Punching {villain}!")


attack("Thanos")
attack("Joker")
attack("Trump")
attack("Sinestro")

introduce("Bruce Wayne", "Batman")
introduce("Hal Jordan", "Green Lantern")

hulk_punch = calculate_force(1000, 50)
print(f"Hulk's punch force: {hulk_punch} Newtons")

wonder_woman_punch = calculate_force(500, 80)
print(f"Wonder Woman's punch force: {wonder_woman_punch} Newtons")
