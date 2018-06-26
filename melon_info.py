"""Print out all the melons in our inventory."""

from melons import melons


def print_melon(melon_dictionary):
    """Print each melon with corresponding attribute information.
    :param melon_dictionary: dictionary of melon data
    :return:  prints a report of melon data
    """
    for name in melon_dictionary:
        is_seedless = melon_dictionary[name]["seedless"]
        price = melon_dictionary[name]["price"]
        flesh_color = melon_dictionary[name]["flesh_color"]
        weight = melon_dictionary[name]["weight"]
        rind_color = melon_dictionary[name]["rind_color"]

        print(name.upper())
        print("    seedless: {}".format(is_seedless))
        print("    price: {}".format(price))
        print("    flesh color: {}".format(flesh_color))
        print("    weight: {}".format(weight))
        print("    rind color: {}".format(rind_color))
        print()


print_melon(melons)
