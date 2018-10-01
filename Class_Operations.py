class Operations:
    def sum(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class ChildOperations(Operations):
    def multi(self,n1,n2):
        return n1*n2
    def sum(self,n1,n2):
        #return (n1+n2)*2
        return super().sum(n1,n2)*4

def main():
    myTEST= ChildOperations()
    print("multi : {}".format(myTEST.multi(4,7)))
    print("multi : {}".format(myTEST.sum(4,7)))
    print("multi : {}".format(myTEST.div(4,7)))


if __name__ == '__main__':main()
