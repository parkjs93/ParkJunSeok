from random import randint, randrange
from unicodedata import name


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} : 유닛 생성 [체력 : {1}, 이동 속도 : {2}]".format(self.name, self.hp, self.speed))

    def move(self, location):
        self.location = location
        print("{0} : {1} 방향으로 이동 [이동속도 : {2}] ".format(self.name, location, self.speed))

    def damaged(self, location, damage):
        self.location = location
        self.damage = damage
        self.hp -= damage
        print ("{0} : {1}방향으로 부터 공격 받았습니다. [피해량:{2}, 잔여 체력 {3}]".format(self.name, location, self.damage, self.hp))
        if self.hp <= 0:
            print("{0} : 유닛 사망 ".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage
        print("{0} 공격력 : {1}".format(self.name, self.damage))

    def attack(self, location):
        self.location = location
        print("{0} : {1}방향으로 공격 [데미지 : {2}]".format(self.name, location, self.damage))

class FlyUnit(Unit):
    def __init__(self, name, hp, fly_speed):
        super().__init__(name, hp, 0)
        self.fly_speed=fly_speed
        print("{0} : 공중 유닛 [이동 속도 : {1}]".format(self.name, self.fly_speed))

    def move(self, location):
        print("{0} : {1}방향으로 공중 이동 [이동 속도 : {2}]".format(self.name, location, self.fly_speed))

class FlyAttackUnit(AttackUnit, FlyUnit):
    def __init__(self, name, hp, fly_speed, damage):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyUnit.__init__(self,name, hp, fly_speed)
        print("{0} : 공중 유닛 [공격력 : {1}]".format(self.name, self.damage))

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            self.speed += 1
            self.damage += 2
            print("{0} : 스팀팩 사용 ".format(self.name))
        else:
            print("{0} : 체력 부족으로 스팀팩 사용 불가 [체력 : {1}]".format(self.name, self.hp))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self,"시즈",150, 1, 30)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if (Tank.seize_developed == False):
            print("{0} : 시즈모드 미개발".format(self.name)) 
        if (self.seize_mode == False):
            self.damage *= 2
            self.speed = 0
            self.seize_mode =True
            print("{0} : 시즈 모드로 전환합니다. [공격력 {1}]".format(self.name, self.damage))
        elif (self.seize_mode == True) :
            self.damage /= 2
            self.speed = 1
            self.seize_mode = False
            print("{0} : 시즈 모드 해제 [공격력 : {1}]".format(self.name, self.damage))

class Wriath(FlyAttackUnit):
    def __init__(self):
        FlyAttackUnit.__init__(self,"레이스",80, 20, 5)
        self.clocking = False

    def clocking_mode(self):
        if (self.clocking == True) :
            print("{0} : 클로킹 모드 해제 ".format(self.name))
            self.clocking = False
        elif (self.clocking == False) :
            print("{0} : 클로킹 모드 설정 ".format(self.name))
            self.clocking = True
        else:
            print("{} : Error ".format(self.name))

wrath1 = Wriath()
wrath1.clocking_mode()
wrath1.clocking_mode()

tank1 = Tank()
#Tank.seize_developed = True
tank1.set_seize_mode()
tank1.set_seize_mode()

def game_start():
    print("[알림] 게임 시작")

def game_end():
    print("[알림] 게임 종료")

#게임 시작
game_start()

#유낫 생성
m1 = Marine()
m2 = Marine()
t1 = Tank()
w1 = Wriath()

#유닛 리스트 저장
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(t1)
attack_unit.append(w1)

#전체 유닛 이동
for unit in attack_unit:
    unit.move("2시")

#공격 준비
Tank.seize_developed = True
print("시즈 모드 개발 완료")

for unit in attack_unit:
    if isinstance(unit, Marine): #unit의 클래스의 속성이 Marine인지
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wriath):
        unit.clocking_mode()
    else:
        print("error")

#공격 시작 
for unit in attack_unit:
    unit.attack("7시")

#데미지 받음
for unit in attack_unit:
    unit.damaged("5시", randint(10, 60))