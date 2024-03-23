class carshowroom:
    def __init_(self):
        self.sgst=0.18
        self.cgst=0.92
        self.insurance=100000
    def company(self,companyname):
         while True:
             print("toyota,mercedes")
             self.n=input("enter the car company")
             if self=="toyota":
                print("welcome to toyo")
                self.model()
                break
             elif self.n=="mercedes":
                print("welcome to merc")
                self.model()
                break
             else:
                print("enter the valid car company")
    def model(self):
        while True:
            print("bolero","thar")
            if self.n=="toyato":
                while True:
                    print("select from fourtner and LC")
                    self.choice=input("enter the car model:")
                    if self.choice=="fourtner":
                       self.price(self.choice)
                       break
                    else:
                        print("enter valid")
            elif self.n=="mercedes":
                while True:
                    print("select from amg and gw")
                    self.choice=input("enter the car model:")
                    if self.choice=="amg":
                        self.price(self.choice)
                        break
                    else:
                        print("enter valid")
    def price(self,choice):
        if choice=="fourtner":
            self.p=4500000
        elif choice=="LC":
            self.p==1000000
        elif choice=="amg":
            self.p=24563789
        elif choice=="gw":
            self.p=98765443
    tot_p=self.p+self.sgst+self.cgst+self.insurance
    print(tot_p)
a=carshowroom()
a.company()
