import os
from tkinter import filedialog
from dataclasses import dataclass
import pandas as pd
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def is_nan(x):
    return (x!=x)

@dataclass
class Order:
    publisher: str=''
    author: str=''
    title: str=''
    link: str=''
    price: str=''
    name: str=''
    date: str=''
    comment: str=''

orders = []
def read_data(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')

    for row in df.iterrows():
        if(is_nan(row[1][1])):
            continue;
        order=Order(publisher=row[1][1],
        author=row[1][2],
        title=row[1][3],
        link=row[1][4],
        price=row[1][5],
        name=row[1][6],
        date=row[1][7],
        comment=row[1][8])
        orders.append(order)


print("Book-Duk2 Beta by 최아연")

#파일 읽어오기
print("파일을 선택하세요.")
file_path=""
while(len(file_path)==0):
    file_path=filedialog.askopenfilename(initialdir=".",\
        title="파일을 선택 해 주세요.",\
        filetypes=(("*.xlsx","*xlsx"),("*.xls","*xls"),("*.csv","*csv")))
    read_data(file_path)

user_id=input("yes24 아이디 : ")
user_pw=getpass("yes24 비밀번호 :")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.maximize_window()
driver.implicitly_wait(10)

# 로그인
driver.get("https://www.yes24.com/Templates/FTLogin.aspx")
driver.find_element(By.ID, 'SMemberID').send_keys(user_id)
driver.find_element(By.ID, 'SMemberPassword').send_keys(user_pw)
driver.find_element(By.ID, 'btnLogin').click()


print(f"=====카트 담기 시작(전체 {len(orders)} 항목)=====")
failed_cnt=0
success_cnt=0
for order in orders:
    failed=False
    log=f"{order.name}님의 책 \"{order.title}\""
    error_reason=""
    driver.get(order.link)
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    price=soup.select_one('.nor_price > .yes_m').text
    site_value=price.replace(',','')
    user_value=str(int(order.price))
    if(site_value==user_value):
        try:
            add_to_cart=driver.find_element(By.XPATH, '//*[@id="addToCartForDetail"]/span/em')
            add_to_cart.click()
        except:
            error_reason="카트에 추가할 수 없습니다.(품절, 절판)"
            failed=True
    else:
        error_reason=f"금액이 맞지 않습니다.(입력:{user_value}, 실제:{site_value}"
        failed=True
    if(failed):
        print(f"[실패] {log} : {error_reason}\n\t링크 : {order.link}")
        failed_cnt+=1
    else:
        print(f"{log} 추가 완료")
        success_cnt+=1

print(f"=====카트 담기 완료(성공 : {success_cnt} 실패 : {failed_cnt})=====")
#장바구니로 이동
driver.get("https://ssl.yes24.com/dMyCart/CartMain")

print("주문 완료 후 엔터를 입력하세요.")
input()
