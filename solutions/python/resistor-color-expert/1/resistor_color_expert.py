COLOR_BAND_COLORS = [
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

TOLERANCE_COLORS = {
    "grey": .05,
    "violet": .1,
    "blue": .25,
    "green": .5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

PREFIXES = [
    "",
    "kilo",
    "mega",
    "giga"
]

def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    elif len(colors) == 4:
        digits = [COLOR_BAND_COLORS.index(color) for color in colors[:2]]
        multiplier = COLOR_BAND_COLORS.index(colors[2])
        # num = digits[0] * 10**(1 + multiplier) + digits[1] * 10**(0 + multiplier)
        tolerance = TOLERANCE_COLORS[colors[3]]
    elif len(colors) == 5:
        digits = [COLOR_BAND_COLORS.index(color) for color in colors[:3]]
        multiplier = COLOR_BAND_COLORS.index(colors[3])
        tolerance = TOLERANCE_COLORS[colors[4]]
    else:
        raise ValueError("length of colors must be 1 (black) or 4 or 5")

    digits.reverse()
    num = sum([digit * 10**(i + multiplier) for i, digit in enumerate(digits)])

    prefix_index = 0
    while num >= 1000:
        prefix_index += 1
        num /= 1000 # we want the decimals unless they're 0...i think {num:g} in f-string does this?
    prefix = PREFIXES[prefix_index]
    
    return f"{num:g} {prefix}ohms {chr(0x00B1)}{tolerance}%"
        

    
        
