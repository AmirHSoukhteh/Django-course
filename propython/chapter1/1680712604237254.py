def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

dic = {}
for i in range(10):
    num = int(input())
    divisors = get_divisors(num)
    prime_divisors = [d for d in divisors if prime(d)]
    num_prime_divisors = len(prime_divisors)
    dic[num] = num_prime_divisors

sor = dict(sorted(dic.items(), key=lambda x:(x[1], x[0])))
a = list(sor.keys())[-1]
print(a, dic[a])