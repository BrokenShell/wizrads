"""
Wizard Tournament: Wands
Robert Sharp
March 13, 2021

"""
from random import choice

from dice import d


class Wand:
    cores = (
        "Unicorn hair", "Dragon heartstring", "Phoenix feather", "Veela hair",
        "Thestral tail hair", "Troll whisker", "Kelpie hair",
        "Thunderbird tail feather", "Wampus cat hair",
        "White River Monster spine", "Rougarou hair", "Kneazle whiskers",
        "Horned Serpent horn", "Snallygaster heartstring", "Jackalope antler",
        "Basilisk horn",
    )
    woods = (
        "Acacia", "Alder", "Apple", "Ash", "Aspen", "Beech", "Blackthorn",
        "Black Walnut", "Cedar", "Cherry", "Chestnut", "Cypress", "Dogwood",
        "Ebony", "English oak", "Elder", "Elm", "Fir", "Hawthorn", "Hazel",
        "Holly", "Hornbeam", "Larch", "Laurel", "Maple", "Pear", "Pine",
        "Poplar", "Red Oak", "Redwood", "Reed", "Rosewood", "Rowan",
        "Silver lime", "Spruce", "Snakewood", "Sugar Maple", "Sycamore",
        "Tamarack", "Vine", "Walnut", "Willow", "Yew",
    )

    def __init__(self):
        self.core = choice(self.cores)
        self.wood = choice(self.woods)
        self.bonus = d(6)

    def __call__(self):
        return d(6) + self.bonus

    def __str__(self):
        output = (
            f"Wand Components:",
            f"  Bonus: {self.bonus}",
            f"  Core: {self.core}",
            f"  Wood: {self.wood}",
        )
        return "\n".join(output)


if __name__ == '__main__':
    print()
    my_wand = Wand()
    print(my_wand)
    print(my_wand())
