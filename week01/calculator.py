#1. 사칙연산 계산기

a = int(input()) # 사용자에게 숫자 1개 입력받기
b = int(input()) # 사용자에게 숫자 1개 입력받기

sum = a+b # 두 숫자의 합
subtraction = a-b # 두 숫자의 차
product = a*b # 두 숫자의 곱

#연산 결과 출력
print(a,"+", b, "=", sum) 
print(a,"-", b, "=", subtraction) 
print(a,"*", b, "=", product)

#두 숫자 나누기(예외)
if b == 0:
    print("0으로 나눌 수 없습니다.") #b값이 0이라면 해당 문구 출력
else:
    division = a / b #0이 아니라면 나누기 진행 
    print(a, "/", b, "=", division) #나누기 연산 진행



