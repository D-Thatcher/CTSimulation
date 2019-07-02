import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import data_dir
from skimage.transform import radon, rescale
from skimage.transform import iradon


# Image is a 2D NumPy array.
# SNR is the signal-to-noise ratio to simulate
def simulate_ct(image, snr):

    # image = imread(data_dir + "/phantom.png", as_gray=True)
    image = rescale(image, scale=0.4, mode='reflect', multichannel=False)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

    ax1.set_title("Original")
    ax1.imshow(image, cmap=plt.cm.Greys_r)

    theta = np.linspace(0., 180., int(np.sqrt(image.shape[0]**2 + image.shape[1]**2)), endpoint=False)
    sinogram = radon(image, theta=theta, circle=True)
    ax2.set_title("Radon transform\n(Sinogram)")
    ax2.set_xlabel("Projection angle (deg)")
    ax2.set_ylabel("Projection position (pixels)")
    ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
               extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')

    fig.tight_layout()
    plt.show()


    sinogram += (1./float(snr))*np.random.rand(*sinogram.shape)


    reconstruction_fbp = iradon(sinogram, theta=theta, circle=True)
    error = reconstruction_fbp - image
    print('FBP rms reconstruction error: %.3g' % np.sqrt(np.mean(error**2)))

    imkwargs = dict(vmin=-0.2, vmax=0.2)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5),
                                   sharex=True, sharey=True)
    ax1.set_title("Reconstruction\nFiltered back projection")
    ax1.imshow(reconstruction_fbp, cmap=plt.cm.Greys_r)
    ax2.set_title("Reconstruction error\nFiltered back projection")
    ax2.imshow(reconstruction_fbp - image, cmap=plt.cm.Greys_r, **imkwargs)
    plt.show()




disk = np.zeros((256, 256))
for i in range(disk.shape[0]):
    for j in range(disk.shape[1]):
        if i**2 + j**2 < 40000:
            disk[i,j] = 1.
simulate_ct(disk, 1000)