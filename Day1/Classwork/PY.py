#1) შექმენით პროგრამა სადაც მომხმარებელი ტერმინალიდან შემოიტანს ორ პროდუქტს, ეს ორი პროდუქტი კი დაბეჭდეთ (მოიძიეთ ინფორმაცია როგორ უნდა გაკეთდეს input პითონში)

#2) გამოიყენეთ while ციკლი (მოიძიეთ) და მომხმარებელს იქამდე შემოატანინეთ პროდუქტები სანამ არ შემოიტანს სიტყვა exit, ყველა შემოტანიული პროდუქტი უნდა ემატებოდეს სიაში (მოიძიეთ list ების შესახებ ინფორმაცია)

#3) ორივე კოდი ახსენით კომენტარებით


#1.

name = input("Enter your name:")

if name == "Giorgi" :
    print ("Passed")
else:
    print ("Not passed")

#2.

Password = "Giorgi123"
user_input = input("Enter your Password:")

while user_input != Password:
    print("incorect")
    if user_input == Password:
        print ("Pass is correct")
    else:
        print("pass is uncorrect try again")