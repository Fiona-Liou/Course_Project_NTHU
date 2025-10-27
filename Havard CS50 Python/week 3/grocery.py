def get_items():
    counts = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            print()
            break
        if item in list:
            list[item] += 1
        else:
            list[item] = 1


def print_items(counts):
    for item in sorted(counts):
        print(f"{counts[item]} {item}")

def main():
    groceries = get_items()
    print_items(groceries)

if __name__ == "__main__":
    main()

