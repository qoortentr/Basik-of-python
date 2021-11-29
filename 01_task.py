class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def fun(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def valid_date(date):
        if 1 <= Date.fun(date)[0] <= 31 and 1 <= Date.fun(date)[1] <= 12:
            return 'Is Valid'
        else:
            raise ValueError("Date is not valid")


print(Date.fun('05-07-2021'))
# print(Date.valid_date('05-07-2021'))
print(Date.valid_date('12-13-14'))
