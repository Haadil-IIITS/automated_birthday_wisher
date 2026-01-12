# =========================================================================
#  CONFIGURATION SECTION
# =========================================================================
#  PLEASE READ:
#  1. Replace 'email' with your own Gmail address.
#  2. Replace 'password' with your 16-character Google App Password.
#     (Do NOT use your regular Gmail login password).
#  3. 'senderemail' determines who receives the mail.
#     (In the code, this is automatically pulled from dates.csv).
# =========================================================================

# email = "your_email@gmail.com"
# password = "your_app_password"

import pandas
#todays datetime
import smtplib
import datetime as dt
date=dt.datetime.now()

month_=date.month
today_=date.day

#finding today's date of birth
data=pandas.read_csv("dates.csv")
#data collection

birth_month=data[data.month==month_]
birth_day=birth_month[birth_month.day==today_]

names=""


print(birth_day)#will print u the column which contain the info of the birthday boy
for i in birth_day.names:
    names=i
f=open("letter.txt","r")
letter=f.read()
letter=letter.replace("[name]",names)

email = "moviebox1123@gmail.com"
password = "ojooyjuacjzzhtku"
senderemail=birth_day.email
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email,password=password)


for i in birth_day.index:
    birth_row=birth_day[birth_day.index==i]
    names = birth_row.names.item()
    f = open("letter.txt", "r")
    letter = f.read()
    letter = letter.replace("[name]", names)
    senderemail=birth_row.email

    connection.sendmail(
        from_addr=email,
        to_addrs=senderemail,
        msg=f"Subject: wishing u happy birthday\n\n{letter}"
)
connection.close()

