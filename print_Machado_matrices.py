from scipy.linalg import null_space

from utility import *

np.set_printoptions(precision=6, suppress=True)

print("RGB conversion:")
print("Protanopia")
print("{")
for alpha_L_index in range(11):
    alpha_L = alpha_L_index / 10

    M = get_Machado_matrix(sensitivities, spds_rgb_lcd, alpha_L=alpha_L)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))

print("Deuteranopia")
print("{")
for alpha_M_index in range(11):
    alpha_M = alpha_M_index / 10

    M = get_Machado_matrix(sensitivities, spds_rgb_lcd, alpha_M=alpha_M)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))

print("Tritanopia")
print("{")
for lambda_S_index in range(11):
    lambda_S = lambda_S_index * 6

    M = get_Machado_matrix(sensitivities, spds_rgb_lcd, lambda_S=lambda_S)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))


print("\nCMY conversion:")

print("Protanopia")
print("{")
for alpha_L_index in range(11):
    alpha_L = alpha_L_index / 10

    M = get_Machado_matrix(sensitivities, spds_cmy_abebe, alpha_L=alpha_L)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))

print("Deuteranopia")
print("{")
for alpha_M_index in range(11):
    alpha_M = alpha_M_index / 10

    M = get_Machado_matrix(sensitivities, spds_cmy_abebe, alpha_M=alpha_M)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))


print("Tritanopia")
print("{")
for lambda_S_index in range(11):
    lambda_S = lambda_S_index * 6

    M = get_Machado_matrix(sensitivities, spds_cmy_abebe, lambda_S=lambda_S)

    print(
        f"        {{ {{ {M[0,0]:.6f}, {M[0,1]:.6f}, {M[0,2]:.6f} }},"
        f" {{ {M[1,0]:.6f}, {M[1,1]:.6f}, {M[1,2]:.6f} }},"
        f" {{ {M[2,0]:.6f}, {M[2,1]:.6f}, {M[2,2]:.6f} }} }},"
    )
print("}")
print("Near-null space")
print(null_space(M, rcond=1e-3))
