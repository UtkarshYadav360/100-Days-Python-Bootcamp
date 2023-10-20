import requests
from datetime import datetime
import smtplib
import time


# PROJECT 33 :
# ISS OVERHEAD NOTIFIER


# CONSTANTS
MY_LAT = 28.669155  # Your latitude
MY_LONG = 77.453758  # Your longitude


def is_iss_overhead():
    """Checks if the ISS position is similar to my position."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night():
    """Checks if there is night time now or not."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # checking the time now
    time_now = datetime.now().hour()
    if time_now >= sunset or time_now <= sunrise:
        return True


# sending the email
while True:
    # loop runs after every 60 seconds
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user="smtptesting360@gmail.com", password="zfvhjjsyzheckdpq")
        connection.sendmail(
            to_addrs="smtptesting360@gmail.com",
            from_addr="utkarshprogrammer360@gmail.com",
            msg="Subject:Look Up👆\n\nThe Iss is above you in the sky",
        )
