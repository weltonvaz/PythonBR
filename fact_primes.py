def primes_up_to(N):
    sieve = N*[True]
    for i in range(2, N):
        if not sieve[i]: continue
        yield i
        for j in range(i*i, N, i):
            sieve[j] = False

def primeFactors(N):
    answer = ''
    for p in primes_up_to(int(N**0.5)+1):
        count = 0
        while N % p == 0:
            N //= p
            count += 1

        if count == 1:
            answer += '({})'.format(p)
        elif count > 1:
            answer += '({}**{})'.format(p, count)

    if N>1: 
        answer += '({})'.format(N)
    
    return answer

print(primeFactors(86240))
print(primeFactors(7775460))
print(primeFactors(7919))
