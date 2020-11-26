import calendar
import datetime
import webbrowser
from periods import *

#get current time
now = datetime.datetime.now()

# math zoom link
def math():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)    

# homeroom zoom link
def homeroom():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)    


# socail studies zoom link
def socailStudies():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)

# music zoom link
def music():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)

# english zoom link
def english():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)

# computer class zoom link
def comp():
    url = "ZOOM LINK HERE"
    webbrowser.open(url)

# monday Schedule
def monday():
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    time1()
    if hour == "8" and minute == "00":
        homeroom()
        time2()
    elif hour == "8" and minute == "10":
        time3()
        pass
    elif hour == "8" and minute == "30":
        time4()
        pass
    elif hour == "9" and minute == "15":
        time5()
        pass
    elif hour == "10" and minute == "00":
        math()
        time6()
    elif hour == "10" and minute == "45":
        socailStudies()
        time7()
    elif hour == "11" and minute == "30":
        time8()
        pass
    elif hour == "12" and minute == "00":
        homeroom()
        time9()
    elif hour == "12" and minute == "30":
        english()
        time10()
    elif hour == "13" and minute == "15":
        music()
        time11()
    elif hour == "14" and minute == "00":
        homeroom()
    else:
        exit()


# tuesday Schedule
def tuesday():
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    time1()
    if hour == "8" and minute == "00":
        homeroom()
        time2()
    elif hour == "8" and minute == "10":
        time3()
        pass
    elif hour == "8" and minute == "30":
        time4()
        pass
    elif hour == "9" and minute == "15":
        time5()
        pass
    elif hour == "10" and minute == "00":
        math()
        time6()
    elif hour == "10" and minute == "45":
        socailStudies()
        time7()
    elif hour == "11" and minute == "30":
        time8()
        pass
    elif hour == "12" and minute == "00":
        homeroom()
        time9()
    elif hour == "12" and minute == "30":
        english()
        time10()
    elif hour == "13" and minute == "15":
        time11()
        pass
    elif hour == "14" and minute == "00":
        homeroom()
    else:
        exit()

# PASTE IN THE TIME FOR IT TO CHECK FOR THE TIME

# wednessdays Schedule
def wednessday():
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    print(hour, minute)
    time1()
    if hour == "8" and minute == "00":
        homeroom()
        time2()
    elif hour == "8" and minute == "10":
        pass
    elif hour == "8" and minute == "30":
        time12()
        pass
    elif hour == "9" and minute == "20":
        time13()
        pass
    elif hour == "10" and minute == "05":
        math()
        time14()
    elif hour == "10" and minute == "50":
        socailStudies()
        time15()
    elif hour == "11" and minute == "35":
        time16()
        pass
    elif hour == "12" and minute == "05":
        homeroom()
        time17()
    elif hour == "12" and minute == "35":
        time18()
        english()
    elif hour == "13" and minute == "25":
        music()
    else:
        exit()


# thursday Schedule
def thursday():
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    time1()
    if hour == "8" and minute == "00":
        homeroom()
        time2()
    elif hour == "8" and minute == "10":
        time3()
        pass
    elif hour == "8" and minute == "30":
        time4()
        pass
    elif hour == "9" and minute == "15":
        time5()
        pass
    elif hour == "10" and minute == "00":
        math()
        time6()
    elif hour == "10" and minute == "45":
        socailStudies()
        time7()
    elif hour == "11" and minute == "30":
        time8()
        pass
    elif hour == "12" and minute == "00":
        homeroom()
        time9()
    elif hour == "12" and minute == "30":
        english()
        time10()
    elif hour == "13" and minute == "15":
        comp()
        time11()
    elif hour == "14" and minute == "00":
        homeroom()
    else:
        exit()


# fridays Schedule
def friday():
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    time1()
    if hour == "8" and minute == "00":
        homeroom()
        time2()
    elif hour == "8" and minute == "10":
        time3()
        pass
    elif hour == "8" and minute == "30":
        math()
        time4()
    elif hour == "9" and minute == "15":
        time5()
        pass
    elif hour == "10" and minute == "00":
        socailStudies()
        time6()
    elif hour == "10" and minute == "45":
        homeroom()
        time7()
    elif hour == "11" and minute == "30":
        time8()
        pass
    elif hour == "12" and minute == "00":
        homeroom()
        time9()
    elif hour == "12" and minute == "30":
        english()
        time10()
    elif hour == "13" and minute == "15":
        time11()
        pass
    elif hour == "14" and minute == "00":
        homeroom()
    else:
        exit()