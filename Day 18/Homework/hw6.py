#6) მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
#შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
#A – თუ score მეტია 80-ზე
#B – თუ score მეტია 60-ზე
#C – თუ score მეტია 40-ზე
#D – თუ score მეტია 20-ზე
#F – თუ score 20-ზე ნაკლებია



user_input_score = int(input("enter your score:"))
if user_input_score >= 80 and user_input_score <= 100:
    print("A")
if user_input_score >= 60 and  user_input_score <80:
    print("B")
if user_input_score >= 40 and user_input_score < 60:
    print("C")
if user_input_score >= 20 and user_input_score <40:
    print("D")
if user_input_score < 20:
    print("F")

