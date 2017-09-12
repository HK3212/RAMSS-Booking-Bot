from datetime import timedelta
from datetime import datetime
import webbrowser
import pyautogui

#Finds the difference between two dates.

def days_between(day1, day2):
    """Determines the number of days between two dates."""
    day1 = datetime.strptime(day1, "%Y-%m-%d")
    day2 = datetime.strptime(day2, "%Y-%m-%d")
    return abs((day2 - day1).days)

logins = {'user1', 'pass1', 'user2', 'pass2'}

BOOKING_URL = "http://apps.library.ryerson.ca/room_booking/booking/book_room?slot="

DAY_OF_WEEK = datetime.today().weekday()

#Amount slot increases by every 2 hours.

TWO_HOUR_INCREASE = 7200

#Amount slot increases by per day.

DAILY_INCREASE = 86400

#Slot of first booking day.

slot_710 = 0
FIRST_DAY = "2017-05-17"

#Day of booking (3 weeks from current date).

BOOKING_DAY = (datetime.today() + timedelta(days=21)).strftime("%Y-%m-%d")

#Add daily increase to slot days_between times

for i in range(0, days_between(FIRST_DAY, BOOKING_DAY)):
    slot_710 = slot_710 + DAILY_INCREASE

temp = slot_710
pyautogui.PAUSE = 4.0
for user in logins:
    webbrowser.open(BOOKING_URL + str(temp) + "&room_id=213")
    pyautogui.press('tab')
    pyautogui.PAUSE = 0.1
    pyautogui.typewrite(user)
    pyautogui.press('tab')
    pyautogui.typewrite(logins[user])
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.PAUSE = 4
    for i in range(0, 14):
        pyautogui.press('tab')
        pyautogui.PAUSE = 0.1
    pyautogui.press(['enter', 'down', 'down', 'down', 'enter', 'tab', 'tab', 'enter'])
    pyautogui.PAUSE = 3
    for i in range(0, 18):
        pyautogui.press('tab')
        pyautogui.PAUSE = 0.1
    pyautogui.press('enter')
    temp = temp + TWO_HOUR_INCREASE
