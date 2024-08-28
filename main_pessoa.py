from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

def main():
    # Instanciando a classe Pessoa
    pessoa = Pessoa("João", "123456", "2024-08-27", False)
    print('Instancia da classe Pessoa: ')
    print(pessoa.imprimir_dados())

    # Instanciando a classe PessoaFisica
    pessoa_fisica = PessoaFisica("Ana", "654321", "2023-01-01", True, "1990-01-01", "000.111.222-33", "123456789")
    print('\nInstancia da classe PessoaFisica: ')
    print(pessoa_fisica.imprimir_dados())

    # Instanciando a classe PessoaJuridica
    pessoa_juridica = PessoaJuridica("Empresa X", "789012", "2022-01-01", True, "2020-01-01", "12.345.678/0001-95")
    print('\nInstancia da classe PessoaJuridica: ')
    print(pessoa_juridica.imprimir_dados())

    # Testando setters e validações
    try:
        pessoa_fisica.cpf = "123.456.789-0"  # CPF incorreto
    except ValueError as e:
        print(e)

    try:
        pessoa_juridica.cnpj = "12.345.678/0001-9"  # CNPJ incorreto
    except ValueError as e:
        print(e)

    # Ajustando os valores válidos
    pessoa_fisica.cpf = "123.456.789-00"
    pessoa_juridica.cnpj = "12.345.678/0001-95"

    # Imprimindo novamente após as alterações
    print('\nApós alterações:')
    print(pessoa_fisica.imprimir_dados())
    print(pessoa_juridica.imprimir_dados())

if __name__ == "__main__":
    main()
