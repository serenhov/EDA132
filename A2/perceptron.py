from random import randint
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
    print(len(label), len(words), len(nbr_of_a))
    return label, words, nbr_of_a


def perceptron_stochastic(svm_data, w1, w2, learning_rate):
    while True:
        print()
        missed = 0
        random = randint(0, 27)
        print('random: ', random)
        if (w1 * svm_data[1][random] + w2 * svm_data[2][random]) > 0:
            hw = 1
            print('hw1')
        else:
            hw = 0
            print('hw0')
        w1 += learning_rate * (svm_data[0][random] - hw) * svm_data[1][random]
        w2 += learning_rate * (svm_data[0][random] - hw) * svm_data[2][random]
        print(svm_data[0][random], svm_data[1][random], svm_data[2][random], "hej")
        print('w1', w1, 'w2', w2, 'heja på')
        for i in range(27):
            if (w1 * svm_data[1][i] + w2 * svm_data[2][i]) > 0:
                res1 = 1
            else:
                res1 = 0
            if res1 != svm_data[0][i]:
                missed += 1
                print("Missed++")
        if missed < 1:
            break
    return w1, w2


def plot_data(data, perceptron):
    for i in range(0, 27):
        if data[0][i] == 0:
            plt.plot(data[1][i], data[2][i], 'ro')
        else:
            plt.plot(data[1][i], data[2][i], 'bo')
    plt.plot(perceptron, 'g')
    plt.show()


ddata = read_svm_file('file.txt')
result = perceptron_stochastic(ddata, 0, 1, 0.1)
print(result, "RESULTAT")
plot_data(ddata, result)



