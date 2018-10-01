import Class_Car
def main():
    myCar = Class_Car.Car()
    myCar.SetType("BMW")
    myCar.SetModel(2012)
    myCar.SetPrice(26000)
    myCar.SetMilesDrive(15)
    myCar.SetOwner("Imzoughene")
    currentPrice=myCar.GetPriceByMiles()
    print("{}'s Car : New Price : {}".format(myCar.GetOwner(),currentPrice))

    HamidCar = Class_Car.Car()
    HamidCar.SetType("GMC")
    HamidCar.SetModel(2006)
    HamidCar.SetPrice(28000)
    HamidCar.SetMilesDrive(7)
    HamidCar.SetOwner("hamid")
    currentPrice = HamidCar.GetPriceByMiles()
    print("{}'s Car : New Price : {}".format(HamidCar.GetOwner(),currentPrice))

if __name__ == '__main__':main()