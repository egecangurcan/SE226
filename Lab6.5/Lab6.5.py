# Task 1
def common_list(list1, list2):
    common = []
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
    return common


# Task 2
def palindrome_list(words_list):
    palindrome_list = []
    for string in words_list:
        if string == string[::-1]:
            palindrome_list.append(string)
    return palindrome_list


# Task 3
def sieve_of_eratosthenes(nums):
    if len(nums) == 0:
        return []

    max_num = max(nums)
    primes = [True] * (max_num + 1)

    primes[0] = primes[1] = False

    p = 2
    while p ** 2 <= max_num:
        if primes[p]:
            for i in range(p ** 2, max_num + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [num for num in nums if primes[num]]
    return prime_numbers


# Task 4
def anagrams(word, word_list):
    sorted_word = sorted(word)
    anagram_list = []
    for w in word_list:
        sorted_w = sorted(w)
        if sorted_w == sorted_word:
            anagram_list.append(w)
    return anagram_list


list1 = [1, 3, 5, 7, 8]
list2 = [0, 3, 6, 7, 9]

common = common_list(list1, list2)
print(common)

words_list = ['efe', 'ege', 'easy', 'hard', 'tacocat']
palindrome = palindrome_list(words_list)
print(palindrome)

nums = [5, 17, 35, 67, 35, 89]
print(sieve_of_eratosthenes(nums))

word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
print(anagrams(word, word_list))
