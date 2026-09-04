# Informe - Trabajo Práctico Integrador Unidad 3

## Parte 1: Tabla de Java-ismos

| # | Java-ismo | Dónde  | Inversión que lo explica |  Observable |
|---|---|---|---|---|
| 1 | **Getters preventivos sin lógica** | `Figura.getNombre`, `getColor` | **Compilador → Acuerdo** | Código más largo sin ningún beneficio real. |
| 2 | **Métodos Getter/Setter explícitos** | `Lado.getLongitud`, `setLongitud` | **Compilador → Acuerdo** | Se usa (`setLongitud(5)`) en vez de usar `=` directamente. |
| 3 | **Atributo de clase mutable (Fake Static)**| `Poligono.catalogo` | **Declaración → Runtime** | Todas las instancias de Polígonos comparten la misma lista en memoria. |
| 4 | **Argumentos por defecto mutables** | `Poligono.__init__` (lados=[], obs=[]) | **Declaración → Runtime** | Polígonos creados sin argumentos comparten la misma lista de lados. |
| 5 | **Omisión de `super().__init__()`** | `Poligono.__init__` | **Compilador → Acuerdo**  | Python no llama automáticamente al constructor,la variable `_construida` nunca se inicializa. |
| 6 | **Guardar el alias sin copia defensiva** | `Poligono.__init__`, `getLados` | **Compilador → Acuerdo** | Si cambias la lista desde afuera del objeto, cambia el estado interno del Polígono. |
| 7 | **Sobrecarga de constructores (`isinstance`)**| `Triangulo.__init__`, `Cuadrado.__init__` | **Herencia → Duck typing** | Lógica dificil para inicializar una clase. |
| 8 | **Type hint falso (Mentirle al IDE)** | `Poligono.area` | **Declaración → Runtime** | El IDE espera un `int`, pero en el método devuelve un `str`. |