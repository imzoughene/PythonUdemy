import Kwargs
def main():
    myCar = Kwargs.CarKwargs(Type ="BMW",Model=2012,Price=26000,MilesDrive=15,Owner="Imzoughene")

    currentPrice=myCar.GetPriceByMiles()
    print("{}'s Car : New Price : {}".format(myCar.GetOwner(),currentPrice))

    HamidCar = Kwargs.CarKwargs(Type ="GMC",Model=2006,Price=28000,MilesDrive=7,Owner="hamid")

    currentPrice = HamidCar.GetPriceByMiles()
    print("{}'s Car : New Price : {}".format(HamidCar.GetOwner(),currentPrice))

if __name__ == '__main__':main()