import requests
from bs4 import BeautifulSoup

def download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url,headers=headers)
    return r.text


def get_content(html):
    output = """作者：{} {}\n------------\n"""
    soup = BeautifulSoup(html,'html.parser')
    con = soup.find("div",class_= "col1 old-style-col1")
    con_list = con.find_all("div",class_ = "article block untagged mb15 typs_hot")
    for item in con_list:
        author = item.find('h2').string # 获取作者名字
        content = item.find('a',class_ = "contentHerf").find("div",class_ = "content").find("span").get_text() # 获取内容
        save_txt(output.format(author,content))
def save_txt(*args):
    for i in args:
        with open('qiushi.txt','a',encoding='utf-8') as f:
            f.write(i)

if __name__ == '__main__':
    url = "https://qiushibaike.com/text/page/"
    te = download_page(url)
    get_content(te)