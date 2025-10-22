def convert(number):
    result = ""
    sound_map = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }

    for value in sound_map:
        if number % value == 0:
            result += sound_map[value]

    if result == "":
        return str(number)
    else:
        return result
