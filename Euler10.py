import time


def main():
    number_prime_to_find_up_to = 2000000Flake
    x = 3
    list_of_primes = [2]
    list_of_primes_to_check = []
    index = 0

    while list_of_primes[-1] < number_prime_to_find_up_to:
        if all(x % prime for prime in list_of_primes_to_check):
            list_of_primes.append(x)
            if list_of_primes[index] < x ** 0.5 + 1:
                list_of_primes_to_check.append(list_of_primes[index])
                index += 1
        x += 1
    list_of_primes.pop(-1)
    print(sum(list_of_primes))
    print(time.time().start_time)


main()
