

def bite(n_bites):
    output = f"{n_bites} candy bites: " + ", ".join(
        "yummy" for _ in range(n_bites)
    ) + "!"
    return output


def candy_factory(flavor, binding, coloring, decoration):
    candy = {
        "Flavor": flavor,
        "Binding": binding,
        "Color": coloring,
        "Decoration": decoration,
        "Bite": lambda n_bites: bite(n_bites)
    }
    return candy


if __name__ == '__main__':
    my_candy = candy_factory("Chocolate", "Nugget", "Red #5", "Peanut")
    print(my_candy["Bite"](5))
