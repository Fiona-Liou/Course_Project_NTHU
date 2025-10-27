months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        date = input("Date: ").strip()

        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except ValueError:
                continue
              
        elif "," in date:
            try:
                month_day, year = date.split(",")
                month_day = month_day.strip()
                year = int(year.strip())
                month, day = month_day.split()
                day = int(day)

                if month in months:
                    month_num = months.index(month) + 1
                    if 1 <= day <= 31:
                        print(f"{year:04d}-{month_num:02d}-{day:02d}")
                        break
            except ValueError:
                continue
        else:
            continue


if __name__ == "__main__":
    main()
