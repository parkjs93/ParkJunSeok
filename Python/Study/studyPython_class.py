#######클래스#######
# 클래스는 보통 붕어빵 틀에 비유, 함수와 변수의 집합
# 예시, 스타크래프트
# 마린 : 공격, 군인, 총 사용

class Unit:
    def __init__(self, name, hp, damage):
        #생성자, 객체(클래스를 통해 만들어지는 것들)를 만들 때 호출되는 함수
        #self는 자기 자신을 의미, 클래스 맨 처음 맴버 변수는 self를 지정해줘야 한다.
        self.name = name #맴버 변수 .name과 같은 
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #객체 wraith1의 맴버 변수 .name, .damage를 사용한다.

# wraith2 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith2.name, wraith2.damage))
# wraith2.clocking = True #클래스에 없는 맴버 변수를 추가할 수 있다.

# if wraith2.clocking == True:
#     print("{0} : 클로킹 상태".format(wraith2.name))


#매쏘드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("생성 유닛 : {}".format(self.name))
        print("공격력 : {0}, 체력 : {1}".format(self.damage, self.hp))
    
    def attack(self, location):
        print("{0} : {1}방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        self.hp -= damage
        print("{0} : {1}만큼 공격 받았습니다. [현재 체력:{2}]".format(self.name, damage,self.hp))
        if (self.hp <=0 ):
            print("{0} : 유닛 사망".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 25)
# firebat1.attack("4시")
# firebat1.damaged(30)
# firebat1.damaged(30)


#상속
class Unit2:
    def __init__(self, name, hp, speed):
        #생성자, 객체(클래스를 통해 만들어지는 것들)를 만들 때 호출되는 함수
        #self는 자기 자신을 의미, 클래스 맨 처음 맴버 변수는 self를 지정해줘야 한다.
        self.name = name #맴버 변수 .name과 같은 
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 이동 속도 : {1}".format(self.hp, self.speed))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}방향으로 이동합니다. [이동속도 : {2}]".format(self.name, location, self.speed))

class AttackUnit2(Unit2): #AttackUnit 클래스는 Unit 클래스를 상속 받는다
    def __init__(self, name, hp, damage, speed):
        Unit2.__init__(self, name, hp, speed) #Unit 클래스의 name, hp를 상속받아서 사용
        self.damage = damage
        #print("생성 유닛 : {}".format(self.name))
        print("공격력 : {0}, 체력 : {1}, 이동 속도 : {2}".format(self.damage, self.hp, self.speed, self.speed))
    
    def attack(self, location):
        print("{0} : {1}방향으로 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        self.hp -= damage
        print("{0} : {1}만큼 공격 받았습니다. [현재 체력:{2}]".format(self.name, damage,self.hp))
        if (self.hp <=0 ):
            print("{0} : 유닛 사망".format(self.name))
# firebat2 = AttackUnit2("파이어뱃", 50, 25)
# firebat2.attack("4시")
# firebat2.damaged(30)
# firebat2.damaged(30)


########다중 상속 (여러 곳에서 상속 받는 것)########
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed #값 초기화
    def fly(self, name, location):
        print("{0} : {1}방향으로 날아감. [이동속도 : {2}]".format(name,location, self.flying_speed))
    
class AttackFlyableUnit(AttackUnit2, Flyable): #AttackFlyableUnit,Flyable class  중복 상속 받음
    #클래스 변수 선언
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit2.__init__(self, name, hp, damage, 0) #지상 스피드 0 처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# valkyrie = AttackFlyableUnit("발키리", 200, 6, 5)
# valkyrie.move(valkyrie.name, "3시")



######## 연산자 오버로딩 : 자식 클래스에 따라 함수 동작하게 할 수 있도록 하는 것 
######## Unit class에 있는 move()가 AttackUnit class에도 있으나 AttackFlyableUnit class에서 재정의
######## AttackFlyableUnit의 객체들은 재정의된 move함수를 사용

# vulture = AttackUnit2("벌처", 80, 10, 20)
# battlecruiser = AttackFlyableUnit("배틀크루져", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("12시")


########pass########
#일단 아무것도 하지 않고 넘어간다

class BuildingUnit(Unit2):
    def __init__(self, name, hp, location):
        pass #아무것도 하지 않고 넘어감

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


########super########
# 상속 받는 클래스를 선언하는 함수, super(). ,self는 사용하지 않는다
# 다중 상속 시 먼저 선언된 클래스에 대한 init 함수가 호출된다
class BuildingUnit2(Unit2):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) #상속받는 클래스 이름을 작성하지 않아도 되며 매개변수 맨앞에 self를 넣지 않아도 됌
        self.location = location


