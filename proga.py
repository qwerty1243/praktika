import random

n = random.randint(4,31)
print("Число камней в куче: ",n)
while n > 0:
    try:
        us = int(input("Сколько камней возьмём?"))
    except:
        print("Недопустимое кол-во камней!")
        exit()
    if us <= 0 or us > 3:
        print("Вы можете взять от 3 до 4 камней")
        exit()
    n -= us
    
    if n == 1:
        print("ПОБЕДА!")
        exit()
    n - random.randint(1,4)
    
    if n < 4:
        n -= 2
        print("Камней в куче после хода соперника: ", n)
        print("ПОРАЖЕНИЕ((")
        exit()
    if n == 4:
        n -= 3
        print("Камней в куче после хода соперника: ", n)
        print("ПОРАЖЕНИЕ((")
        exit()
    n -= random.randint(1,4)
    print("Камней в куче после хода соперника: ", n)
    if n == 1:
        print("ПОРАЖЕНИЕ((")
