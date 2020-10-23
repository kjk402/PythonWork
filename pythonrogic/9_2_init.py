class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marien1 = Unit("마린", 40, 5)
marien2 = Unit("마린", 50, 7)
tank = Unit("탱크", 150, 35)
marien3 = Unit

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 90, 6)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹상태입니다.".format(wraith2.name))

