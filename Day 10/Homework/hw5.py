#5) მომხმარებელს შემოატანინეთ თავისი ასაკი, შემდეგ შემოატანინეთ წლების რაოდენობა. მიღებული ინფორმაცია შეინახეთ ცვლადებში და გამოითვალეთ, რამდენი წლის იქნება მომხმარებელი y (მომხმარებლის მიერ შემოტანილი) წლის შემდეგ. საბოლოოდ გამოუტანეთ შედეგი შემდეგი სახით: "[წლები] წლის შემდეგ თქვენ იქნებით [მომავალი ასაკი] წლის". დავალების შესასრულებლად გამოიყენეთ მონაცემთა ტიპების ხელოვნურად შეცვლის მეთოდები: int() - რომ შეასრულოთ ართიმეტიკული მოქმედებები, str() - რომ დაბეჭდოთ შედეგი შეცდომების გარეშე

age = int(input("Enter your age:"))

after_years = int(input("Enter your years:"))

final_result = age + after_years 

print("you will be " + str(final_result) + " years old after " + str(after_years) + " years")
