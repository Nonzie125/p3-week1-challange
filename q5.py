# Define a function named 'factorial' that calculates the factorial of a number 'n'
def calculate_factorial(n):
   # determne whether the number 'n' is 0
    if n == 0:
      return 1   # If 'n' is 0, return 1 (factorial of 0 is 1)
    else:
       return n * calculate_factorial(n- 1)
   
result = calculate_factorial (5)
print(result)# Print the factorial of the number entered by the user by calling the 'factorial' function