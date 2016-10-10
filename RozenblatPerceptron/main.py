from RozenblatPerceptron.test_binary import *
from RozenblatPerceptron.perceptron import *


if __name__ == '__main__':

    t1 = alphabet[u'В']
    t2 = alphabet[u'Р']

    perceptron = RozenblatPerceptronOneR(len(t1), 2)

    a_res_1 = perceptron.calculate_row_a(t1)
    a_res_2 = perceptron.calculate_row_a(t2)

    t = 0
