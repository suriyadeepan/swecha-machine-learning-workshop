import numpy as np


def show_mnist_image(plt, im, cmap=None):
    assert im.shape[0] == 784
    # reshape
    im_reshaped = im.reshape([28,28])
    plt.imshow(im_reshaped, cmap=cmap)

def show_mnist_image_multi(plt, ims, cmap=None):
    assert ims.shape[1] == 784
    # reshape
    ims_reshaped = ims.reshape([ims.shape[0], 28,28])
    for im in ims_reshaped:
        plt.figure()
        plt.imshow(im, cmap=cmap)


def read_wine_data(filename='data/wine.txt'):

    def process(split_line):
        x, y = [], []
        for i, item in enumerate(split_line):
            if i > 12:
                y.append(int(item))
            else:
                x.append(float(item))
        return x,y

    def read_file():
        with open(filename, 'r') as f:
            return [ process(line.split('\t')) for line in f.read().split('\n')[:-1] ]

    content = read_file()

    X, Y = [], []
    for x, y in content:
        X.append(x)
        Y.append(y)

    return np.array(X, dtype=np.float32), np.array(Y, dtype=np.int64)
