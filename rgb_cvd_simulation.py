from PIL import Image
from utility import *

alpha_L = float(input("Strength of protanopia (0=normal, 1=full): "))
alpha_M = float(input("Strength of deuteranopia (0=normal, 1=full): "))
lambda_S = int(input("Strength of tritanopia (0=normal, 59=extreme): "))

M = get_Machado_matrix(sensitivities, spds_rgb_lcd, alpha_L, alpha_M, lambda_S)

img = np.array(Image.open("./test_image.png"))

transformed_img = np.clip(np.einsum("ij,...j->...i", M, img), 0, 255).astype(
    np.uint8
)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img)
ax[0].set_title("Original")
ax[0].axis("off")

ax[1].imshow(transformed_img)
ax[1].set_title("Transformed")
ax[1].axis("off")

plt.tight_layout()
plt.show()
