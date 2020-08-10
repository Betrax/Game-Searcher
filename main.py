import requests
import json
import time
import os


def clear():
    os.system("cls")  # On Windows System, just for easier debugging


def f_GetData(PageNumber):
    ApiData = {"message": "Internal server error"}
    x = 0
    # Check until valid data is send to us
    while ApiData == {"message": "Internal server error"}:
        clear()
        x = x + 1
        print("Trying...", x)

        time.sleep(1)  # To prevent spamming (spamming causes ip ban by the api provider).
        ApiUrl = "https://api.crackwatch.com/api/games?page=" + str(PageNumber) + "&sort_by=release_date"

        ApiData = requests.get(ApiUrl).json()  # gets the data from the url, turns it into dictionary

    return ApiData


def f_navInput():
    action = input()
    if action == "down":
        return True
    elif action == "up":
        return False


def f_print():
    clear()
    for page in range(len(StaticData)):
        print(StaticData[page]["title"], StaticData[page]["releaseDate"].rjust(60 - len(StaticData[page]["tile"])))


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
        print("Youre already at page 0")
