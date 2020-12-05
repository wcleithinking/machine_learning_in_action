# coding: UTF-8
import requests, sys
from bs4 import BeautifulSoup

class downloader(object):
    def __init__(self):
        self.server = "http://www.biqukan.com/"
        self.target = "http://www.biqukan.com/1_1094/"
        self.names = []
        self.urls = []
        self.nums = 0
        
    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, features="html.parser")
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]), features="html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
    
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all('div', class_ = "showtxt")
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts
    
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    '''
        For TXT
    '''
    # dl = downloader()
    # dl.get_download_url()
    # print("开始下载《一念永恒》：")
    # for i in range(dl.nums):
    #     dl.writer(dl.names[i], 'ch00_using_requests/一念永恒.txt', dl.get_contents(dl.urls[i]))
    #     sys.stdout.write("\t已下载：%.3f%%" % float(i/dl.nums*100) + '\r')
    #     sys.stdout.flush()
    # print("《一念永恒》下载完成")
    '''
        For Figure
    '''
    target = "https://unsplash.com/napi/feeds/home"
    headers = {'Referer': 'https://unsplash.com/', 
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-Dest': 'empty',
               'Sec-Fetch-Site': 'same-origin',
               'Host': 'unsplash.com',
               'Connection': 'keep-alive',
               'Set-Cookie': 'ugid=e2ca36e0d8116d0755dbadc9462313ab5357198;domain=.unsplash.com;path=/;expires=Sun, 05 Dec 2021 11:40:58 GMT;SameSite=None;Secure',
               'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    req = requests.get(url=target, headers = headers,verify=False)
    print(req.text)