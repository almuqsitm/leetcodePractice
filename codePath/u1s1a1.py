# Problem 1: Hunny Hunt
print("\nProblem 1")


def linear_search(lst, target):
    for index, element in enumerate(lst):
        if target == element:
            return index
    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
print(linear_search(items, target))


print("\nProblem 2: Bouncy, Flouncy, Trouncy, Pouncy")


def final_value_after_operations(operations):
    result = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            result += 1
        elif op == "trouncy" or op == "pouncy":
            result -= 1

    return result


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))


print("\nProblem 3: T-I-Double Guh-Er II")


def tiggerfy(word):
    word = word.lower()
    result = ""
    dbleG = False
    avoidER = False
    for index, char in enumerate(word):
        if char == "t" or char == "i":
            continue
        elif char == "g" and (word[index + 1] is not None and word[index + 1] == "g"):
            continue
        elif char == "e" and (word[index + 1] is not None and word[index + 1] == "r"):
            continue
        else:
            result += char
    return result


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
