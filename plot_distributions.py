from utility import *

plt.plot(wavelengths, sensitivities.values[:, 0], color="red", label="L")
plt.plot(wavelengths, sensitivities.values[:, 1], color="green", label="M")
plt.plot(wavelengths, sensitivities.values[:, 2], color="blue", label="S")
plt.legend()
plt.grid()
plt.xlabel("Wavelength [nm]")
plt.ylabel("Cone sensitivity relative to maximum")
plt.title("Cone sensitivities of the CIE 2015 2 Degree Standard Observer")
plt.show()

plt.plot(wavelengths, spds_rgb_lcd.values[:, 0], color="red", label="r")
plt.plot(wavelengths, spds_rgb_lcd.values[:, 1], color="green", label="g")
plt.plot(wavelengths, spds_rgb_lcd.values[:, 2], color="blue", label="b")
plt.legend()
plt.grid()
plt.xlabel("Wavelength [nm]")
plt.ylabel("Spectral power distribution")
plt.title(
    "Approximations to the spectral power distributions of the average screen"
)
plt.show()

plt.plot(wavelengths, spds_cmy_abebe.values[:, 0], color="cyan", label="c")
plt.plot(wavelengths, spds_cmy_abebe.values[:, 1], color="magenta", label="m")
plt.plot(wavelengths, spds_cmy_abebe.values[:, 2], color="yellow", label="y")
plt.legend()
plt.grid()
plt.xlabel("Wavelength [nm]")
plt.ylabel("Spectral power distribution")
plt.title(
    "Approximations to the spectral power distributions of the average printer"
)
plt.xlim(400, 700)
plt.show()
