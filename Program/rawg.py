import requests

######Delete#########
import os

os.system("cls")
#####################


#### Functions
def _Date_ToDay_Year():
    print("Year")


def _Date_ToDay_Month():
    print("Month")


def _Date_ToDay_Day():
    print("Day")


def _Platforms():
    return "4,187,1,18"


def _Url(Year1, Month1, Day1, Year2, Month2, Day2, PageNumber=1, Platforms=_Platforms()):
    if Month1 < 10:
        Month1 = "0" + str(Month1)
    if Day1 < 10:
        Day1 = "0" + str(Day1)
    if Month2 < 10:
        Month2 = "0" + str(Month2)
    if Day2 < 10:
        Day2 = "0" + str(Day2)

    Url = (
        "https://api.rawg.io/api/games?dates="
        + str(Year1)
        + "-"
        + str(Month1)
        + "-"
        + str(Day1)
        + ","
        + str(Year2)
        + "-"
        + str(Month2)
        + "-"
        + str(Day2)
        + "&page="
        + str(PageNumber)
        + "&platforms="
        + Platforms
        + "&page_size=40&ordering=released"
    )
    return Url


def _GetData_Popular_Date(Year1=2020, Month1=8, Day1=4, Year2=2020, Month2=8, Day2=4):  # just place holder values

    Url = _Url(Year1, Month1, Day1, Year2, Month2, Day2)
    StaticData = requests.get(Url).json()
    AmountOfGames = StaticData["count"]
    AmountOfPages = AmountOfGames // 40  # 1 page contains 40 so it does amount//40 to get pages
    if AmountOfGames % 40 != 0:
        AmountOfPages = AmountOfPages + 1  # does +1 if there's a leftover page
    PageNumber = 1

    #############Delete############
    Succes = 0
    Fail = 0
    #################################

    while PageNumber <= AmountOfPages:

        for x in range(len(StaticData["results"])):
            if StaticData["results"][x]["added"] > 0:
                try:  # can't start with an empty Game variable
                    AStaticData = (StaticData["results"][x],)  # the ","turns it to tulpe, it keeps adding tulpes to 1 giant one that contains all the filtered information
                    Game = Game + AStaticData
                except:
                    AStaticData = (StaticData["results"][x],)  # the ","turns it to tulpe
                    Game = AStaticData
#######################################################Delete#################
                os.system("cls")
                Succes = Succes + 1
                print("succes: ", (Succes))
                print("fail:", Fail)
                print("Total:", AmountOfGames, Succes + Fail)
            else:
                os.system("cls")
                Fail = Fail + 1
                print("succes: ", (Succes))
                print("fail:", Fail)
                print("Total:", AmountOfGames, "-", Succes + Fail)
##############################################################################
        # goes trough pages
        PageNumber = PageNumber + 1
        if PageNumber <= AmountOfPages:
            Url = _Url(Year1, Month1, Day1, Year2, Month2, Day2, PageNumber)
            StaticData = requests.get(Url).json()

    return Game


#### Save it to local variables #####
StaticData = _GetData_Popular_Date()

### Main program ###################
for x in range(len(StaticData)):
    print(StaticData[x]["name"])

