import datetime as dt
import smtplib
import pandas
import random


# PROJECT 32 :
# AUTOMATIC BIRTHDAY WISHER


# CONSTANTS
SENDERS_EMAIL = "smtptesting360@gmail.com"
SENDERS_PASSWORD = "zfvhjjsyzheckdpq"


# 1. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)


# 2. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDERS_EMAIL, password=SENDERS_PASSWORD)
        connection.sendmail(
            from_addr=SENDERS_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Happy Birthday\n\n{contents}",
        )
