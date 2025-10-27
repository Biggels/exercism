COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]
def value(colors):
    return int("".join([str(num) for num in [COLORS.index(colors[0]), COLORS.index(colors[1])]]))
