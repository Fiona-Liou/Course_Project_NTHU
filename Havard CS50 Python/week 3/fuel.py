def get_input(x,y):
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            break
        except (ValueError, ZeroDivisionError):
            pass

def get_input():
    while True:
        try:
            x_input, y_input = input("Fraction: ").strip().split("/")
            x = int(x_input)
            y = int(y_input)
            if y == 0 or x > y or x < 0:
                raise ValueError
            return x, y
        except (ValueError, ZeroDivisionError):
            pass

def fraction(x, y):
    percentage = round(x / y * 100)
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    x, y = get_input()
    print(fraction(x, y))

if __name__ == "__main__":
    main()
    fraction(x,y)

