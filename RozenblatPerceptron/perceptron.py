from random import random


class RozenblatPerceptronOneR:
    def __init__(self, s_number, a_number):

        self.s_number = s_number
        self.a_number = a_number
        self.r_number = 1

        self.init_sa_matrix()
        self.init_ar_matrix()

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


