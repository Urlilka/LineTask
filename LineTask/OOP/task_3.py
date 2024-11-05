# Цена товара
class TaskThree():
    # Конструкт
    def __init__(self, price, count):
        self.price = price # атрибут - цена
        self.count = count # атрибут - кол-во товара
    # метод отображения информации
    def description_product(self):
        print(f"стоимость продукта равна {self.price}, в количестве {self.count} штук")
    # метод подсчёта стоимости продукта
    def sum(self):
        result = self.price * self.count
        print(f"Стоимость товара в количестве {self.count} штук - {result} рублей")

if __name__ == "__main__":
    iphone_15 = TaskThree(80000, 2) # создан объект, ему передали значение
    iphone_15.description_product()
    redos = TaskThree(5000,10)
    redos.description_product()
    redos.sum()
