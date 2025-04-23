##1. Provea una clase que dado un número entero cualquiera retorne el factorial del
##mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
##instancia de clase.
class FactorialSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialSingleton, cls).__new__(cls)
        return cls._instance

    def calcular(self, numero):
        if numero < 0:
            raise ValueError("El número debe ser no negativo")
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado


# Prueba
if __name__ == "__main__":
    factorial1 = FactorialSingleton()
    factorial2 = FactorialSingleton()

    print("¿Es la misma instancia?", factorial1 is factorial2)  # True
    print("Factorial de 5:", factorial1.calcular(5))  # 120