# Homework 3

# 3.1 Say Goodbye

def say_goodbye(name):
    print("Goodbye,", name)

# 3.2 Area of a Circle

def circle_area(radius):
    print(3.14 * radius**2)

# 4.1 Subtract, Multiply, and Divide

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    return(a / b)

# 5.1 What Should I Wear? 

def low_high(temp):
    return (min(temp), max(temp))

# 5.2 Check if it's the Weekend

def is_weekend(num):
    if num == 6 or num == 7:
        return True
    else:
        return False

# 5.3 Fuel Efficiency Calculator

def fuel_efficiency(distance, fuel):
    return distance/fuel

# 5.4 Secret Code

def secret_code(num):
    return (num % 10) * 10**(len(str(num)) - 1) + (num//10)

# 6.1 Oski Stole Your Power

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

# 6.2.1 For Loops

def min_for(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min

def max_for(list):
    max = list[0]
    for num in list: 
        if num > max:
            max = num
    return max

# 6.2.2 While Loops

def min_while(list):
    min = list[0]
    count = 1
    while count < (len(list)):
        if min > list[count]:
            min = list[count]
            count += 1
        elif min <= list[count]:
            min = min
            count += 1
    return min

def max_while(list):
    max = list[0]
    count = 1
    while count < (len(list)):
        if max < list[count]:
            max = list[count]
            count += 1
        elif max >= list[count]:
            max = max
            count += 1
    return max

# 6.3 Calculate the Sum

def digit_sum(num):
    num_string = str(num)
    count = 0
    sum = 0
    for digit in num_string:
        digit = num_string[count]
        count += 1
        sum += int(digit)
    return sum

num = 4278
result = digit_sum(num) # sums the digits of num
print(f"The result of Calculate the Sum (6.3) with num = 4278 is {result}")