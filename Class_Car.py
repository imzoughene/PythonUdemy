class Car:
    def __init__(self,type,Model,Price,MilesDrive,Owner):
        self._type=type
        self._Model = Model
        self._Price = Price
        self._MilesDrive = MilesDrive
        self._Owner = Owner

    def SetType(self,type):
        self._type=type
    def GetType(self):
        return self._type

    def SetModel(self, Model):
        self._Model = Model

    def GetModel(self):
        return self._Model

    def SetPrice(self, Price):
        self._Price = Price

    def GetPrice(self):
        return self._Price

    def SetMilesDrive(self, MilesDrive):
        self._MilesDrive = MilesDrive

    def GetMilesDrive(self):
        return self._MilesDrive


    def SetOwner(self, Owner):
        self._Owner = Owner

    def GetOwner(self):
        return self._Owner

    def GetPriceByMiles(self):
        return  self._Price-(self._MilesDrive*10)