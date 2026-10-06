# 3.1 List Operations

favorite_foods = ["pho", "gimbap", "burrito", "pasta", "tomato soup"]

print(favorite_foods[1])

print(favorite_foods[-1])

favorite_foods.append("dumplings")

favorite_foods.insert(0, "apple")

del favorite_foods[2]

print(len(favorite_foods))

for food in favorite_foods:
    print(food.upper())

firstlast_foods = favorite_foods[0::5]

if food in favorite_foods == "potato":
    print("A potato!")
else:
    print("No potato!")


# 3.2 Slicing and Striding

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]
step1 = get_first_15(numbers)

def get_every_5th(step1):
    return get_first_15(step1)[::5]
step2 = get_every_5th(step1)

def reverse_and_stride(step2):
    reversed = get_first_15(step2)[::-1]
    every_3rd = reversed[::3]
    return every_3rd
step3 = reverse_and_stride(step2)


# 3.3 Nested Lists

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2][0:2])

print(numbers[1][1])

numbers.append([10, 11, 12])

def sum_nested(numbers):
    total = 0
    for list in numbers:
        total += sum(list)
    return total


# 3.4 Create a 5x5 List

def create_5x5():
    list_5x5 = []
    m = 1
    for i in range(5):
        row = []
        added_row = list(range(m, m + 5))
        list_5x5.append(added_row)
        m += 5
    return list_5x5

my_5x5_list = create_5x5()

def replace_3x(list):
    for row in list:
        for num in row:
            if (num % 3) == 0:
                row[row.index(num)] = "?"
    return list

new_5x5_list = replace_3x(my_5x5_list)
print(new_5x5_list)

def sum_my_5x5(list):
    total = 0
    for row in list:
        for num in row:
            if num != "?":
                total += num
    return total

sum_5x5 = sum_my_5x5(new_5x5_list)
print(sum_5x5)


# 4.1 Dictionary Operations

ages = {
    "Katie": 30, 
    "Mariam": 42, 
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"])

ages["Mariam"] = 100

del ages["Mariam"]

for name in ages:
    print(name, ages[name])


# 5.2

my_5x5_list = create_5x5()
print(my_5x5_list)