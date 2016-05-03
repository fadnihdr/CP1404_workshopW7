COLOR_NAMES = {"AliceBlue":"#f0f8ff", "AntiqueWhite":"#faebd7", "AntiqueWhite1":"#ffefdb",
               "AntiqueWhite2":"#eedfcc", "AntiqueWhite3":"#cdc0b0", "AntiqueWhite4":"#8b8378",
               "aquamarine1":"#7fffd4", "aquamarine2":"#7fffd4", "aquamarine4":"#458b74"}

name = input("Enter color name: ")
while name != "":
    if name in COLOR_NAMES:
        print(name, "is", COLOR_NAMES[name])
    else:
        print("Invalid code")
    name = input("Enter color name: ")
