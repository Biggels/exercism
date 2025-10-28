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

PREFIXES = [
    "",
    "kilo",
    "mega",
    "giga"
]

def label(colors):
    digits = [COLORS.index(colors[i]) for i in range(3)]
    # return digits
    ohms_num = 10**(1 + digits[2]) * digits[0] + 10**(digits[2]) * digits[1]

    prefix_index = 0
    while ohms_num >= 1000:
        prefix_index += 1
        ohms_num = ohms_num // 1000

    prefix = PREFIXES[prefix_index]
    label = f"{ohms_num} {prefix}ohms"

    return label
