import math

test_cases = int(input())

for i in range(1, test_cases + 1):

    V, D = input().split()
    V = int(V)
    D = int(D)

    deg = round(math.degrees((math.asin((D * 9.8) / (V ** 2)) / 2)), 7)

    print(f"Case #{i}: {deg}")
