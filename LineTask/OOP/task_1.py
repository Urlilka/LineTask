# номинал купюры (1, 2, 5, 10 и т.п; кол-во купюрж;)
# вычислить сумму купюр
class TaskOne():
    def __init__(self,price,count):
        self.price = price
        self.count = count
    def desc(self):
        print(f"Имеется {self.count} купюр номиналом каждая в {self.price} рубль")
    def sum(self):
        result = self.count * self.price
        print(f"Всего имеется {result} рублей")


if __name__ == "__main__":
    bank = TaskOne(10000,100000)
    bank.desc()
    bank.sum()