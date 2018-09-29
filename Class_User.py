class User:
    def SetUserName(self,userName):
        self._userName=userName
    def GetUserName(self):
        return self._userName
def main():
    userA=User()
    userA.SetUserName("imzoughene")
    print(userA.GetUserName())
    userB = User()
    userB.SetUserName("fouaji")
    print(userB.GetUserName())

if __name__ == '__main__':main()
