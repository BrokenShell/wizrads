"""
Wizard Tournament: Wizard Class
Robert Sharp
March 2021

Magic Schools:
    Earth: Defense Specialists
    Air: Accuracy Specialists
    Fire: Offense Specialists
    Water: Generalists (Solid, Liquid, Gas)
"""
from random import choice

from dice import d, dice
from wands import Wand


class MagicSchool:
    school_names = ("Earth", "Air", "Fire", "Water")
    school_modifiers = {
        "Earth": {"Offense": 0, "Defense": 3, "Accuracy": 0},
        "Air": {"Offense": 0, "Defense": 0, "Accuracy": 3},
        "Fire": {"Offense": 3, "Defense": 0, "Accuracy": 0},
        "Water": {"Offense": 1, "Defense": 1, "Accuracy": 1},
    }

    def __init__(self, school_name):
        if school_name.title() in self.school_names:
            self.name = school_name.title()
        else:
            self.name = choice(self.school_names)
        self.modifiers = self.school_modifiers[self.name]

    def __str__(self):
        return self.name


class Wizard:

    def __init__(self, wizard_name: str, school_name: str):
        self.name = wizard_name
        self.school = MagicSchool(school_name)
        self.offense = d(6) + self.school.modifiers["Offense"]
        self.defense = d(6) + self.school.modifiers["Defense"]
        self.accuracy = d(6) + self.school.modifiers["Accuracy"]
        self.health = dice(3, 6)
        self.wand = Wand()

    def __str__(self):
        output = (
            f"{self.name}, Wizard of {self.school}",
            f"Health: {self.health}",
            f"Modifiers:",
            f"  Offence: +{self.offense}",
            f"  Defense: +{self.defense}",
            f"  Accuracy: +{self.accuracy}",
            f"{self.wand}",
        )
        delimiter = "\n"
        return delimiter.join(output)


if __name__ == '__main__':
    print()
    my_wizard = Wizard(
        wizard_name="Zack",
        school_name="Air",
    )
    print(my_wizard)
    print()
    print(f"{my_wizard.name} flicks his wand for {my_wizard.wand()} damage.")
