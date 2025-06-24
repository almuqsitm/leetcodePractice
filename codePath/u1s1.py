# s = "Never gonna give you up"
# print(s)
# s = s.split()
# print(s)
# s = " ".join(s)
# print(s)

# names = ["Alice", "Bob", "Charlie", "lol", "sdasd", "sdasdsa"]
# ages = [25, 30, 35, 33, 34]
# zipped = zip(names, ages)
# print(list(zipped))
# print(zipped)

n1 = [1, 32, 3, 5, 6]
n2 = [val + 2 for val in n1]
print(n2)


# Problem 1: Hundred Acre Wood
# Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
def welcome():
    print("Welcome to The Hundred Acre Wood!")


welcome()


# Problem 2: Greeting
def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Mohammed")


greeting("Bob")


# Problem 3: Catchphrase
def print_catchphrase(character):
    if character == "Pooh":
        print('"Oh bother!"')
    elif character == "Tigger":
        print('"TTFN: Ta-ta for now!"')
    elif character == "Eeyore":
        print('"Thanks for noticing me."')
    elif character == "Christopher Robin":
        print('"Silly old bear."')
    else:
        print(f"\"Sorry! I don't know {character}'s catchphrase!\"")


character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)
print("\n\nProblem 4")


# Problem 4: Return Item
def get_item(items, x):
    if x >= len(items) or x < 0:
        return None
    else:
        return items[x]


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))

print("\n\nProblem 5")
# Problem 5: Total Honey


def sum_honey(hunny_jars):
    if len(hunny_jars) == 0:
        return 0
    else:
        total = 0
        for i in hunny_jars:
            total += i
        return total


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

print("\n\nProblem 6")


# Problem 6: Double Trouble
def doubled(hunny_jars):
    if hunny_jars is None:
        return None
    dbled = [i * 2 for i in hunny_jars]
    return dbled


hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
hunny_jars = [1, 100]
print(doubled(hunny_jars))
hunny_jars = []
print(doubled(hunny_jars))
hunny_jars = None
print(doubled(hunny_jars))

print("\n\nProblem 7")
# Problem 7: Poohsticks


def count_less_than(race_times, threshold):
    if race_times is None or race_times == []:
        return 0
    else:
        counter = 0
        for i in race_times:
            if i < threshold:
                counter += 1

        return counter


race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))


print("\n\nProblem 8")
# Problem 8: Pooh's To Do's


def print_todo_list(task):
    print("Pooh's To Dos:")
    for i, n in enumerate(task):
        print(f" {i}. {n}")
    print()


task = [
    "Count all the bees in the hive",
    "Chase all the clouds from the sky",
    "Think",
    "Stoutness Exercises",
]
print_todo_list(task)

task = []
print_todo_list(task)

print("\n\nProblem 9")
# Problem 9: Pairs


def can_pair(item_quantities):
    if item_quantities == []:
        return True
    else:
        for i in item_quantities:
            if i % 2 != 0:
                return False
        return True


item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))
item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))
item_quantities = []
print(can_pair(item_quantities))


print("\n\nProblem 10")
# Problem 10: Split Haycorns


def split_haycorns(quantity):
    if quantity <= 0:
        return []
    result = []

    for i in range(1, quantity + 1):
        if quantity % i == 0:
            result.append(i)

    return result


quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

print("\n\nProblem 11")
# Problem 11: T-I-Double Guh-ER


def tiggerfy(s):
    tiger = "tiger"
    result = ""
    for char in s:
        temp = char.lower()
        if temp not in tiger:
            result += char

    return result


s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

print("\n\nProblem 12")
# Problem 12: Thistle Hunt


def locate_thistles(items):
    result = []

    for index, val in enumerate(items):
        if val == "thistle":
            result.append(index)

    return result


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
