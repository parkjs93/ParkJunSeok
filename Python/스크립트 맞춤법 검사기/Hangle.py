import tkinter
from tkinter import filedialog
from openpyxl import load_workbook

#윈도우 생성하기 
window = tkinter.Tk()

window.title("스크립트 맞춤법 검사기")
window.geometry("350x200+200+200")
window.resizable(False,False)

#함수 부분
def txtFileOpen():
    #파일 탐색기 오픈
    txtfilename = filedialog.askopenfilename(initialdir="",title="Select File")
    print(txtfilename)

    ######엑셀 작업부분######
    #지정된 파일 불러오기 (뒤 인자값 xlsm 데이터 적용을 위함)
    wb=load_workbook("Script Check.xlsm",read_only=False, keep_vba=True)
    ws=wb['script']

    #txt 파일 오픈하여 lines 리스트 변수에 저장
    with open(txtfilename,"r",encoding="utf8") as file:
        lines = file.readlines()

        #한 줄 씩 엑셀에 값 입력하기
        j=0
        for line in lines:
            ####여기에 sayface 함수 조건문 및 슬라이싱 넣기
            ws.cell(row=5+j, column=2).value=str(line)
            j+=1

    wb.save("Script CheckT.xlsm")



#UI 부분
fucLabelFrame=tkinter.LabelFrame(window, text="스크립트 변환 파일 선택")
fucLabelFrame.place(relx=0.01,relwidth=0.98,relheight=0.8)

nameLabel=tkinter.Label(window, text=" @hjong @jeonyul @parkjs")
nameLabel.place(relx=0.5,rely=0.82)

fileText1 = tkinter.Label(fucLabelFrame, text="파일 선택")
fileText1.place(relx=0.05,rely=0.1)

fileOpenBtn = tkinter.Button(window, width=20, text="파일 불러오기", command=txtFileOpen)
fileOpenBtn.place(relx=0.25, rely=0.4)


label1 = tkinter.Label(fucLabelFrame, text="a")
label1.place()
####

window.mainloop()