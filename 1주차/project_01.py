# --------------------------------------------------------
# 계산기 응용 프로그램
# 클래스 기반
# 데이터 저장 => File or 다른 자료형
# 속성 => total, reset
# 기능 => + , - , × , ÷ , reset
# --------------------------------------------------------

filename = "C:\\Users\\KDP-50\\Desktop\\python\\PROJECT\\calculator.txt"

class Calculator:
    def __init__(self):
        self.total = 0
        self.reset = 0
    def _plus(self, num) : self.total += num
    def _minus(self, num) : self.total -= num
    def _multiple(self, num) : self.total *= num
    def _division(self, num): 
        if num != 0 : self.total /= num
        else : 
            with open(filename, 'a', encoding='utf-8') as fp : fp.write(f"{int(num)}으로 나눌 수 없습니다. 다시 입력하세요.\n")
    def _reset(self) : self.total = self.reset
calculator = Calculator()
# 계산기 실행
with open(filename, 'w', encoding='utf-8') as fp: fp.write('=============Calculate Result=============\n')
while True:
    operator = input("'Q' 또는 'q'를 입력하면 종료합니다.\n연산자 입력 (+, -, *, /, reset) : ")
    if operator.lower() == 'q' : break
    try:
        if operator == 'reset':
            calculator._reset()
            with open(filename, 'w', encoding='utf-8') as fp : fp.write(f"=============Calculate Result=============\n연산자: {operator}되었습니다. , 결과 : {calculator.total}\n")
            continue
        num = float(input("숫자를 입력하세요: "))
        if operator == '+' : calculator._plus(num)
        elif operator == '-' : calculator._minus(num)
        elif operator == '*' : calculator._multiple(num)
        elif operator == '/' : calculator._division(num)
        else:
            print("잘못된 연산자입니다. 다시 입력해주세요.")
            continue
        print(f"현재 합계: {calculator.total}")
        # 계산 결과를 파일에 저장
        with open(filename, 'a', encoding='utf-8') as fp : fp.write(f"연산자: {operator}, 숫자: {num}, 결과: {calculator.total}\n")
    except ValueError:print("숫자가 아닙니다. 다시 입력해주세요.")
# 종료 후 최종 결과
with open(filename, 'a', encoding='utf-8') as fp: fp.write(f'최종 결과값 : {calculator.total}')