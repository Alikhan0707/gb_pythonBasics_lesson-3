def new_user(firstName, secondName, birthday, city, email, tel):
    return f"My name is {firstName} {secondName}, I was born in {city} in {birthday}. My email address and telephone number is {email}, {tel} "


first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
birthday = input("Enter date of your birth. (dd.mm.yyyy): ")
city = input("Enter city of birth: ")
email = input("Enter your email")
tel_num = input("Enter your phone numbers: ")

user1 = new_user(firstName=first_name, secondName=second_name, birthday=birthday, city=city, email=email, tel=tel_num)

print(user1)
