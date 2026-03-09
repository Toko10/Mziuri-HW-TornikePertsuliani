class Ticket:
    def __init__(self, movie_name, price, amount, language="Geo"):
        self.movie_name = movie_name
        self.price = price
        self.amount = amount
        self.language = language

    def __str__(self):
        return f"Movie Name: {self.movie_name} Price: {self.price} Amount: {self.amount} Language: {self.language}"

    def __gt__(self, other):
        if other.amount > other.amount:
            return True
        else:
            return False

class User:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

    def __str__(self):
        return f"User: {self.user}, balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("successfully deposited")

    def ticket_dot_ge(self, t_obj, atb): # t_obj = ticket object, atb = amount to buy
        total_price = t_obj.price * atb

        if total_price <= self.balance:
            self.balance -= total_price
            print(f"succsessfully bought ticket with total price of {total_price}. remaining balance: {self.balance}")

        elif self.balance < total_price:
            print(f"not enough money. total price is {total_price}. remaining balance is {self.balance}")

        else:
            self.balance -= total_price
            t_obj.amount -= atb
            print(f"you bought {atb} ticket with total price of {total_price}. remaining balance is {self.balance}")



t = Ticket("Interstellar", 6, 7)
user1 = User("Napoleon Bonaparte", 20)
user1.deposit(67)
user1.__str__()
user1.ticket_dot_ge(t, 2)
user1.__str__()
user1.__gt__(user1)
print(user1.balance)

t2 = Ticket("Titanic", 67, 20)
user1 = User("Iago Xvichia", 50)
user1.ticket_dot_ge(t2, 2)
user1.deposit(100)
print(user1)
print(t2)