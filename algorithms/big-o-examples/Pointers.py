num1 = 11
# Start of the main code block.

# Assign the value 11 to the variable num1.

num2 = num1
# Assign the value of num1 to num2.

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Print the value of num1 and num2.

print("\nnum1 points to:", id(num1))
# Print the memory address of num1.

print("num2 points to:", id(num2)) 
# Print the memory address of num2.

num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 
# Print the value of num1 and num2 after num2 is updated.

print("\nnum1 points to:", id(num1))
# Print the memory address of num1.

print("num2 points to:", id(num2))
# Print the memory address of num2.


#####################################

# Start of the main code block.

# Create a dictionary with a key 'value' and a value of 11.

dict1 = {
         'value': 11
        }

# Assign the dictionary dict1 to dict2.

dict2 = dict1 

# Print the value of dict1 and dict2.

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Print the memory address of dict1 and dict2.

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

# Update the value of dict2 to 22.

dict2['value'] = 22

# Print the value of dict1 and dict2 after the update.

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

# Print the memory address of dict1 and dict2 after the update.
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

