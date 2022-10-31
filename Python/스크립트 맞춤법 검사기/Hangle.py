import tkinter
from tkinter import filedialog
from openpyxl import load_workbook
import pathlib
import os

#윈도우 생성하기 
window = tkinter.Tk()

window.title("스크립트 맞춤법 검사기")
window.geometry("350x120+200+200")
window.resizable(False,False)

######비슷한 구조의 대사함수 리스트화 하기######
# "NPC","대사" : 두번째 인자에 대사 나오는 함수
sayfunc = ['sayface', 'askYesNoface']
# "대사" : 바로 대사 나오는 함수
sayScreenc= ['adventuretpcheck']

#####함수 부분####
#대사 부분만 출력하기
def extraction(text):
    #대사 함수 추출해서 저장하기
    funcName_index= text.find("(")
    func_sentence = text[:funcName_index]
    func_sentence=func_sentence.lstrip()
    
    #추출한 대사 함수랑 대사 리스트들 비교하기
    for sf in range(0,len(sayfunc)):    #"이름","대사"  구조인 경우 추출하는 함수
        if (sayfunc[sf] == func_sentence):
            if (text.find(sayfunc[sf]) != -1):
                # NPC or 유저 이름 " 시작 전까지 제거
                sentenceStart_index = text.find('"')
                sentence = text[sentenceStart_index+1:]
                # NPC or 유저 이름 " 끝까지 제거
                sentenceStart_index = sentence.find('"')
                sentence = sentence[sentenceStart_index+1:]
                # 대사 시작 " 전까지 제거 
                sentenceStart_index = sentence.find('"')
                sentence = sentence[sentenceStart_index+1:]
                # 대사 중 마지막 " 이후로 제거
                sentenceEnd_index = sentence.find('"')
                sentence = sentence[:sentenceEnd_index]
                print(sf,sentence)
                return sentence
        
        elif (sayfunc[sf] != None): #"대사" 구조인 경우 바로 추출하는 함수
            for sf2 in range(0, len(sayScreenc)):
                if(sayScreenc[sf2]==func_sentence):
                    # 첫 " 전까지의 모든 내용 지우기
                    sentenceStart_index = text.find('"')
                    sentence = text[sentenceStart_index+1:]
                    # 대사 마지막의 " 전까지만 추출하기
                    sentenceEnd_index = sentence.find('"')
                    sentence = sentence[:sentenceEnd_index]
                    print(sf2,sentence)
                    return sentence

        else:
            print(func_sentence)
            pass
        
#파일 오픈 함수
def txtFileOpen():

    #파일 탐색기 오픈
    txtfilename = filedialog.askopenfilename(initialdir="",title="Select File")

    ######엑셀 작업부분######
    #지정된 파일 불러오기 (뒤 인자값 xlsm 데이터 적용을 위함) !!!!!지금 테스트를 위해 T 파일로 해뒀으니 나중에 변경할 것!!!!!
    wb=load_workbook("ScriptCheckT.xlsm",read_only=False,keep_vba=True)#VBA 매크로 형태로 파일 오픈할 때 선언
    ws=wb['script']

    #엑셀에 값이 있는지 확인 후 빈 값 아니면 지우기
    row_check=5
    for r in ws.rows:
        for c in range(6):
            if(ws.cell(row=row_check, column=2+c).value == None):
                pass
            else:
                ws.cell(row=row_check, column=2+c).value = None
        row_check += 1
    print("빈값 처리 완료")

    #txt 파일 오픈하여 lines 리스트 변수에 저장
    path = pathlib.Path(txtfilename)
    with open(path,"r",encoding="utf16") as file: # !! utf16은 .s파일 오픈할 때만... .txt
        try:
            lines = file.readlines()
        except UnicodeError:
             with open(path,"r",encoding="utf8") as file:
                lines = file.readlines()
        
        #한 줄 씩 엑셀에 값 입력하기
        j=5
        for line in lines:
            scriptSentence = extraction(line)
            if(scriptSentence != None):
                ws.cell(row=j, column=2).value = scriptSentence
                j+=1
            else:
                pass

    #!!!!!!!! 파일명 나중에 다시 변경해주기!!!!!
    wb.save("ScriptCheckT.xlsm")

    os.system("start ScriptCheckT.xlsm")  #노트북에선 주석처리
    
    print("end")

#UI 부분
fucLabelFrame=tkinter.LabelFrame(window, text="스크립트 변환 파일 선택")
fucLabelFrame.place(relx=0.01,relwidth=0.98,relheight=0.8)

nameLabel=tkinter.Label(window, text=" @hjong  @jeonyul  @parkjs", bg="black",fg="white")
nameLabel.place(relx=0.5,rely=0.82)

fileOpenBtn = tkinter.Button(fucLabelFrame, width=20, text="파일 불러오기", command=txtFileOpen)
fileOpenBtn.place(relx=0.25, rely=0.3)

label1 = tkinter.Label(fucLabelFrame, text="a")
label1.place()

window.mainloop()