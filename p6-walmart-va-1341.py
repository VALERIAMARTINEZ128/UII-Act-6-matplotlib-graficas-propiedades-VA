import matplotlib.pyplot as plt 

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]
num_control = "1341"

# --- 1. PRIMERA GRÁFICA (Básica) ---
plt.figure()
plt.plot(cant_productos, precio)
plt.title(f"Gráfica Básica - No. Control: {num_control}")
# Texto sobre la gráfica
plt.text(120, 16000, f"No. Control: {num_control}", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
plt.show()

# --- 2. SEGUNDA GRÁFICA (Personalizada como la imagen) ---
plt.figure()
plt.plot(
    cant_productos, 
    precio, 
    color='green', 
    marker='o', 
    linestyle='dashed', 
    linewidth=2, 
    markersize=12
)
plt.title(f"Gráfica Personalizada - No. Control: {num_control}")
# Texto resaltado sobre la gráfica
plt.text(120, 16000, f"No. Control: {num_control}", fontsize=11, fontweight='bold', bbox=dict(facecolor='yellow', alpha=0.6))
plt.show()