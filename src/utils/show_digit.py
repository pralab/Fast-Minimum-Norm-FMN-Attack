import matplotlib.pyplot as plt
import torch


def convert_image(image):
    if isinstance(image, torch.Tensor):
        image = image.cpu().numpy()
    if image.ndim == 3:
        image = image.transpose((1, 2, 0))
    if image.shape[-1] == 1:
        image = image.squeeze(-1)
    return image

def show_image(title, samples, perturbed, preds, labels, n_display=8, img_shape=(28, 28)):
    n_display = min(n_display, samples.shape[0])
    fig = plt.figure(figsize=(2 * n_display, 6))
    plt.suptitle(title)
    classes = range(10)
    for idx in range(n_display):
        plt.subplot(3, n_display, idx + 1)
        if idx == 0:
            plt.ylabel('clean')
        plt.xticks([])
        plt.yticks([])
        plt.imshow(convert_image(samples[idx, ...].reshape(img_shape)), cmap='gray')
        plt.subplot(3, n_display, idx + n_display + 1)
        if idx == 0:
            plt.ylabel('adv')
        plt.xticks([])
        plt.yticks([])
        plt.imshow(convert_image(perturbed[idx, ...].reshape(img_shape)), cmap='gray')
        plt.title("{} ({})".format(classes[labels[idx].item()],
                                   classes[preds[idx]]),
                  color=("green" if labels[idx].item() == preds[idx].item()
                         else "red"))

    fig.tight_layout()
