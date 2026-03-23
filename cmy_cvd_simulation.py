from PIL import Image

from utility import *

alpha_L = float(input("Strength of protanopia (0=normal, 1=full): "))
alpha_M = float(input("Strength of deuteranopia (0=normal, 1=full): "))
lambda_S = int(input("Strength of tritanopia (0=normal, 59=extreme): "))

"""
Note: In this test, we do not use the SPDs from physical printer ink!
This is due to the fact that we start from an RGB image that is first
transformed into CMY, after which we apply the CVD simulation.

But the CMY values of our image are still in a color model that assumes SPDs
deduced from the SPDs of an LCD screen.

Therefore, in this test, we use SPDs that are the inverse of the SPDs of an
LCD screen to get consistent results.

To test the Machado matrices obtained from printer CMY SPDs, one would need to
start with a true CMY(K) image, perform the transformation and print the
resulting image.
"""

spds_cmy_test = colour.MultiSpectralDistributions(
    data={wl: 1 - spds_rgb_lcd[wl] for wl in sensitivities.wavelengths},
    labels=["C", "M", "Y"],
    name="Proxy SPDs for CMY",
)

M = get_Machado_matrix(
    sensitivities,
    spds_cmy_test,
    alpha_L,
    alpha_M,
    lambda_S,
)

img = np.array(Image.open("./test_image.png"))

transformed_img = np.clip(
    255 - np.einsum("ij,...j->...i", M, 255 - img), 0, 255
).astype(np.uint8)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img)
ax[0].set_title("Original")
ax[0].axis("off")

ax[1].imshow(transformed_img)
ax[1].set_title(f"Transformed")
ax[1].axis("off")

plt.tight_layout()
plt.show()
