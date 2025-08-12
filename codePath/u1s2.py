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
