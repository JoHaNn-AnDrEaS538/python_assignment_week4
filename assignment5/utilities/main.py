import calculator
import lambda_calculator
import string_oprations

calculator.add(10,5)
calculator.subtract(10,5)
calculator.multiply(10,5)
calculator.divide(10,5)

sample_string = "hello World"

print("Original:", sample_string)
print("Reversed:")
string_oprations.reverse_string(sample_string)
print("Capitalized:")
string_oprations.capitalize_string(sample_string)
print("Lowercase:")
string_oprations.lowercase_string(sample_string)
print("Uppercase:")
string_oprations.uppercase_string(sample_string)
