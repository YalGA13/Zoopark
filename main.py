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
        return super().__str__() + f", Цвет меха: {self.fur_color}"


class Reptile(Animal):
    def __init__(self, name, age, growth, scale_type):
        super().__init__(name, age, growth)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шипит..."

    def moves(self):
        return f"{self.name} ползает."

    def __str__(self):
        return super().__str__() + f",Тип кожи: {self.scale_type}"


# Polymorphism demonstration
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


def animal_moves(animals):
    for animal in animals:
        print(animal.moves())


# Example usage
if __name__ == "__main__":
    bird = Bird("Попугай", 2, 25, "Средний")
    mammal = Mammal("Лев", 5, 120, "Золотистый")
    reptile = Reptile("Питон", 3, 50, "Чешуйчатый")

    animals = [bird, mammal, reptile]

    print("Звуки животных:")
    animal_sound(animals)

    print("\nДвижения животных:")
    animal_moves(animals)
