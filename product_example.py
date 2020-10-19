# 중복 순열
from itertools import product

arr = ['A', 'B', 'C']

result = list(product(arr, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]