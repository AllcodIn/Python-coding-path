import datetime

#getting user input
date_of_birth = input("Enter your date of birth in this format(DD/MM/YYYY): \n")
format_of_date = '%d/%m/%Y'

try:
    #input conversion to a datetime object
    date_of_birth_obj = datetime.datetime.strptime(date_of_birth, format_of_date)

    #getting today date
    today_date = datetime.datetime.now()

    #age calculation in full years
    age = today_date.year - date_of_birth_obj.year
    print(f"\nYou are {age} years old ")

    #finding next year
    this_year_birthday  = datetime.datetime(
        year= today_date.year,
        month= date_of_birth_obj.month,
        day= date_of_birth_obj.day
    )

    if this_year_birthday < today_date:

        next_birthday  = datetime.datetime(
        year= today_date.year + 1,
        month= date_of_birth_obj.month,
        day= date_of_birth_obj.day
        )
    else:
        next_birthday = this_year_birthday
    days_until_birthday = (next_birthday - today_date).days
    print(f"{days_until_birthday} days to go until your birthday")

except ValueError:
    print("Invalid format! Please enter the date in this format(DD/MM/AAAA)")