from turtle import window_width
import pyperclip
from tkinter import *
import tkinter.ttk
from tkinter.ttk import LabelFrame

window = tkinter.Tk()

window.title("스텟창 수치 계산기")
window.geometry("660x700+100+100")
window.wm_iconbitmap('iccon.ico')
window.resizable(False,False)

menubar=Menu(window)

menu1 = Menu(menubar)
menu1.add_command(label="um")
menu1.add_command(label="um2")
menubar.add_cascade(label="uuuum", menu=menu1)
window.config(menu=menubar)

#################버튼 동작#################
#데미지 계산 
def d_calc():
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

#최종뎀 계산
def f_calc():
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
#쿨타임 계산
def c_calc():
    c_input1 = float(cooltime_input1.get())      #기본 쿨
    c_input2 = float(cooltime_input2.get())      #유니온 쿨감
    c_input3 = float(cooltime_input3.get())      #쿨감뚝

    c_result_union=c_input1*(1-(c_input2/100))
    c_time_result4.config(text=str(round(c_result_union,3))+"초")    #유니온 쿨감만

    c_result_item=c_input1-c_input3
    c_time_result6.config(text=str(round(c_result_item,3))+"초")    #쿨감 뚝만

    c_result_total=c_input1*(1-(c_input2/100))-c_input3
    c_time_result2.config(text=str(round(c_result_total,3))+"초")     #총 쿨감
#벞지 계산
def b_calc():  
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
#방무 계산
# def ignor_calc():  
#     ig_input1 = float(ignoreGuard_input1.get())
#     ig_input2 = float(ignoreGuard_input2.get())
#     ig_input3 = float(ignoreGuard_input3.get())
#     ig_input4 = float(ignoreGuard_input4.get())
#     ig_input5 = float(ignoreGuard_input5.get())

#     ig_result=(1-(1-(ig_input1/100))*(1-(ig_input2/100))*(1-(ig_input3/100))*(1-(ig_input4/100))*(1-(ig_input5/100)))*100
#     ignoreGuard_result2.config(text=str(round(ig_result,3))+"%")

#명령어 복사
def copy_c1():
    #명령어 클립보드 복사 
    a="/cpsset 1 70000045 20"
    pyperclip.copy(a)    
def copy_c2():
    a="/createex 1002019 4 3 40557 40557 40557"
    pyperclip.copy(a)
def copy_c3():    
    a="/fmcreate 9300881"
    pyperclip.copy(a)
def copy_c4():
    a="/runecreate 7"
    pyperclip.copy(a)
def copy_b1():
    a="/cpsset 1 70000048 40"
    pyperclip.copy(a)
def copy_b2():
    a="/fmcreate 2600800"
    pyperclip.copy(a) 
def copy_m1():
    a="/cpsset 1 70000047 10"
    pyperclip.copy(a)
def copy_m2():
    a="/fmcreate 9300752"
    pyperclip.copy(a)
def copy_m3():
    a="/create 1402224"
    pyperclip.copy(a)
def copy_e1():
    a="/cpsset 1 70000046 10"
    pyperclip.copy(a)
def copy_e2():
    a="/showskillactioninfo 1"
    pyperclip.copy(a)
def copy_e3():
    a="/hitdamagetestmsg 1"
    pyperclip.copy(a)
def copy_e4():
    a="/create 2436125"
    pyperclip.copy(a)
def copy_mob3_13():
    a="/create 2022198"
    pyperclip.copy(a)
def copy_mob1_1():
    a="/summon 9501011"
    pyperclip.copy(a)
def copy_mob1_2():
    a="/summon 9501012"
    pyperclip.copy(a)
def copy_mob1_3():
    a="/summon 9501013"
    pyperclip.copy(a)
def copy_mob2_1():
    a="/summon 9990000"
    pyperclip.copy(a)
def copy_mob2_2():
    a="/summon 9990009"
    pyperclip.copy(a)
def copy_mob2_3():
    a="/summon 9990023"
    pyperclip.copy(a)
def copy_mob2_4():
    a="/summon 9990085"
    pyperclip.copy(a)
def copy_mob3_1():
    a="/summon 9501000"
    pyperclip.copy(a)
def copy_mob3_2():
    a="/summon 9501001"
    pyperclip.copy(a)
def copy_mob3_3():
    a="/summon 9501002"
    pyperclip.copy(a)
def copy_mob3_4():
    a="/summon 9501003"
    pyperclip.copy(a)
def copy_mob3_5():
    a="/summon 9501004"
    pyperclip.copy(a)
def copy_mob3_6():
    a="/summon 9501005"
    pyperclip.copy(a)
def copy_mob3_7():
    a="/summon 9501006"
    pyperclip.copy(a)
def copy_mob3_8():
    a="/summon 9501007"
    pyperclip.copy(a)
def copy_mob3_9():
    a="/summon 9501008"
    pyperclip.copy(a)
def copy_mob3_10():
    a="/summon 9501009"
    pyperclip.copy(a)
def copy_mob3_11():
    a="/summon 9501010"
    pyperclip.copy(a)
def copy_mob3_12():
    a="/summon 8950103"
    pyperclip.copy(a)

#입력칸 초기화동작
def d_Clear():
    #입력칸 초기화
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
def f_Clear():
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
def c_Clear():
    cooltime_input1.delete(0,100)
    cooltime_input1.insert(0,"0")
    cooltime_input2.delete(0,100)
    cooltime_input2.insert(0,"0")
    cooltime_input3.delete(0,100)
    cooltime_input3.insert(0,"0")
def b_Clear():
    #방무 입력칸 초기화
    bufftime_input1.delete(0,100)
    bufftime_input1.insert(0,"0")
    bufftime_input2.delete(0,100)
    bufftime_input2.insert(0,"0")
    bufftime_input3.delete(0,100)
    bufftime_input3.insert(0,"0")
    bufftime_input4.delete(0,100)
    bufftime_input4.insert(0,"0")
# def ig_Clear():
#     #방무 입력칸 초기화
#     ignoreGuard_input1.delete(0,100)
#     ignoreGuard_input1.insert(0,"0")
#     ignoreGuard_input2.delete(0,100)
#     ignoreGuard_input2.insert(0,"0")
#     ignoreGuard_input3.delete(0,100)
#     ignoreGuard_input3.insert(0,"0")
#     ignoreGuard_input4.delete(0,100)
#     ignoreGuard_input4.insert(0,"0")
#     ignoreGuard_input5.delete(0,100)
#     ignoreGuard_input5.insert(0,"0")

#################노트 만들기#################
note = tkinter.ttk.Notebook(window, width=545, height=600)
note.pack()

d_note = tkinter.Frame(window)
note.add(d_note, text="데미지 계산")

f_note = tkinter.Frame(window)
note.add(f_note, text="최종뎀, 방무")

c_note = tkinter.Frame(window)
note.add(c_note, text="쿨타임 감소")

b_note = tkinter.Frame(window)
note.add(b_note, text="버프 지속 시간")

# ig_note = tkinter.Frame(window)
# note.add(ig_note, text="방어율 무시")

test_note = tkinter.Frame(window)
note.add(test_note, text="테스트용 몹")

test2_note = tkinter.Frame(window)
note.add(test2_note, text="세팅 명령어")

#################출처 달기#################
parkjs=tkinter.Label(window, text="MapleQA PARKJS (ver.2)",fg="white",bg="black")
parkjs.place(x=320, y=626)

#################라벨 만들기#################
#데미지 계산
lbf_calDam = LabelFrame(d_note, text="입력")
lbf_calDam.place(relx=0.01,relwidth=0.98,relheight=0.65)
lbf_calDam_result = LabelFrame(d_note,text="결과")
lbf_calDam_result.place(relx=0.01,rely=0.66,relwidth=0.98,relheight=0.34)

#최종뎀, 방무
lbf_FDam = LabelFrame(f_note)
lbf_FDam.place(relx=0.01,relwidth=0.98,relheight=0.70)

lbf_FDam_result = LabelFrame(f_note, text="result")
lbf_FDam_result.place(relx=0.01,rely=0.71,relwidth=0.98,relheight=0.29)

#쿨타임
lbf_cool = LabelFrame(c_note)
lbf_cool.pack(fill="both",expand="yes")

lbf_cool_result = LabelFrame(c_note, text="result")
lbf_cool_result.pack(fill="both", expand="yes")

#벞지
lbf_buff = LabelFrame(b_note)
lbf_buff.pack(fill="both",expand="yes")

lbf_buff_result = LabelFrame(b_note, text="result")
lbf_buff_result.pack(fill="both", expand="yes")

# #방무
# ldf_ig = LabelFrame(ig_note)
# ldf_ig.pack(fill="both", expand="yes")

# ldf_ig_result = LabelFrame(ig_note, text="result")
# ldf_ig_result.pack(fill="both", expand="yes")

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

#################버튼 만들기#################
d_calResetBut = tkinter.Button(lbf_calDam, text="적용", width=15, command=d_calc)
d_calResetBut.place(x=230, y=330)
d_calBut = tkinter.Button(lbf_calDam, text="초기화", width=15, command=d_Clear)
d_calBut.place(x=350, y=330)

f_calBut = tkinter.Button(lbf_FDam, text="적용", command=f_calc, width=15)
f_calBut.place(x=255, y=330)
f_calResetBut = tkinter.Button(lbf_FDam, text="초기화", width=15, command=f_Clear)
f_calResetBut.place(x=380, y=330)

c_calBut = tkinter.Button(lbf_cool, text="적용", command=c_calc, width=15)
c_calBut.place(x=255, y=230)
c_calResetBut = tkinter.Button(lbf_cool, text="초기화", width=15, command=c_Clear)
c_calResetBut.place(x=380, y=230)

b_calBut = tkinter.Button(lbf_buff, text="적용", command=b_calc, width=15)
b_calBut.place(x=255, y=230)
b_calResetBut = tkinter.Button(lbf_buff, text="초기화", width=15, command=b_Clear)
b_calResetBut.place(x=380, y=230)

# ig_calBut = tkinter.Button(ldf_ig, text="적용", command=ignor_calc, width=15)
# ig_calBut.place(x=255, y=230)
# ig_calResetBut = tkinter.Button(ldf_ig, text="초기화", width=15, command=ig_Clear)
# ig_calResetBut.place(x=380, y=230)

#################데미지 계산#################
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

#################최종뎀#################
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

#################방무 중첩 계산#################
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

#################쿨타임 감소#################
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

#################버프 지속 시간 계산#################
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

#################QA Test Mob#################
#테스트 몹 ID
test_mob1_ID1=tkinter.Button(test_guide1, justify="left", text="9501011   속성 무효",relief="groove", borderwidth=0, command=copy_mob1_1)
test_mob1_ID1.place(x=30, y=10)
test_mob1_ID2=tkinter.Button(test_guide1, justify="left", text="9501012   속성 반감", relief="groove", borderwidth=0, command=copy_mob1_2)
test_mob1_ID2.place(x=30, y=50)
test_mob1_ID3=tkinter.Button(test_guide1, justify="left",text="9501013   속성 증폭", relief="groove", borderwidth=0, command=copy_mob1_3)
test_mob1_ID3.place(x=30, y=90)

test_mob2_ID1=tkinter.Button(test_guide2, justify="left", text="9990000   무형", relief="groove", borderwidth=0, command=copy_mob2_1)
test_mob2_ID1.place(x=30, y=10)
test_mob2_ID2=tkinter.Button(test_guide2, justify="left", text="9990009   보스형", relief="groove", borderwidth=0, command=copy_mob2_2)
test_mob2_ID2.place(x=30, y=50)
test_mob2_ID3=tkinter.Button(test_guide2, justify="left", text="9990023   공격 반사", relief="groove", borderwidth=0, command=copy_mob2_3)
test_mob2_ID3.place(x=30, y=90)
test_mob2_ID4=tkinter.Button(test_guide2, justify="left", text="9990085   방무100%", relief="groove", borderwidth=0, command=copy_mob2_4)
test_mob2_ID4.place(x=30, y=130)

test_mob3_ID1=tkinter.Button(test_guide3, justify="left", text="9501000   봉인", relief="groove", borderwidth=0, command=copy_mob3_1)
test_mob3_ID1.place(x=30, y=10)
test_mob3_ID2=tkinter.Button(test_guide3, justify="left", text="9501001   암흑", relief="groove", borderwidth=0, command=copy_mob3_2)
test_mob3_ID2.place(x=30, y=40)
test_mob3_ID3=tkinter.Button(test_guide3, justify="left", text="9501002   허약", relief="groove", borderwidth=0, command=copy_mob3_3)
test_mob3_ID3.place(x=30, y=70)
test_mob3_ID4=tkinter.Button(test_guide3, justify="left", text="9501003   기절", relief="groove", borderwidth=0, command=copy_mob3_4)
test_mob3_ID4.place(x=30, y=100)
test_mob3_ID5=tkinter.Button(test_guide3, justify="left", text="9501004   저주", relief="groove", borderwidth=0, command=copy_mob3_5)
test_mob3_ID5.place(x=30, y=130)
test_mob3_ID6=tkinter.Button(test_guide3, justify="left", text="9501005   중독", relief="groove", borderwidth=0, command=copy_mob3_6)
test_mob3_ID6.place(x=30, y=160)

test_mob3_ID7=tkinter.Button(test_guide3, justify="left", text="9501006   슬로우", relief="groove", borderwidth=0, command=copy_mob3_7)
test_mob3_ID7.place(x=300, y=10)
test_mob3_ID8=tkinter.Button(test_guide3, justify="left", text="9501007   버프 무효화", relief="groove", borderwidth=0, command=copy_mob3_8)
test_mob3_ID8.place(x=300, y=40)
test_mob3_ID9=tkinter.Button(test_guide3, justify="left", text="9501008   유혹", relief="groove", borderwidth=0, command=copy_mob3_9)
test_mob3_ID9.place(x=300, y=70)
test_mob3_ID10=tkinter.Button(test_guide3, justify="left", text="9501009   물리 이뮨", relief="groove", borderwidth=0, command=copy_mob3_10)
test_mob3_ID10.place(x=300, y=100)
test_mob3_ID11=tkinter.Button(test_guide3, justify="left", text="9501010   마법 이뮨", relief="groove", borderwidth=0, command=copy_mob3_11)
test_mob3_ID11.place(x=300, y=130)
test_mob3_ID12=tkinter.Button(test_guide3, justify="left", text="8950103   Fixdmar10%", relief="groove", borderwidth=0, command=copy_mob3_12)
test_mob3_ID12.place(x=300, y=160)
test_mob3_setting=tkinter.Button(test_guide3, text="/create 2022198\t\t\t\t오래된 러셀론의 알약",relief="groove",borderwidth=0, command=copy_mob3_13)
test_mob3_setting.place(x=30, y=190)

#세팅 명령어
test_c_setting=tkinter.Button(test_skill1, justify="left", text="/cpsset 1 70000045 20\t    어빌리티 재사용 대기시간 초기화 (5차 스킬 적용 X)", relief="groove", borderwidth=0, command=copy_c1)
test_c_setting.place(x=15, y=10)

test_c_setting2=tkinter.Button(test_skill1, justify="left", text="/createex 1002019 4 3 40557 40557 40557\t\t 쿨감 효과 아이템 생성",relief="groove",borderwidth=0, command=copy_c2)
test_c_setting2.place(x=15, y=40)

test_c_setting3=tkinter.Button(test_skill1, justify="left", text="/fmcreate 9300881\t\t\t\t      몬스터라이프 쁘띠 은월 소환",relief="groove",borderwidth=0, command=copy_c3)
test_c_setting3.place(x=15, y=70)

test_c_setting4=tkinter.Button(test_skill1, justify="left", text="/runecreate 7\t\t\t\t\t           초월의 룬 소환",relief="groove",borderwidth=0, command=copy_c4)
test_c_setting4.place(x=15, y=100)

test_b_setting1=tkinter.Button(test_skill2, justify="left", text="/cpsset 1 70000048 40\t\t\t     어빌리티 버프 지속 시간 증가",relief="groove",borderwidth=0, command=copy_b1)
test_b_setting1.place(x=15, y=10)
test_b_setting2=tkinter.Button(test_skill2, justify="left", text="/fmcreate 2600800\t\t\t\t      몬스터라이프 군단장 윌 소환",relief="groove",borderwidth=0, command=copy_b2)
test_b_setting2.place(x=15, y=40)

test_mc_setting1=tkinter.Button(test_skill3, justify="left", text="/cpsset 1 70000047 10\t\t\t            어빌리티 몹 카운트 증가",relief="groove",borderwidth=0, command=copy_m1)
test_mc_setting1.place(x=15, y=10)
test_mc_setting2=tkinter.Button(test_skill3, justify="left", text="/fmcreate 9300752\t\t\t\t   몬스터라이프 빛 루미너스 소환",relief="groove",borderwidth=0, command=copy_m2)
test_mc_setting2.place(x=15, y=40)
test_mc_setting3=tkinter.Button(test_skill3, justify="left", text="/create 1402224\t\t\t\t 류드의 검 생성(어택카운트 증가)",relief="groove",borderwidth=0, command=copy_m3)
test_mc_setting3.place(x=15, y=70)

test_etc_setting1=tkinter.Button(test_skill4,text="/cpsset 1 70000046 10\t\t\t  어빌리티 패시브 스킬 레벨 증가",relief="groove",borderwidth=0, command=copy_e1)
test_etc_setting1.place(x=15, y=10)
test_etc_setting2=tkinter.Button(test_skill4,text="/showskillactioninfo 1\t\t\t\t        ActionDelay 확인",relief="groove",borderwidth=0, command=copy_e2)
test_etc_setting2.place(x=15, y=40)
test_etc_setting3=tkinter.Button(test_skill4,text="/hitdamagetestmsg  1\t\t\t             피격데미지 확인 명령어",relief="groove",borderwidth=0, command=copy_e3)
test_etc_setting3.place(x=15, y=70)
test_etc_setting3=tkinter.Button(test_skill4,text="/create 2436125\t\t\t\t     스폐셜 SP 초기화 주문서 생성",relief="groove",borderwidth=0, command=copy_e4)
test_etc_setting3.place(x=15, y=100)

window.mainloop()