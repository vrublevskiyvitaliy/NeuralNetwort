
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
            s = 0
            for j in range(self.n_receptors + 1):
                s += self.network_connections[j][i] * d[j]
            if s > 0:
                answer.append(1)
            else:
                answer.append(-1)
        return answer

    def get_reaction_row(self, data):
        answer = []
        d = list(data)
        # add 1 at the begging of test case
        d.insert(0, 1)
        for i in range(self.n_neurons):
            s = 0
            for j in range(self.n_receptors + 1):
                s += self.network_connections[j][i] * d[j]
            answer.append(s)
        return answer

    def teach_neuron(self, index_of_neuron, data, val):
        d = list(data)
        d.insert(0, 1)

        for j in range(self.n_receptors + 1):
            self.network_connections[j][index_of_neuron] = \
                self.network_connections[j][index_of_neuron] + d[j] * val
