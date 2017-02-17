import matplotlib.pyplot as plt
import numpy as np
from random import randint


def read_file_and_scale(my_file):
    file = open(my_file, "r")
    x_val = []
    y_val = []
    px_val = []
    py_val = []
    for line in file:
        line = line.strip()
        line = line.split()
        i = 0;
        for word in line:
            if i % 2 == 0:
                i += 1
                py_val.append(int(word))
            else:
                px_val.append(int(word))
    max_y = 76725
    max_x = 5312
    for val in px_val:
        new_val = val / max_x
        x_val.append(new_val)
    for val in py_val:
        new_val = val / max_y
        y_val.append(new_val)
    return x_val, y_val


def plot_data(my_data1, my_data2, grad1, grad2):
    plt.plot(my_data1[0], my_data1[1], 'ro')
    plt.plot(my_data2[0], my_data2[1], 'bo')
    #plt.plot(grad1, 'b')
    #plt.plot(grad2, 'r')

    k = grad1[1]
    m = grad1[0]
    x_0 = 0
    y_0 = m
    x_1 = 1
    y_1 = k * (x_1 - x_0) + y_0
    plt.plot([x_0, x_1], [y_0, y_1], 'r')

    k = grad2[1]
    m = grad2[0]
    print(grad2[0], "m")
    x_0 = 0
    y_0 = m
    x_1 = 1
    y_1 = k * (x_1 - x_0) + y_0
    plt.plot([x_0, x_1], [y_0, y_1], 'b')

    plt.show()


# m is slope, b is y-intercept
def compute_error(b, m, data):
    total_error = 0
    for i in range(0, 14):
        x = data[0][i]
        y = data[1][i]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(14)


def step_gradient(b_current, m_current, data, learning_rate):
    random = randint(0, 14)
    b_gradient = 0
    m_gradient = 0
    N = float(14)
    x = data[0][random]
    y = data[1][random]
    b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
    m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent_stochastic(data, starting_b, starting_m, learning_rate):
    b = starting_b
    m = starting_m
    while compute_error(b, m, data) > 0.0001:
        b, m = step_gradient(b, m, data, learning_rate)
    #print(b, m, 'grad')
    return [b, m]


def run_stochastic(data):
    learning_rate = 0.001
    initial_b = 0
    initial_m = 0
    [b, m] = gradient_descent_stochastic(data, initial_b, initial_m, learning_rate)
    return b, m


# alpha is slope, beta y-intercept
def prediction(data):
    s_xy = 0
    s_xx = 0
    e = 0
    x_hat = np.mean(data[0])
    y_hat = np.mean(data[1])
    for val in data:
        s_xy += (val[0] - x_hat) * (val[1] - y_hat)
        s_xx += (val[0] - x_hat) ** 2
    beta = s_xy / s_xx
    alpha = y_hat - (beta * x_hat)
    for val in data:
        e += val[1] - alpha - (beta * val[0])
    beta = beta + e
    return beta, alpha


data_english = read_file_and_scale('english')
data_french = read_file_and_scale('french')
english_grad = run_stochastic(data_english)
french_grad = run_stochastic(data_french)

plot_data(data_english, data_french, english_grad, french_grad)