"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código
"""

from abc import ABC, abstractmethod 

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo esta buscando cliente')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro Popular esta buscando cliente')

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto esta buscando cliente')

class VeiculoFactory:
    #Metodo fabrica
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo não existe'

if __name__ == "__main__":
    from random import choice
    
    carros_disponiveis = ['luxo', 'popular', 'moto']
    
    for i in range(3):
        carro = VeiculoFactory.get_veiculo(choice(carros_disponiveis))
        carro.buscar_cliente()