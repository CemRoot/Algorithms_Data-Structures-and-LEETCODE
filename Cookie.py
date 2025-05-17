class Cookie:
    # Defines the Cookie class.
    # This class is a simple representation of a cookie, primarily to demonstrate
    # basic object-oriented principles such as instantiation, attributes, and methods.

    def __init__(self, color):
        # Constructor method for the Cookie class.
        # This method is automatically called when a new Cookie object is created (instantiated).
        # It initializes the cookie's attributes.
        # 
        # Args:
        #     color (str): The initial color of the cookie.
        self.color = color  # Sets the instance attribute 'color' to the value passed as an argument.

    def get_color(self):
        # Method to retrieve the current color of the cookie.
        # 
        # Returns:
        #     str: The current color of this cookie instance.
        return self.color

    def set_color(self, color):
        # Method to change the color of the cookie.
        # 
        # Args:
        #     color (str): The new color to set for the cookie.
        self.color = color  # Updates the instance attribute 'color' with the new value.

# Main part of the script demonstrating the use of the Cookie class.
# This section shows how to create Cookie objects and interact with them using their methods.

# Create two instances (objects) of the Cookie class.
cookie_one = Cookie('green')  # Creates a Cookie object named cookie_one with color 'green'.
cookie_two = Cookie('blue')   # Creates a Cookie object named cookie_two with color 'blue'.

# Demonstrate the get_color method.
print('Cookie one is', cookie_one.get_color())  # Calls get_color() on cookie_one and prints its color.
print('Cookie two is', cookie_two.get_color())  # Calls get_color() on cookie_two and prints its color.

# Demonstrate the set_color method.
cookie_one.set_color('yellow')  # Calls set_color() on cookie_one to change its color to 'yellow'.

# Verify the color change and observe that cookie_two remains unchanged.
print('\nCookie one is now', cookie_one.get_color())  # Prints the new color of cookie_one.
print('Cookie two is still', cookie_two.get_color()) # Prints the color of cookie_two, showing it's independent.
