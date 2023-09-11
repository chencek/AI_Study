import random
# 로또 번호 추출 함수
def lotto():
    l_num = []

    while len(l_num) < 6:
        picked_number = random.randint(1, 45)
        if picked_number not in l_num:
            l_num.append(picked_number)
    l_num= sorted(l_num)
    return l_num

while True:
    n = input("로또를 몇장 구매하시겠습니까? ")
    if not n.isdigit() or int(n)>5:
        print("잘못된 입력입니다. 다시 입력하세요.")
    else:
        l_nums = []
        lucky_num = lotto()
        n=int(n)
        for i in range(n):
            l_nums.append(lotto())
        print("-------------------------------")
        print("자동 생성번호")
        for i in range(n):
            print(f"[ {i+1}]\t{l_nums[i][0]:>2}  {l_nums[i][1]:>2}  {l_nums[i][2]:>2}  {l_nums[i][3]:>2}  {l_nums[i][4]:>2}  {l_nums[i][5]:>2}")
        print("-------------------------------")
        print("당첨 번호")
        print(f'[ 1]\t{lucky_num[0]}  {lucky_num[1]:>2}  {lucky_num[2]:>2}  {lucky_num[3]:>2}  {lucky_num[4]:>2}  {lucky_num[5]:>2}')
        for i in range(n):
            print(f"당첨 결과:  {i+1}")
            print(f"{l_nums[i][0]:>2}  {l_nums[i][1]:>2}  {l_nums[i][2]:>2}  {l_nums[i][3]:>2}  {l_nums[i][4]:>2}  {l_nums[i][5]:>2}")
            for j in range(6):
                if l_nums[i][j] in lucky_num:
                    print(' O', end='  ')
                else:
                    print(' X', end='  ')
            print(f"\n-------------------------------")

        break
