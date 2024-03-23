a=int(input("enter the ticket price:"))
if(a>250 and a<300):
    print("recliners")
elif(a>150 and a<200):
    print("gold")
elif(a>100 and a<150):
    print("silver")
elif(a>200 and a<250):
    print("platinum")
else:
    print("Balcony")
