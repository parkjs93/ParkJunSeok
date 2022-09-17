########문자열 처리 함수########
from copyreg import pickle
from encodings import utf_8
from this import d
from turtle import st
from unicodedata import name


python = "ParKjsjunsuk"

# 소문자 만들기
print(python.lower())

# 전체 대문자 만들기
print(python.upper())

# 문자열의 특정 인덱스 값만 대문자인지 확인하기(bool)
print(python[3].isupper())

# 문자열 길이 구하기
print(len(python))

# 특정 문자 다른 문자로 변경하기 
print(python.replace("js","JS"))

# 문자열에서 특정 문자 인덱스 찾아내기
# 없으면 오류
print(python.index("k"))

# 문자열 중 특정 문자의 두번째 인덱스 찾아내기
# 없으면 오류, 
index=python.index("j")
index=python.index("j",index+1) #두번째 j의 값 넣기
print(index)
# 문자열에서 특정 문자의 위치 찾기 
# 없으면 -1 출력
print(python.find("k"))

# 문자열에서 특정 문자의 갯수 찾기
print(python.count("j"))


########문자열 포맷########
# 1)
print("정수 : %d"%20)  #%d는 정수값
print("문자열 : %s" %"python") # %s는 문자열 값
print("문자 : %c" %"a")
print("문자열 : %s, %s" %("python", "java")) # %s는 문자열 값

# 2) 
print("중괄호 : {}".format("내용")) #출력내용.format()
print("중괄호 2개 : {}, {}".format("내용1","내용2")) #출력내용.format()
print("중괄호 2개 : {1}, {0}".format("내용1","내용2")) # 순서 변경 가능

# 3)
print("중괄호 2개 : {aa}, {bb}".format(aa="내용1",bb="내용2"))

# 4)
aa="내용3"
bb="내용4"
print(f"중괄호 : {aa}, {bb}")

########탈출 문자########
#\n : 문자열 내에서 줄 바꿈
# 문자열 내에 큰따옴표 출력 시키는 방법 \"\"
print(" aa \"bb\" ")

#문장 내에서 \ 출력하기  : \\
print("c:\\user\\...")

# 문자열 커서 맨 앞으로 이동 
print("red Apple\rpine") #\r 이후 글자수 만큼 커서 위치의 문자가 지워지고 써짐

# \b : 백스페이스 (한 글자 삭제)
print("red Apple\bpine")

#\t : 탭 기능과 동일


########리스트########
# 리스트 []
#다양한 자료형 함께 사용 가능


pyList = ["a","b","c","d"]

# 원하는 값의 인덱스 번호 구하기
print(pyList.index("c"))

# 리스트에 값 추가 (맨 뒤)
pyList.append("e")
print(pyList)

# 리스트 특정 위치에 값 추가
pyList.insert(1,"f") # 1번 인덱스에 값 추가하기
print(pyList)

# 리스트 값 중 맨 뒤의 값 하나씩 뽑아내기
print(pyList.pop()) # 뽑아낸 값
print(pyList) # 뽑힌 값 제외 리스트 값

# 특정 값과 같은 값이 있는 개수 구하기
pyList.append("c")
print(pyList.count("c"))

#리스트 값 정렬하기
pyList2 = [5,4,3,1,2]
pyList2.sort()
print(pyList2)

#리스트 순서 뒤집기 
pyList2.reverse()
print(pyList2)

#값 모두 삭제하기 
pyList2.clear()

#리스트 붙이기
pyList.extend(pyList2)
print(pyList)

########딕셔너리########
#딕셔너리 {키:값} // 키 = 문자열이 와도 상관없음
# 키에 대한 중복 불가
dictionaly = {3:"a", 33:"b"}

# 키에 따른 값 출력하기
# 1) 키가 없을 경우 오류 발생하고 종료
print(dictionaly[3])
print(dictionaly[33])
# 2) 키가 없을 경우 None 값 저장
print(dictionaly.get(3))
print(dictionaly.get(5,"값 없을 경우")) # 해당 키에 값이 없을 경우 뒤에 문자열 출력

# 딕셔너리 값 안에 키가 있는지 확인하는 방법
print(3 in dictionaly) # bool 타입으로 저장

# 값 추가하기 : 만약 해당 키에 값이 있을 경우 덮어씌워짐
dictionaly["aav"] = "c"
print(dictionaly)

# 값 제거
del dictionaly["aav"] #키에 맞는 값 삭제

# 모든 키 값들만 출력
print(dictionaly.keys())
# 값만 출력하기 
print(dictionaly.values())
# 키, 값 쌍으로 출력하기
print(dictionaly.items())

# 딕셔너리 값 초기화
dictionaly.clear()

########튜플########
# 내용 변경 추가 불가, 고정된 값만 사용 가능
# 속도 빠름
pyTuple = ("ABC", "DEF")

#값 출력
print(pyTuple[0])
print(pyTuple[1])

#여러 값 튜플로 저장하기 
(fir, sec, thr) = ("AAA", "BBB", "CCC")
print(fir,sec, thr)

########세트########
# 집합, 중복불가, 순서 없음
pyset = {1,2,3,3,3,3}
print(pyset) #{1,2,3} 출력

#교집합
java ={"AAA", "BBB", "CCC"}
python = set(["CCC", "DDD"])
print(java & python) #교집합
print(java.intersection(python)) #교집합

#합집합
print(java | python)
print(java.union(python))

#차집합 
print(java - python)
print(java.difference(python))

#값 추가
python.add("FFF")

#값 제거
java.remove("AAA")


########자료구조의 변경########
#set -> 타입 변경
menu = {"A","B","C"}
menu = list(menu) #리스트로 변경
menu = tuple(menu) #튜플로 변경
menu = set(menu) # 다시 set으로 변경



########IF########
# if 조건문: 
#   실행 명령문
# elif 조건문:
#   실행 명령문
# else: 
#   실행 명령문

#또는 or / 그리고 and


########반복문########
# 1) for
for waiting in range(1,6): #1~5까지 값이 waiting 값에 입력되며 반복
    print(waiting)

# 한줄 for
stu = ["AAAAA", "BBB","ccccccccc"]
stu = [len(i) for i in stu] #len(i)의 i는 stu[0] 부터 반복


# 2) while
# while (조건): #조건이 만족할 때 까지 반복
# 만약 조건부가 True 일 경우 무한 반복 (무한 루프)



########continue , break########
# 1) continue : 반복문 중 continue를 만났을 경우 해당 구문 스킵하고 다음 반복 시작
# 2) break : 반복문 중 break를 만났을 경우 반복문 탈출



########함수########
#함수 선언 
#def 함수명():
#   실행 문구


########기본값########
# 같은 함수 내에 항상 같은 값일 경우 기본 값으로 설정할 수 있음
# 전달받을 경우 전달받은 값으로 저장, 전달받지 못한 경우 기본 값이 저장됨

########키워드 값########
# 함수 값 전달하는 부분에 키워드=값 형태로 입력할 경우 순서에 무관하게 사용할 수 있음

########가변 인자########
def test(a,b,*c): # *c 캰에 입력하는 값은 개수 상관없이 전달받을 수 있다
    for i in c:
        print(i, end=" ")
    print()

########지역 변수와 전역 변수########
#전역 변수라 check 함수 내에 gun에 접근 불가
gun = 10

def check(sol):
    global gun #전역 공간에 있는 gun 사용 가능!
    gun = gun - sol

check(2)

########표준 입출력########
#1)
print("a", "b", sep=",") #출력값 2개 사이에 , 출력
#end= "문장의 끝을 줄 바꿈이 아닌 문자열로 바꿔주어라"

#2)
score = {"A":0, "B":50, "C":100}
for subject, score in score.items():
    print(subject.ljust(8), score.rjust(4), sep=":")
    #subject에 8칸을 확보한 뒤 왼쪽 정렬하여라
    #score는 4칸 확보 후 오른쪽 정렬하여라

#3)
for num in range(1,21):
    print( "aaa :   "+str(num).zfill(3)) # 3칸 확보 후 빈 공간 확보 후 값이 없을 경우 0



########파일 입출력########
#1) txt 파일 열기 (w=쓰기, a=이어서 쓰기, r=읽기)
score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기 형태로 열기
print("수학 : 0", file=score_file) #score_file에 저장된 score.txt 파일에 해당 문구 입력
score_file.close() # open헸던 파일 종료

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("값 이어서 입력")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

#1-1) txt 파일의 값이 얼마나 있는지 모르는 상태에서 한줄씩 읽기
score_file=open("score.txt","r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

#1-2) txt 파일의 값을 리스트로 받아와서 출력시키기
score_file = open ("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #리스트 형태로 파일 내의 모든 정보 저장
for line in lines:
    print(line, end="")
score_file.close()


########pickle########
#데이터를 파일 형태로 넘겨주는 것
#1) 파일 쓰기
import pickle
profile_file = open("profile.pickle", "wb") #wb = 쓰기
profile = {"A":"name", "b":["a","b","c","d"]}
print(profile)
pickle.dump(profile, profile_file) #profile의 데이터를 pickle파일에 저장해라
profile_file.close()

#2) 파일 열기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

#3) with 사용하기
with open("profile.pickle","rb") as profile_file: #pickle 파일을 불러와서 변수에 저장
    print(pickle.load(profile_file))    #따로 close()를 해주지 않아도 된다

with open("study.txt","w", encoding="utf8") as study_file:
    print(study_file.write("stuuuuudy"))

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.readlines())


########예외처리########
# try: 실행문
# 에러 강제 발생 : raise 에러구문
# except 에러문:
#   해당 에러 발생 시 실행문
# 에러문 빈값일 경우 에러 발생 시 실행문 시작
#########사용자 정의 예외처리#########
#class 에러명(Exception)
#   pass
#########finally#########
# 결과에 상관없이 무조건 실행되는 구문 (에러가 발생하든 안하든,,)


class BigNumver(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("나누기")
    nums=[]
    nums.append(int(input("첫 번째 숫자 입력 : ")))
    nums.append(int(input("첫 번째 숫자 입력 : ")))
    if (nums[0] >= 10 or nums[1] >= 10):
        raise BigNumver("문제 발생 입력 값 : ".format(nums[0],nums[1]))
    nums.append(int(nums[0]/nums[1]))
except ValueError:
    print("잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except BigNumver as err:
    print(err)  
    #raise BigNumver("문제 발생 입력 값 : ".format(nums[0],nums[1])) 값을 class BigNumver에서 처리 후 값을 가지고 있다가 출력
    print("너무 큰 숫자")
except Exception as err: #어떤 오류인지 값을 받고 싶을 때
    print("알 수 없는 오류 발생 : "+err)
finally:
    print("끝.")

