from itertools import combinations
import math


def domain_name(url):
    domain = url.replace("http://", "").replace("https://", "").replace("www.", "").split(".")[0]
    return domain


def int32_to_ip(int32):
    binary = bin(int32)[2:]
    binary_add_zero = binary.zfill(32)
    result = []
    for index in range(0, len(binary_add_zero), 8):
        result.append(str(int(binary_add_zero[index:index + 8], 2)))
    return '.'.join(result)


def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def bananas(s) -> set:
    result = set()
    word = 'banana'
    for combination in combinations(range(len(s)), len(s) - len(word)):
        list_s = list(s)
        for index in combination:
            list_s[index] = '-'
        if [item for item in list_s if item != '-'] == list(word):
            result.add(''.join(list_s))
    return result


def count_find_num(primesL, limit):
    all_nums = [math.prod(primesL)]
    if all_nums[0] > limit:
        return []

    for prime_num in primesL:
        for num in all_nums:
            calc_num = prime_num * num
            if limit >= calc_num not in all_nums:
                all_nums.append(calc_num)
    return [len(all_nums), max(all_nums)]
