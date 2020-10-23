# 전달

def open_account():
    print("새로운 계좌 생성되었습니다.")

def deposit(balance, money):  # 입금
    print("입금 완료. 잔액은 {0}원 입니다. ".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은{0}입니다".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 #수수료 100원
    return commission, balance - money - commission

# balance = 0 #처음 잔액
# balance = deposit(balance, 1000)
# print(balance)

balance = 3000
balance = withdraw(balance, 1000)
print("")
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며 잔액은 {1}원입니다".format(commission, balance))


