# В 100 грамм продукта клорийность --- X
# Вес продукта --- X грамм
class TaskFour():
    def __init__(self,weight,calories):
        self.weight = weight
        self.calories = calories
    def desc(self):
        print(f"В ста грамм X продукта - {self.calories} калориев. Вес X продукта - {self.weight} грамм")
    def sum(self):
        result = self.calories * self.weight / 100
        print(f"общая калорийность - {result} грамм")


if __name__ == "__main__":
    salad = TaskFour(1500,45)
    salad.desc()
    salad.sum()

# S = x * w / 100
# s - общая калорийность
# x - калорийность в 100г
# w - вес блюда
# 100 г