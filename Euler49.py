def sieve(n):
    """generates primes up to n."""
    s = [True] * (n + 1)
    for p in range(2, n):
        if s[p]:
            yield p
            for i in range(p * p, n, p):
                s[i] = False


def is_permutation(n1, n2):
    """returns True if n1 is permutation of n2"""
    to_str_1 = str(n1)
    to_str_2 = str(n2)
    if n1 == n2:
        return False
    to_str_1_digits = {digit: to_str_1.count(digit) for digit in to_str_1}
    to_str_2_digits = {digit: to_str_2.count(digit) for digit in to_str_2}
    if not to_str_1_digits == to_str_2_digits:
        return False
    return True


def get_permutations(n):
    """generates tuples of 3 permutations each within range n."""
    primes = set(sieve(n))
    for prime1 in primes:
        for prime2 in primes:
            if is_permutation(prime1, prime2):
                for prime3 in primes:
                    if is_permutation(prime3, prime1) and is_permutation(
                        prime3, prime2
                    ):
                        yield prime1, prime2, prime3


def check_subtraction(n):
    """checks permutations within range n for subtraction rules.
    returns valid permutations."""
    permutations = get_permutations(n)
    for x, y, z in permutations:
        if abs(x - y) == abs(y - z):
            return x, y, z


if __name__ == "__main__":
    x, y, z = sorted(check_subtraction(10000))
    print(str(x) + str(y) + str(z))
