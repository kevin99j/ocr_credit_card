import matplotlib.pyplot as plt


def show_image(image, tittle, cmap):
    img_plot = plt.imshow(image, cmap=cmap)
    plt.title(tittle)
    plt.show()


def show_contours(image, contours):
    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
