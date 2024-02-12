# Entrada de datos  por el usuario en Kilopascales
presion_kpa = float(input("Ingresa la presion en kilopascales: "))

# Detallando los factores de conversion correspondientes
kpa_a_psi = 0.14503773773375  # libras por pulgada cuadrada
kpa_a_mmhg = 7.50062  # milimetros de mercurio
kpa_a_atm = 0.00986923267  # atmosferas

# Calcuando la presion kpa a otras unidades
presion_kpa_psi = presion_kpa*kpa_a_psi  # kpa a psi
presion_mmhg = presion_kpa*kpa_a_mmhg  # kpa a mmhg
presion_atm = presion_kpa*kpa_a_atm  # kpa a atm

# Mostrando los resultados
print(f"\nLa presión de {presion_kpa} en kpa, a equivalencia:")
print(f"En libras por pulgada cuadrada (psi): {presion_kpa_psi:.4f} psi")
print(f"En milimetros de mercurio (mmHg): {presion_mmhg:.4f} mmHg")
print(f"En atmosferas (atm): {presion_atm:.4f} atm")
