from time import sleep


class TraficLights:
    __color = 'black'

    def running(self):
        self.__color = "red"
        print(f'\r{self.__color}', end='')
        sleep(8)

        self.__color = "yellow"
        print(f'\r{self.__color}', end='')
        sleep(2)

        self.__color = "green"
        print(f'\r{self.__color}', end='')
        sleep(4)

        self.__color = "yellow"
        print(f'\r{self.__color}', end='')
        sleep(2)


run = TraficLights()
run.running()
