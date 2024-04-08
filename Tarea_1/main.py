from MFC import MFC
import time
import matplotlib.pyplot as plt

#TESTING
inicio = time.time()
mfc = MFC("./data/1-2024.txt")
mfc.run()
fin = time.time()
tiempo_transcurrido = fin - inicio
print("Tiempo de ejecucion:", tiempo_transcurrido/60, "minutos")

#print(mfc.Max_Fo_time)
#print(mfc.Time)

plt.plot(mfc.Time, mfc.Max_Fo_time)
plt.xlabel('Tiempo de Ejecución')
plt.ylabel('Valor de MaxFo')
plt.title('Valor de MaxFo en función del Tiempo de Ejecución')
plt.grid(True)
plt.show()
