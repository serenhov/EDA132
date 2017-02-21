import numpy as np
import math
import matplotlib.pyplot as plt


def read_svm_file(my_file):
    label = []
    words = []
    nbr_of_a = []
    svm = open(my_file, "r")
    for line in svm:
        line = line.split(' ')
        first = line[0]
        line_1 = line[1]
        line_2 = line[2]
        line_1_split = line_1.split(':')
        second = line_1_split[1]
        line_2_split = line_2.split(':')
        third = line_2_split[1]
        label.append(int(first))
        words.append(float(second))
        nbr_of_a.append(float(third))
    return label, words, nbr_of_a


def logistic_regression(svm_data, w1, w2, learning_rate):
    w0 = 1
    weights = []
    new_weights = []
    probs = []
    weights.append(w0)
    weights.append(w1)
    weights.append(w2)
    arr = np.arange(30)
    while True:
        np.random.shuffle(arr)
        probs.clear()
        for i in arr:
            new_weights.clear()
            x = - (w0 + (w1 * svm_data[1][i]) + (w2 * svm_data[2][i]))
            # Calculates the probability for each point having class 1
            hw = 1 / (1 + math.exp(x))
            probs.append(hw)
            w0 += learning_rate * (svm_data[0][i] - hw) * hw * (1 - hw)
            w1 += learning_rate * (svm_data[0][i] - hw) * hw * (1 - hw) * svm_data[1][i]
            w2 += learning_rate * (svm_data[0][i] - hw) * hw * (1 - hw) * svm_data[2][i]
            new_weights.append(w0)
            new_weights.append(w1)
            new_weights.append(w2)
            if stop_criteria(weights, new_weights) < 0.001:
                print(probs)
                return w0, w1, w2
            weights.clear()
            weights.append(new_weights[0])
            weights.append(new_weights[1])
            weights.append(new_weights[2])


# Stop criteria for the logistic regression function
def stop_criteria(weights, new_weights):
    sum = 0
    for i in range(3):
        sum += math.fabs((weights[i] - new_weights[i]) / new_weights[i])
    result = sum / 3
    return result


def plot_data(data, regression):
    for i in range(0, 27):
        if data[0][i] == 0:
            plt.plot(data[1][i], data[2][i], 'ro')
        else:
            plt.plot(data[1][i], data[2][i], 'bo')
    k = - 1 * regression[1] / regression[2]
    m = regression[0] / regression[2]
    x_0 = 0
    y_0 = m
    x_1 = 1
    y_1 = k * (x_1 - x_0) + y_0
    plt.plot([x_0, x_1], [y_0, y_1], 'g')
    plt.show()


svm_data = read_svm_file('file.txt')
result = logistic_regression(svm_data, 0, 1, 0.1)
print(result, "RESULTAT")
plot_data(svm_data, result)



