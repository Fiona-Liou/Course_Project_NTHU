def main():
    original = input("Input: ")
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    shorten = ""
    for char in original:
        if char not in vowels:
            shorten += char
    print(f"Output: {shorten}")


if __name__ == "__main__":
    main()
