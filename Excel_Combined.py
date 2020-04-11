import pandas as pd
import matplotlib.pyplot as plt
files = [r'C:\Users\roman\Documents\Testes excel_python/january.xlsx',
         r'C:\Users\roman\Documents\Testes excel_python/february.xlsx',
         r'C:\Users\roman\Documents\Testes excel_python/march.xlsx']
combined = pd.DataFrame()

for file in files:
  df = pd.read_excel(file, skiprows = 3)
  combined = combined.append(df, ignore_index = True)

combined.to_excel('combined.xlsx')
ler = pd.read_excel(r'C:\Users\roman\PycharmProjects\I.A\combined.xlsx')
print(ler)
plt.pie(ler['Oranges'],labels=ler['Location'],autopct="%1.0f%%")
plt.show()

#Outra opção para abrir o arquivo combinado:
#import os
#os.startfile(r"diretório")

'''print("FICHA DE FREQUÊNCIA:")
mes = input('Informe o mês: ')
ano = input('Informe o ano: ')
semana = {
    'SEG':['7:30', '12:50'],
    'SEG2':['15:50', '18:20'],
    'TER':['9:10', '13:50'],
    'TER2':['16:40', '18:20'],
    'QUA':['9:10', "11:10"],
    'QUI':['11:10', '12:50']}'''