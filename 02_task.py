class Zero:
    @staticmethod
    def zero(num):
        nums = list(map(int, num.split('/')))
        try:
            nums[0] / nums[1]
        except ZeroDivisionError:
            return 'Ноль не может быть делителем'
        else:
            return nums[0] / nums[1]


add = '121/11'
print(Zero.zero(add))

add = '121/0'
print(Zero.zero(add))

