import webbrowser
import pyautogui
from datetime import timedelta
from datetime import datetime

#Finds the difference between two dates.

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

logins = {
    'User1': 'Pass1'
}

fridayLogins = {
}

#Amount slot increases by every 2 hours.

twoHourInc = 7200

#Amount slot increases by per day.

dailyInc = 86400

#Slot of first booking day.

710slot = 0
firstDay = "2017-05-17"

#Day of booking (3 weeks from current date).

bookingDay = (datetime.today() + timedelta(days=21)).strftime("%Y-%m-%d")

#Add daily increase to slot days_between times

for i in range(0, days_between(firstDay, bookingDay)):
    slot = slot + dailyInc

temp = 710slot
pyautogui.PAUSE = 4
for user in logins:
    webbrowser.open("http://apps.library.ryerson.ca/room_booking/booking/book_room?slot=" + str(temp) + "&room_id=213")
    pyautogui.press('tab')
    pyautogui.PAUSE = 0.1
    pyautogui.typewrite(user)
    pyautogui.press('tab')
    pyautogui.typewrite(logins[user])
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.PAUSE = 4
    for i in range(0,14):
        pyautogui.press('tab')
        pyautogui.PAUSE = 0.1
    pyautogui.press(['enter', 'down', 'down', 'down', 'enter', 'tab', 'tab', 'enter'])
    pyautogui.PAUSE = 3
    for i in range(0,18):
        pyautogui.press('tab')
        pyautogui.PAUSE = 0.1
    pyautogui.press('enter')
    temp = temp + twoHourInc
