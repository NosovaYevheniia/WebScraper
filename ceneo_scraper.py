import os
import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True
url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
headers = {
    "Host": "www.ceneo.pl",
    "Cookie": "sv3=1.0_9011ebe0-3ccc-11f1-9f64-c265b7fa39fd; urdsc=1; userCeneo=ID=9aaf8704-e927-416f-a87a-24ff5a68667e; __RequestVerificationToken=ON1ymB9UK3ZiztEauQcjxgPfsgKxr1DaOU4qR1ri6sWVMdOhOBgMPU5NBaccksFTCZiw6RmFrfTGjPXmdAyt2sk52D9YO74NxIXwS5c-msM1; ai_user=Y/Xgp|2026-04-20T15:21:11.622Z; __utmf=b005f137479d61dcd846fea07a2e7c2c_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.9011ebe0-3ccc-11f1-9f64-c265b7fa39fd; _gcl_au=1.1.729151786.1776698474; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.0wzWTJIYxmFVGcjoDftsh25yvy2wxrIl%2Ft1RPY1v1ME%3D; FPLC=q613aVbvdzsWkNTYSWrjn67vxr4z81oEM2hspEzV5jPG%2FH%2B3tpvoMPLKbaChbkqMfJRa03%2BTHpoogOMzpiwcwvrtzlea75eKRriMkwrXqZLZhQM%3D; _tt_enable_cookie=1; _ttp=01KPNQPSZPTXS4T14GQ9PQ0XAG_.tt.1; _fbp=fb.1.1776698484968.539038401192988288; nps3=SessionStartTime=1776698482,SurveyId=68,ClosedOrCompleted=True; ai_session=L1aPc|1776698472538|1776698573986; ga4_ga_K2N2M0CBQ6=GS2.2.s1776698472$o1$g1$t1776698574$j59$l0$h1688183814; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A54.185Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%229011ebe0-3ccc-11f1-9f64-c265b7fa39fd%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A54.185Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22RJsn1LLThftlxKucPqxT%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A54.186Z%22%7D; ttcsid_CNK74OBC77U1PP7E4UR0=1776698484729::_l0D5cE10cjABVfI663T.1.1776698574345.1; ttcsid=1776698484729::gCpRHc1yjnSXMicXnxaV.1.1776698574345.0::1.88419.89616::0.0.0.0::0.0.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

path_to_driver = "D:\\chromedriver-win64\\chromedriver.exe"
service = Service(path_to_driver)
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(2)
driver.find_element(by="xpath", value="//*[@id='js_cookie-consent-general']/div/div[2]/button[1]").click()

all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.status_code)

        page_dom = BeautifulSoup(response.text, "html.parser")
        if page == 1:
            product_name = page_dom.find("h1", {"class": "product-top__product-info__name"}).get_text()
            print(product_name)

        opinions = page_dom.select("div.js_product-review:not(.user-post-highlight)")
        print(len(opinions))

        opinions = [r for r in page_dom.find_all("div", {"class": "js_product-review"}) if "user-post-highlight" not in r.get("class", [ ])]

        for opinion in opinions:
            single_opinion = {
                "opinion_id": opinion["data-entry-id"],
                "author": opinion.select_one("span.user-post__author-name").get_text().strip() if opinion.select_one("span.user-post__author-name") else None,
                "recommendation": opinion.select_one("span.user-post__author-recomendation > em").get_text().strip() if opinion.select_one("span.user-post__author-recomendation > em") else None,
                "score": opinion.select_one("span.user-post__score-count").get_text().strip() if opinion.select_one("span.user-post__score-count") else None,
                "content": opinion.select_one("div.review-feature__item--positive").get_text().strip() if opinion.select_one("div.review-feature__item--positive") else None,
                "pros": [p.get_text() for p in opinion.select("div.review-feature__item--positive")],
                "cons": [c.get_text() for c in opinion.select("div.review-feature__item--negative")],
                "like": opinion.select_one("button.vote-yes > span").get_text().strip() if opinion.select_one("button.vote-yes > span") else None,
                "dislike": opinion.select_one("button.vote-no > span").get_text().strip() if opinion.select_one("button.vote-no > span") else None,
                "publish_date": opinion.select_one("user-post__published > time:nth-child(1)[datatime]")["datetime"].strip() if opinion.select_one("user-post__published > time:nth-child(1)[datatime]") else None,
                "purchase_date": opinion.select_one("user-post__published > time:nth-child(2)[datatime]")["datetime"].strip() if opinion.select_one("user-post__published > time:nth-child(2)[datatime]") else None,
            }

            all_opinions.append(single_opinion)

        next = True if page_dom.select_one("button.pagination__next") else False
        if next: page += 1

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")

with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

