from bs4 import BeautifulSoup
import http.client
import os
import csv
# 定義初始變數
info=[]
host="www.ptt.cc"
pageNumHref="/bbs/Lottery/index.html"
pageNeed=3
conn=http.client.HTTPSConnection(host)

# func1：依url取得發文時間
def getTime(conn,href):
    conn.request("GET", href)
    response = conn.getresponse()
    htmlSource=response.read()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    if soup.findAll(attrs={'class':'article-metaline'}):
        return soup.findAll(attrs={'class':'article-metaline'})[2].find(attrs={'class':'article-meta-value'}).string
    else:
        return ''
# func2：依bs4取得的需求的資料組迭代取得該頁面資料
def readInfo(conn,items,info):
    for item in reversed(items):
        temp=[]
        title=item.find("a")
        if title:
            temp.append(title.string)
        else:
            temp.append('')
        push=item.find(attrs={'class':'nrec'}).string
        if push:
            temp.append(push)
        else:
            temp.append('0')
        if item.find("a"):
            # 調用func1依href進入頁面取得時間
            time=getTime(conn,item.find("a")['href'])
        else:
            time=''
        temp.append(time)
        info.append(temp)

#Step0：需求頁數迭代取得資料
for page in range(pageNeed):
    #Step1：依url取得頁面，並轉換為bs4物件
    conn.request("GET", pageNumHref)
    response = conn.getresponse()
    htmlSource=response.read()
    soup = BeautifulSoup(htmlSource, 'html.parser')
    #Step2：取得下一頁的url
    pageNumHref=soup.findAll(attrs={'class':'btn wide'})[1]['href']
    #Step3：將bs4物件擷取為需求的資料組
    items=soup.findAll(attrs={'class':'r-ent'})
    #Step4：調用func2轉換資料並存入
    readInfo(conn,items,info)

#Step5：調用csv存入資料
article_result_fp=os.path.join(os.path.dirname(__file__),"article.csv")
fieldnames = ['results']
writer = csv.DictWriter(open(article_result_fp, "w", newline=''),fieldnames)
for res in info:
    writer.writerow({'results':','.join(res)})
