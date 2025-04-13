#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა


corect_password = "1234"
counter = 0

user_input = input("Enter your password")
while user_input != corect_password:
    counter += 1
    user_input = input("incorect please try again")


print("corect this password your try is "+ str(counter))




