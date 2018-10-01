class User:
    def __init__(self,userName,age):
        print("Constructor Called")
    #def SetUserName(self,userName):
        self._userName=userName
        self._Age=age
    def GetUserName(self):
        return self._userName

    def GetUserAge(self):
        return self._Age
def main():
    userA=User("imzoughene",25)
    #userA.SetUserName("imzoughene")
    print(userA.GetUserName())
    userB = User("fouaji",23)
    #userB.SetUserName("fouaji")
    print(userB.GetUserName())

if __name__ == '__main__':main()
