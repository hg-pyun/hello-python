# 값의 복사
a = [1, 2, 3]
b = a
print(b)
print(id(b)) # 주소값 출력
print(a is b) # a와 b는 동일한 객체인가

# 값의 깊은 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a, b)

from copy import copy
b = copy(a)
print(b is a)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
print(a, b)
a, b = ('python', 'life')   # 튜플은 가로 생략 가능
print(a, b)
[a, b] = ['python', 'life']  # 리스트로 변수를 만들 수도 있음
print(a, b)

