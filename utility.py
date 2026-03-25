import colour
import matplotlib.pyplot as plt
import numpy as np

# cone sensitivities
sensitivities_XYZ = colour.MSDS_CMFS["CIE 2015 2 Degree Standard Observer"]
sensitivities = colour.MultiSpectralDistributions(
    data={
        wl: colour.appearance.hunt.MATRIX_XYZ_TO_HPE @ sensitivities_XYZ[wl]
        for wl in sensitivities_XYZ.wavelengths
    },
    labels=["L", "M", "S"],
    name="Cone sensitivities",
)

wavelengths = sensitivities.wavelengths

# SPD curves for a typical CRT monitor (Machado)
spds_rgb_crt = (
    colour.characterisation.datasets.displays.crt.MSDS_DISPLAY_PRIMARIES_CRT[
        "Typical CRT Brainard 1997"
    ]
)
spds_rgb_crt.align(sensitivities.shape)

# SPD curves for a typical LCD monitor (Fairchild Wyble)
spds_rgb_lcd = (
    colour.characterisation.datasets.displays.lcd.MSDS_DISPLAY_PRIMARIES_LCD[
        "Apple Studio Display"
    ]
)
spds_rgb_lcd.align(sensitivities.shape)

# SPD curves for a typical printer (CMYK)
r_cmy_abebe = colour.MultiSpectralDistributions(
    data={
        400: [0.2, 0.16, 0.09],
        410: [0.24, 0.21, 0.075],
        420: [0.34, 0.25, 0.08],
        430: [0.49, 0.27, 0.09],
        440: [0.63, 0.27, 0.1],
        450: [0.71, 0.25, 0.11],
        460: [0.75, 0.22, 0.13],
        470: [0.76, 0.18, 0.16],
        480: [0.75, 0.15, 0.21],
        490: [0.72, 0.13, 0.26],
        500: [0.68, 0.11, 0.35],
        510: [0.62, 0.09, 0.44],
        520: [0.52, 0.08, 0.54],
        530: [0.43, 0.075, 0.63],
        540: [0.35, 0.075, 0.7],
        550: [0.27, 0.075, 0.74],
        560: [0.18, 0.075, 0.755],
        570: [0.13, 0.075, 0.77],
        580: [0.1, 0.09, 0.78],
        590: [0.08, 0.14, 0.79],
        600: [0.07, 0.25, 0.8],
        610: [0.065, 0.41, 0.805],
        620: [0.06, 0.58, 0.81],
        630: [0.06, 0.71, 0.815],
        640: [0.06, 0.78, 0.82],
        650: [0.07, 0.82, 0.83],
        660: [0.085, 0.84, 0.835],
        670: [0.1, 0.855, 0.84],
        680: [0.13, 0.87, 0.845],
        690: [0.17, 0.875, 0.85],
        700: [0.2, 0.88, 0.85],
    },
    labels=["C", "M", "Y"],
    name="Printer ink reflectivities",
)
r_cmy_abebe = r_cmy_abebe.align(sensitivities.shape)
illuminant = colour.SDS_ILLUMINANTS["D65"]
spds_cmy_abebe = colour.MultiSpectralDistributions(
    data={
        wl: illuminant[wl] * r_cmy_abebe[wl] for wl in r_cmy_abebe.wavelengths
    },
    labels=["C", "M", "Y"],
    name="Printer spectral power distributions",
)


def get_T(sensitivities, spds):
    if not sensitivities.shape == spds.shape:
        raise ValueError("Shape mismatch!")
    lms_to_opponent = np.array(
        [[0.6, 0.4, 0], [0.24, 0.105, -0.7], [1.2, -1.6, 0.4]]
    )
    opponent_sensitivities = np.einsum(
        "ij,lj->li", lms_to_opponent, sensitivities.values
    )
    That = np.einsum("lC,li->iC", spds.values, opponent_sensitivities)
    rho = 1 / np.sum(That, axis=1)
    T = np.einsum("i,iC->iC", rho, That)
    return T


def get_Machado_matrix(
    sensitivities, spds, alpha_L=0.0, alpha_M=0.0, lambda_S=0, magic_number=0.94
):
    T_normal = get_T(sensitivities, spds)

    area_ratio = np.sum(sensitivities.values[:, 0]) / np.sum(
        sensitivities.values[:, 1]
    )

    adjusted_values = np.zeros_like(sensitivities.values)
    adjusted_values[:, 0] = (1 - alpha_L) * sensitivities.values[
        :, 0
    ] + alpha_L * sensitivities.values[:, 1] * magic_number * area_ratio
    adjusted_values[:, 1] = (1 - alpha_M) * sensitivities.values[
        :, 1
    ] + alpha_M * sensitivities.values[:, 0] / magic_number / area_ratio
    adjusted_values[:, 2] = np.roll(sensitivities.values[:, 2], lambda_S)

    sensitivities_adjusted = colour.MultiSpectralDistributions(
        data={
            wl: adjusted_values[i]
            for i, wl in enumerate(sensitivities.wavelengths)
        },
        labels=["L", "M", "S"],  # Names for each spectrum
        name="Adjusted cone sensitivities",
    )

    T = get_T(sensitivities_adjusted, spds)
    T_normal_inv = np.linalg.inv(T_normal)
    M = T_normal_inv @ T

    return M
