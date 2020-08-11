from functions import f_GetData, f_navInput, f_navInput

# Startup values!
PageNumber = 0
StaticData = f_GetData(PageNumber)
f_print()


# The whole program loop (for console I think)
while True:
    StaticInput = f_navInput()
    if StaticInput == True:

        PageNumber = PageNumber + 1

        StaticData = f_GetData(PageNumber)
        f_print()

    elif StaticInput == False and PageNumber != 0:

        PageNumber = PageNumber - 1

        StaticData = f_GetData(PageNumber)
        f_print()

    else:
        print("You're already at page 0")
