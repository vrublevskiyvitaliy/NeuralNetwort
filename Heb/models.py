
class HebNeuronNetworkBipolar:
    def __init__(self, receptors, neurons):
        self.network_connections = []
        self.n_receptors = receptors
        self.n_neurons = neurons

        # initialize connections
        for i in range(receptors + 1):
            new = []
            for j in range(neurons):
                new.append(0)
            self.network_connections.append(new)

    def get_reaction(self, data):
        answer = []
        # add 1 at the begging of test case
        d = list(data)
        d.insert(0, 1)
        for i in range(self.n_neurons):
            # add w0
            s = 0
            #s = self.network_connections[0][i]
            for j in range(self.n_receptors + 1):
                s += self.network_connections[j][i] * d[j]
            if s > 0:
                answer.append(1)
            else:
                answer.append(-1)
        return answer

    def get_reaction_row(self, data):
        answer = []
        # add 1 at the begging of test case
        # data.insert(0, 1)
        for i in range(self.n_neurons):
            # add w0
            s = self.network_connections[0][i]
            for j in range(1, self.n_receptors):
                s += self.network_connections[j][i] * data[j]
            answer.append(s)
        return answer

    def teach_neuron(self, index_of_neuron, data, val):
        #current_val = self.get_reaction(data)[index_of_neuron]
        d = list(data)
        d.insert(0, 1)

        for j in range(self.n_receptors + 1):
            self.network_connections[j][index_of_neuron] = \
                self.network_connections[j][index_of_neuron] + d[j] * val

'''
class HebNeuronNetworkBinary:
    def __init__(self, receptors, neurons):
        self.network_connections = []
        self.n_receptors = receptors
        self.n_neurons = neurons

        # initialize connections
        for i in range(receptors + 1):
            new = []
            for j in range(neurons):
                new.append(0)
            self.network_connections.append(new)

    def get_reaction(self, data):
        answer = []
        # add 1 at the begging of test case
        # data.insert(0, 1)
        for i in range(self.n_neurons):
            # add w0
            s = self.network_connections[0][i]
            for j in range(1, self.n_receptors + 1):
                s += self.network_connections[j][i] * data[j]
            if s > 0:
                answer.append(1)
            else:
                answer.append(0)
        return answer

    def get_reaction_row(self, data):
        answer = []
        # add 1 at the begging of test case
        # data.insert(0, 1)
        for i in range(self.n_neurons):
            # add w0
            s = self.network_connections[0][i]
            for j in range(1, self.n_receptors + 1):
                s += self.network_connections[j][i] * data[j]
            answer.append(s)
        return answer

    def teach_neuron(self, index_of_neuron, data, val):
        #current_val = self.get_reaction(data)[index_of_neuron]

        data.insert(0, 1)

        for j in range(self.n_receptors + 1):
            if data[j] * val == 1:
                diff = 1
            elif data[j] == 0:
                diff = 0
            else:
                diff = -1
            self.network_connections[j][index_of_neuron] += diff

'''







