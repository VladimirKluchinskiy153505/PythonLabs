class Goods:
    def __init__(self,name, weight, price):
        super().__init__(1,2)
        print('init googs')
        self.name = name
        self.weight = weight
        self.price = price
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixingLog:
    ID = 0
    def __init__(self,x, y):
        super().__init__(1,2,3)
        print('init MixingLog')
        self.ID +=1
        self.id = self.ID
    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00")

class MixingLog2:
    ID = 0
    def __init__(self,x,y,z):
        print('init MixingLog2')
        self.ID +=1
        self.id = self.ID
    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 22")

class NoteBook(Goods, MixingLog, MixingLog2):
    pass
if __name__ == '__main__':
    n = NoteBook('Acer', 1.5, 3000)
    n.print_info()
    n.save_sell_log()
    print(NoteBook.__mro__)