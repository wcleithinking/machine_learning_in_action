from time import sleep
import json
import urllib.request

def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
    sleep(5)
    pg = urllib.request.urlopen("http://www.baidu.com")
    print(pg.read())
    return pg