# номинал монет (1, 2, 5, 10 и т.п; кол-во купюрж;)
# вычислить сумму монет
class TaskOne():
    def __init__(self,price,count):
        self.price = price
        self.count = count
    def desc(self):
        print(f"Имеется {self.count} монет номиналом каждая в {self.price} рубль")
    def sum(self):
        result = self.count * self.price
        print(f"Всего имеется {result} рублей")


if __name__ == "__main__":
    wallet = TaskOne(5,27)
    wallet.desc()
    wallet.sum()