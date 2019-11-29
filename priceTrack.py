import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Test-Exclusive-747/dp/B07DJCVTDN/ref=sr_1_1?keywords=PIXEL&qid=1575019344&smid=A23AODI1X2CEAE&sr=8-1'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page=requests.get(URL, headers=headers)

soup=BeautifulSoup(page.content, 'html.parser')

def check_price():

 title=soup.find(id="title").get_text()
 price= soup.find(id="priceblock_dealprice").get_text()
 updated_price=float(price[2:8].replace(",",""))
 if(updated_price)<33999.0:
    send_mail()

 print(title.strip())
 print(updated_price)

 if (updated_price) < 33999.0:
     send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your_Email', 'APP PASSWORD')

    subject="Price fell down"
    body="Check the amazon link https://www.amazon.in/Test-Exclusive-747/dp/B07DJCVTDN/ref=sr_1_1?keywords=PIXEL&qid=1575019344&smid=A23AODI1X2CEAE&sr=8-1"
    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'ashuprince121@gmail.com',
        'allyouwantstore@outlook.com',
        msg
    )
    print("Email Has Been Sent!!")
    server.quit()


while(True):
    check_price()
