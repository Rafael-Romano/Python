from math import exp
class Van_Laar:
    def __init__(self):
        print('Calculo dos Gamas pelo modelo de Van Laar')
        self.A = float(input("Informe o parâmetro A "))
        self.B = float(input("Informe o parâmetro B "))
        self.R = float(input("Informe o parâmetro R "))
        self.Xa = float(input("Informe o parâmetro Xa "))
        self.T = float(input("Informe o parâmetro T "))
        self.Xb = (1 - self.Xa)
        self.ge = self.Xa * self.Xb * ((self.A * self.B) / ((self.A * self.Xa) + (self.B * self.Xb)))
        print("Gibbs em excesso é {}".format(self.ge))
        self.gama_A = exp(self.A * (((self.B * self.Xb) / ((self.A * self.Xa) + (self.B * self.Xb))) ** 2 ) / (self.R * self.T))
        self.gama_B = exp(self.B * (((self.A * self.Xa) / ((self.A * self.Xa) + (self.B * self.Xb))) ** 2 ) / (self.R * self.T))
        print("Gama de A é {:.4f}".format(self.gama_A))
        print("Gama de B é {:.4f}".format(self.gama_B))