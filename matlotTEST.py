import matplotlib.pyplot as plt


plt.title('Matplotlib Python', color='green')

#plt.plot([1, 2, 3, 4],[1, 3, 4, 6],[1, 2, 3, 4],[2, 4, 6, 5])
plt.plot([1, 2, 3, 4],[1, 3, 4, 6], label='voiture1')
plt.plot([1, 2, 3, 4],[2, 4, 6, 5], label='voiture2')
plt.plot([1, 2, 3, 4],[2, 3.5, 4, 4.5], label='voiture3')

plt.ylabel("Vitesse", color='red', fontweight='bold')
plt.xlabel("Temps", color='red', fontweight='bold')
plt.grid(True)
plt.text(1.5, 3, r'Test')

plt.legend()
plt.show()