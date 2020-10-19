# 중복 조합
from itertools import combinations_with_replacement

arr = ['A', 'B', 'C']

result = list(combinations_with_replacement(arr, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]