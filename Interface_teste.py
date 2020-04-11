import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBlack1')
        # Layout DarkGreen3
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Yahoo', key='yahoo'), sg.Checkbox('Hotmail', key='hotmail')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Não', 'cartoes', key='naoaceitaCartao')],
            [sg.Text('Velocidade de processamento')],
            [sg.Slider(range=(0, 100), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30, 10))]
        ]
        # Janela
        self.janela = sg.Window('Dados usuário').layout(layout)

    def iniciar(self):
        while True:
            # extrair dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_Gmail = self.values['gmail']
            aceita_Yahoo = self.values['yahoo']
            aceita_Hotmail = self.values['hotmail']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoaceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            if aceita_Gmail == True:
                print(f'aceita_Gmail: {aceita_Gmail}')
            if aceita_Yahoo == True:
                print(f'aceita_Yahoo: {aceita_Yahoo}')
            if aceita_Hotmail == True:
                print(f'aceita_Hotmail: {aceita_Hotmail}')
            if aceita_cartao == True:
                print(f'aceita_Cartão: {aceita_cartao}')
            if aceita_cartao == False:
                print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade do script: {velocidade_script}')


tela = TelaPython()
tela.iniciar()
