class P_sat:
    def __init__(self, nome):
        self.nome = nome
        print("Calculo da Psat do Composto {} pela equação de Antoine:".format(nome))
        self.t = float(input('Informe a Temperatura '))
        self.a = float(input('Informe o parâmetro A '))
        self.b = float(input('Informe o parâmetro B '))
        self.c = float(input('Informe o parâmetro C '))
        self.Psaturation = 10 ** (self.a - (self.b / (self.t + self.c)))
        print("A pressão de saturação de {} é {:.2f}".format(self.nome, self.Psaturation))
        print("")
