n=4

if n<=1:
    print("No")
else:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print("prime")
else:
    print("No")

#prime number in array:
arr=[1,2,3,4,5,6,7,8,9,10]
primes = []

for n in arr:
    if n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)

print("Prime numbers in array:", primes)

