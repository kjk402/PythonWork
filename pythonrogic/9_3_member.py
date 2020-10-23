class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    def move(self, location):
        print("지상유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도:{2}]".format(self.name, location, self.speed))

        # print("{0} 유닛이 생성되었습니다.".format(self.name))
        # print("체력 {0}".format(self.hp))

    def damaaged(self, damage):
        print("{0}유닛이 {1}의 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛의 남은 체력은{1}입니다.\n".format(self.name, self.hp))
        if self.hp <=0 :
            print("{0}유닛은 죽었습니다.\n".format(self.name))

# 공격 유닛
class AttackUnit(Unit): # Unit 부모클래스 상속, AttackUnit이 자식클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} 유닛이 {1}방향으로 공격합니다. [공격력:{2}]".format(\
            self.name, location,self.damage))



# 공중 수송 유닛 드랍쉽

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}이 {1}방향으로 날아갑니다. [속도:{2}]\n".format(name, location, self.flying_speed))

#공중 공격 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp >10:
            self.hp -=10
            self.speed += 5
            self.damage += 10
            print("{0}: 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩 사용불가".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode() == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 탱크모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#레이스

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.colocked = False

    def clocking(self):
        if self.colocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.colocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새 게임 시작.")

def game_over():
    print("GG")

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(self, name, hp, 0)
#         self.location = location


firebat1 = AttackUnit("파이어뱃", 50, 16, 20)
firebat1.attack("5시")
firebat1.damaaged(10)

# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 7, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛,
vulture = AttackUnit("벌쳐", 70, 30, 5)
vulture.move("6시")
vulture.attack("5시")

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

print("=========================")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()


t1 = Tank()
t1








