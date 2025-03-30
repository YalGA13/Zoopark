import json


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
        return f"{self.name} гуляет."

    def to_dict(self):
        return self.__dict__

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

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Bird"
        return data

    def __str__(self):
        return super().__str__() + f",Размах крыла: {self.wing_span}"


class Mammal(Animal):
    def __init__(self, name, age, growth, fur_color):
        super().__init__(name, age, growth)
        self.fur_color = fur_color

    def make_sound(self):
        return "Рычит!"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Mammal"
        return data

    def __str__(self):
        return super().__str__() + f", Цвет меха: {self.fur_color}"


class Reptile(Animal):
    def __init__(self, name, age, growth, scale_type):
        super().__init__(name, age, growth)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шипит..."

    def moves(self):
        return f"{self.name} ползает."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Reptile"
        return data

    def __str__(self):
        return super().__str__() + f", Тип кожи: {self.scale_type}"


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"Сотрудник:{self.name}, Должность: {self.position}"


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель")

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            "name": self.name,
            "animals": [animal.to_dict() for animal in self.animals],
            "employees": [employee.to_dict() for employee in self.employees]
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        zoo = cls(data["name"])
        for animal_data in data["animals"]:
            if animal_data["type"] == "Bird":
                animal = Bird(animal_data["name"], animal_data["age"], animal_data["growth"], animal_data["wing_span"])
            elif animal_data["type"] == "Mammal":
                animal = Mammal(animal_data["name"], animal_data["age"], animal_data["growth"],
                                animal_data["fur_color"])
            elif animal_data["type"] == "Reptile":
                animal = Reptile(animal_data["name"], animal_data["age"], animal_data["growth"],
                                 animal_data["scale_type"])
            else:
                continue
            zoo.add_animal(animal)
        for employee_data in data["employees"]:
            if employee_data["position"] == "Смотритель":
                employee = ZooKeeper(employee_data["name"])
            elif employee_data["position"] == "Ветеринар":
                employee = Veterinarian(employee_data["name"])
            else:
                continue
            zoo.add_employee(employee)
        return zoo

    def __str__(self):
        animal_list = "\n".join(str(animal) for animal in self.animals)
        employee_list = "\n".join(str(employee) for employee in self.employees)
        return f"Зоопарк: {self.name}\nЖивотные:\n{animal_list}\nСотрудники:\n{employee_list}"


# Example usage
if __name__ == "__main__":
    zoo = Zoo("Парк дикой природы")
    zoo.add_animal(Bird("Попугай", 2, 25, "Средний"))
    zoo.add_animal(Mammal("Лев", 5, 120, "Золотистый"))
    zoo.add_animal(Reptile("Питон", 3, 50, "Чешуйчатый"))
    zoo.add_employee(ZooKeeper("Иван Сидоров"))
    zoo.add_employee(Veterinarian("Петр Иванов"))

    # Save to file
    zoo.save_to_file("zoo_data.json")

    # Load from file
    loaded_zoo = Zoo.load_from_file("zoo_data.json")
    print(loaded_zoo)
