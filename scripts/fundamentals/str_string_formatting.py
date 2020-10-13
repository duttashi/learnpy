# Objective: to discuss string formatting
name = "Bob"
greeting = "Hello, Bob"
print(greeting)

# F-Strings
name = "Anne"
print(greeting) # This will still print, Hello Bob

# but if we use embedeed string like given, it will print different
print(f"Hello, {name}")

# Using .format()
# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)