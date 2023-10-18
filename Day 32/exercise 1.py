import datetime as dt
import smtplib
import random

# EXERCISE 1 :
# MONDAY MOTIVATIONAL QUOTE EMAIL APPLICATION


# accessing the quotes file and storing it's data as a list
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()


# getting the current day
current_info = dt.datetime.now()
current_day = current_info.weekday()

# getting the random quote
monday_quote = random.choice(all_quotes)

# sending the quote when it's Monday
if current_day == 0:
    senders_email = "smtptesting360@gmail.com"
    senders_password = "zfvhjjsyzheckdpq"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user=senders_email, password=senders_password)
        server.sendmail(
            from_addr=senders_email,
            to_addrs="jyotiutkarsh2010@gmail.com",
            msg=monday_quote,
        )
