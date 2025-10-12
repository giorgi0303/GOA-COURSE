#1) დაწერეთ პროგრამა რომლის გაშვებისას მომმხმარებელს შეეძლება 2 ათწილადი რიცხვის შემოტანა, შემოტანილი რიცხვებზე ჩაატარეთ ყველა მათემატიკური მოქმედება

#2) გამოიყენეთ ყველა  converter ფუნქცია int, str, float გააკეთეთ 2-2 მაგალითი და კომენტარებით ახსენით რას აკეთებს თითოეული

#3)  input საშუალებით შემოიტანეთ 2 რიცხვი ეს რიცხვები გარდაქმენით float შემდეგ გამოიყენეთ ამ რიცხვებზე ყველა მათემატიკური ოპერაცია და შედარებები (კომენბატრებით ახსენით თითოეული კოდის დეტალი რას აკეთებთ და რატომ გამოიყენეთ შესაბამისი ფუნქციები)

#4) ახსენით კომენტარებით რა არის Boolean მონაცემთა ტიპი და რაში გამოიუყენება


#1.

User_input = float(input("Enter your number just decimal:"))
user_input = float(input("Enter your number just decimal:"))

print(User_input + user_input)
print(User_input - user_input)
print(User_input * user_input)
print(User_input / user_input)
print(User_input % user_input)

#2.
num = int(5.5) # int არის ფუნქცია რომელსაც შეუძლია მონაცემი გადააქციოს მთელ რიცხვად მაგ მივიღებთ აქ - 5
num1 = float(5) # float არის ფუნქცია რომელსაც შეუძლია მონაცემი გადააქციოს ათწილად რიცხვად მაგ მივიღებთ აქ - 5.0
num2 = str("5" + "3") #str არის ფუნქცია რომელიც გვატყობინებს რომ ეს არის ტექსტური მონაცემი მაგ მიიღებთ აქ - 53

print(num)
print(num1)
print(num2)

#3.
User_Input = float(input("Enter your number just decimal:"))
UseR_InpuT = float(input("Enter your number just decimal:")) #აქ კოდი ისე არის დაწერილი რომ მომხმარებლის მიერ შემოყვანილი რიცხვი გარდაიქმნება ათწილადის სახით და შეასრულებს ნებისმისერ მოქმედებას ათწილადის სახით და ამ ყველაფერს განაპირობებს float ფუნქცია

print(User_Input + UseR_InpuT)
print(User_Input - UseR_InpuT)
print(User_Input * UseR_InpuT)
print(User_Input / UseR_InpuT)
print(User_Input % UseR_InpuT)

#4.

#boool_იანი მონაცემის ტიპი განსაძრვრავს ლოგიკური მონაცემებს ანუ ეს არის ფუნქცია რომელიც დაწერილ კოდს განსაღვრას ჭეშმარიტია თუ მცდარი