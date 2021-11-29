class Warehouse:
    def __init__(self, worker, car, box):
        self.worker = worker
        self.car = car
        self.box = box


class OfficeEquipment:
    all_product = 0
    all_price = 0
    amount_product = {"notebook": "", "phone": "", "headphone": ""}

    def get_product(self):
        OfficeEquipment.all_product += 1

    def __str__(self):
        return f"Всего коробок: {OfficeEquipment.all_product}. Стоимость всей продукции: {OfficeEquipment.all_price}"


class Notebook(OfficeEquipment):
    count = 0
    note_list = []

    def __init__(self, price, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.price = price
        Notebook.count += 1
        super().get_product()
        OfficeEquipment.all_price += self.price
        Notebook.note_list.append(f"Марка CPU: {self.cpu}, объем RAM: {self.ram}, марка GPU: {self.gpu}, цена: {price}")
        OfficeEquipment.amount_product["notebook"] = f"{Notebook.note_list}"

    def __str__(self):
        return f"На складе {Phone.count} коробок телефонов. Информация о телефонах в выбранной коробке: цена - " \
               f"{self.price}, марка процессора - {self.cpu}, марка видеокарты - {self.gpu}, объем ОЗУ - {self.ram}\n" \
               f"Обновление информации о складе: {OfficeEquipment()}\n\n"


class Phone(OfficeEquipment):
    count = 0
    phone_list = []

    def __init__(self, price, size, color, camera):
        self.size = size
        self.color = color
        self.camera = camera
        self.price = price
        Phone.count += 1
        super().get_product()
        OfficeEquipment.all_price += self.price
        Phone.phone_list.append(f"Цена: {price}, диагональ: {size}, цвет: {color}, кол-во камер: {camera}")
        OfficeEquipment.amount_product["phone"] = f"{Phone.phone_list}"

    def __str__(self):
        return f"На складе {Phone.count} коробок телефонов. Информация о телефонах в выбранной коробке: цена - " \
               f"{self.price}, диагональ - {self.size}, цвет - {self.color}, кол-во камер - {self.camera}\n" \
               f"Обновление информации о складе: {OfficeEquipment()}\n\n"


class Headphone(OfficeEquipment):
    count = 0
    headphone_list = []

    def __init__(self, price, volume):
        self.volume = volume
        self.price = price
        Headphone.count += 1
        super().get_product()
        OfficeEquipment.all_price += self.price
        Headphone.headphone_list.append(f"Цена: {price}, громкость: {volume}")
        OfficeEquipment.amount_product["headphone"] = f"{Headphone.headphone_list}"

    def __str__(self):
        return f"На складе: {Headphone.count} коробка наушников. Информация о наушниках в выбранной коробке: громкость - " \
               f"{self.volume}, цена - {self.price}.\nОбновление информации о складе: {OfficeEquipment()}\n\n"


box_1 = Headphone(15000, 56)
box_2 = Headphone(10000, 34)
print(box_2)

box_3 = Phone(70000, 5.5, 'black', 3)
print(box_3)

box_4 = Notebook(120000, "Intel", "Nvidia", 8)
box_5 = Notebook(128000, "Intel", "Nvidia", 16)
print(box_5)

print(OfficeEquipment.amount_product["notebook"])
print(OfficeEquipment.amount_product["phone"])
print(OfficeEquipment.amount_product["headphone"])
