#1) დაბეჭდეთ 2 რიცხვს შორის (რიცხვები შეცვალეთ) ყველა შესაძლო შედარების ოპერაცია გვერდზე კომენტარის სახით მიუწერეთ პასუხი

#2) სამივე ლოგიკურ ოპერატორზე: not, or, and: ჩამოწერეთ ყველა შესაძლო ვარიანტი და დაბეჭდეთ შედეგი გვერდზე კომენტარის საშვალებით მიწუერეთ შედეგი

print(5>2)#true
print(14<7)#folse
print(8==8)#true
print(8>=8)#true
print(8!=7)#true

#განვიხილოთ true ების შემთხვევა:
x=5
y=10
#not
print(not(x==6))
print(not(x>y))
#or
print(x>4 or y<9)
print(x<4 or y>7)
#and
print(x==5 and y==10)
print(x>=4 and y<15)

#განვიხილოთ folse ების შემთხვევა:
x=5
y=10
#not
print(not(x==5))
print(not(y>9))
#or
print(x>6 or y<9)
print(x==6 or y>20)
#and
print(x==10 and y<44)
print(x>=2 and y<=7)