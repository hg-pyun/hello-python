# 불 자료형은 다음의 2가지 값만을 가질 수 있다.

a = True
b = False
print(a, b)

# 비교 연산자
print(1 == 1) # True
print(2 > 1)  # True
print(2 < 1)  # False

# 연습문제 1
print('연습문제 1')
print(1 != 1) # False
print(3 > 1)  # True
print('a' in 'abc') # True
print('a' not in [1, 2, 3]) # True

# 연습문제 2
print('연습무넺 2')
a = "python"
print(bool(a)) # True
b = ""
print(bool(b)) # False
c = (1, 2, 3)
print(bool(c)) # true
d = 0
print(bool(d)) # false