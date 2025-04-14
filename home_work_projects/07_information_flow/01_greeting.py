def main():
    name = input("What's your name? ")
    print(greet(name))

def greet(name):
    return "Greetings " + name + "!"

if __name__ == '__main__':
    main()