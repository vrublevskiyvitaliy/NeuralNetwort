from Heb.test_bipolar import tests
from Heb.models import *


def create_data_for_learning_bipolar():
    data = list()

    for j in range(len(tests)):
        c_l = [-1] * len(tests)
        c_l[j] = 1
        data.append([
            tests[j],
            c_l
        ])
    return data


def create_data_for_learning_binary():
    data = list()

    for j in range(len(tests)):
        c_l = [0] * len(tests)
        c_l[j] = 1
        data.append([
            tests[j],
            c_l
        ])
    return data

if __name__ == '__main__':

    n = len(tests)

    network = HebNeuronNetworkBipolar(len(tests[0]), n)
    learning_data = create_data_for_learning_bipolar()

    counter = 0
    while True:

        # firstly learn them

        # for each learning case
        for i in range(n):
            # for each neuron
            for n_index in range(n):
                network.teach_neuron(n_index, learning_data[i][0], learning_data[i][1][n_index])

        # check if all know
        flag = True
        for i in range(n):
            reaction = network.get_reaction(learning_data[i][0])
            #print(str(i) + ' ', end='')
            #print(network.get_reaction_row(learning_data[i][0]))
            #print(network.get_reaction(learning_data[i][0]))
            for j in range(n):
                if reaction[j] != learning_data[i][1][j]:
                    flag = False
                    break

        if flag:
            print('We know everything!')
            break

        counter += 1

        if counter > 100:
            print('Too long!')
            break

    r1 = network.get_reaction(learning_data[0][0])
    r2 = network.get_reaction(learning_data[1][0])
    r3 = network.get_reaction(learning_data[2][0])
    r4 = network.get_reaction(learning_data[3][0])

    print(r1)
    print(r2)
    print(r3)
    print(r4)
