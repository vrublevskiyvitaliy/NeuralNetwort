from RozenblatPerceptron.test_binary import *
from RozenblatPerceptron.perceptron import *


if __name__ == '__main__':

    t1 = alphabet[u'В']
    t2 = alphabet[u'І']

    perceptron = RozenblatPerceptronOneR(len(t1), 5)

    # make random
    while True:
        a_res_1_1 = perceptron.calculate_row_a(t1)
        a_res_2_1 = perceptron.calculate_row_a(t2)

        a_bigger_1 = 0
        a_bigger_2 = 0

        # check if we can divide it
        for a_index in range(len(a_res_1_1)):
            if a_res_1_1[a_index] > a_res_2_1[a_index]:
                a_bigger_1 += 1
            else:
                a_bigger_2 += 1
        if a_bigger_1 == len(a_res_1_1) or a_bigger_2 == len(a_res_1_1):
            perceptron.init_sa_matrix()
        else:
            break


    '''
    a_res_all = [] + a_res_1_1 + a_res_2_1

    max_a_1 = max(a_res_1_1)
    min_a_1 = min(a_res_1_1)

    max_a_2 = max(a_res_2_1)
    min_a_2 = min(a_res_2_1)

    max_a = min([max_a_1, max_a_2])
    min_a = max([min_a_1, min_a_2])

    sigma_a = (max_a + min_a) / 2

    # calculate sigma_a
    while True:
        perceptron.set_sigma_a(sigma_a)

        a_res_1 = perceptron.calculate_a(t1)
        a_res_2 = perceptron.calculate_a(t2)

        # check if they are crossing
        flag = True
        for a_index in range(len(a_res_1)):
            c = a_res_1[a_index] + a_res_2[a_index]

            if c != 1:
                flag = False

        if not flag:
            sigma_a = random()*(max_a - min_a) + min_a
        else:
            break
    '''
    a_res_1_1 = perceptron.calculate_row_a(t1)
    a_res_2_1 = perceptron.calculate_row_a(t2)

    for a_index in range(len(a_res_1_1)):
        s = (a_res_1_1[a_index] + a_res_2_1[a_index]) / 2
        perceptron.set_sigma_a(a_index, s)

    a_res_1 = perceptron.calculate_a(t1)
    a_res_2 = perceptron.calculate_a(t2)


    t = 0
