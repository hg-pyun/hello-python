odd = [1, 3, 5, 7, 9]
print(odd)

# index
tripleList = [1, 2, ['a', 'b', ['Life', 'is']]]
print(tripleList[2][2][0])

# slice
list = [1, 2, 3, 4, 5]
print(list[0:2])

# 리스트 연산자
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a*2)

# 리스트 수정
list = [1, 2, 3]

# 추가
list[1:2] = ['a', 'b', 'c']
print(list)  # [1, 'a', 'b', 'c', 3]

# 삭제
list[1:3] = []
print(list)  # [1, 'c', 3]

del list[1]
print(list)  # [1, 3]