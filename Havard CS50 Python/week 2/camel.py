def main():
    x = input("camelCase: ").strip()
    s = ""
    for c in x:
        if c.isupper() == True:
            s += "_" + c.lower()
        else:
            s += c
    print(f"snake_case: {s}")

main()
