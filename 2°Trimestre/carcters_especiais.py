import re
import time
import os

class Registro:
    registros_cadastrados = []
       
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def __str__(self):
        return f'Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}'
        time.sleep(0.5)
    
    @staticmethod
    def fazer_registro():
        
        nome = input("Digite seu nome: ")
        if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", nome):
            print('\rNome Registrado com sucesso.\n\n')
            time.sleep(0.3)
            email = input("Digite seu e-mail: ")
            
            if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
                print("E-mail Registrado com sucesso!\n\n")
                telefone = input("Digite seu telefone no formato XX X XXXXXXXX: ")
                
                #if re.match(r"^\d{2} \d \d{4}-\d{4}$", telefone):
                if re.match(r"^\d{2} \d{9}$", telefone):
                    print("Telefone Registrado com sucesso!\n\n")
                    time.sleep(0.3)
                    registro = Registro(nome, email, telefone)
                    print(registro)
                    Registro.registros_cadastrados.append(registro)
                    print('Progesso Salvo Com SUCESSO !!!!\n')
                    print('Digite Qualquer tecla para Continuar...')
                    input()
                    os.system('cls')
                    exibir_menu()
                    #print("\nRegistro Completo:\n", registro)
                else:
                    print("Telefone inválido. Formato correto: XX X XXXX-XXXX\nTente novamente...")
                    time.sleep(0.3)
                    print('Digite Qualquer tecla para Continuar...')
                    input()
                    exibir_menu()
            else:
                print('Caracteres especiais não permitidos foram inseridos na hora de preencher o e-mail.\nPermitidos (@, ., +, %, -, _)\n\nTente novamente...')
                time.sleep(0.3)
                print('Digite Qualquer tecla para Continuar...')
                input()
                exibir_menu()
                
        else:
            print('Você inseriu caracteres especiais ou números na hora de preencher o nome, o que não é aceito.\n\nTente novamente...')
            time.sleep(0.3)
            print('Digite Qualquer tecla para Continuar...')
            input()
            exibir_menu()
            
    def imprimir_usuarios():
        for registro in Registro.registros_cadastrados:
            print(registro);
            time.sleep(0.5)
            print('-'*20)
            print('\n')
        
        print('Digite Qualquer tecla para Continuar...')
        input()
        os.system('cls')
        exibir_menu()

def logo():
    GREEN = '\033[92m'
    RESET = '\033[0m'

    print(GREEN + """
  _________.__            ___.               .___                             __   
 /   _____/|__| ____  ____\\_ |__             |   | _______  __ ____   _______/  |_ 
 \\_____  \\ |  |/ ___\\/  _ \\| __ \\    ______  |   |/    \\  \\/ // __ \\ /  ___/\\   __\\
 /        \\|  \\  \\__(  <_> ) \\_\\ \\  /_____/  |   |   |  \\   /\\  ___/ \\___ \\  |  |  
/_______  /|__|\\___  >____/|___  /           |___|___|  /\\_/  \\___  >____  > |__|  
        \\/         \\/          \\/                     \\/          \\/     \\/         
                                                                                            © China - Menu ™ \n\n""" + RESET)

def exibir_menu():
    logo()            
    print('Digite "1" para Fazer Cadastro. ')
    print('Digite "2" para ver usuarios Cadastrados.')
    print('Digite "0" para sair.\n\n')

    Input_User = input('Digite o numero de Acordo com a escolha do menu: ')
    print('\n\n')

    if Input_User == '1':
        Registro.fazer_registro()
    elif Input_User == '2':
        Registro.imprimir_usuarios()
    elif Input_User == '0':
        print("Encerrando programa.")
        time.sleep(1)
        print("Encerrando programa..")
        time.sleep(1)
        print("Encerrando programa...")
        print('Até logo')
        exit()
    else:
        print('\n\nERRO: Escolha Inválida. Somente números são aceitos...')
        print('\nDigite Qualquer tecla para Continuar... BURRO !!!')
        input()
        time.sleep(1)
        os.system('cls')
        exibir_menu()

exibir_menu()
