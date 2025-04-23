class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total_con_impuestos(self, base):
        iva = base * 0.21
        iibb = base * 0.05
        contribuciones = base * 0.012
        total = base + iva + iibb + contribuciones
        return round(total, 2)
    
if __name__ == "__main__":
    

    impuestos = CalculadoraImpuestos()
    base = 1000
    print(f"Total con impuestos sobre {base}:", impuestos.calcular_total_con_impuestos(base))