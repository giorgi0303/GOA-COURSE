#6) Bonus დავალება
#შექმენით პროგრამა, რომელიც განსაზღვრავს productive ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
#read_pages ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).
#free_time ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.
#productive ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი და თავისუფალი დრო ჰქონდა.

#მაგალითი:
#თუ read_pages = 25 და free_time = True, მაშინ productive = True.
#თუ read_pages = 15 და free_time = True, მაშინ productive = False.
#თუ read_pages = 30 და free_time = False, მაშინ productive = False.

read_pages = int (input ("Enter your read pages:"))
free_time = int (input("Enter your free time 1=Yes/0=No:"))
productive = bool (read_pages >= 20 or free_time)
if productive == True:
    print("good job!!!")
else:
    print("you are lazy")

    

sales = int (input ("enter your sales:"))
many_sales = int (input (" enter your winner:")) 
producty_sales = bool (sales >=1000000 and many_sales >=1000000)

if producty_sales == True:
    print("congrulaion")
else:
    print("none_enought")



