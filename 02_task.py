class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        # self.mass()

    def mass(self):
        mass_asf = self._length * self._width * 25 * 5 // 1000
        print(f'{self._length} m * {self._width} m * 25 kg * 5 cm = {mass_asf} t.')


road_1 = Road(int(input('Add length ')), int(input('Add width ')))
road_1.mass()
