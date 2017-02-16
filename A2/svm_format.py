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


def read_svm(my_file):
    file = open(my_file, "r")
    x_val = []
    y_val = []
    for line in file:
        line = line.strip()
        line = line.split()
        i = 0;
        for word in line:
            if i % 2 == 0:
                i += 1
                y_val.append(word)
            else:
                x_val.append(word)
    return x_val, y_val


english = read_file_and_scale('english')
french = read_file_and_scale('french')


f = open("file.txt", 'w')
for i in range(0, 15):
    f.write('0 1:')
    f.write('{}'.format(english[1][i]))
    f.write(' 2:')
    f.write('{}'.format(english[0][i]))
    f.write('\n')
for i in range(0, 15):
    f.write('1 1:')
    f.write('{}'.format(french[1][i]))
    f.write(' 2:')
    f.write('{}'.format(french[0][i]))
    f.write('\n')


