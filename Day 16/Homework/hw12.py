#13) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123


corect_paswword = "goabest123"
user_input = ""

while user_input != corect_paswword:
    user_input = input("Enter your password:")
    if user_input == corect_paswword:
        print(" Password corect")

    else:
        print("incorect please try again")


