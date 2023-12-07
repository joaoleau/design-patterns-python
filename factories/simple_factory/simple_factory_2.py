"""
O termo factory refere-se a uma classe ou método que é responsavel por criar objetos.

Vantagens:
    
Desvantagens:

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
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_veiculo(tipo)
    
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

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == "__main__":
    from random import choice
    
    carros_disponiveis = ['luxo', 'popular', 'moto']
    
    for i in range(3):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()