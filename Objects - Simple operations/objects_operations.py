import math
import random
import turtle


def main():
    print(find_double_return(100, 0.01, return_fixed_rate))


def encrypt_dist(input_str='example', pos=1):
    # to decrypt, use pos = -1 * pos_initial
    normal_str = 'abcdefghijklmnopqrtsuvwxyz '
    result = ''

    for char in input_str:
        char_pos = normal_str.index(char)
        if char_pos + pos < len(normal_str):
            result = result + normal_str[char_pos + pos]
        else:
            char_pos = char_pos + pos - len(normal_str)
            result = result + normal_str[char_pos]

    return result


def turtle_life2(nr_moves=18):
    # move turtle based on nr of moves, with random angles and distances
    # f - forward
    # b - backward
    # l - left
    # r - right

    tarta = turtle.Turtle()

    for a in range(nr_moves):
        i = random.choice('fblr')
        if i == 'f':
            dist = random.randint(10, 100)
            tarta.forward(dist)
        elif i == 'b':
            dist = random.randint(10, 100)
            tarta.backward(dist)
        elif i == 'r':
            angle = random.randint(10, 180)
            tarta.right(angle)
        elif i == 'l':
            angle = random.randint(10, 180)
            tarta.left(angle)
    turtle.exitonclick()


def turtle_life1(moves='ffrfbblff'):
    # move turtle based on string command, with random angles and distances
    # f - forward
    # b - backward
    # l - left
    # r - right

    tarta = turtle.Turtle()

    for i in moves:
        if i == 'f':
            dist = random.randint(10, 100)
            tarta.forward(dist)
        elif i == 'b':
            dist = random.randint(10, 100)
            tarta.backward(dist)
        elif i == 'r':
            angle = random.randint(10, 180)
            tarta.right(angle)
        elif i == 'l':
            angle = random.randint(10, 180)
            tarta.left(angle)
    turtle.exitonclick()


def turtle_life(moves='ffrfbblff'):
    # move turtle based on string command
    # f - forward
    # b - backward
    # l - left
    # r - right

    tarta = turtle.Turtle()
    dist = 20
    angle = 90

    for i in moves:
        if i == 'f':
            tarta.forward(dist)
        elif i == 'b':
            tarta.backward(dist)
        elif i == 'r':
            tarta.right(angle)
        elif i == 'l':
            tarta.left(angle)
    turtle.exitonclick()


def suffixes(phrase='Monty Python'):
    for i in range(len(phrase)):
        print(phrase[-i - 1:])


def prefixes(phrase='Monty Python'):
    for i in range(len(phrase)):
        print(phrase[:i + 1])


def sub_string(phrase, length):
    # print all substrings of 'length'
    for i in range(len(phrase) - length + 1):
        print(phrase[i:i + length])


def replace_vowels(text):
    # replace vowels with a blank space ' '.
    vowels = 'AEIOUaeiou'
    result = text
    for vowel in vowels:
        result = result.replace(vowel, ' ')
    return result


def random_DNA(size=20):
    result = ''
    for i in range(20):
        result = result + random.choice('TACG')
    return result


def DNA_pair(dna):
    # Transforms a DNA chain in its pair (using if-else)
    # bases = 'TACG'
    # pairs = 'ATGC'
    result = ''
    for base in dna.upper():
        if base == 'T':
            result = result + 'A'
        elif base == 'A':
            result = result + 'T'
        elif base == 'C':
            result = result + 'G'
        elif base == 'G':
            result = result + 'C'
        else:
            print("One of the bases is not valid")
    return result


def encrypt_replacement_key(input_str, key_str='pocdefghijklmnbaqrtsuvwxyz '):
    normal_str = 'abcdefghijklmnopqrtsuvwxyz '
    result = ''
    for i in input_str:
        result = result + key_str[normal_str.find(i)]

    return result


def decrypt_even_odd(input_str):
    # Decrypts a 'String', encrypted by the function 'encrypt_even_odd'
    result = ''
    nr_odd = int(len(input_str) / 2)
    nr_even = len(input_str) - nr_odd
    odd_str = input_str[nr_even:]
    even_str = input_str[0:nr_even]

    for i in range(len(even_str)):
        if i + 1 <= len(odd_str):
            result = result + even_str[i] + odd_str[i]
        else:
            result = result + even_str[i]

    return odd_str, even_str, result


def encrypt_even_odd(input_str):
    # Encrypts a 'String' by separating the characters by their position, even or odd
    even_str = ''
    odd_str = ''

    even_str = input_str[0::2]
    odd_str = input_str[1::2]

    return even_str + odd_str


def method_bisection1(list_coefficients, min_int, max_int, repetitions=10):
    # Finds the value x with f(x) = 0, for a polynomial f(x) = a[n] * x^n + a[n-1] * x^(n-1) + ... + a[1] * x + a[0]
    # [a, x] [x, b]
    # https://en.wikipedia.org/wiki/Bisection_method

    a = min_int
    b = max_int

    for i in range(repetitions):
        x = (a + b) / 2
        sol_a = polynomial(a, list_coefficients)
        sol_b = polynomial(b, list_coefficients)
        sol_x = polynomial(x, list_coefficients)

        if sol_b * sol_x <= 0:
            # goes right
            a = x
        elif sol_a * sol_x <= 0:
            # goes left
            b = x
        else:
            print('No answer found!')

    return x, sol_x


def method_bisection2(list_coefficients, min_int, max_int, max_error):
    # Finds the value x with f(x) = 0, for a polynomial f(x) = a[n] * x^n + a[n-1] * x^(n-1) + ... + a[1] * x + a[0]
    # [a, x] [x, b]
    # https://en.wikipedia.org/wiki/Bisection_method
    # max_error, max difference between 2 consecutive results

    a = min_int
    b = max_int

    x = (a + b) / 2
    sol_x = polynomial(x, list_coefficients)

    while max_error < abs(sol_x):
        x = (a + b) / 2
        sol_a = polynomial(a, list_coefficients)
        sol_b = polynomial(b, list_coefficients)
        sol_x = polynomial(x, list_coefficients)

        if sol_b * sol_x <= 0:
            # goes right
            a = x
        elif sol_a * sol_x <= 0:
            # goes left
            b = x
        else:
            print('No answer found!')

    return x, sol_x


def show_polynomial(list_coefficients):
    # Gives a 'String' that represents a polynomial, given the list of coefficients
    # list_coefficients = [a[0], a[1], ..., a[n]]
    # f(x) = a[n] * x^n + a[n-1] * x^(n-1) + ... + a[1] * x + a[0]
    result = ''
    for n, a in enumerate(list_coefficients):
        if a != 0:
            # determine sign
            if a > 0:
                sign = '+'
            else:
                sign = '-'

            if n == 0:
                result = result + f' {sign} {abs(a)}'
            elif n == 1:
                result = result + f' {sign} {abs(a)} x'
            else:
                result = result + f' {sign} {abs(a)} x^{n}'
    return result


def polynomial(x, list_coefficients):
    # list_coefficients = [a[0], a[1], ..., a[n]]
    # f(x) = a[n] * x^n + a[n-1] * x^(n-1) + ... + a[1] * x + a[0]
    result = 0
    for n, a in enumerate(list_coefficients):
        result += a * x ** n
    return result


def triangle_area_heron(a, b, c):
    # calculate triangle area by Heron's formula
    # a: size of side a
    # b: size of side b
    # c: size of side c

    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def hypotenuse(height, angle):
    # angle: angle in degrees
    angle_rad = math.pi * angle / 180
    return height / math.sin(angle_rad)


def max_heart_beat(age):
    # Average maximum heart beat for a given age
    return 163 + 1.16 * age - 0.018 * age ** 2


def return_fixed_rate(value, rate, years, n=1):
    # value: initial investment value
    # rate: decimal rate, for example: 1% -> 0.01
    # n: number of times the rate is compounded
    return value * (1 + rate) ** (years * n)


def find_double_return(value, rate, function=return_fixed_rate):
    # returns how many years to double an investment and final value
    value_required = 2 * value
    current_value = value
    years = 0
    while current_value < value_required:
        current_value = function(value, rate, years)
        years += 1
    return years - 1, current_value


if __name__ == '__main__':
    main()
