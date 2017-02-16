import matplotlib.pyplot as plt
import numpy as np


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
    print('x:', max_x, 'y', max_y)
    print(px_val)
    for val in px_val:
        new_val = val / max_x
        x_val.append(new_val)
    for val in py_val:
        new_val = val / max_y
        y_val.append(new_val)
    print(x_val, y_val)
    return x_val, y_val


def plot_data(my_data1, my_data2, grad1, grad2):
    plt.plot(my_data1[1], my_data1[0], 'ro')
    plt.plot(my_data2[1], my_data2[0], 'bo')
    plt.plot(grad1, 'b')
    plt.plot(grad2, 'r')
    plt.show()


def compute_error_for_line_given_points(b, m, data):
    total_error = 0
    for i in range(0, 15):
        x = data[0][i]
        y = data[1][i]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(14)


def step_gradient(b_current, m_current, data, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(14)
    for i in range(0, 14):
        x = data[0][i]
        y = data[1][i]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(data, starting_b, starting_m, learning_rate):
    b = starting_b
    m = starting_m
    while compute_error_for_line_given_points(b, m, data) > 0.001:
        b, m = step_gradient(b, m, np.array(data), learning_rate)
    #print(b, m, 'grad')
    return [b, m]


def runnow(data):
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, data)))
    print("Running...")
    [b, m] = gradient_descent_runner(data, initial_b, initial_m, learning_rate)
    print("After {0}, m = {1}, error = {2}".format(b, m, compute_error_for_line_given_points(b, m, data)))
    return b, m


data_english = read_file_and_scale('english')
data_french = read_file_and_scale('french')
eng_grad = runnow(data_english)
fren_grad = runnow(data_french)
plot_data(data_english, data_french, eng_grad, fren_grad)
