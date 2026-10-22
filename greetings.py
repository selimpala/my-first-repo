def greet(name):
    return f"Hey, {name}! Welcome to the interactive lab session."

def farewell(name):
    return f"Goodbye, {name}, see you next time!"

def shout(name):
    return f"HELLO {name.upper()}!!!"

def thank_you(name):
    return f"Thank you, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(shout("World"))
    print(thank_you("World"))

print("DEBUG: delete me before sharing!")
