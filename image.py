from bs4 import BeautifulSoup
import requests
import os

response = requests.get("https://yande.re/post")
soup = BeautifulSoup(response.text , "html.parser")
data = soup.select("div.inner a")

list_URL = []
list_img = []

count = 0
n = 0
for i in data:
    count += 1

    list_URL.append(i.text[3:]) 

    if count >=10:
        break

for u in list_URL:
    response2 = requests.get(u)
    soup2 = BeautifulSoup(response2.text , "html.parser")
    data2 = soup2.select("div.content div img")
    
    for d in data2:

        list_img.append(d["src"])        

for a in list_img:

    r = requests.get(a)

    n = n+1
    folder_path = f'./image/'
    img_name = folder_path + f"{n}.jpg"
    os.makedirs(folder_path , exist_ok=True)

    with open(img_name , 'wb') as f :
        f.write(r.content)
        print(f"Download {img_name} ......")