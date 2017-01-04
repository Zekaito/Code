def get_year():
    check=False

    while not check:
        year=input("Please input a 4 digit year")
        if len(year)==4:
            try:
                year=int(year)
                print(year)
                check=True
            except:
                pass

get_year()
