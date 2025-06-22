import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Étape 1 : Définir une variable symbolique
x = sp.Symbol('x')

# Étape 2 : Définir la fonction symbolique
f_sym = sp.sin(x) * sp.exp(-x / 5)

# Étape 3 : Calculer la dérivée symbolique
f_prime_sym = sp.diff(f_sym, x)

# Étape 4 : Convertir les fonctions symboliques en fonctions utilisables avec numpy
f_lambdified = sp.lambdify(x, f_sym, modules=['numpy'])
f_prime_lambdified = sp.lambdify(x, f_prime_sym, modules=['numpy'])

# Étape 5 : Créer un espace de valeurs pour x
x_vals = np.linspace(0, 20, 400)

# Étape 6 : Calculer les valeurs des fonctions
y_vals = f_lambdified(x_vals)
y_prime_vals = f_prime_lambdified(x_vals)

# Étape 7 : Tracer les courbes
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) = sin(x) * exp(-x/5)", color='blue', linewidth=2)
plt.plot(x_vals, y_prime_vals, label="f'(x)", color='red', linestyle='--', linewidth=2)

# Étape 8 : Personnalisation du graphique
plt.title("Fonction et sa dérivée", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Étape 9 : Affichage
plt.show()
