#N1

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 2500:
#             print("2500 Larze mets ver gamoitant :|")
#         else:
#             self.balance += amount
#             print("tanxa warmatebit chairicxa :)")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("angarishze sakmarisi tanxa ar aris :(")
#         else:
#             self.balance -= amount
#             print("tanxa warmatebit gamoitanet :)")
#
#     def display_balance(self):
#         print("Account Owner:", self.owner)
#         print("Balance:", self.balance, "GEL")
# account1 = BankAccount("Tornike", 1000)
# account1.display_balance()
# account1.deposit(int(input("sheitanet chasaricxi tanxa: ")))
# account1.withdraw(int(input("sheitanet gamosatani tanxa: ")))
# account1.display_balance()

#N2

# class Shape:
#     def describe(self):
#         print("I am a shape")
# class Polygon(Shape):
#     def __init__(self, *sides):
#         self.sides = sides
# class Triangle(Polygon):
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)
#         self.a = a
#         self.b = b
#         self.c = c
#     def calculate_area(self):
#         s = (self.a + self.b + self.c) / 2
#         area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
#         return area
# triangle1 = Triangle(3, 4, 5)
# triangle1.describe()
# print("samkutxedis fartobi:", triangle1.calculate_area())