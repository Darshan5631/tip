print("WELCOME TO TIP CALCULATOR\n")
a=float(input("ENTER THE TOTAL BILL AMOUNT\n"))
t=float(input("HOW MUCH TIP WOULD YOU LIKE TO GIVE ? 10% , 12% OR 15%\n"))
p=float(input("HOW MANY PEOPLE R THERE TO SPLIT BILL\n"))
tip = (a*t)/100
total = (tip+a)/p
final = round(total,2)
print(f"EACH PERSON SHOULD PAY {final}")