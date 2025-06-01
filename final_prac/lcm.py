def gcd(a, b): # 最大公因數
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): # 最小公倍數
    return abs(a * b) // gcd(a, b) # 取整數

a, b = map(int, input().split())
print(lcm(a, b))