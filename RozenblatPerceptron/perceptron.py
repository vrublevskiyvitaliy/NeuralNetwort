from random import random


class RozenblatPerceptronOneR:
    def __init__(self, s_number, a_number):

        self.s_number = s_number
        self.a_number = a_number
        self.r_number = 1

        self.init_sa_matrix()
        self.init_ar_matrix()

        self.sigma_a = 0

    def init_sa_matrix(self):
        self.sa_matrix = []

        for i in range(self.s_number):
            new = []
            for j in range(self.a_number):
                new.append(random())
            self.sa_matrix.append(new)

    def init_ar_matrix(self):
        self.ar_matrix = []

        for i in range(self.a_number):
            new = []
            for j in range(self.r_number):
                new.append(0)
            self.ar_matrix.append(new)

    def set_sigma_a(self, a):
        self.sigma_a = a

    def calculate_row_a(self, test):
        res = []
        for a_index in range(self.a_number):
            c = 0
            for s_index in range(self.s_number):
                c += self.sa_matrix[s_index][a_index]
            res.append(c)
        return res

    def calculate_a(self, test):
        row_res = self.calculate_row_a(test)
        res = []
        for a_index in range(self.a_number):
            c = 0
            if row_res[a_index] >= self.sigma_a:
                c = 1
            res.append(c)

        return res

