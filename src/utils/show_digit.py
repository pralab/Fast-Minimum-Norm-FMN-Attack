import matplotlib.pyplot as plt


def show_image(title, samples, perturbed, diffs, preds, labels, n_display=8):
    n_display = min(n_display, samples.shape[0])
    fig = plt.figure(figsize=(2 * n_display, 6))
    plt.suptitle(title)
    classes = range(10)
    for idx in range(n_display):
        plt.subplot(3, n_display, idx + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(samples[idx, ...].reshape((28, 28)), cmap='gray')
        plt.subplot(3, n_display, idx + n_display + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(perturbed[idx, ...].reshape((28, 28)), cmap='gray')
        plt.title("{} ({})".format(classes[labels[idx].item()],
                                   classes[preds[idx]]),
                  color=("green" if labels[idx].item() == preds[idx].item()
                         else "red"))
        plt.subplot(3, n_display, idx + (n_display * 2) + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(diffs[idx, :].reshape((28, 28)), cmap='seismic',
                   vmin=-1, vmax=1)

    fig.tight_layout()
