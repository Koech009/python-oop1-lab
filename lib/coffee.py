#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")

        self.price += 1


# testing if it works
# Creating a coffee object
coffee1 = Coffee("Medium", 4)

# Printing attributes
print(coffee1.size)
print(coffee1.price)

# Calling method
coffee1.tip()

# Printing updated price
print(coffee1.price)
