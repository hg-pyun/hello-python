# 파이썬에서는 ', ", ''', """을 사용해서 문자열을 나타낼 수 있음
food = "Python's favorte food is perl"
print(food);

multiLine = '''
This is linebreak
You use this!
'''
print(multiLine)

# 문자열 더하기
head = "Python"
tail = " is Fun!"
print(head + tail)

# 문자열 곱하기
multiple = "multi"
print(multiple*2)

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 indexing
w = "Hello World!"
print(w[0], w[2], w[-1])

# 문자열 slicing
s = w[0:5]
print([s]) # 0~4 까지

s1 = w[6:]
s2 = w[:5]
print(s1, s2)

# 문자열 formatting
number = 3
print("I eat %d apples." % number)

# 문자열 관련 function
# count / find
text = "hobby"
print(text.count('b'))  # 2
print(text.find('y'))   # 4

# join
comma = ","
print(comma.join('abcd'))

# 공백 제거
spaceText = " hi "
print(spaceText.lstrip(), spaceText.rstrip())
print(spaceText.strip())

# formating 2
print("I eat {0} apples".format(3))
print("I eat {number} {something}".format(number=5, something="bananas"))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))