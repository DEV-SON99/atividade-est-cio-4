from Calculadora import Calculadora

def main():
    # Criação da instância da classe Calculadora
    calc = Calculadora(10, 5, '+')
    
    # Exibir o resultado da operação
    calc.mostrarResultado()

if __name__ == "__main__":
    main()
