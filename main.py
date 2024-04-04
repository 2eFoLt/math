from math import sqrt


class StatArray:
    precision = 0
    x_i = []
    m_i = []
    med_x = 0
    Db = 0
    n = 0
    sig = 0

    def __init__(self, x_array, m_array, precision):
        self.precision = precision
        self.x_i = x_array
        self.m_i = m_array
        self.n = sum(m_array)
        self.med_x = 1 / self.n * sum([self.x_i[i] * self.m_i[i] for i in range(len(self.m_i))])
        self.Db = 1 / self.n * sum([self.m_i[i] * (self.x_i[i] - self.med_x) ** 2 for i in range(len(self.m_i))])
        self.sig = sqrt(self.Db)

    def h(self, number):
        return round(number, self.precision)

    def __str__(self):
        return f'\n{self.n}:\nXi: {self.x_i}\nMi: {self.m_i}\n' \
               f'medX: {self.h(self.med_x)}\nDb: {self.h(self.Db)}\nSigma: {self.h(self.sig)}'


stat_object = StatArray([6, 8, 10, 12, 14, 16, 18, 20, 22],
                        [16, 24, 28, 32, 25, 24, 20, 18, 15], precision=4)
print(stat_object)

