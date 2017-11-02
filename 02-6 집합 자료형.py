s1 = set("Hello")
print(s1)

set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([4, 5, 6, 7, 8, 9])

print(set1 & set2)
print(set1 | set2)
print(set1 - set2)

# 값 한 개 추가
set1.add(7)
print(set1)

# 여러 값 추가
set1.update([8,9,10])
print(set1)

# 값 제거
set1.remove(5)
print(set1)