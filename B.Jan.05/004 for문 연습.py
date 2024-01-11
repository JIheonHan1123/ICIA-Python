list1 = [15, 20, 30, 90]
# cf) list, tuple, set만났는데 반복문 써야되면 웬만하면 무조건 for문 사용

# list1의 길이를 구하시오 -> len() 안쓰고
'''
length = 0
for x in list1:
    length += 1
print(length)
'''

# list1의 합계를 구하시오 -> sum() 안쓰고
# 155
'''
total = 0
for x in list1:
    total += x
print(total)
'''

# list1의 평균 구하시오
# 38.75
length, total = 0, 0
for x in list1:
    length += 1
    total += x
print(total/length)

# list1에서 70점 이상인 점수의 개수
size = 0
for x in list1:
    if x >= 70:
        size += 1
print(size)
