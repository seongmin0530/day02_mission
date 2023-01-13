import random
secret = random.randint(1, 10)                # 1~10 사이의 정수 랜덤으로 생성하여 secret에 대입
guess = random.randint(1,10)                  # 1~10 사이의 정수 랜덤으로 생성하여 guess에 대입

print(f'secret : {secret}, guess : {guess}') # 랜덤으로 생성된 값 출력
if secret > guess:                           # secret값이 guess값보다 큰 경우
    print('too low')
elif secret < guess:                         # secret값이 guess값보다 작은 경우
    print('too high')
else:                                        # secret값과 guess값이 같은 경우
    print('just right')