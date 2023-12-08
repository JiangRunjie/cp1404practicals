COLOUR_TO_HEXADECIMAL_COLOUR = {"Amaranth": "#e52b50", "Aqua": "#00ffff",
              "Aureolin": "#fdee00", "Apricot": "#fbceb1",
              "Azure1": "#f0ffff", "Bittersweet": "#fe6f5e",
              "Black": "#000000", "Blond": "#faf0be",
              "Blue1": "#0000ff", "Blue2": "#0000ee"}
colour_name = input("Which colour are you looking for?: ")
while colour_name != "":
    try:
        print(f"The colour is {COLOUR_TO_HEXADECIMAL_COLOUR[colour_name]}")
    except KeyError:
        print("Sorry, we do not have that color")
    colour_name = input("Which colour are you looking for?: ")