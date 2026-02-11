#N1
from encodings.idna import ace_prefix

# try:
#     x = int(input("Sheitane ricxvi chemidzma: "))
#     y = int(input("Sheitane ricxvi chemidzma: "))
#     z = x / y
#     print(z)
# except ZeroDivisionError:
#     print("Division by zero")
# except ValueError:
#     print("Value Error")
# except TypeError:
#     print("Type Error")

#N2

# def divide_numbers(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Division by zero"
#     except TypeError:
#         return "type Error"
#     except ValueError:
#         return "Value Error"
# print(divide_numbers(10, 2))
# print(divide_numbers(5, 0))
# print(divide_numbers(8, "a"))

#N3

# random_list = [6, 7, "xachapuri", "lobiani", "chixirtma", 0.6, "67"]
# try:
#     a=int(input("sheitanet index: "))
#     print(random_list[a])
# except IndexError:
#     print("index out of range")

#N4

# try:
#     with open("myresult.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File myresult.txt does not exist")

#N5

# try:
#     a = int(input("sheitanet ricxvi 1: "))
#     b = int(input("sheitanet ricxvi 2: "))
#     c = int(input("sheitanet ricxvi 3: "))
#     D = b**2 - 4 * a * c
#     if D > 0:
#         X1 = (-b + D) / (2 * a)
#         X2 = (-b - D) / (2 * a)
#         print(f"X1={X1}, X2={X2}")
#     elif D == 0:
#         X1 = (-b + D) / (2 * a)
#         print(f"X1={X1}")
#     elif D < 0:
#         print("X1=0")
# except ValueError:
#     print("value error")
# except ZeroDivisionError:
#     print("zero division")
# except TypeError:
#     print("type error")

#N6

# def triangle_average(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return (a + b + c) / 3
#     else:
#         return print("ar akmayofilebs samkutxedis sigrdzeebis wess")
# try:
#     x = int(input("sheiyvanet ricxvi 1: "))
#     y = int(input("sheiyvanet ricxvi 2: "))
#     z = int(input("sheiyvanet ricxvi 3: "))
#     result = triangle_average(x, y, z)
#     print("sashualo aritmetikulia:", result)
# except ValueError:
#     print("value error")
