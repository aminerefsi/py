# New Python file

print("Hello, world!")
print
spam = input("what is your name?")
print (f"it is good to meet you, {spam}!")
print(f"your name has {len(spam)} letters in it.")
age = int(input("what is your age?"))
print(f"next year, you will be {age + 1} years old.")

if age == 10:
    print('eggs')
    if age > 5:
       print('bacon')
    else:
        print('ham')
    