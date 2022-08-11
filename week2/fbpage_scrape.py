import requests
from bs4 import BeautifulSoup
import csv


page_handler = []
with open("page_handler.csv") as file:
    read_csv = csv.reader(file)
    for handler in read_csv:
            page_handler.append(handler[0])
print(page_handler)


def raw_data(url):
    response = requests.get(url)
    return response.content.decode()

def parsed_data(data):
    soup= BeautifulSoup(data,"html.parser")
    return soup.select_one('span[class="_52id _50f5 _50f7"]').text[1:8]

likes=[]
base_url = "https://www.facebook.com/"
for handlers in page_handler:
    base_url+=handlers
    print(base_url)
    raw= raw_data(base_url)
    like=parsed_data(raw)
    likes.append(like)
    base_url="https://www.facebook.com/"    


with open("likes.csv","w",encoding='utf-16') as f:
    csv_writer= csv.DictWriter(f,fieldnames=["FB_page_Handler","Likes_Count"])
    csv_writer.writeheader()

    for i in range(len(page_handler)):
        csv_writer.writerow({"FB_page_Handler":page_handler[i],"Likes_Count":likes[i]})
        