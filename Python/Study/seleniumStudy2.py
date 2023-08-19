#크롤링을 위한 헤더 선언 (셀리니움)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#API 호출 받고 데이터 가공을 위한 헤더 선언
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize   

#UI를 만들기 위한 Tkinter 헤더 선언
import tkinter
import tkinter.ttk

#slack API 호출을 위한 헤더
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
# ###slack API 중 에러 발생하는 경우 방어##
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

#멀티프로세스 동작을 위한 헤더 선언
from multiprocessing import Process

#크롤링 동작 함수(메인 url, 검색어 입력) : 네이버 검색창에 검색 후 지식인 페이지로 이동하여 검색
def chromWebselenium(url,words):
    print('========web crawling========')
    browser = webdriver.Chrome()                                            #셀리니움 하기위한 크롬드라이버 선언
    browser.get(url)                                                        #url을 받아 웹페이지 오픈
    time.sleep(0.5)                                                         #대기 0.5초
    searchElement = browser.find_element(By.CLASS_NAME,"search_input")      #검색창 class name을 찾기
    searchElement.send_keys("지식인")                                         #찾은 검색창에 "지식인" 단어 검색
    searchElement.send_keys(Keys.ENTER)                                     #찾은 클래스 엔터 버튼 입력
    time.sleep(0.5)                                                         #시간 대기
    gisikElement=browser.find_element(By.CLASS_NAME,"direct_link")          #바로가기 링크가 걸린 element 찾기
    gisikElement.click()                                                    #찾은 element 클릭
    time.sleep(1)                                                           #시간 대기
    browser.switch_to.window(browser.window_handles[1])                     #새 창이 띄워지니 창 바꾸기
    qnaElement=browser.find_element(By.XPATH,'//*[@id="au_lnb"]/li[2]/a')   #Xpath 찾기
    qnaElement.click()
    time.sleep(1)
    wordEle=browser.find_element(By.CLASS_NAME,"keyword")                   #키워드 입력 칸 찾기
    wordEle.send_keys(words)                                                #ui에서 입력 받은 단어 입력
    wordEle.send_keys(Keys.ENTER)                                           #엔터 버튼 입력
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[2])                     #새로운 창으로 다시 변경

#    bs=BeautifulSoup(browser.get(),"html")                                  #웹 페이지 html 정보를 저장
    print('========web crawling end========')

#api 통신하는 함수
def testApi():
    print("========API Read Start========")
    url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList'        #공공기관 데이터의 api를 받아오는 url 
    #api 통신 시 필수 파라미터, 해당 사이트에서 예시 확인 가능하고 파라미터의 정보를 알 수 있음
    params ={'ServiceKey' : '+q2XavISdGORP3SFmXN1u1GiJ0txKilEypOyuFY4d7sN6qLrPL97cTiVLc0B8lr5JcaVok3nacBd59XJ4HaERA==', 
    'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'HR', 
    'startDt' : '20230813', 'startHh' : '01', 'endDt' : '20230814', 'endHh' : '01', 'stnIds' : '119' }

    response = requests.get(url, params=params)                             #파라미터를 요청해서 받아오기
    json_text = json.loads(response.text)                                   #json 형태로 요청했기 때문에 json문자열을 python 객체로 변환(반대로 python 객체를 json으로 바꿀 땐 dumps)
    jsonexport=json_text['response']['body']['items']['item']               #resopnse의 body/items/item 하위의 정보만 저장
    dataFrame=pd.json_normalize(jsonexport)                                 #복잡한 데이터 구조를 pandas구조로 변경하기 위해 사용하는 함수(.json_normalize())
    print(dataFrame)                                                        
    print("========API Read End========")

def slackMsg(word):
    print("=========slack msg start============")
    slack_token='xoxb-5765068503152-5765674771664-Vtv8C2HF7ZZCkfHrvjpGUJvH' #슬랙 토근 입력
    channelID = 'C05MTQZU8QK'                                               #채널 ID 입력
    response=requests.post("https://slack.com/api/chat.postMessage",        #슬랙 API 통신 요청 : "슬랙 메신저 보내는 API url"
        headers={"Authorization":"Bearer "+slack_token},                    #핸들러 선언 : ("Authorization":"Bearer"+슬랙 토큰 입력)
        data={"channel":channelID,"text":word})                             #data 선언 : ("channel":채널ID, "text":보낼 메시지 작성)
    print("=========slack msg end============")

    
def multiProcess(url,word):
    start=time.time()                                                       #첫 동작하는 시간 저장
    print("멀티 프로세스 시작")
    p1=Process(target=chromWebselenium(url,word))                           #첫 번째 병렬 프로세스 선언 
    p2=Process(target=testApi())                                            #두 번째 병렬 프로세스 선언
    p3=Process(target=slackMsg(word))                                       #세 번째 병렬 프로세스 선언
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("멀티")
    print(time.time()-start)                                                #소비되는 시간 출력 (현재 시간 - 첫 동작 시간)

#병별 멀티 프로세스로 동작시키기 위해 main으로 선언
if __name__ =="__main__":
    window = tkinter.Tk()                                                   #tkinter 선언
    window.geometry("300x250+500+500")                                      #윈도우 창 사이즈, 시작 좌표 설정
    titleLable=tkinter.Label(window, text="MultiProcess / Api / WebCrawling",anchor="c")
    titleLable.place(relwidth=0.98)
    urltext=tkinter.Label(window,text="Crawling Url : ")
    urltext.place(rely=0.13)
    inputUrl=tkinter.Entry(window,width=20)
    inputUrl.place(relwidth=0.99, rely=0.23)
    wordtext=tkinter.Label(window, text="Search Word :")
    wordtext.place(rely=0.35)
    inputwords=tkinter.Entry(window,width=20)
    inputwords.place(relwidth=0.99, rely=0.45)
    proBtn=tkinter.Button(window,text="Test Button",command=lambda:multiProcess(inputUrl.get(),inputwords.get()))
    proBtn.place(rely=0.7,relwidth=1)
    window.mainloop()
    