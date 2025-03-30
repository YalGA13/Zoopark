class Animal:
    def __init__(self, name, age, growth):
        self.name = name
        self.age = age
        self.growth = growth

    def make_sound(self):
        return "Звуки животных"

    def eat(self):
        return f"{self.name} питается."

    def moves(self):
        return f"{self.name}  гуляет."

    def __str__(self):
        return f"Животное: {self.name}, Возраст: {self.age}, Рост: {self.growth}"


class Bird(Animal):
    def __init__(self, name, age, growth, wing_span):
        super().__init__(name, age, growth)
        self.wing_span = wing_span

    def make_sound(self):
        return "Громко кричит"

    def moves(self):
        return f"{self.name} летает."

    def __str__(self):
        return super().__str__() + f", Размах крыла: {self.wing_span}"


class Mammal(Animal):
    def __init__(self, name, age, growth, fur_color):
        super().__init__(name, age, growth)
        self.fur_color = fur_color

    def make_sound(self):
        return "Рычит!"

    def __str__(self):
        return super().__str__() + f",Цвет меха: {self.fur_color}"


class Reptile(Animal):
    def __init__(self, name, age, growth, scale_type):
        super().__init__(name, age, growth)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шипит..."

    def moves(self):
        return f"{self.name} ползает."

    def __str__(self):
        return super().__str__() + f", Тип кожи: {self.scale_type}"


# Polymorphism demonstration
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


def animal_moves(animals):
    for animal in animals:
        print(animal.moves())


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Сотрудник: {self.name}, Должность: {self.position}"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        animal_list = "\n".join(str(animal) for animal in self.animals)
        employee_list = "\n".join(str(employee) for employee in self.employees)
        return f"Зоопарк: {self.name}\nЖивотные:\n{animal_list}\nСотрудники:\n{employee_list}"


# Example usage
if __name__ == "__main__":
    bird = Bird("Попугай", 2, 25, "Средний")
    mammal = Mammal("Лев", 5, 120, "Золотистый")
    reptile = Reptile("Питон", 3, 50, "Чешуйчатый")

    zookeeper = Employee(" Иван Сидоров", "Смотритель зоопарка")
    veterinarian = Employee(" Петр Иванов", "Ветеринар")

    zoo = Zoo("Парк дикой природы")
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)

    print(zoo)
