# 최대공약수(gcd())
import math

# 최소공배수(lcm)을 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대공약수 계산
print(lcm(21, 14)) # 최소공배수 계산

# 7
# 42