import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image

A=np.random.randint(0, 101,size=(5,3))
print(f"Vector A\n{A}")
print(f"La suma del vector es {A.sum()}")
print(f"El promedio del vector es {A.mean()}")

print("\n------Vector de 10x10 aleatorio en rango 0-9---------------")
B=np.random.randint(0, 10,size=(10,10))
print(B)
print("\nValores mayores que 5 remplazados por -1")
B[B>5]=-1
print(B)
print("\nIMAGEN")
img = Image.open('TALLERNUMPY\Pikachu_de_Ash_en_Alola.png').convert('RGB')
img_array = np.array(img)
print(f"\nSHAPE {img_array.shape}")
print(f"\nMIN {img_array.min()}")
print(f"\nMAX {img_array.max()}")
print(f"\nPROM {img_array.mean()}")
plt.imshow(img_array)
plt.show()



