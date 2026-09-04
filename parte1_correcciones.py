"""parte1_diagnostico.py — El dominio Figura / Polígono / Lado, funcionando.

⚠️ Este módulo corre de punta a punta sin lanzar un solo traceback. No tiene bugs
de sintaxis: tiene ACENTO DE JAVA.

Contiene exactamente 8 java-ismos de DISEÑO. Siete están en el checklist de la
Actividad 4; el octavo no está en ese checklist y hay que encontrarlo con criterio,
no con la lista.

Además hay ruido sintáctico (punto y coma al final de línea, comparaciones contra
True, concatenación con + donde iría un f-string). Ese ruido también se limpia, pero
NO cuenta dentro de los 8.

Tu trabajo (Parte 1): encontrarlos, listarlos en informe.md y corregirlos, cada uno
justificado con la inversión conceptual que lo explica.
"""
import math

class Figura:
    def __init__(self, nombre: str, color: str):
        self._nombre = nombre
        self._color = color
        self._construida = True

    def area(self) -> float:
        return 0.0


class Lado:
    def __init__(self, longitud: float):
        self.longitud = longitud

    @property
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter
    def longitud(self, valor: float):
        if valor <= 0:
            raise ValueError("La longitud debe ser positiva")
        self._longitud = valor

class Poligono(Figura):
    #creamos la lista adentro
    def __init__(self, nombre: str, color: str, lados: list = None, observaciones: list = None):
        super().__init__(nombre, color)
        
        #si nos pasan una lista, la clonamos,si es None creamos una vacía
        self._lados = list(lados) if lados else []
        self._observaciones = list(observaciones) if observaciones else []

    def lados_esperados(self) -> int:
        return 0

    def perimetro(self) -> float:
        return sum(lado.longitud for lado in self._lados)

    def area(self) -> float:
        return 0.0

    def agregar_observacion(self, texto: str):
        self._observaciones.append(texto)

    def lados(self) -> list:
        return list(self._lados)
    
class Triangulo(Poligono):
    def __init__(self, nombre="triángulo", color="negro", lados: list = None):
        super().__init__(nombre, color, lados)

    def lados_esperados(self) -> int:
        return 3


class Cuadrado(Poligono):
    def __init__(self, nombre="cuadrado", color="negro", lados: list = None):
        super().__init__(nombre, color, lados)

    def lados_esperados(self) -> int:
        return 4


class PoligonoRegular(Poligono):
    """Polígono de N lados de igual longitud.

    ⚠️ PARTE 3 — esta clase NO es uno de los 8 java-ismos de la Parte 1.

    Se modeló heredando de Poligono para poder guardarla en la misma lista que
    los demás polígonos y recorrerla con un único tipo común. En Java esa
    herencia hacía falta; en Python no. Si su lugar en la jerarquía lo justifica
    el dominio («un polígono regular ES-UN polígono») o solamente la ceremonia
    del compilador es, exactamente, la decisión que se te pide tomar, justificar
    e IMPLEMENTAR en la Parte 3.
    """

    def __init__(self, nombre, color, medida, cantidad):
        super().__init__(nombre, color, [Lado(medida) for _ in range(cantidad)])
        self._cantidad = cantidad

    def lados_esperados(self):
        return self._cantidad


if __name__ == "__main__":
    activo = True
    if activo == True:                                      # ruido: == True
        t = Triangulo("Triángulo", "rojo", [Lado(3), Lado(4), Lado(5)]);   # ruido: ;
        c = Cuadrado("Cuadrado", "azul", [Lado(2), Lado(2), Lado(2), Lado(2)])
        print("Perímetro del triángulo: " + str(t.perimetro()))            # ruido: +
        print("Perímetro del cuadrado: " + str(c.perimetro()))
        t.agregar_observacion("revisar el vértice A")
        print("Figuras en el catálogo: " + str(len(Poligono.catalogo)))
        print("Nombre (via getter): " + t.getNombre())
        r = PoligonoRegular("Pentágono", "verde", 4, 5)
        print("Perímetro del pentágono: " + str(r.perimetro()))
