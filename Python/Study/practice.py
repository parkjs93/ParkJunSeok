# 문제 1)
url="http://google.com"
url = url.replace("http://", "")
print("1 : " + url)
index=url.find(".")
url=url[:index]
print("2 : "+url)
url = str(url[:3]) + str(len(url)) + str(url.count("e")) + "!"
print(url)

# 문제 2)
from random import *

userList = range(1,21)
userList = list(userList)

shuffle(userList)
winner = sample(userList, 4)
print(winner)
print(winner[0])
print(winner[1:])

#문제 3)
count=0
for cs in range(1,51):
    time = randrange(5,51)
    if (5<= time <=15):
        print("[{0}] {1}번째 (time : {2})".format("O",cs,time))
        count+=1
    else:
        print("[{0}] {1}번째 (time : {2})".format(" ",cs,time))
print("total : {}".format(count))

#문제 4)

def std_weight(gender, height):
    if (gender == "남"):
        weight = height/100 * height/100 * 22
        print(str(round(weight,2))+"kg")
    elif (gender == "여"):
        weight = height/100 * height/100 * 21
        print(str(round(weight, 2))+"kg")
    else:
        weight = "error"
        print(weight)

park = std_weight("남",175)

#문제 5)
# for i in range(1,11):
#     with open("{}주차.txt".format(i), "w", encoding="utf8") as daly:
#         daly.writelines(" - {} 주차 주간 보고 -".format(i))
#         daly.writelines("부서 :")
#         daly.writelines("이름 :")
#         daly.writelines("업무  요약 :")


#문제 6)
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} {4} ".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

h_list =[]
h_list.append(h1)
h_list.append(h2)
h_list.append(h3)
for h in h_list:
    h.show_detail()


#문제 7)
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 
while(True):
    try:
        print("잔여 : {0}".format(chicken))
        order = int(input("오더 수 : "))
    
        if(order>=1):
            if (order > chicken):
                print("부족")
                raise SoldOutError("제고가 소진되었")
            else:
                print("[대기] {0}번, {1}개 완료".format(waiting, order))
                waiting += 1
                chicken -= order
        else:
            raise ValueError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break