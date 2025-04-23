# TP3 - Patrones de Creación

Este trabajo práctico implementa diferentes patrones de creación en Python, abordando cada uno de los puntos propuestos.

---

## Punto 1: Singleton - Cálculo de factorial
**Archivo:** `singleton_factorial.py`  
Se implementa una clase `FactorialSingleton` que asegura que todas las instancias usen el mismo objeto. Método `calcular(n)` para obtener el factorial de un número entero.

---

## Punto 2: Singleton - Cálculo de impuestos
**Archivo:** `calculadoraImpuestos.py`  
Clase `CalculadoraImpuestos`, también con patrón Singleton, que calcula el total de un importe base sumando:
- IVA (21%)
- IIBB (5%)
- Contribuciones municipales (1.2%)

---

## Punto 3: Factory - Hamburguesa
**Archivo:** `Hamburguesa.py`  
Clase `Hamburguesa` que permite crear hamburguesas con diferentes métodos de entrega:
- Mostrador
- Retiro en tienda
- Delivery

---

## Punto 4: Factory - Factura con condición impositiva
**Archivo:** `factura.py`  
Clase `Factura` que incluye el importe total y la condición impositiva del cliente:
- IVA Responsable
- IVA No Inscripto
- IVA Exento

---

## Punto 5: Builder - Avión
**Archivo:** `taller_avion.py`  
Se implementa un patrón Builder para construir objetos de tipo `Avion` con:
- Cuerpo
- 2 Turbinas
- 2 Alas
- Tren de aterrizaje

---

## Punto 6: Prototype - Clonado de documentos
**Archivo:** `taller_prototipo.py`  
Clase `Documento` que hereda de `Prototipo` e implementa clonado profundo para duplicar objetos fácilmente.

---

## Punto 7: Abstract Factory (teórico)
**Archivo:** `avion_factory_ejemplo.py`  
Ejemplo teórico de una posible aplicación del patrón Abstract Factory.
