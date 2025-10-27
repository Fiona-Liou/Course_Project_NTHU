def main():
  plate = input("Plate: ")
  if is_valid(plate):
        print("Valid")
  else:
        print("Invalid")


def is_valid(plate):
  if not plate[0:2].isalpha():
    return False
  elif len(plate) < 2 or len(plate) > 6:
    return False
  elif not plate.isalnum():
        return False
  found_digit = False
  
  for char in plate:
      if char.isdigit():
          if found_digit == False:
            found_digit = True
            if char == '0':
              return False
      else:
          if found_digit == True:
            return False
  return True


if __name__ == "__main__":
    main()
