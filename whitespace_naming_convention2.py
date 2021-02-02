# By Kami Bigdely
# PEP8 - whitespaces and variable names.
"""Create a class for making a pizza."""
class Pizza:
    """Initialialize the pizza class."""
    def __init__ (self, my_bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.my_bread_type= my_bread_type
        self.cheese_type = cheese_type
        self.meat_type= meat_type
        self.toppings = pizza_toppings
        self.size = size
    @classmethod
    def create_chicago_pizza(cls, size):
        """create the chicago pizza method."""
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return cls (bread, cheese, meat_type, toppings, size)
    @classmethod
    def create_california_pizza(cls, meat_type, size):
        """create the california pizza method."""
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings =[ 'garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper' ]
        return cls(bread, cheese, meat_type, toppings, size)
    def print_info(self):
        """create the print pizza method."""
        print('bread type is: ', self.my_bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

my_pizza = Pizza.create_california_pizza('chicken', 'large')
my_pizza.print_info()
