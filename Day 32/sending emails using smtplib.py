import smtplib


# senders email
senders_email = "smtptesting360@gmail.com"


# senders email 'apppasswords'
senders_password = "zfvhjjsyzheckdpq"


# connecting to the email providers SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # securing the connection to our email server
    server.starttls()

    # login to our email
    server.login(user=senders_email, password=senders_password)

    # sending the email
    server.sendmail(
        from_addr=senders_email,
        to_addrs="utkarshprogrammer360@gmail.com",
        msg="Subject:Testing SMTP Using Python\n\nHello World!",
    )
