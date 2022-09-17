import os
from tkinter import messagebox, ttk
from turtle import title
import pyperclip
import tkinter
import tkinter.ttk
from tkinter.ttk import LabelFrame

window = tkinter.Tk()

window.title("스킬 테스트 도구")
window.geometry("515x650+100+100")
#window.wm_iconbitmap('iccon.ico')
window.resizable(False,False)

#################노트 만들기#################
note = tkinter.ttk.Notebook(window, width=510, height=600)
note.pack()
#노트에 프레임 추가
d_note = tkinter.Frame(window)
f_note = tkinter.Frame(window)
c_note = tkinter.Frame(window)
b_note = tkinter.Frame(window)
test_note = tkinter.Frame(window)
test2_note = tkinter.Frame(window)
stat_PAD_note=tkinter.Frame(window)
archiving_note =tkinter.Frame(window)


#활성화된 탭 종료하는 함수
def ui_active():
    if(note.tabs()==('.!frame',)):      #.tabs() -> 탭이름을 가져오는 함수 (탭 이름과 탭 text는 다르다.)
        print(note.tabs())
        note.forget(d_note)             #탭 삭제
    elif(note.tabs()==('.!frame2',)):
        print(note.tabs())
        note.forget(f_note)
    elif(note.tabs()==('.!frame3',)):
        print(note.tabs())
        note.forget(c_note)
    elif(note.tabs()==('.!frame4',)):
        print(note.tabs())
        note.forget(b_note)
    elif(note.tabs()==('.!frame5',)):
        print(note.tabs())
        note.forget(test_note)
    elif(note.tabs()==('.!frame6',)):
        print(note.tabs())
        note.forget(test2_note)
    elif(note.tabs()==('.!frame7',)):
        print(note.tabs())
        note.forget(stat_PAD_note)
    elif(note.tabs()==('.!frame8',)):
        print(note.tabs())
        note.forget(archiving_note)
    else:
        print(note.tabs())

#하위 메뉴 선택 시 동작할 함수 (하위 메뉴 선택 시 해당 노트 출력되도록)
def note_State(category):
    if (category=="damage"):
        ui_active()
        note.add(d_note, text="데미지 계산기")
    elif(category=="final"):
        ui_active()
        note.add(f_note, text="최종데미지, 방어율무시")
    elif(category=="cool"):
        ui_active()
        note.add(c_note,text="쿨타임 감소")
    elif(category=="buff"):
        ui_active()
        note.add(b_note,text="버프 지속 시간")
    elif(category=="testmob"):
        ui_active()
        note.add(test_note, text="테스트용 몹")
    elif(category=="setting"):
        ui_active()
        note.add(test2_note, text="세팅 명령어")
    elif(category=="statPAD"):
        ui_active()
        note.add(stat_PAD_note, text="스텟 공격력")
    elif(category=="archiving"):
        ui_active()
        note.add(archiving_note, text="스킬 아카이빙")
    else:
        print(category)

def test_ui():
    #웹 페이지 띄우기 함수
    #os.system('start https://nexono365.sharepoint.com/:x:/s/-QA-maple-9/EWSrLR6HO0lPrbKwHGybhSYBQvKGNBvD6X0iTkso9uvj_w?e=hPC9N2')
    #print(stat_pad_combobox.get())
    #print(a)
    helpPage=tkinter.Toplevel(window)
    helpPage.title("도움말")
    helpPage.geometry("300x300+500+300")
    helptext=tkinter.Label(helpPage, text="스킬 관련 설명")
    helptext.place(x=10, y=10)

#메뉴바 추가
menubar = tkinter.Menu(window)
#하위 메뉴 추가
menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="스킬 데미지 수치", command=lambda:note_State("damage"))
menu_1.add_command(label="최종뎀, 방무", command=lambda:note_State("final"))
menu_1.add_command(label="쿨타임 감소", command=lambda:note_State("cool"))
menu_1.add_command(label="버프 지속 시간", command=lambda:note_State("buff"))
menu_1.add_command(label="테스트용 몹", command=lambda:note_State("testmob"))
menu_1.add_command(label="세팅 명령어", command=lambda:note_State("setting"))
menu_1.add_command(label="스텟 공격력", command=lambda:note_State("statPAD"))
menu_1.add_command(label="스킬 아카이빙", command=lambda:note_State("archiving"))
menu_1.add_separator()
menu_1.add_command(label="리셋", command=ui_active)
menu_1.add_command(label="테스트", command=test_ui)

menubar.add_cascade(label="테스트 항목 선택", menu=menu_1)   #상위 메뉴 이름 지정
window.config(menu=menubar)

#################버튼 동작#################
#스공 계산
def stat_cal_test(jobBtn):
    weapon_constant=float(input_constant.get()) #무기 상수
    pad = float(input_pad.get()) #공/마
    mainstat = float(input_mainStat.get()) #주스텟
    substat1 = float(input_subStat1.get()) #부스텟1
    substat2 = float(input_subStat2.get()) #부스텟2
    pureHP = float(input_pureHP.get()) #순수체력
    addHP = float(input_addHP.get()) #증가체력
    finalDam = 1+float(input_finalDam.get())/100
    addDam=1+float(input_addDam.get())/100

    #공격방식 편차
    if(stat_pad_combobox.get()=="근접공격"):
        deviation=float(0.2)
    elif(stat_pad_combobox.get()=="원거리공격"):
        deviation=float(0.15)
    elif(stat_pad_combobox.get()=="마법공격"):
        deviation=float(0.25)
    else:
        deviation=0

    #무기 상수 보정
    if(stat_pad_combobox2.get()=="히어로"):
        addConstant=0.1
    elif(stat_pad_combobox2.get()=="모험가 마법사"):
        addConstant=0.2
    else:
        addConstant=0    

    #스공 계산 공식
    if(jobBtn=="nomal"):
        resultMAXPAD=round((mainstat*4+substat1+substat2)/100*(pad*weapon_constant+addConstant),0) #(주스텟*4+부스텟1+부스텟2)/100*(공/마*무기상수+보정상수)
        resultMINPAD=round(resultMAXPAD*deviation,0) #근접공격 데미지 편차 적용...
        result_nomalstat_pad.config(text=str(resultMINPAD)+"\t~\t"+str(resultMAXPAD)) #뎀증 효과 없는 스텟 공격력
        result_addstat_pad.config(text=str(round(resultMINPAD*finalDam*addDam,0))+"\t~\t"+str(round(resultMAXPAD*finalDam*addDam,0)))    #뎀증 효과 적용된 스텟 공격력
    elif(jobBtn=="xenon"):
        resultMAXPAD=round(((mainstat+substat1+substat2)*3.5)/100*(pad*weapon_constant),0) #((주스텟+부스텟1+부스텟2)*3.5/100*(공/마*무기상수))
        resultMINPAD=round(resultMAXPAD*deviation,0)
        result_nomalstat_pad.config(text=str(resultMINPAD)+"\t~\t"+str(resultMAXPAD)) #뎀증 효과 없는 스텟 공격력
        result_addstat_pad.config(text=str(round(resultMINPAD*finalDam*addDam,0))+"\t~\t"+str(round(resultMAXPAD*finalDam*addDam,0)))   #뎀증 효과 적용된 스텟 공격력
    elif(jobBtn=="demon"):
        resultMAXPAD=round(((pureHP+(addHP*0.8))/7+substat1)/100*(pad*weapon_constant),0) #((순수체력 + (추가체력*0.8))/7+부스텟(str))/100*(공/마*무기상수)
        resultMINPAD=round(resultMAXPAD*deviation,0)
        result_nomalstat_pad.config(text=str(resultMINPAD)+"\t~\t"+str(resultMAXPAD)) #뎀증 효과 없는 스텟 공격력
        result_addstat_pad.config(text=str(round(resultMAXPAD*finalDam*addDam,0))+"\t~\t"+str(round(resultMAXPAD*finalDam*addDam,0)))   #뎀증 효과 적용된 스텟 공격력
    # elif(jobBtn=="dual"):
    #     resultMAXPAD=round((mainstat*4+substat1+substat2)/100*(pad*weapon_constant),0) #(주스텟*4+부스텟1+부스텟2)/100*(공/마*무기상수)
    #     resultMINPAD=round(resultMAXPAD*deviation,0)
    #     result_nomalstat_pad.config(text=str(resultMINPAD)+"\t~\t"+str(resultMAXPAD))  #뎀증 효과 적용되지 않은 스텟 공격력
    #     result_addstat_pad.config(text=str(round(resultMINPAD*finalDam*addDam,0))+"\t~\t"+str(round(resultMAXPAD*finalDam*addDam,0)))   #뎀증 효과 적용된 스텟 공격력
    else:
        result_nomalstat_pad.config(text="error")
        result_addstat_pad.config(text="error")
    
def calc(tab):
    if(tab=="damage"):
        #데미지 계산 
        stat_PadMin=float(stat_input1.get()) #최소 스공
        stat_PadMax=float(stat_input2.get()) #최대 스공
        skill_Damage=float(stat_input3.get()) #스킬 데미지
        mob_Pddr=float(stat_input4.get())   #몹 방무
        stat_Cri=float(stat_input5.get())   #크뎀증
        stat_DamP1=float(stat_input6.get()) #뎀증1
        stat_DamP2=float(stat_input7.get()) #뎀증2
        stat_DamP3=float(stat_input8.get()) #뎀증3
        stat_DamP4=float(stat_input9.get()) #뎀증4
        stat_FDamP1=float(stat_input10.get()) #최종뎀증1
        stat_FDamP2=float(stat_input11.get()) #최종뎀증2
        stat_FDamP3=float(stat_input12.get()) #최종뎀증3
        stat_FDamP4=float(stat_input13.get()) #최종뎀증4
        stat_FDamP5=float(stat_input14.get()) #최종뎀증5
        stat_FDamP6=float(stat_input15.get()) #최종뎀증6
        stat_FDamP7=float(stat_input16.get()) #최종뎀증7
        stat_FDamP8=float(stat_input17.get()) #최종뎀증8
        stat_FDamP9=float(stat_input18.get()) #최종뎀증9

        #최소 스공 값
        nomalMinDamage = (stat_PadMin*(skill_Damage/100)*(1+(stat_DamP1+stat_DamP2+stat_DamP3+stat_DamP4)/100)*(1+(stat_FDamP1/100))*(1+(stat_FDamP2/100))*(1+(stat_FDamP3/100))*(1+(stat_FDamP4/100))*(1+(stat_FDamP5/100))*(1+(stat_FDamP6/100))*(1+(stat_FDamP7/100))*(1+(stat_FDamP8/100))*(1+(stat_FDamP9/100))*(1+(-mob_Pddr)/100))
        stat_result_DamageMin.config(text=round(nomalMinDamage,3))

        #최대 스공 값
        nomalMaxDamage = (stat_PadMax*(skill_Damage/100)*(1+(stat_DamP1+stat_DamP2+stat_DamP3+stat_DamP4)/100)*(1+(stat_FDamP1/100))*(1+(stat_FDamP2/100))*(1+(stat_FDamP3/100))*(1+(stat_FDamP4/100))*(1+(stat_FDamP5/100))*(1+(stat_FDamP6/100))*(1+(stat_FDamP7/100))*(1+(stat_FDamP8/100))*(1+(stat_FDamP9/100))*(1+(-mob_Pddr)/100))
        stat_result_DamageMax.config(text=round(nomalMaxDamage,3))

        #최소 크리뎀 값(크뎀 x)
        nomalMinCriDamage = nomalMinDamage*1.2
        stat_result_NcriMin.config(text=round(nomalMinCriDamage,3))

        #최대 크리뎀 값(크뎀 x)
        nomalMaxCriDamage = nomalMaxDamage*1.5
        stat_result_NcriMax.config(text=round(nomalMaxCriDamage,3))

        #최소 크리뎀 값(크뎀 o)
        FinalMinCriDamage = nomalMinDamage*(1+((20+stat_Cri)/100))
        stat_result_CriMin.config(text=round(FinalMinCriDamage,3))

        #최대 크리뎀 값(크뎀 o)
        FinalMaxCriDamage = nomalMaxDamage*(1+((50+stat_Cri)/100))
        stat_result_CriMax.config(text=round(FinalMaxCriDamage,3))
    elif(tab=="final"):
        #최종뎀 계산
        F_input1 = float(finalDam_input1.get())
        F_input2 = float(finalDam_input2.get())
        F_input3 = float(finalDam_input3.get())
        F_input4 = float(finalDam_input4.get())
        F_input5 = float(finalDam_input5.get())
        F_input6 = float(finalDam_input6.get())

        F_result=(1*(1+F_input1/100)*(1+F_input2/100)*(1+F_input3/100)*(1+F_input4/100)*(1+F_input5/100)*(1+F_input6/100)-1)*100
        f_Dam_result2.config(text=str(round(F_result,3))+"%")

        ig_input1 = float(ignoreGuard_input1.get())
        ig_input2 = float(ignoreGuard_input2.get())
        ig_input3 = float(ignoreGuard_input3.get())
        ig_input4 = float(ignoreGuard_input4.get())
        ig_input5 = float(ignoreGuard_input5.get())

        ig_result=(1-(1-(ig_input1/100))*(1-(ig_input2/100))*(1-(ig_input3/100))*(1-(ig_input4/100))*(1-(ig_input5/100)))*100
        ignoreGuard_result2.config(text=str(round(ig_result,3))+"%")
    elif(tab=="cool"):
        #쿨타임 계산
        c_input1 = float(cooltime_input1.get())      #기본 쿨
        c_input2 = float(cooltime_input2.get())      #유니온 쿨감
        c_input3 = float(cooltime_input3.get())      #쿨감뚝

        c_result_union=c_input1*(1-(c_input2/100))
        c_time_result4.config(text=str(round(c_result_union,3))+"초")    #유니온 쿨감만

        c_result_item=c_input1-c_input3
        c_time_result6.config(text=str(round(c_result_item,3))+"초")    #쿨감 뚝만

        c_result_total=c_input1*(1-(c_input2/100))-c_input3
        c_time_result2.config(text=str(round(c_result_total,3))+"초")     #총 쿨감
    elif(tab=="buff"):
        #벞지 계산
        b_input1 = float(bufftime_input1.get())      #기본벞지
        b_input2 = float(bufftime_input2.get())      #유니온
        b_input3 = float(bufftime_input3.get())      #몬라
        b_input4 = float(bufftime_input4.get())      #어빌

        b_result_union=b_input1*(1+(b_input2/100))
        bufftime_result2.config(text=str(round(b_result_union,3))+"초")  #유니온 효과만

        b_result_monla=b_input1*(1+(b_input3/100))
        bufftime_result4.config(text=str(round(b_result_monla,3))+"초")    #몬라 효과만

        b_result_ability=b_input1*(1+(b_input4/100))
        bufftime_result6.config(text=str(round(b_result_ability,3))+"초")    #어빌 효과만

        b_result=b_input1*((b_input2/100)+(b_input3/100)+(b_input4/100))
        bufftime_result8.config(text=str(round(b_result,3))+"초")            #증가량만

        b_result_total= b_input1*(1+(b_input2/100)+(b_input3/100)+(b_input4/100))
        bufftime_result10.config(text=str(round(b_result_total,3))+"초")     #총 증가량

#명령어 복사
def copy(func):
    #명령어 클립보드 복사 
    if(func=="c1"):
        a="/cpsset 1 70000045 20"
        pyperclip.copy(a)    
    elif(func=="c2"):
        a="/createex 1002019 4 3 40557 40557 40557"
        pyperclip.copy(a)
    elif(func=="c3"):
        a="/fmcreate 9300881"
        pyperclip.copy(a)
    elif(func=="c4"):
        a="/runecreate 6"
        pyperclip.copy(a)
    elif(func=="b1"):
        a="/cpsset 1 70000048 40"
        pyperclip.copy(a)
    elif(func=="b2"):
        a="/fmcreate 2600800"
        pyperclip.copy(a) 
    elif(func=="m1"):
        a="/cpsset 1 70000047 10"
        pyperclip.copy(a)
    elif(func=="m2"):
        a="/fmcreate 9300752"
        pyperclip.copy(a)
    elif(func=="m3"):
        a="/create 1402224"
        pyperclip.copy(a)
    elif(func=="e1"):
        a="/cpsset 1 70000046 10"
        pyperclip.copy(a)
    elif(func=="e2"):
        a="/showskillactioninfo 1"
        pyperclip.copy(a)
    elif(func=="e3"):
        a="/hitdamagetestmsg 1"
        pyperclip.copy(a)
    elif(func=="e4"):
        a="/create 2436125"
        pyperclip.copy(a)
    elif(func=="mob1_1"):
        a="/summon 9501011"
        pyperclip.copy(a)
    elif(func=="mob1_2"):
        a="/summon 9501012"
        pyperclip.copy(a)
    elif(func=="mob1_3"):
        a="/summon 9501013"
        pyperclip.copy(a)
    elif(func=="mob1_4"):
        a="/create 2435744"
        pyperclip.copy(a)
    elif(func=="mob2_1"):
        a="/summon 9990000"
        pyperclip.copy(a)
    elif(func=="mob2_2"):
        a="/summon 9990009"
        pyperclip.copy(a)
    elif(func=="mob2_3"):
        a="/summon 9990023"
        pyperclip.copy(a)
    elif(func=="mob2_4"):
        a="/summon 9990085"
        pyperclip.copy(a)
    elif(func=="mob3_1"):
        a="/summon 9501000"
        pyperclip.copy(a)
    elif(func=="mob3_2"):
        a="/summon 9501001"
        pyperclip.copy(a)
    elif(func=="mob3_3"):
        a="/summon 9501002"
        pyperclip.copy(a)
    elif(func=="mob3_4"):
        a="/summon 9501003"
        pyperclip.copy(a)
    elif(func=="mob3_5"):
        a="/summon 9501004"
        pyperclip.copy(a)
    elif(func=="mob3_6"):
        a="/summon 9501005"
        pyperclip.copy(a)
    elif(func=="mob3_7"):
        a="/summon 9501006"
        pyperclip.copy(a)
    elif(func=="mob3_8"):
        a="/summon 9501007"
        pyperclip.copy(a)
    elif(func=="mob3_9"):
        a="/summon 9501008"
        pyperclip.copy(a)
    elif(func=="mob3_10"):
        a="/summon 9501009"
        pyperclip.copy(a)
    elif(func=="mob3_11"):
        a="/summon 9501010"
        pyperclip.copy(a)
    elif(func=="mob3_12"):
        a="/summon 8950103"
        pyperclip.copy(a)
    elif(func=="mob3_13"):
        a="/create 2022198"
        pyperclip.copy(a)

#입력칸 초기화동작
def clear(tab):
    if(tab=="damage"):
        #스킬 데미지 초기화
        stat_input1.delete(0,100)
        stat_input1.insert(0,"0")
        stat_input2.delete(0,100)
        stat_input2.insert(0,"0")
        stat_input3.delete(0,100)
        stat_input3.insert(0,"0")
        stat_input4.delete(0,100)
        stat_input4.insert(0,"0")
        stat_input5.delete(0,100)
        stat_input5.insert(0,"0")
        stat_input6.delete(0,100)
        stat_input6.insert(0,"0")
        stat_input7.delete(0,100)
        stat_input7.insert(0,"0")
        stat_input8.delete(0,100)
        stat_input8.insert(0,"0")
        stat_input9.delete(0,100)
        stat_input9.insert(0,"0")
        stat_input10.delete(0,100)
        stat_input10.insert(0,"0")
        stat_input11.delete(0,100)
        stat_input11.insert(0,"0")
        stat_input12.delete(0,100)
        stat_input12.insert(0,"0")
        stat_input13.delete(0,100)
        stat_input13.insert(0,"0")
        stat_input14.delete(0,100)
        stat_input14.insert(0,"0")
        stat_input15.delete(0,100)
        stat_input15.insert(0,"0")
        stat_input16.delete(0,100)
        stat_input16.insert(0,"0")
        stat_input17.delete(0,100)
        stat_input17.insert(0,"0")
        stat_input18.delete(0,100)
        stat_input18.insert(0,"0")
    elif(tab=="final"):
        #최종뎀 입력칸 초기화
        finalDam_input1.delete(0,100)
        finalDam_input1.insert(0,"0")
        finalDam_input2.delete(0,100)
        finalDam_input2.insert(0,"0")
        finalDam_input3.delete(0,100)
        finalDam_input3.insert(0,"0")
        finalDam_input4.delete(0,100)
        finalDam_input4.insert(0,"0")
        finalDam_input5.delete(0,100)
        finalDam_input5.insert(0,"0")
        finalDam_input6.delete(0,100)
        finalDam_input6.insert(0,"0")
        #방무 초기화
        ignoreGuard_input1.delete(0,100)
        ignoreGuard_input1.insert(0,"0")
        ignoreGuard_input2.delete(0,100)
        ignoreGuard_input2.insert(0,"0")
        ignoreGuard_input3.delete(0,100)
        ignoreGuard_input3.insert(0,"0")
        ignoreGuard_input4.delete(0,100)
        ignoreGuard_input4.insert(0,"0")
        ignoreGuard_input5.delete(0,100)
        ignoreGuard_input5.insert(0,"0")
    elif(tab=="cool"):
        #쿨타임 초기화
        cooltime_input1.delete(0,100)
        cooltime_input1.insert(0,"0")
        cooltime_input2.delete(0,100)
        cooltime_input2.insert(0,"0")
        cooltime_input3.delete(0,100)
        cooltime_input3.insert(0,"0")
    elif(tab=="buff"):
        #벞지 입력칸 초기화
        bufftime_input1.delete(0,100)
        bufftime_input1.insert(0,"0")
        bufftime_input2.delete(0,100)
        bufftime_input2.insert(0,"0")
        bufftime_input3.delete(0,100)
        bufftime_input3.insert(0,"0")
        bufftime_input4.delete(0,100)
        bufftime_input4.insert(0,"0")
    elif(tab=="stat"):
        input_constant.delete(0,100)
        input_constant.insert(0,"0")
        input_pad.delete(0,100)
        input_pad.insert(0,"0")
        input_mainStat.delete(0,100)
        input_mainStat.insert(0,"0")
        input_subStat1.delete(0,100)
        input_subStat1.insert(0,"0")
        input_subStat2.delete(0,100)
        input_subStat2.insert(0,"0")
        input_pureHP.delete(0,100)
        input_pureHP.insert(0,"0")
        input_addHP.delete(0,100)
        input_addHP.insert(0,"0")
        input_finalDam.delete(0,100)
        input_finalDam.insert(0,"0")
        input_addDam.delete(0,100)
        input_addDam.insert(0,"0")

#도움말 출력
def helpBtn():
    helpPage=tkinter.Toplevel(window)
    helpPage.title("도움말")
    helpPage.geometry("400x550+200+200")

    helpTitle=""
    helpMessage=""

    helpText=tkinter.Message(helpPage,text=helpTitle,width="350", anchor="w",bg="yellow")
    helpText.pack()
    helpText=tkinter.Message(helpPage,text=helpMessage,width="350", anchor="w",bg="yellow")
    helpText.pack()

#아카이빙 쉐어포인트 웹으로 이동
def connect_shearpoint(job):
    if (job == "hero"):
        os.system('start https://nexono365.sharepoint.com/:x:/r/sites/-QA-maple/_layouts/15/Doc.aspx?sourcedoc=%7BB0DDE059-ED1D-4AC4-BEEC-993E9562C4C1%7D&file=%ED%9E%88%EC%96%B4%EB%A1%9C.xlsm&action=default&mobileredirect=true')
    elif (job=="firepoison"):
        print(job)
    elif (job=="bowmaster"):
        print(job)
    elif (job=="nightroad"):
        print(job)
    elif (job=="viper"):
        print(job)    
    elif (job=="paladin"):
        print(job)
    elif (job=="icelightning"):
        print(job)
    elif (job=="crossbowmaster"):
        print(job)
    elif (job=="shadower"):
        print(job)
    elif (job=="captain"):
        print(job)
    elif (job=="darknight"):
        print(job)
    elif (job=="bishop"):
        print(job)
    elif (job=="pathfinder"):
        print(job)
    elif (job=="dualblade"):
        print(job)
    elif (job=="cannonshooter"):
        print(job)
    elif (job=="soulmaster"):
        print(job)
    elif (job=="flamewizard"):
        print(job)
    elif (job=="windbreaker"):
        print(job)
    elif (job=="nightwalker"):
        print(job)
    elif (job=="striker"):
        print(job)
    elif (job=="mihile"):
        print(job)
    elif (job=="blaster"):
        print(job)
    elif (job=="battlemage"):
        print(job)
    elif (job=="wildhunter"):
        print(job)
    elif (job=="xenon"):
        print(job)
    elif (job=="mechanic"):
        print(job)
    elif (job=="demonslayer"):
        print(job)   
    elif (job=="demonavenger"):
        print(job)
    elif (job=="aran"):
        print(job)
    elif (job=="evan"):
        print(job)
    elif (job=="mercedes"):
        print(job)
    elif (job=="phantom"):
        print(job)
    elif (job=="eunwol"):
        print(job)
    elif (job=="luminous"):
        print(job)
    elif (job=="kaiser"):
        print(job)
    elif (job=="kain"):
        print(job)
    elif (job=="cadena"):
        print(job)
    elif (job=="angelicbuster"):
        print(job)
    elif (job=="adele"):
        print(job)
    elif (job=="illium"):
        print(job)
    elif (job=="ark"):
        print(job)
    elif (job=="lala"):
        print(job)
    elif (job=="hoyoung"):
        print(job)
    elif (job=="zero"):
        print(job)
    elif (job=="kinesis"):
        print(job)
    else:
        print("error")

#################출처 달기#################
parkjs=tkinter.Label(window, text="MapleQA PARKJS (Ver.3)",fg="white",bg="black")
parkjs.place(x=320, y=626)

#################라벨 만들기#################
#데미지 계산
lbf_calDam = LabelFrame(d_note)
lbf_calDam.place(relx=0.01,relwidth=0.98,relheight=0.65)
lbf_calDam_result = LabelFrame(d_note,text="result")
lbf_calDam_result.place(relx=0.01,rely=0.66,relwidth=0.98,relheight=0.34)

#최종뎀, 방무
lbf_FDam = LabelFrame(f_note)
lbf_FDam.place(relx=0.01,relwidth=0.98,relheight=0.70)

lbf_FDam_result = LabelFrame(f_note, text="result")
lbf_FDam_result.place(relx=0.01,rely=0.71,relwidth=0.98,relheight=0.29)

#쿨타임
lbf_cool = LabelFrame(c_note)
lbf_cool.place(relx=0.01,relwidth=0.98,relheight=0.50)

lbf_cool_result = LabelFrame(c_note, text="result")
lbf_cool_result.place(relx=0.01, rely=0.51, relwidth=0.98,relheight=0.99)

#벞지
lbf_buff = LabelFrame(b_note)
lbf_buff.place(relx=0.01,relwidth=0.98,relheight=0.50)

lbf_buff_result = LabelFrame(b_note, text="result")
lbf_buff_result.place(relx=0.01, rely=0.51, relwidth=0.98,relheight=0.99)


#테스트 몹
test_guide1=LabelFrame(test_note, text='속성 몬스터')
test_guide1.place(relx=0.01,relwidth=0.98,relheight=0.25)

test_guide2=LabelFrame(test_note, text='무형 몬스터')
test_guide2.place(relx=0.01, rely=0.26 ,relwidth=0.98,relheight=0.56)

test_guide3=LabelFrame(test_note, text='상태이상 몬스터')
test_guide3.place(relx=0.01, rely=0.57,relwidth=0.98,relheight=0.99)

#명령어
test_skill1 = LabelFrame(test2_note, text="쿨타임 감소")
test_skill1.pack(fill="both", expand="yes")

test_skill2 = LabelFrame(test2_note, text="버프 지속 시간")
test_skill2.pack(fill="both", expand="yes")

test_skill3 = LabelFrame(test2_note, text="몹, 어택 카운트 증가")
test_skill3.pack(fill="both", expand="yes")

test_skill4 = LabelFrame(test2_note, text="기타 명령어")
test_skill4.pack(fill="both", expand="yes")

#스텟 공격력
input_test_statPAD1=LabelFrame(stat_PAD_note)
input_test_statPAD1.place(relx=0.01, relwidth=0.98, relheight=0.69)

result_test_statPAD=LabelFrame(stat_PAD_note, text="result")
result_test_statPAD.place(relx=0.01, rely=0.70,relwidth=0.98, relheight=0.99)

#아카이빙
test_archiving1=LabelFrame(archiving_note, text="모험가")
test_archiving1.place(relx=0.01, relwidth=0.98, relheight=0.20)

test_archiving2=LabelFrame(archiving_note, text="시그너스")
test_archiving2.place(relx=0.01, rely=0.21, relwidth=0.98, relheight=0.15)

test_archiving3=LabelFrame(archiving_note, text="레지스탕스 & 데몬")
test_archiving3.place(relx=0.01, rely=0.37, relwidth=0.98, relheight=0.15)

test_archiving4=LabelFrame(archiving_note, text="영웅")
test_archiving4.place(relx=0.01, rely=0.52, relwidth=0.98, relheight=0.15)

test_archiving5=LabelFrame(archiving_note, text="노바 & 레프")
test_archiving5.place(relx=0.01, rely=0.68, relwidth=0.98, relheight=0.15)

test_archiving6=LabelFrame(archiving_note, text="아니마 & 제로 & 키네시스 ")
test_archiving6.place(relx=0.01, rely=0.84, relwidth=0.98, relheight=0.15)

#################버튼 만들기#################
#스킬 데미지 계산
d_calResetBut = tkinter.Button(lbf_calDam, text="적용", width=15, command=lambda:calc("damage"))
d_calResetBut.place(x=230, y=330)
d_calBut = tkinter.Button(lbf_calDam, text="초기화", width=15, command=lambda:clear("damage"))
d_calBut.place(x=350, y=330)
#최종 데미지 계산
f_calBut = tkinter.Button(lbf_FDam, text="적용", command=lambda:calc("final"), width=15)
f_calBut.place(x=255, y=330)
f_calResetBut = tkinter.Button(lbf_FDam, text="초기화", width=15, command=lambda:clear("final"))
f_calResetBut.place(x=380, y=330)
#쿨타임 계산
c_calBut = tkinter.Button(lbf_cool, text="적용", command=lambda:calc("cool"), width=15)
c_calBut.place(x=255, y=230)
c_calResetBut = tkinter.Button(lbf_cool, text="초기화", width=15, command=lambda:clear("cool"))
c_calResetBut.place(x=380, y=230)
#버프 지속시간 계산
b_calBut = tkinter.Button(lbf_buff, text="적용", command=lambda:calc("buff"), width=15)
b_calBut.place(x=255, y=230)
b_calResetBut = tkinter.Button(lbf_buff, text="초기화", width=15, command=lambda:clear("buff"))
b_calResetBut.place(x=380, y=230)
#스텟 공격력 계산
stat_pad_calBut1 = tkinter.Button(input_test_statPAD1, text="일반", width=12, command= lambda:stat_cal_test("nomal"))
stat_pad_calBut1.place(x=20, y=240)
stat_pad_calBut2 = tkinter.Button(input_test_statPAD1, text="제논", width=12, command= lambda:stat_cal_test("xenon"))
stat_pad_calBut2.place(x=140, y=240)
stat_pad_calBut3 = tkinter.Button(input_test_statPAD1, text="데몬어벤져", width=12, command= lambda:stat_cal_test("demon"))
stat_pad_calBut3.place(x=260, y=240)
# stat_pad_calBut3 = tkinter.Button(input_test_statPAD1, text="듀얼블레이드", width=12, command= lambda:stat_cal_test("dual"))
# stat_pad_calBut3.place(x=380, y=240)
stat_pad_combobox = ttk.Combobox(input_test_statPAD1, values=["근접공격","원거리공격","마법공격"])
stat_pad_combobox.set("데미지 편차(공격 방식)")
stat_pad_combobox.place(x=250, y=10)

stat_pad_combobox2 = ttk.Combobox(input_test_statPAD1, values=["히어로","모험가 마법사","기타"])
stat_pad_combobox2.place(x=250, y=50)
stat_pad_combobox2.set("무기 상수 보정(직업 선택)")

helpPageBtn=tkinter.Button(input_test_statPAD1, text="도움말", width=20, command=helpBtn)
helpPageBtn.place(x=100, y=280)

stat_pad_resetBut = tkinter.Button(input_test_statPAD1, text="초기화", width=20, command=lambda:clear("stat"))
stat_pad_resetBut.place(x=340, y=280)

#################데미지 계산 페이지#################
stat_text=tkinter.Label(lbf_calDam, text="MIN")
stat_text.place(x=255, y=5)
stat_text=tkinter.Label(lbf_calDam, text="MAX")
stat_text.place(x=380, y=1)

stat_inputtext1=tkinter.Label(lbf_calDam, text="스탯 공격력")
stat_inputtext1.place(x=10, y=25)
stat_input1=tkinter.Entry(lbf_calDam, width=20)
stat_input1.place(x=180, y=25)
stat_input1.insert(0,"0")
stat_input2=tkinter.Entry(lbf_calDam, width=20)
stat_input2.place(x=330, y=25)
stat_input2.insert(0,"0")

stat_inputtext2=tkinter.Label(lbf_calDam, text="스킬 데미지")
stat_inputtext2.place(x=10, y=65)
stat_input3=tkinter.Entry(lbf_calDam, width=41)
stat_input3.place(x=180, y=65)
stat_input3.insert(0,"0")

stat_inputtext3=tkinter.Label(lbf_calDam, text="몹 방어율")
stat_inputtext3.place(x=10, y=105)
stat_input4=tkinter.Entry(lbf_calDam, width=41)
stat_input4.place(x=180, y=105)
stat_input4.insert(0,"0")

stat_inputtext4=tkinter.Label(lbf_calDam, text="크리티컬 데미지 증가")
stat_inputtext4.place(x=10, y=145)
stat_input5=tkinter.Entry(lbf_calDam, width=41)
stat_input5.place(x=180, y=145)
stat_input5.insert(0,"0")

stat_inputtext4=tkinter.Label(lbf_calDam, text="데미지 증가 (보공 포함)")
stat_inputtext4.place(x=10, y=185)
stat_input6=tkinter.Entry(lbf_calDam, width=9)
stat_input6.place(x=180, y=185)
stat_input6.insert(0,"0")
stat_input7=tkinter.Entry(lbf_calDam, width=9)
stat_input7.place(x=255, y=185)
stat_input7.insert(0,"0")
stat_input8=tkinter.Entry(lbf_calDam, width=9)
stat_input8.place(x=330, y=185)
stat_input8.insert(0,"0")
stat_input9=tkinter.Entry(lbf_calDam, width=9)
stat_input9.place(x=405, y=185)
stat_input9.insert(0,"0")

stat_inputtext5=tkinter.Label(lbf_calDam, text="최종 데미지 증가")
stat_inputtext5.place(x=10, y=225)
stat_input10=tkinter.Entry(lbf_calDam, width=13)
stat_input10.place(x=180, y=225)
stat_input10.insert(0,"0")
stat_input11=tkinter.Entry(lbf_calDam, width=13)
stat_input11.place(x=280, y=225)
stat_input11.insert(0,"0")
stat_input12=tkinter.Entry(lbf_calDam, width=13)
stat_input12.place(x=380, y=225)
stat_input12.insert(0,"0")
stat_input13=tkinter.Entry(lbf_calDam, width=13)
stat_input13.place(x=180, y=260)
stat_input13.insert(0,"0")
stat_input14=tkinter.Entry(lbf_calDam, width=13)
stat_input14.place(x=280, y=260)
stat_input14.insert(0,"0")
stat_input15=tkinter.Entry(lbf_calDam, width=13)
stat_input15.place(x=380, y=260)
stat_input15.insert(0,"0")
stat_input16=tkinter.Entry(lbf_calDam, width=13)
stat_input16.place(x=180, y=295)
stat_input16.insert(0,"0")
stat_input17=tkinter.Entry(lbf_calDam, width=13)
stat_input17.place(x=280, y=295)
stat_input17.insert(0,"0")
stat_input18=tkinter.Entry(lbf_calDam, width=13)
stat_input18.place(x=380, y=295)
stat_input18.insert(0,"0")

stat_resultmin=tkinter.Label(lbf_calDam_result, text="MIN")
stat_resultmin.place(relx=0.5, rely=0.03)

stat_resultmax=tkinter.Label(lbf_calDam_result, text="MAX")
stat_resultmax.place(relx=0.8, rely=0.03)

stat_result_Damagetext=tkinter.Label(lbf_calDam_result, text="적용 데미지")
stat_result_Damagetext.place(relx=0.01, rely=0.2)
stat_result_DamageMin=tkinter.Label(lbf_calDam_result)
stat_result_DamageMin.place(relx=0.38, rely=0.2, relwidth=0.30)
stat_result_DamageMax=tkinter.Label(lbf_calDam_result)
stat_result_DamageMax.place(relx=0.68, rely=0.2, relwidth=0.30)

stat_result_Ncritext=tkinter.Label(lbf_calDam_result, text="크리티컬 데미지(기본)")
stat_result_Ncritext.place(relx=0.01, rely=0.45)
stat_result_NcriMin=tkinter.Label(lbf_calDam_result)
stat_result_NcriMin.place(relx=0.38, rely=0.45, relwidth=0.30)
stat_result_NcriMax=tkinter.Label(lbf_calDam_result)
stat_result_NcriMax.place(relx=0.68, rely=0.45, relwidth=0.30)

stat_result_Critical=tkinter.Label(lbf_calDam_result, text="크리티컬 데미지(증가 효과 적용)")
stat_result_Critical.place(relx=0.01, rely=0.7)
stat_result_CriMin=tkinter.Label(lbf_calDam_result)
stat_result_CriMin.place(relx=0.38, rely=0.7, relwidth=0.30)
stat_result_CriMax=tkinter.Label(lbf_calDam_result)
stat_result_CriMax.place(relx=0.68, rely=0.7, relwidth=0.30)

#################최종뎀 페이지#################
finalDam=tkinter.Label(lbf_FDam, text="최종데미지")
finalDam.place(x=20, y=5)

finalDam_input1 = tkinter.Entry(lbf_FDam)
finalDam_input1.place(x=70, y=40)
finalDam_input1.insert(0,"0")

finalDam_input2 = tkinter.Entry(lbf_FDam)
finalDam_input2.place(x=270, y=40)
finalDam_input2.insert(0,"0")

finalDam_input3 = tkinter.Entry(lbf_FDam)
finalDam_input3.place(x=70, y=75)
finalDam_input3.insert(0,"0")

finalDam_input4 = tkinter.Entry(lbf_FDam)
finalDam_input4.place(x=270, y=75)
finalDam_input4.insert(0,"0")

finalDam_input5 = tkinter.Entry(lbf_FDam)
finalDam_input5.place(x=70, y=115)
finalDam_input5.insert(0,"0")

finalDam_input6 = tkinter.Entry(lbf_FDam)
finalDam_input6.place(x=270, y=115)
finalDam_input6.insert(0,"0")

f_Dam_result=tkinter.Label(lbf_FDam_result, text="최종데미지 계산 결과(%) : ")
f_Dam_result.place(x=10, y=40)
f_Dam_result2=tkinter.Label(lbf_FDam_result)
f_Dam_result2.place(x=400, y=40)

#################방무 중첩 계산 페이지#################
ignoreGuard=tkinter.Label(lbf_FDam, text="방어율 무시 수치(%) : ")
ignoreGuard.place(x=20, y=170)

ignoreGuard_input1 = tkinter.Entry(lbf_FDam)
ignoreGuard_input1.place(x=70, y=210)
ignoreGuard_input1.insert(0,"0")

ignoreGuard_input2 = tkinter.Entry(lbf_FDam)
ignoreGuard_input2.place(x=270, y=210)
ignoreGuard_input2.insert(0,"0")

ignoreGuard_input3 = tkinter.Entry(lbf_FDam)
ignoreGuard_input3.place(x=70, y=250)
ignoreGuard_input3.insert(0,"0")

ignoreGuard_input4 = tkinter.Entry(lbf_FDam)
ignoreGuard_input4.place(x=270, y=250)
ignoreGuard_input4.insert(0,"0")

ignoreGuard_input5 = tkinter.Entry(lbf_FDam)
ignoreGuard_input5.place(x=70, y=290)
ignoreGuard_input5.insert(0,"0")

ignoreGuard_result=tkinter.Label(lbf_FDam_result, text="방어율 무시 계산 결과(%)  : ")
ignoreGuard_result.place(x=10, y=100)
ignoreGuard_result2=tkinter.Label(lbf_FDam_result) 
ignoreGuard_result2.place(x=400, y=100)

#################쿨타임 감소 페이지#################
cooltime1=tkinter.Label(lbf_cool, text="기존 쿨타임     :")
cooltime1.place(x=60, y=30)

cooltime_input1 = tkinter.Entry(lbf_cool)
cooltime_input1.place(x=280, y=30)
cooltime_input1.insert(0,"0")

cooltime2=tkinter.Label(lbf_cool, text="유니온 효과 %  :")
cooltime2.place(x=60, y=100)

cooltime_input2 = tkinter.Entry(lbf_cool)
cooltime_input2.place(x=280, y=100)
cooltime_input2.insert(0,"0")

cooltime3=tkinter.Label(lbf_cool, text="아이템 잠재 효과(초)  :")
cooltime3.place(x=60, y=170)

cooltime_input3 = tkinter.Entry(lbf_cool)
cooltime_input3.place(x=280, y=170)
cooltime_input3.insert(0,"0")

c_time_result3=tkinter.Label(lbf_cool_result, text="유니온 감소량 : ")
c_time_result3.place(x=10, y=30)
c_time_result4=tkinter.Label(lbf_cool_result)
c_time_result4.place(x=400, y=30)

c_time_result5=tkinter.Label(lbf_cool_result, text="잠재 효과 감소량 : ")
c_time_result5.place(x=10, y=80)
c_time_result6=tkinter.Label(lbf_cool_result)
c_time_result6.place(x=400, y=80)

c_time_result1=tkinter.Label(lbf_cool_result, text="총 감소량 : ")
c_time_result1.place(x=10, y=130)
c_time_result2=tkinter.Label(lbf_cool_result)
c_time_result2.place(x=400, y=130)

c_time_test1=tkinter.Label(lbf_cool_result, text=" * 참고 사항 (유니온 효과, 잠재 능력 효과)")
c_time_test1.place(x=20, y=165)
c_time_test2=tkinter.Label(lbf_cool_result, justify="left", text="1) 5차 스킬에 효과 적용\n2) 하이퍼 스킬에 효과 적용 되지 않음 \n3) 일정 시간마다 스택 쌓이는 스킬은 적용되지 않음 (ex. 하울링 게일)\n4) 잠재능력 효과 10초 이하는 10% 감소\n5) 잠재능력 효과 5초 미만으로 감소 불가")
c_time_test2.place(x=10, y=190)

#################버프 지속 시간 계산 페이지#################
bufftime1=tkinter.Label(lbf_buff, text="스킬 버프 시간 : ")
bufftime1.place(x=60, y=30)

bufftime_input1 = tkinter.Entry(lbf_buff)
bufftime_input1.place(x=280, y=30)
bufftime_input1.insert(0,"0")

bufftime2=tkinter.Label(lbf_buff, text="유니온 효과 % : ")
bufftime2.place(x=60, y=80)

bufftime_input2 = tkinter.Entry(lbf_buff)
bufftime_input2.place(x=280, y=80)
bufftime_input2.insert(0,"0")

bufftime3=tkinter.Label(lbf_buff, text="몬스터 라이프 효과 % : ")
bufftime3.place(x=60, y=130)

bufftime_input3 = tkinter.Entry(lbf_buff)
bufftime_input3.place(x=280, y=130)
bufftime_input3.insert(0,"0")

bufftime4=tkinter.Label(lbf_buff, text="어빌리티 효과 % : ")
bufftime4.place(x=60, y=180)

bufftime_input4 = tkinter.Entry(lbf_buff)
bufftime_input4.place(x=280, y=180)
bufftime_input4.insert(0,"0")

bufftime_result1=tkinter.Label(lbf_buff_result, text="유니온 적용(초) : ")
bufftime_result1.place(x=10, y=0)
bufftime_result2=tkinter.Label(lbf_buff_result, justify="right")
bufftime_result2.place(x=400, y=0)

bufftime_result3=tkinter.Label(lbf_buff_result, text="몬스터라이프 적용(초) : ")
bufftime_result3.place(x=10, y=40)
bufftime_result4=tkinter.Label(lbf_buff_result, justify="right")
bufftime_result4.place(x=400, y=40)

bufftime_result5=tkinter.Label(lbf_buff_result, text="어빌리티 적용(초) : ")
bufftime_result5.place(x=10, y=80)
bufftime_result6=tkinter.Label(lbf_buff_result, justify="right")
bufftime_result6.place(x=400, y=80)

bufftime_result7=tkinter.Label(lbf_buff_result, text="총 증가량(초) : ")
bufftime_result7.place(x=10, y=120)
bufftime_result8=tkinter.Label(lbf_buff_result, justify="right")
bufftime_result8.place(x=400, y=120)

bufftime_result9=tkinter.Label(lbf_buff_result, text="모든 효과 적용(초)  : ")
bufftime_result9.place(x=10, y=160)
bufftime_result10=tkinter.Label(lbf_buff_result)
bufftime_result10.place(x=400, y=160)

bufftime_test1=tkinter.Label(lbf_buff_result, text=" * 참고 사항 (유니온 효과, 몬스터 라이프 효과 ,잠재 능력 효과)")
bufftime_test1.place(x=20, y=205)

bufftime_test2=tkinter.Label(lbf_buff_result, justify="left", text="1) 하이퍼 스킬, 5차 스킬에 적용되지 않음")
bufftime_test2.place(x=10, y=230)

#################QA Test Mob 페이지#################
test_mob1_ID1=tkinter.Button(test_guide1, justify="left", text="9501011   속성 무효",relief="groove", borderwidth=0, command=lambda:copy("mob1_1"))
test_mob1_ID1.place(x=30, y=10)
test_mob1_ID2=tkinter.Button(test_guide1, justify="left", text="9501012   속성 반감", relief="groove", borderwidth=0, command=lambda:copy("mob1_2"))
test_mob1_ID2.place(x=30, y=50)
test_mob1_ID3=tkinter.Button(test_guide1, justify="left",text="9501013   속성 증폭", relief="groove", borderwidth=0, command=lambda:copy("mob1_3"))
test_mob1_ID3.place(x=30, y=90)
test_mob1_ID4=tkinter.Button(test_guide1, justify="left", text="2435744   무형 보따리", relief="groove", borderwidth=0, command=lambda:copy("mob1_4"))
test_mob1_ID4.place(x=300, y=10)

test_mob2_ID1=tkinter.Button(test_guide2, justify="left", text="9990000   무형", relief="groove", borderwidth=0, command=lambda:copy("mob2_1"))
test_mob2_ID1.place(x=30, y=10)
test_mob2_ID2=tkinter.Button(test_guide2, justify="left", text="9990009   보스형", relief="groove", borderwidth=0, command=lambda:copy("mob2_2"))
test_mob2_ID2.place(x=30, y=50)
test_mob2_ID3=tkinter.Button(test_guide2, justify="left", text="9990023   공격 반사", relief="groove", borderwidth=0, command=lambda:copy("mob2_3"))
test_mob2_ID3.place(x=30, y=90)
test_mob2_ID4=tkinter.Button(test_guide2, justify="left", text="9990085   방무100%", relief="groove", borderwidth=0, command=lambda:copy("mob2_4"))
test_mob2_ID4.place(x=30, y=130)

test_mob3_ID1=tkinter.Button(test_guide3, justify="left", text="9501000   봉인", relief="groove", borderwidth=0, command=lambda:copy("mob3_1"))
test_mob3_ID1.place(x=30, y=10)
test_mob3_ID2=tkinter.Button(test_guide3, justify="left", text="9501001   암흑", relief="groove", borderwidth=0, command=lambda:copy("mob3_2"))
test_mob3_ID2.place(x=30, y=40)
test_mob3_ID3=tkinter.Button(test_guide3, justify="left", text="9501002   허약", relief="groove", borderwidth=0, command=lambda:copy("mob3_3"))
test_mob3_ID3.place(x=30, y=70)
test_mob3_ID4=tkinter.Button(test_guide3, justify="left", text="9501003   기절", relief="groove", borderwidth=0, command=lambda:copy("mob3_4"))
test_mob3_ID4.place(x=30, y=100)
test_mob3_ID5=tkinter.Button(test_guide3, justify="left", text="9501004   저주", relief="groove", borderwidth=0, command=lambda:copy("mob3_5"))
test_mob3_ID5.place(x=30, y=130)
test_mob3_ID6=tkinter.Button(test_guide3, justify="left", text="9501005   중독", relief="groove", borderwidth=0, command=lambda:copy("mob3_6"))
test_mob3_ID6.place(x=30, y=160)

test_mob3_ID7=tkinter.Button(test_guide3, justify="left", text="9501006   슬로우", relief="groove", borderwidth=0, command=lambda:copy("mob3_7"))
test_mob3_ID7.place(x=300, y=10)
test_mob3_ID8=tkinter.Button(test_guide3, justify="left", text="9501007   버프 무효화", relief="groove", borderwidth=0, command=lambda:copy("mob3_8"))
test_mob3_ID8.place(x=300, y=40)
test_mob3_ID9=tkinter.Button(test_guide3, justify="left", text="9501008   유혹", relief="groove", borderwidth=0, command=lambda:copy("mob3_9"))
test_mob3_ID9.place(x=300, y=70)
test_mob3_ID10=tkinter.Button(test_guide3, justify="left", text="9501009   물리 이뮨", relief="groove", borderwidth=0, command=lambda:copy("mob3_10"))
test_mob3_ID10.place(x=300, y=100)
test_mob3_ID11=tkinter.Button(test_guide3, justify="left", text="9501010   마법 이뮨", relief="groove", borderwidth=0, command=lambda:copy("mob3_11"))
test_mob3_ID11.place(x=300, y=130)
test_mob3_ID12=tkinter.Button(test_guide3, justify="left", text="8950103   Fixdmar10%", relief="groove", borderwidth=0, command=lambda:copy("mob3_12"))
test_mob3_ID12.place(x=300, y=160)
test_mob3_setting=tkinter.Button(test_guide3, text="/create 2022198\t\t\t\t오래된 러셀론의 알약",relief="groove",borderwidth=0, command=lambda:copy("mob3_13"))
test_mob3_setting.place(x=30, y=190)

#################세팅 명령어 페이지#################
test_c_setting=tkinter.Button(test_skill1, justify="left", text="/cpsset 1 70000045 20\t    어빌리티 재사용 대기시간 초기화 (5차 스킬 적용 X)", relief="groove", borderwidth=0, command=lambda:copy("c1"))
test_c_setting.place(x=15, y=10)

test_c_setting2=tkinter.Button(test_skill1, justify="left", text="/createex 1002019 4 3 40557 40557 40557\t\t 쿨감 효과 아이템 생성",relief="groove",borderwidth=0, command=lambda:copy("c2"))
test_c_setting2.place(x=15, y=40)

test_c_setting3=tkinter.Button(test_skill1, justify="left", text="/fmcreate 9300881\t\t\t\t      몬스터라이프 쁘띠 은월 소환",relief="groove",borderwidth=0, command=lambda:copy("c3"))
test_c_setting3.place(x=15, y=70)

test_c_setting4=tkinter.Button(test_skill1, justify="left", text="/runecreate 6\t\t\t\t\t           초월의 룬 소환",relief="groove",borderwidth=0, command=lambda:copy("c4"))
test_c_setting4.place(x=15, y=100)

test_b_setting1=tkinter.Button(test_skill2, justify="left", text="/cpsset 1 70000048 40\t\t\t     어빌리티 버프 지속 시간 증가",relief="groove",borderwidth=0, command=lambda:copy("b1"))
test_b_setting1.place(x=15, y=10)
test_b_setting2=tkinter.Button(test_skill2, justify="left", text="/fmcreate 2600800\t\t\t\t      몬스터라이프 군단장 윌 소환",relief="groove",borderwidth=0, command=lambda:copy("b2"))
test_b_setting2.place(x=15, y=40)

test_mc_setting1=tkinter.Button(test_skill3, justify="left", text="/cpsset 1 70000047 10\t\t\t            어빌리티 몹 카운트 증가",relief="groove",borderwidth=0, command=lambda:copy("m1"))
test_mc_setting1.place(x=15, y=10)
test_mc_setting2=tkinter.Button(test_skill3, justify="left", text="/fmcreate 9300752\t\t\t\t   몬스터라이프 빛 루미너스 소환",relief="groove",borderwidth=0, command=lambda:copy("m2"))
test_mc_setting2.place(x=15, y=40)
test_mc_setting3=tkinter.Button(test_skill3, justify="left", text="/create 1402224\t\t\t\t 류드의 검 생성(어택카운트 증가)",relief="groove",borderwidth=0, command=lambda:copy("m3"))
test_mc_setting3.place(x=15, y=70)

test_etc_setting1=tkinter.Button(test_skill4,text="/cpsset 1 70000046 10\t\t\t  어빌리티 패시브 스킬 레벨 증가",relief="groove",borderwidth=0, command=lambda:copy("e1"))
test_etc_setting1.place(x=15, y=10)
test_etc_setting2=tkinter.Button(test_skill4,text="/showskillactioninfo 1\t\t\t\t        ActionDelay 확인",relief="groove",borderwidth=0, command=lambda:copy("e2"))
test_etc_setting2.place(x=15, y=40)
test_etc_setting3=tkinter.Button(test_skill4,text="/hitdamagetestmsg  1\t\t\t             피격데미지 확인 명령어",relief="groove",borderwidth=0, command=lambda:copy("e3"))
test_etc_setting3.place(x=15, y=70)
test_etc_setting3=tkinter.Button(test_skill4,text="/create 2436125\t\t\t\t     스폐셜 SP 초기화 주문서 생성",relief="groove",borderwidth=0, command=lambda:copy("e4"))
test_etc_setting3.place(x=15, y=100)

#################스텟 공격력 계산 페이지#################
text_constant = tkinter.Label(input_test_statPAD1,text="무기상수 : ")
text_constant.place(x=10, y=10)
input_constant = tkinter.Entry(input_test_statPAD1, width=10)
input_constant.place(x=90, y=10)
input_constant.insert(0,"0")

text_pad = tkinter.Label(input_test_statPAD1,text="공격력/마력 : ")
text_pad.place(x=10, y=50)
input_pad = tkinter.Entry(input_test_statPAD1, width=10)
input_pad.place(x=90, y=50)
input_pad.insert(0,"0")

text_mainStat = tkinter.Label(input_test_statPAD1, text="주스텟 : ")
text_mainStat.place(x=10, y=90)
input_mainStat = tkinter.Entry(input_test_statPAD1,width=10)
input_mainStat.place(x=90, y=90)
input_mainStat.insert(0,"0")

text_subStat1 = tkinter.Label(input_test_statPAD1, text="부스텟1 : ")
text_subStat1.place(x=180, y=90)
input_subStat1 = tkinter.Entry(input_test_statPAD1,width=10)
input_subStat1.place(x=240, y=90)
input_subStat1.insert(0,"0")

text_subStat2 = tkinter.Label(input_test_statPAD1, text="부스텟2 : ")
text_subStat2.place(x=330, y=90)
input_subStat2 = tkinter.Entry(input_test_statPAD1,width=10)
input_subStat2.place(x=390, y=90)
input_subStat2.insert(0,"0")

text_pureHP = tkinter.Label(input_test_statPAD1, text="순수 체력 : ")
text_pureHP.place(x=170, y=130)
input_pureHP = tkinter.Entry(input_test_statPAD1,width=10)
input_pureHP.place(x=240, y=130)
input_pureHP.insert(0,"0")

text_addHP = tkinter.Label(input_test_statPAD1, text="추가 체력 : ")
text_addHP.place(x=320, y=130)
input_addHP = tkinter.Entry(input_test_statPAD1,width=10)
input_addHP.place(x=390, y=130)
input_addHP.insert(0,"0")

text_finalDam = tkinter.Label(input_test_statPAD1, text="최종 데미지 : ")
text_finalDam.place(x=160, y=170)
input_finalDam = tkinter.Entry(input_test_statPAD1,width=10)
input_finalDam.place(x=240, y=170)
input_finalDam.insert(0,"0")

text_addDam = tkinter.Label(input_test_statPAD1, text="데미지 : ")
text_addDam.place(x=330, y=170)
input_addDam = tkinter.Entry(input_test_statPAD1,width=10)
input_addDam.place(x=390, y=170)
input_addDam.insert(0,"0")

#결과
text_nomalstat_pad=tkinter.Label(result_test_statPAD, text="기본 스텟 공격력 : ", justify="left")
text_nomalstat_pad.place(x=10, y=50)
result_nomalstat_pad=tkinter.Label(result_test_statPAD, justify="right")
result_nomalstat_pad.place(x=170, y=50)

text_addstat_pad=tkinter.Label(result_test_statPAD, text="효과 적용 스텟 공격력 : ")
text_addstat_pad.place(x=10, y=100)
result_addstat_pad=tkinter.Label(result_test_statPAD, justify="right")
result_addstat_pad.place(x=170, y=100)

#################아카이빙 페이지#################
#모험가
test_job_archiving1=tkinter.Button(test_archiving1, text="히어로", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("hero"))
test_job_archiving1.place(relx=0.001, rely=0.01, relwidth=0.196)
test_job_archiving2=tkinter.Button(test_archiving1, text="아크메이지(불,독)",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("firepoison"))
test_job_archiving2.place(relx=0.196, rely=0.01, relwidth=0.196)
test_job_archiving3=tkinter.Button(test_archiving1, text="보우마스터",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("bowmaster"))
test_job_archiving3.place(relx=0.392, rely=0.01, relwidth=0.196)
test_job_archiving4=tkinter.Button(test_archiving1, text="나이트로드",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("nightroad"))
test_job_archiving4.place(relx=0.588, rely=0.01, relwidth=0.196)
test_job_archiving5=tkinter.Button(test_archiving1, text="바이퍼",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("viper"))
test_job_archiving5.place(relx=0.784, rely=0.01, relwidth=0.196)

test_job_archiving6=tkinter.Button(test_archiving1, text="팔라딘", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("paladin"))
test_job_archiving6.place(relx=0.001, rely=0.35, relwidth=0.196)
test_job_archiving7=tkinter.Button(test_archiving1, text="아크메이지(썬,콜)",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("icelightning"))
test_job_archiving7.place(relx=0.196, rely=0.35, relwidth=0.196)
test_job_archiving8=tkinter.Button(test_archiving1, text="신궁",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("crossbowmaster"))
test_job_archiving8.place(relx=0.392, rely=0.35, relwidth=0.196)
test_job_archiving9=tkinter.Button(test_archiving1, text="섀도어",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("shadower"))
test_job_archiving9.place(relx=0.588, rely=0.35, relwidth=0.196)
test_job_archiving10=tkinter.Button(test_archiving1, text="캡틴",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("captain"))
test_job_archiving10.place(relx=0.784, rely=0.35, relwidth=0.196)

test_job_archiving11=tkinter.Button(test_archiving1, text="다크나이트", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("darknight"))
test_job_archiving11.place(relx=0.001, rely=0.7, relwidth=0.196)
test_job_archiving12=tkinter.Button(test_archiving1, text="비숍",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("bishop"))
test_job_archiving12.place(relx=0.196, rely=0.7, relwidth=0.196)
test_job_archiving13=tkinter.Button(test_archiving1, text="패스파인더",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("pathfinder"))
test_job_archiving13.place(relx=0.392, rely=0.7, relwidth=0.196)
test_job_archiving14=tkinter.Button(test_archiving1, text="듀얼블레이드",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("dualblade"))
test_job_archiving14.place(relx=0.588, rely=0.7, relwidth=0.196)
test_job_archiving15=tkinter.Button(test_archiving1, text="캐논슈터",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("cannonshooter"))
test_job_archiving15.place(relx=0.784, rely=0.7, relwidth=0.196)

#시그너스
test_job_archiving16=tkinter.Button(test_archiving2, text="소울마스터", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("soulmaster"))
test_job_archiving16.place(relx=0.001, rely=0.1, relwidth=0.196)
test_job_archiving17=tkinter.Button(test_archiving2, text="플레임위자드",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("flamewizard"))
test_job_archiving17.place(relx=0.196, rely=0.1, relwidth=0.196)
test_job_archiving18=tkinter.Button(test_archiving2, text="윈드브레이커",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("windbreaker"))
test_job_archiving18.place(relx=0.392, rely=0.1, relwidth=0.196)
test_job_archiving19=tkinter.Button(test_archiving2, text="나이트워커",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("nightwalker"))
test_job_archiving19.place(relx=0.588, rely=0.1, relwidth=0.196)
test_job_archiving20=tkinter.Button(test_archiving2, text="스트라이커",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("striker"))
test_job_archiving20.place(relx=0.784, rely=0.1, relwidth=0.196)
test_job_archiving21=tkinter.Button(test_archiving2, text="미하일", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("mihile"))
test_job_archiving21.place(relx=0.001, rely=0.6, relwidth=0.196)

#레지스탕스 & 데몬
test_job_archiving22=tkinter.Button(test_archiving3, text="블래스터", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("blaster"))
test_job_archiving22.place(relx=0.001, rely=0.1, relwidth=0.196)
test_job_archiving23=tkinter.Button(test_archiving3, text="배틀메이지",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("battlemage"))
test_job_archiving23.place(relx=0.196, rely=0.1, relwidth=0.196)
test_job_archiving24=tkinter.Button(test_archiving3, text="와일드헌터",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("wildhunter"))
test_job_archiving24.place(relx=0.392, rely=0.1, relwidth=0.196)
test_job_archiving25=tkinter.Button(test_archiving3, text="제논",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("xenon"))
test_job_archiving25.place(relx=0.588, rely=0.1, relwidth=0.196)
test_job_archiving26=tkinter.Button(test_archiving3, text="메카닉",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("mechanic"))
test_job_archiving26.place(relx=0.784, rely=0.1, relwidth=0.196)
test_job_archiving27=tkinter.Button(test_archiving3, text="데몬슬레이어", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("demonslayer"))
test_job_archiving27.place(relx=0.001, rely=0.6, relwidth=0.196)
test_job_archiving27=tkinter.Button(test_archiving3, text="데몬어벤져", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("demonavenger"))
test_job_archiving27.place(relx=0.196, rely=0.6, relwidth=0.196)

#영웅
test_job_archiving28=tkinter.Button(test_archiving4, text="아란", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("aran"))
test_job_archiving28.place(relx=0.001, rely=0.1, relwidth=0.196)
test_job_archiving29=tkinter.Button(test_archiving4, text="에반",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("evan"))
test_job_archiving29.place(relx=0.196, rely=0.1, relwidth=0.196)
test_job_archiving30=tkinter.Button(test_archiving4, text="메르세데스",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("mercedes"))
test_job_archiving30.place(relx=0.392, rely=0.1, relwidth=0.196)
test_job_archiving31=tkinter.Button(test_archiving4, text="팬텀",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("phantom"))
test_job_archiving31.place(relx=0.588, rely=0.1, relwidth=0.196)
test_job_archiving32=tkinter.Button(test_archiving4, text="은월",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("eunwol"))
test_job_archiving32.place(relx=0.784, rely=0.1, relwidth=0.196)
test_job_archiving33=tkinter.Button(test_archiving4, text="루미너스", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("luminous"))
test_job_archiving33.place(relx=0.001, rely=0.6, relwidth=0.196)

#노바 & 레프
test_job_archiving34=tkinter.Button(test_archiving5, text="카이저", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("kaiser"))
test_job_archiving34.place(relx=0.001, rely=0.1, relwidth=0.196)
test_job_archiving35=tkinter.Button(test_archiving5, text="카인",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("kain"))
test_job_archiving35.place(relx=0.196, rely=0.1, relwidth=0.196)
test_job_archiving36=tkinter.Button(test_archiving5, text="카데나",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("cadena"))
test_job_archiving36.place(relx=0.392, rely=0.1, relwidth=0.196)
test_job_archiving37=tkinter.Button(test_archiving5, text="엔젤릭버스터",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("angelicbuster"))
test_job_archiving37.place(relx=0.588, rely=0.1, relwidth=0.196)
test_job_archiving38=tkinter.Button(test_archiving5, text="아델",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("adele"))
test_job_archiving38.place(relx=0.001, rely=0.6, relwidth=0.196)
test_job_archiving39=tkinter.Button(test_archiving5, text="일리움", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("illium"))
test_job_archiving39.place(relx=0.196, rely=0.6, relwidth=0.196)
test_job_archiving40=tkinter.Button(test_archiving5, text="아크", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("ark"))
test_job_archiving40.place(relx=0.196, rely=0.6, relwidth=0.196)

#아니마 & 제로 & 키네시스
test_job_archiving41=tkinter.Button(test_archiving6, text="라라", relief="groove", borderwidth=0, command=lambda:connect_shearpoint("lala"))
test_job_archiving41.place(relx=0.001, rely=0.1, relwidth=0.196)
test_job_archiving42=tkinter.Button(test_archiving6, text="호영",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("hoyoung"))
test_job_archiving42.place(relx=0.392, rely=0.1, relwidth=0.196)
test_job_archiving43=tkinter.Button(test_archiving6, text="제로",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("zero"))
test_job_archiving43.place(relx=0.001, rely=0.6, relwidth=0.196)
test_job_archiving44=tkinter.Button(test_archiving6, text="키네시스",relief="groove", borderwidth=0, command=lambda:connect_shearpoint("kinesis"))
test_job_archiving44.place(relx=0.392, rely=0.6, relwidth=0.196)

window.mainloop()