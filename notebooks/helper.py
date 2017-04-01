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
