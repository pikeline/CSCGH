# FizzBuzz is a challenge that involves writing code 
# that labels numbers divisible by three as “Fizz,” four as “Buzz”,
# and numbers divisible by both as “FizzBuzz.”
# Do it for numbers 1 to 100

for i in range(0,100):
    output = f"{i} "
    if (i % 3 == 0):
        output += "Fizz"
    if (i % 4 == 0):
        output += "Buzz"
    print(output)
