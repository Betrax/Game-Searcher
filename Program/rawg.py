import requests
import datetime

#### Functions
def _Sort(StaticData):
    SortedStaticData = sorted(StaticData, key=lambda x: x["added"], reverse=True)
    return SortedStaticData


def _Date_ToDay_Year():
    YearToday = datetime.datetime.now().year
    Year = 2020
    return YearToday


def _Date_ToDay_Month():
    MonthToday = datetime.datetime.now().month
    return MonthToday


def _Date_ToDay_Day():
    DayToday = datetime.datetime.now().day
    return DayToday


def f_Check_Popular(StaticData):

    for x in range(len(StaticData["results"])):
        if StaticData["results"][x]["added"] > 0:
            try:  # can't start with an empty Game variable
                AStaticData = (StaticData["results"][x],)  # the ","turns it to tulpe
                Games = Games + AStaticData
            except:
                AStaticData = (StaticData["results"][x],)  # the ","turns it to tulpe
                Games = AStaticData

    try:
        return Games
    except:
        EmptyTuple = ()
        return EmptyTuple


def f_Url_Search(GameName, PageNumber=1):

    Url = "https://api.rawg.io/api/games?search=" + GameName + "&page=" + str(PageNumber) + "&platforms=4,187,1,18&page_size=40"
    return Url


def f_Url_Date(Year1, Month1, Day1, Year2, Month2, Day2, PageNumber=1):
    if Month1 < 10:
        Month1 = "0" + str(Month1)
    if Day1 < 10:
        Day1 = "0" + str(Day1)
    if Month2 < 10:
        Month2 = "0" + str(Month2)
    if Day2 < 10:
        Day2 = "0" + str(Day2)

    Url = "https://api.rawg.io/api/games?dates=" + str(Year1) + "-" + str(Month1) + "-" + str(Day1) + "," + str(Year2) + "-" + str(Month2) + "-" + str(Day2) + "&page=" + str(PageNumber) + "&platforms=4,187,1,18&page_size=40&ordering=released"
    return Url


def _Search_Name(GameName):
    Url = f_Url_Search(GameName)
    StaticData = requests.get(Url).json()
    AmountOfGames = StaticData["count"]

    print(AmountOfGames)

    AmountOfPages = AmountOfGames // 40  # 1 page contains 40 so it does amount//40 to get pages
    PageNumber = 1
    if AmountOfGames % 40 != 0:
        AmountOfPages = AmountOfPages + 1

    while PageNumber <= AmountOfPages:
        try:
            Games = Games + f_Check_Popular(StaticData)
        except:
            Games = f_Check_Popular(StaticData)

        PageNumber = PageNumber + 1
        if PageNumber <= AmountOfPages:
            Url = f_Url_Search(GameName, PageNumber)
            StaticData = requests.get(Url).json()

    return Games


def _Search_Date(Year1=_Date_ToDay_Year(), Month1=_Date_ToDay_Month(), Day1=_Date_ToDay_Day(), Year2=_Date_ToDay_Year(), Month2=_Date_ToDay_Month(), Day2=_Date_ToDay_Day()):

    Url = f_Url_Date(Year1, Month1, Day1, Year2, Month2, Day2)
    StaticData = requests.get(Url).json()
    AmountOfGames = StaticData["count"]

    print(AmountOfGames)

    AmountOfPages = AmountOfGames // 40  # 1 page contains 40 so it does amount//40 to get pages
    PageNumber = 1
    if AmountOfGames % 40 != 0:
        AmountOfPages = AmountOfPages + 1

    while PageNumber <= AmountOfPages:
        try:
            Games = Games + f_Check_Popular(StaticData)
        except:
            Games = f_Check_Popular(StaticData)

        PageNumber = PageNumber + 1
        if PageNumber <= AmountOfPages:
            Url = f_Url_Date(Year1, Month1, Day1, Year2, Month2, Day2, PageNumber)
            StaticData = requests.get(Url).json()

    return Games


#### Save it to local variables #####
StaticData = _Search_Name((input()))


### Main program ###################
for x in range(len(StaticData)):
    print(StaticData[x]["name"])
