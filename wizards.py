"""
Wizard Tournament: Wizard Class
Robert Sharp
March 13, 2021

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
    names = ("Earth", "Air", "Fire", "Water")
    school_mods = {
        "Earth": {"Offense": 0, "Defense": 3, "Accuracy": 0},
        "Air": {"Offense": 0, "Defense": 0, "Accuracy": 3},
        "Fire": {"Offense": 3, "Defense": 0, "Accuracy": 0},
        "Water": {"Offense": 1, "Defense": 1, "Accuracy": 1},
    }

    def __init__(self, name):
        n = name.title()
        if n in self.names:
            self.name = n
        else:
            self.name = choice(self.names)

        self.modifiers = self.school_mods[self.name]

    def __str__(self):
        return self.name


class Wizard:

    def __init__(self,
                 wizard_name: str,
                 wand_name: str,
                 school: MagicSchool):
        self.name = wizard_name
        self.school = school
        self.offense = d(6) + self.school.modifiers["Offense"]
        self.defense = d(6) + self.school.modifiers["Defense"]
        self.accuracy = d(6) + self.school.modifiers["Accuracy"]
        self.health = dice(3, 6)
        self.wand = Wand(wand_name)

    def __str__(self):
        output = (
            f"{self.name}, Wizard of {self.school}",
            f"Health: {self.health}",
            f"Modifiers:",
            f"  Offence: +{self.offense}",
            f"  Defense: +{self.defense}",
            f"  Accuracy: +{self.accuracy}",
            f"Wand: {self.wand}",
        )
        delimiter = "\n"
        return delimiter.join(output)


if __name__ == '__main__':
    print()
    zarn = Wizard(
        wizard_name="Zarn",
        wand_name="Randnoph",
        school=MagicSchool("Random"),
    )
    print(zarn)
