num1, num2 = 10, 3.14
print(f'덧셈{num1+num2}, 뺄셈{num1-num2}, 곱셈{num1*num2}, 나눗셈{num1/num2}')
# 여기서 f는 format

# 절대값 함수 abs
print(abs(100))
print(abs(-100))
print(abs(num1))

str = "0123456789"
# 홀수만 출력
print(str[1::2])
# 3의 배수만 출력
print(str[0::3])
print(str[::3]) # 어차피 처음부터라 0안써도 됨

# 숫자를 입력받아 C R U D 하는 프로그럠
# 메뉴를 띄운다 (1:숫자추가, 2:숫자출력(합계, 평균), 999:종료)

'''
numbers=[]
while True:
    print("=============== 메뉴 선택 ===============")
    print("1:추가, 2:합계출력, 3:평균출력, 4:삭제, 999:종료")
    select = input("번호입력>> ")
    if select=='999':
        print('이용해주셔서 감사합니다')
        break
    elif select=='1':
        num = int(input('숫자입력>> '))
        numbers.append(num)
    elif select=='2':
        print(f'합계: {sum(numbers)}')
    elif select=='3':
        print(f'평균: {sum(numbers)/len(numbers)}')
    elif select=='4':
        val = int(input('삭제할 값 입력>> '))
        if val in numbers:
            numbers.remove(val)
        else:
            print('제대로 된 값을 입력하세요')
'''

# in
# for가 있으면
# for x in nums -nums에 있는 값들을 x에 차례대로 하나씩 담는 것
# for가 없으면
# x in nums     -nums안에 x가 있는지 없는지 >> 결과는 bool로 나온다.            



# 1.숫자추가, 2.숫자출력, 3.합계출력, 4.숫자삭제, 999.종료 - 메뉴로 입력 받아 처리하는 프로그램 작성
# 안보고 처음부터 다 짜보기
numbers = []
while True:
    print("======================= 메뉴 선택 =======================")
    print("1.숫자추가, 2.숫자출력, 3.합계출력, 4.숫자삭제, 999.종료")
    select = input("메뉴 번호선택>> ")
    if select=='999':
        print('이용해주셔서 감사합니다.')
        break
    elif select=='1':
        input_num = int(input('추가할 숫자 입력>> '))
        numbers.append(input_num)
    elif select=='2':
        # print(f'숫자 출력>> {numbers}')
        for number in numbers:
            print(number, end=" ")
        print()
    elif select=='3':
        print(f'합게 출력>> {sum(numbers)}')
    elif select=='4':
        delete_num = int(input('삭제할 숫자 입력>> '))
        if delete_num in numbers:
            numbers.remove(delete_num)
        else:
            print(f'추가한 번호에 {delete_num}이 포함되어 있지 않습니다.')
            print('다른 숫자를 선택해 주세요')
    else:
        print('잘못된 선택입니다.')