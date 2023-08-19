import tkinter
import tkinter.ttk
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time


window=tkinter.Tk()
window.title('CaseManager State Tool')
window.geometry("380x300+100+30")
window.resizable(False,False)

######################################
######각 동작 별 함수 만들기############
#######################################
def crwaling(sitNumList):
    #저장된 login파일 읽어오기
    with open("login.txt",'r') as f:
        loginInfo=f.readlines()

    #0 = ID, 1=PassWord
    loginInfo=loginInfo[0].split('/')
    
    browser = webdriver.Chrome()
    action = ActionChains(browser)
    url = "https://casemanager.nexon.com"
    response = requests.get(url)
    response.raise_for_status()
    browser.maximize_window()
    browser.get(url)
    time.sleep(2)

    #로그인 하기
    idElement = browser.find_element(By.ID,"login-id")
    idElement.send_keys(loginInfo[0])

    passwardElement = browser.find_element(By.ID,"login-password")
    passwardElement.send_keys(loginInfo[1])
    passwardElement.send_keys(Keys.ENTER)
    time.sleep(2)
    print("로그인 동작 끝") 

    #로그인 완료 후 프로젝트 찾아 이동하기
    browser.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/a[1]/div/span').click()
    time.sleep(2)
    
    projectName=browser.find_element(By.CLASS_NAME,'mantine-Input-input.mantine-Select-input.mantine-gkdfdy')
    projectName.send_keys(stateCombo.get())
    time.sleep(0.5)
    action.send_keys(Keys.ARROW_DOWN)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(0.5)
    print("프로젝트 페이지 접속 동작 끝")
    
    # 진행중 폴더 하위 활성화
    browser.find_element(By.CLASS_NAME,"folderTree-item-displayName").click()
    time.sleep(1)
    print("콘텐츠 폴더 열기 동작 끝")

    #폴더 내 콘텐츠 폴더 받아오기
    contentList=browser.find_elements(By.CLASS_NAME,"folder-browse-content-group") #콘텐츠 폴더 번호 저장한 리스트
    print(len(contentList))
    for count in range(0,len(contentList)):
        print(count, contentList[count].text)
        browser.find_element(By.XPATH,'//*[@id="cell-ag-Grid-AutoColumn-{}"]/span'.format(6*count+1)).send_keys(Keys.ENTER)
        time.sleep(0.5)

    print("완료 후 대기")

#Text에 입력한 값을 리스트로 받아오고 빈 값을 제거
def sitNumInput():
    sitNumText=listbox.get("1.0",tkinter.END)
    sitNumList=sitNumText.split("\n")
    sitNumList=list(filter(None,sitNumList))    #빈값제거하는 아주 신박한 방법,,,,
    return sitNumList

#로그인 정보를 메모장에 저장하는 동작
def save(id,passwd):
    if(id and passwd != ""):
        tkinter.messagebox.showinfo(title="로그인 정보 저장",message="로그인 정보를 저장하였습니다.")
        with open("login.txt",'w') as f:
            f.writelines(id)
            f.write('/')
            f.writelines(passwd)
    else:
        tkinter.messagebox.showerror(title="로그인 정보 저장",message="로그인 정보를 입력해주세요")

#로그인 정보 메모장에서 삭제
def removeID():
    with open("login.txt",'w') as f:
            f.writelines('')
    tkinter.messagebox.showerror(title="로그인 정보 삭제",message="로그인 정보를 삭제하였습니다.")

#새로운 윈도우 만들어 오픈하고 로그인 정보 입력
def settingID():
    global settingPage
    settingPage = tkinter.Toplevel(window)
    settingPage.geometry("230x150+150+50")

    idLabelFrame = tkinter.LabelFrame(settingPage,text="웹오피스 정보 입력")
    idLabelFrame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
    idLabel = tkinter.Label(idLabelFrame,text="ID :")
    idLabel.place(relx=0.01,rely=0.05)
    idEntry = tkinter.Entry(idLabelFrame)
    idEntry.place(relx=0.01,rely=0.25)

    passWdLabel = tkinter.Label(idLabelFrame,text="Password : ")
    passWdLabel.place(relx=0.01,rely=0.5)
    passWdEntry = tkinter.Entry(idLabelFrame,show="*")
    passWdEntry.place(relx=0.01,rely=0.7)

    entrybtn=tkinter.Button(idLabelFrame,text="저장",command=lambda:save(idEntry.get(),passWdEntry.get()))
    entrybtn.place(relx=0.68,rely=0.25,relwidth=0.3,relheight=0.6)

#실제 메인 동작하는 함수
def mainFunc():
    #콤보 박스 2개 중 하나라도 선택 안했을 경우 동작 x
    if(stateCombo.get() and stateCombo2.get() == ""):
        tkinter.messagebox.showerror(title="Error",message="국가 및 테스트 상태 선택 확인해주세요")
    else:
        #Text에 입력한 값 리스트로 저장    
        sitNumList=sitNumInput()
        #로그인 등등... 크롤링 시작
        crwaling(sitNumList)
    

testLabel = tkinter.Label(window,text="CaseManager State Tool")
testLabel.place(relx=0.02, rely=0.02)


testLabelFrame=tkinter.LabelFrame(window,text="테스트 시트명",)
testLabelFrame.place(relx=0.01, rely=0.1,width=190,height=230)
listbox = tkinter.Text(testLabelFrame)
listbox.place(relx=0.01, rely=0.01,relheight=0.98,relwidth=0.97)

settingLabelFrame=tkinter.LabelFrame(window,text="세팅")
settingLabelFrame.place(relx=0.52,rely=0.1,width=180,height=230)

stateText = tkinter.Label(settingLabelFrame, text="국가 선택")
stateText.place(relx=0.01, rely=0.1)
stateCombo = tkinter.ttk.Combobox(settingLabelFrame,values=["메이플 QA팀(국내)","메이플 QA팀(북미)","메이플 QA팀(일본)","메이플 QA팀(중국)","메이플 QA팀(대만)","메이플 QA팀(싱가폴)"])
stateCombo.place(relx=0.01,rely=0.18)
stateText2 = tkinter.Label(settingLabelFrame, text="테스트 상태 선택")
stateText2.place(relx=0.01, rely=0.4)
stateCombo2 = tkinter.ttk.Combobox(settingLabelFrame,values=["테스트 중","테스트 완료"])
stateCombo2.place(relx=0.01,rely=0.48)
settingLabel = tkinter.Button(settingLabelFrame, text="로그인 정보 입력", width=22,command=settingID)
settingLabel.place(relx=0.01,rely=0.65)
settingLabel2 = tkinter.Button(settingLabelFrame, text="로그인 정보 삭제", width=22,command=removeID)
settingLabel2.place(relx=0.01,rely=0.85)

testLabel2 = tkinter.Button(window, text="Start",width=52, command=mainFunc)
testLabel2.place(relx=0.01, rely=0.88)

window.mainloop()
print("test")