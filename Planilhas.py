import openpyxl

files = [r'C:\Users\roman\Documents\Testes excel_python/january.xlsx']
values = []

for file in files:
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']
    value = sheet['B5'].value
    values.append(value)
    print(values)