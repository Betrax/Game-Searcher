import requests

######Delete#########
import os

os.system("cls")
###################


#### Functions
def _Url(year1, month1, day1, year2, month2, day2, PageNumber=1):
    if month1 < 10:
        month1 = "0" + str(month1)
    if day1 < 10:
        day1 = "0" + str(day1)
    if month2 < 10:
        month2 = "0" + str(month2)
    if day2 < 10:
        day2 = "0" + str(day2)

    Url = (
        "https://api.rawg.io/api/games?dates="
        + str(year1)
        + "-"
        + str(month1)
        + "-"
        + str(day1)
        + ","
        + str(year2)
        + "-"
        + str(month2)
        + "-"
        + str(day2)
        + "&page="
        + str(PageNumber)
        + "&platforms=4,187,1,18,186&page_size=40&ordering=released"
    )
    return Url


def _GetData_Date(year1=2020, month1=8, day1=4, year2=2020, month2=9, day2=4):

    Url = _Url(year1, month1, day1, year2, month2, day2)
    StaticData = requests.get(Url).json()
    AmountOfGames = StaticData["count"]
    AmountOfPages = AmountOfGames // 40 + 1
    PageNumber = 1

    #######Delete############
    Succes = 0
    Fail = 0
    #####################
    while PageNumber <= AmountOfPages:

        for x in range(len(StaticData["results"])):
            if StaticData["results"][x]["added"] > 0:
                try:
                    AStaticData = (StaticData["results"][x],)  # turns it to tulpe
                    Game = Game + AStaticData
                except:
                    AStaticData = (StaticData["results"][x],)  # turns it to tulpe
                    Game = AStaticData
                #############Delete#################
                os.system("cls")
                Succes = Succes + 1
                print("succes: ", (Succes))
                print("fail:", Fail)
                print("Total:", AmountOfGames, Succes + Fail)
            else:
                os.system("cls")
                Fail = Fail + 1
                print("success: ", (Succes))
                print("fail:", Fail)
                print("Total:", AmountOfGames, Succes + Fail)
            #############################################
        # goes trough pages
        PageNumber = PageNumber + 1
        if PageNumber <= AmountOfPages:
            Url = _Url(year1, month1, day1, year2, month2, day2, PageNumber)
            StaticData = requests.get(Url).json()

    return Game


#### Save it to local variables #####
StaticData = _GetData_Date()


### Main program ###################
for x in range(len(StaticData)):
    print(StaticData[x]["name"])

