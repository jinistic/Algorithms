from itertools import combinations, product

def solution(M, burgerPrices, toppingPrices):
    if M < min(burgerPrices):
        return -1  
        
    all_toppings = [0] + toppingPrices
    all_burgers = [[0] for _ in range(len(burgerPrices))]

    for i in combinations(toppingPrices, 2):
        if sum(i) <= M:
            all_toppings.append(sum(i))

    for i in range(len(burgerPrices)):
        for j in all_toppings:
            if burgerPrices[i] + j <= M:
                all_burgers[i].append(burgerPrices[i] + j)

    result = []
    for i in product(*all_burgers):
        if sum(i) <= M:
            result.append(sum(i))

    print("all_toppings : ", all_toppings)
    print("all_burgers : ", all_burgers)
    print("result : ", result)
    return max(result)

print(solution(23, [5, 20], [8, 10]))
print(solution(43, [5, 20, 30], [8, 10, 20]))
print(solution(3, [5, 20, 30], [8, 10, 20]))
