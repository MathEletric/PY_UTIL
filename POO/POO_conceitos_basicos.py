# EVOLUÇÃO DOS PARADIGMAS
# -> Linguagem de máquina;
# -> Linguagem de montagem;
# -> Linguagem de alto nível;
# -> Programação procedimental;
# -> Programação funcional;
# -> Programação orientada a objetos;

# Conceitos inicias de POO:
# Encapsulamento, onde um objeto é composto de dados (atributos) + código (funcionalidade);
# Objetos enviam mensagens entre si, priorizando a ideia de que um objeto nãoaltera os dados
# de outro objeto diretamente;
# O objeto é extraido de um modelo/forma denomidado classe.

# Definição da classe:
class CachorroVersaoUm:
    pass

# Instância da classe cachorro:
meu_cacharro_um = CachorroVersaoUm()

# Gerando atributos (dados) desse objeto:
meu_cacharro_um.nome = 'Rakan' # (Nome do meu cachorro de verdade rs)
print(meu_cacharro_um.nome) # Imprime no console o valor do atributo.

meu_cacharro_um.idade = 3
print(meu_cacharro_um.idade)

# As funcionalidade de uma classe também recebe o nome método. Métodos, como já
# dito, são as funcionalidades. As funcionalidades ou métodos são definidos por 
# funções desenvolvidas dentro da classe. Na classe versão dois, temos dois métodos.
# O método construtor, que é escrita em termos de uma variável reservada python
# __init__, e outra chamada de aniversário. Note que o método aniversário altera
# o atributo idade, que é o dado de um possível objeto instânciado. As instâncias
# são os objetos criados em função de uma classe. Classes são facilmente instânciadas
# quando o método construtor é criado.
class CachorroVersaoDois:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
    
    def aniversario(self):
        self.idade += 1

# A classe versão dois possui um método construtor, que possibilidade a instânciação
# meu_cachorro_dois:
meu_cacharro_dois = CachorroVersaoDois('Nina', 12)
print("idade antes do aniversário:", meu_cacharro_dois.idade)
meu_cacharro_dois.aniversario()
print(f"idade depois do aniversário: {meu_cacharro_dois.idade}")

# Podemos referenciar o mesmo objeto de uma classe por meio de variáveis diferentes:
class MinhaClasse:
    def __init__(self, who_i_am):
        self.who = who_i_am

essa_classe = MinhaClasse('Sou o objeto 1.')
print("Essa_classe:", essa_classe.who)
outra_classe = essa_classe
print("Outra_classe:", outra_classe.who)
outra_classe.who = 'Sou objeto 2.'
print(f"Outra_classe: {outra_classe.who}\n Essa_classe: {essa_classe.who}")

print("="*60)
# O parâmetro self é padrão no método construtor e está presente em todas as classes.
# Representa o próprio objeto instânciado; é um valor que o interpretador python
# passa para classe quando um objeto é instânciado; valor que representa aonde esse
# objeto está na memória.

# Podemos passar como parâmetro o objeto instanciado na classe 'teamplate'.
MinhaClasse(essa_classe)
