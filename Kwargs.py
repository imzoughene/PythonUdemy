class CarKwargs:
    def __init__(self,**kwargs):
        self._data=kwargs

    def SetType(self,type):
        self._data["Type"]=type
    def GetType(self):
        return self._data["Type"]

    def SetModel(self, Model):
        self._data["Model"] = Model

    def GetModel(self):
        return self._data["Model"]



    def SetPrice(self, Price):
        self._data["Price"] = Price

    def GetPrice(self):
        return self._data["Price"]



    def SetMilesDrive(self, MilesDrive):
        self._data["MilesDrive"] = MilesDrive

    def GetMilesDrive(self):
        return self._data["MilesDrive"]


    def SetOwner(self, Owner):
        self._data["Owner"]= Owner

    def GetOwner(self):
        return self._data["Owner"]

    def GetPriceByMiles(self):
        return self.GetPrice()-(self.GetMilesDrive()*10)