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
    max_x = max(px_val)
    max_y = max(py_val)
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
    plt.plot(grad1, 'b')
    plt.plot(grad2, 'r')
    plt.show()
    print(my_data1)

#plt.plot(read_file_and_scale('english')[0], read_file_and_scale('english')[1], 'ro')


# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, data):
    totalError = 0
    for i in range(0, len(data)):
        x = data[i][0]
        y = data[i][1]
        totalError += (y - (m * x + b)) ** 2
    return print(totalError / float(len(data)))


def step_gradient(b_current, m_current, data, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(data))
    for i in range(0, len(data)):
        x = data[i][0]
        y = data[i][1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    #print(new_b,new_m, 'step')
    return [new_b, new_m]


def gradient_descent_runner(data, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(data), learning_rate)
    #print(b, m, 'grad')
    return [b, m]


def runnow(data):
    learning_rate = 0.1
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, data)))
    print("Running...")
    [b, m] = gradient_descent_runner(data, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, data)))
    return m, b


data_english = read_file_and_scale('english')
data_french = read_file_and_scale('frensh')
eng_grad = runnow(data_english)
fren_grad = runnow(data_french)
plot_data(data_english, data_french, eng_grad, fren_grad)
