def Coffee_Machine():
    # 재고, 잔돈 및 투입 금액
    Money_input = 0
    Coin_Change = 10000
    # Stock ==> Water, Cup, Coffee, Cream, Sugar
    Stock = [1000, 30, 500, 500, 500]
    Black = [100, 1, 30]
    Cream = [100, 1, 15, 15]
    Sugar = [100, 1, 10, 10, 10]

    Money_input = int(input(f'동전을 투입하세요 : '))
    while True:
        # 투입 금액이 부족하거나 숫자가 아닐 시
        if Money_input < 300:
            print(f'돈이 부족합니다. {Money_input}원:\n---------------------------\n커피 자판기 동작을 종료합니다.\n---------------------------')
            break
        else:
            print(f'------------------------------------\n\t\t커피 자판기 (300원)\n 1. 블랙 커피\n 2. 프림 커피\n 3. 설탕 프림 커피\n 4. 재고 현황\n 5. 종료')
            Select_Menu = int(input('메뉴를 선택하세요. '))
            if Select_Menu == 5:
                print(f'커피 자판기 동작을 종료합니다.\n이용해주셔서 감사합니다.\n잔돈: {Money_input}원')
                break
            while True:
                if 1 <= Select_Menu <= 4:
                    if Select_Menu == 1:
                        print(f'블랙 커피를 선택하셨습니다. 잔돈 : {Money_input-300}원\n------------------------------------')
                        if Stock[0] < Black[0] or Stock[1] < Black[1] or Stock[2] < Black[2]:
                            print('재고가 부족합니다.')
                            break
                        elif Money_input < 300:
                            print('잔돈이 부족합니다.')
                            break
                        else:
                            Coin_Change += 300
                            Money_input -= 300
                            for i in range(len(Black)):
                                Stock[i]-=Black[i]
                            break
                    elif Select_Menu == 2:
                        print(f'프림 커피를 선택하셨습니다. 잔돈 : {Money_input-300}원]\n------------------------------------')
                        if Stock[0] < Cream[0] or Stock[1] < Cream[1] or Stock[2] < Cream[2] or Stock[3] < Cream[3]:
                            print('재고가 부족합니다.')
                            break
                        elif Money_input < 300:
                            print('잔돈이 부족합니다.')
                            break
                        else:
                            Coin_Change += 300
                            Money_input -= 300
                            for i in range(len(Cream)):
                                Stock[i]-=Cream[i]
                            break
                    elif Select_Menu == 3:
                        print(f'설탕 프림 커피를 선택하셨습니다. 잔돈 : {Money_input-300}원\n------------------------------------')
                        if Stock[0] < Sugar[0] or Stock[1] < Sugar[1] or Stock[2] < Sugar[2] or Stock[3] < Sugar[3]:
                            print('재고가 부족합니다.')
                            break
                        elif Money_input < 300:
                            print('잔돈이 부족합니다.')
                            break
                        else:
                            Coin_Change += 300
                            Money_input -= 300
                            for i in range(len(Sugar)):
                                Stock[i]-=Sugar[i]
                            break
                    elif Select_Menu == 4:
                        print(f'재고 현황:\n물: {Stock[0]}ml, 종이컵: {Stock[1]}개\n커피: {Stock[2]}g, 프림: {Stock[3]}g, 설탕: {Stock[4]}g\n자판기 남은 돈: {Coin_Change}원, 잔돈현황: {Money_input}원\n------------------------------------')
                        break
                else:
                    print('잘못 선택하였습니다.')
                    break

Coffee_Machine()