import covid19pandas as cod
import matplotlib.pyplot as plt
ler = cod.get_deaths()
plt.pie(ler['3/30/20'],labels=ler['Country/Region'], autopct="%1.0f%%")
plt.show()


