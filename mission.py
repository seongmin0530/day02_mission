import random
small = random.randint(0, 1)                  # 0~1 사이의 정수 랜덤으로 생성하여 small에 대입
green = random.randint(0, 1)                  # 0~1 사이의 정수 랜덤으로 생성하여 green에 대입

print(f'small : {bool(small)}, green : {bool(green)}') # 랜덤으로 생성된 값 bool형태로 출력

if bool(small) :
    if bool(green) :                                   #작고 녹색이라면
        print("It is pea")                                  # 완두콩
    else:                                              #작고 녹색이 아니라면
        print("It is cherry")                               # 체리
else:
    if bool(green) :                                   #크고 녹색이라면
        print("It is watermelon")                           # 수박
    else:                                              #크고 녹색이 아니라면
        print("It is pumpkin")                              # 호박