pessoa = []
soma_idade = 0
h_velho = 0
soma_mulher = 0

for i in range(0,4,1):
    print("Insira o nome, idade e sexo[M/F] da {}° pessoa: ".format(i+1))
    linha = []
    for j in range(0,3,1):
        linha.append(input()) 
    pessoa.append(linha)

for i in range(0,4,1):
    soma_idade = soma_idade + int(pessoa[i][1])
    if (str(pessoa[i][2]) == 'M'):
        if (h_velho < int(pessoa[i][1])):
            h_velho =  int(pessoa[i][1])
            nome_velho = str(pessoa[i][0])
    if ( str(pessoa[i][2])== 'F'):
        if (int(pessoa[i][1]) < 20):
            soma_mulher = soma_mulher + 1


print("A media das idade é {}".format(soma_idade/4))
print("O nome do homem mais velho é {}".format(nome_velho))
print("Tem {} mulheres com menos de 20 anos".format(soma_mulher))