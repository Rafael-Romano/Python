from math import exp
class Margules:
    def __init__(self, n):
        if n == 1:
            print('Calculo dos Gamas por Margules {} parâmetro'.format(n))
            self.A = float(input("Informe o parâmetro A "))
            self.R = float(input("Informe o parâmetro R "))
            self.Xa = float(input("Informe o parâmetro Xa "))
            self.T = float(input("Informe o parâmetro T "))
            self.Xb = (1 - self.Xa)
            self.ge = (self.A * self.Xa * self.Xa)
            print("Gibbs em excesso é {}".format(self.ge))
            self.gama_A = exp((self.A * (self.Xb ** 2)) / (self.R * self.T))
            self.gama_B = exp((self.A * (self.Xa ** 2)) / (self.R * self.T))
            print("Gama de A é {:.4f}".format(self.gama_A))
            print("Gama de B é {:.4f}".format(self.gama_B))
            print("")
        if n == 2:
            print('Calculo dos Gamas por Margules {} parâmetros'.format(n))
            self.A = float(input("Informe o parâmetro A "))
            self.B = float(input("Informe o parâmetro B "))
            self.R = float(input("Informe o parâmetro R "))
            self.Xa = float(input("Informe o parâmetro Xa "))
            self.T = float(input("Informe o parâmetro T "))
            self.Xb = (1 - self.Xa)
            self.ge = self.Xa * self.Xb * (self.A + self.B *(self.Xa - self.Xb))
            print("Gibbs em excesso é {}".format(self.ge))
            self.gama_A = exp((((self.A + (self.B * 3)) * self.Xb ** 2) - (4 * self.B * self.Xb ** 3)) / (self.R * self.T))
            self.gama_B = exp((((self.A - (self.B * 3)) * self.Xa ** 2) - (4 * self.B * self.Xa ** 3)) / (self.R * self.T))
            print("Gama de A é {:.4f}".format(self.gama_A))
            print("Gama de B é {:.4f}".format(self.gama_B))
            print("")
