
while True:
    num = input("주민등록번호(14자리,'-'포함)를 입력하세요.")
    if num.lower() == 'q': break
    elif len(num) != 14 or num[6] !='-' or not (num[:6].isdigit()) or not (num[7:].isdigit()): print("잘못된 주민등록번호입니다.")
    else:
        if int(num[-6:-4]) <= 8 and int(num[-6:-4]) >= 0 : print('출생 지역은 서울입니다.')
        elif int(num[-6:-4]) <= 12 and int(num[-6:-4]) >= 9  : print('출생 지역은 부산입니다.')
        elif int(num[-6:-4]) <= 15 and int(num[-6:-4]) >= 13  : print('출생 지역은 인천입니다.')
        elif int(num[-6:-4]) <= 25 and int(num[-6:-4]) >= 16  : print('출생 지역은 경기입니다.')
        elif int(num[-6:-4]) <= 34 and int(num[-6:-4]) >= 26  : print('출생 지역은 강원입니다.')
        elif int(num[-6:-4]) <= 47 and int(num[-6:-4]) >= 35  : print('출생 지역은 충청입니다.')
        elif int(num[-6:-4]) <= 66 and int(num[-6:-4]) >= 48  : print('출생 지역은 전라입니다.')
        elif int(num[-6:-4]) <= 91 and int(num[-6:-4]) >= 67  : print('출생 지역은 경상입니다.')
        elif int(num[-6:-4]) <= 95 and int(num[-6:-4]) >= 92  : print('출생 지역은 제주입니다.')
        else : print('잘못된 주민등록번호입니다.')