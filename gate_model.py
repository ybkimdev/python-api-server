import numpy as np

class Gate:
    def __init__(self, input, output, operend_count):
        self.is_trained = False
        self.input = np.array(input)
        self.output = np.array(output)
        self.W = np.zeros(operend_count, dtype=np.float32)
        self.b = 0.0

    def training(self, learning_rate, epochs):
        for epoch in range(epochs):
            for i in range(len(self.input)):
                input_i = self.input[i]
                output_i = self.output[i]

                if len(self.W) == 1:
                    dot = input_i = self.W[0] * input_i + self.b
                else:
                    dot = np.dot(self.W, input_i) + self.b
                output_predicted = self.step_function(dot)

                error = output_i - output_predicted

                self.W += learning_rate * error * input_i
                self.b += learning_rate * error

        self.is_trained = True

    def step_function(self, dot):
        return 1 if dot >= 0 else 0

    def operate(self, input):
        dot = np.dot(self.W, input) + self.b
        return self.step_function(dot)
    

class UnaryGate(Gate):
    def __init__(self, output):
        super().__init__([0, 1], output, 1)

class BinaryGate(Gate):
    def __init__(self, output):
        super().__init__([[0, 0], [0, 1], [1, 0], [1, 1]], output, 2)

class NotGate(UnaryGate):
    def __init__(self):
        super().__init__([1, 0])

class AndGate(BinaryGate):
    def __init__(self):
        super().__init__([0, 0, 0, 1])

class OrGate(BinaryGate):
    def __init__(self):
        super().__init__([0, 1, 1, 1])
