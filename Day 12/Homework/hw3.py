
#3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ შედარების ოპერაციათა შედეგებს, შედარების ოპერაციას გვერდზე კომენტარის საშვალებით მიუწერეთ მისი შედეგი (boolean მნიშვნელობა) და ახსენით რა განსხვავებაა ოპერატორსა და ოპერაციას შორის


#რა განსხვავებაა ოპერატორებსა და ოპერაციას შორის:

#ოპერაცია:

#x=10>5 #true
#y=30<=20 #folse
#z=10==10 #true
#b=20!=20 #folse
#c=10>=12 #true

# ოპერაციები გვაგებიენებენ თუ რა ინფორმაციას ინახავს კონკრეტული მაგალითი მაგალიტად: x- (folse)_ია  თუ (true), ეს არის bool ოპერატორები რომლებსაც შედეგის სახით 2 არჩევანი აქვთ ან ჭეშმარიტია მოცემული მაგალითი ან მცდარი ანუ bool ოპერაცია არის ლოგიკური ოპერაცია და მისი 3 ძირითადი ოპერატორია: (not _ != );  (and ); (or) 

#ოპერატორები:
#x1=10
#y1=20
#print(x1>=10 and x1<11 )  # ეს არის and ოპერატორი რომელიც გამიმტანს true
#print(not(x1<y1)) # ეს არის not ოპერატორი რომელიც გამოიტანს false 
#print((x1+5)<y1 or (x1+y1)< y1) # ეს არის or ოპერატორი და შედეგად გამოიტანს true

                  
#რაც შეეხება ოპერაციებს მათ არჩევნის საშუალება არ აქვთ ლოგიკურ ოპერატორებთან განსხვავებით და გამოაქვთ ტერმინალზე ის პასუხი რაც სწორია ანუ სრულდება მოქმედებები როგორიცაა (/, //, *, %, **)
print (21//2+4)
