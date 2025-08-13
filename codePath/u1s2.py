print("Problem 1:")


def are_equivalent(word1, word2):
    w1 = ""
    w2 = ""
    for word in word1:
        w1 += word
    for word in word2:
        w2 += word

    if w1 == w2:
        return True
    else:
        return False


word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))

word1 = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2))

# ---------------
print("\nProblem 2:")


def count_evens(lst):
    res = 0
    for element in lst:
        if len(element) % 2 == 0:
            res += 1

    return res


lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst))

lst = ["the", "joker", "robin"]
print(count_evens(lst))

lst = [
    "you",
    "either",
    "die",
    "a",
    "hero",
    "or",
    "you",
    "live",
    "long",
    "enough",
    "to",
    "see",
    "yourself",
    "become",
    "the",
    "villain",
]
print(count_evens(lst))


# --------------
print("\nProblem 3:")


def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people


people = ["Batman", "Superman", "Bruce Wayne", "The Riddler", "Bruce Wayne"]
secret_identity = "Bruce Wayne"
print(remove_name(people, secret_identity))

# --------------
print("\nProblem 4:")


def count_digits(n):
    res = 0
    if n < 10:
        return 1
    while n > 0:
        n = n // 10
        res += 1
    return res


n = 964
print(count_digits(n))

n = 0
print(count_digits(n))


# --------------
print("\nProblem 5:")


def move_zeroes(lst):
    left = 0
    right = 1

    while right < len(lst):
        if lst[left] != 0:
            left += 1
            right += 1
            continue
        elif lst[right] != 0:  # left = 0 right != 0
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right += 1
        else:
            right += 1
    return lst


lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))
lst = [1, 0, 0, 0, 3, 0]
print(move_zeroes(lst))

# --------------
print("\nProblem 6:")


def reverse_vowels(s):
    vowels = {"a", "e", "i", "o", "u"}
    s = list(s)  # Convert to list to allow swapping
    l, r = 0, len(s) - 1

    while l < r:
        if s[l].lower() not in vowels:
            l += 1
        elif s[r].lower() not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return "".join(s)  # Back to string


s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))


# --------------
print("\nProblem 7:")


def highest_altitude(gain):
    return "Skipped"


gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain))
