"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""
from abc import ABC, abstractmethod 

class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo ZN esta buscando cliente')

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro Popular ZN esta buscando cliente')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto Popular ZN esta buscando cliente')

class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto Luxo ZN esta buscando cliente')

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo ZS esta buscando cliente')

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro Popular ZS esta buscando cliente')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto Popular ZS esta buscando cliente')

class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto Luxo ZS esta buscando cliente')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: return CarroPopularZN()
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: return CarroLuxoZN()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular: return MotoPopularZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: return MotoLuxoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: return CarroPopularZS()
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: return CarroLuxoZS()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular: return MotoPopularZS()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: return MotoLuxoZS()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_popular()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_popular()
            moto_luxo.buscar_cliente()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.busca_clientes()