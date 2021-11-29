class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась\n")

    def turn(self, turn):
        print(f"{self.name} повернула", f"{turn}")


class TownCar(Car):
    def show_speed(self):
        print(
            f"Скорость {self.color, self.name} = {self.speed} км/ч\n" if self.speed <= 60 else f"{self.color} {self.name}"
                                                                                               f" СКОРОСТЬ ПРЕВЫШЕНА\n")


class WorkCar(Car):
    def show_speed(self):
        print(
            f"Скорость {self.color, self.name} = {self.speed} км/ч\n" if self.speed <= 40 else f"{self.color} {self.name}"

                                                                                               f" СКОРОСТЬ ПРЕВЫШЕНА\n")


class SportCar(Car):
    def show_speed(self):
        print(f"Скорость {self.color, self.name} = {self.speed} км/ч\n")

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self, is_polise=True):
        print(f"Скорость полицейской машины = {self.speed} км/ч")


town = Car(60, "blue", "rocket")
town.go()
town.turn("направо")
town.stop()

town = TownCar(65, "Синий", "хомяк")
town.show_speed()  # с превышением

town = TownCar(60, "Синий", "хомяк")
town.show_speed()  # без превышения

work = TownCar(400, "Красный", "слон")
work.show_speed()

sport = SportCar(100, "Призрачный", "гонщик")
sport.show_speed()

police = PoliceCar(100, "Призрачный", "гонщик")
police.show_speed()
