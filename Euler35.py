from eulerlib import primes
from eulerlib import is_prime


def compute():
    isprime = primes(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(is_prime(int(s[i:] + s[:i])) for i in range(len(s)))

    ans = sum(1 for i in isprime if is_circular_prime(i))
    return str(ans)


if __name__ == "__main__":
    print(compute())
