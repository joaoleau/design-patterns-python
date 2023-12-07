"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
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

class VeiculoFactory(ABC):
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_veiculo(tipo)

    @staticmethod
    @abstractmethod
    def get_veiculo(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo não existe'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'

if __name__ == "__main__":
    from random import choice
    
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto']
    veiculos_disponiveis_zona_norte = ['popular']
    
    print("ZonaNorteVeiculoFactory")
    for i in range(3):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()
    
    print()

    print("ZonaSulVeiculoFactory")
    for i in range(3):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro2.buscar_cliente()