def find_prime(num):
    sqrt_num = int(num**0.5)
    if num == 1: return False
    if num == 2: return True
    if num%2 == 0: return False
    for i in range(3, sqrt_num+1, 2):
        if num%i == 0: return False
    return True

def permutateNumber(list_numbers):
    from itertools import permutations
    permutation_numbers = []
    for length in range(1, len(list_numbers)+1):
        temp = permutations(list_numbers, length)
        for number in temp:
            permutation_numbers.append(number)
    return permutation_numbers


def makePrimeList(permutation_numbers):
    list_prime = []
    for number_set in permutation_numbers:
        number = int("".join(number_set))
        if find_prime(number):
            list_prime.append(number)
    return set(list_prime)

def solution(numbers):
    list_numbers = list(numbers)
    permutation_numbers = permutateNumber(list_numbers)
    set_prime = makePrimeList(permutation_numbers)
    return len(set_prime)

if __name__ == "__main__":
    numbers = "17"
    assert solution(numbers) == 3
