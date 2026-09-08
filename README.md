Ejemplo de Cobertura de Pruebas de Software con Python

Este proyecto es una demostración sencilla del concepto de cobertura de código utilizando Python, pytest y coverage.py.

El objetivo es ejecutar pruebas sobre una pequeña calculadora y posteriormente generar un reporte que permita identificar qué partes del código fueron ejecutadas por las pruebas.

Tecnologías utilizadas
Python 3
pytest
coverage.py
GitHub
Docker/Kasm para el entorno de ejecución
Estructura del proyecto
ejemplo-cobertura/
│
├── calculadora.py
├── test_calculadora.py
├── README.md
└── htmlcov/


La carpeta htmlcov se genera automáticamente al crear el reporte HTML.

1. Clonar el proyecto

Desde la terminal de la máquina Kasm:

git clone https://github.com/TU_USUARIO/ejemplo-cobertura.git
cd ejemplo-cobertura-python


Reemplaza TU_USUARIO por el usuario propietario del repositorio.

2. Verificar Python

Ejecutar:

python3 --version


También puede funcionar:

python --version


Se recomienda utilizar Python 3.

3. Instalar las herramientas

Instalar pytest y coverage:

pip install pytest coverage


Si el sistema no permite instalar paquetes directamente, utilizar:

pip install --user pytest coverage

4. Ejecutar las pruebas

Ejecutar:

pytest


El resultado esperado será similar a:

4 passed


Esto significa que las cuatro pruebas fueron ejecutadas correctamente.

5. Generar el reporte de cobertura

Ejecutar:

coverage run --branch -m pytest


Después:

coverage report -m


El resultado será similar a:

Name                   Stmts   Miss Branch BrPart  Cover
--------------------------------------------------------
calculadora.py            10      2      6      2    75%
--------------------------------------------------------
TOTAL                     10      2      6      2    75%


Los valores pueden variar dependiendo de las pruebas realizadas.

6. Generar el reporte HTML

Para obtener un reporte visual:

coverage html


Esto creará una carpeta:

htmlcov/


Dentro estará:

htmlcov/index.html


Para abrirlo desde Kasm se puede utilizar el navegador y abrir el archivo:

htmlcov/index.html


También se puede utilizar:

python3 -m http.server 8000


Después abrir en el navegador:

http://localhost:8000/htmlcov/

7. ¿Qué estamos midiendo?

La cobertura nos permite saber qué partes del código fueron ejecutadas mientras se ejecutaban las pruebas.

Por ejemplo:

def clasificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    return "cero"


Si solamente tenemos esta prueba:

def test_clasificar_positivo():
    assert clasificar_numero(10) == "positivo"


estamos probando únicamente el caso positivo.

Todavía necesitamos probar:

Número positivo → 10
Número negativo → -5
Cero             → 0


Por eso una cobertura menor al 100% nos puede indicar que existen partes del código que no están siendo ejecutadas durante nuestras pruebas.

8. Cobertura de ramas

En este ejemplo utilizamos:

coverage run --branch -m pytest


La opción --branch permite analizar también las diferentes ramas de las decisiones del programa.

Por ejemplo:

if numero > 0:
    ...
elif numero < 0:
    ...
else:
    ...


Existen diferentes caminos que las pruebas deberían recorrer.

9. Actividad para los estudiantes
Paso 1

Ejecutar las pruebas:

pytest

Paso 2

Generar el reporte:

coverage run --branch -m pytest
coverage report -m

Paso 3

Identificar qué líneas o ramas no tienen cobertura.

Paso 4

Agregar nuevas pruebas en:

test_calculadora.py


Por ejemplo:

def test_clasificar_negativo():
    assert clasificar_numero(-10) == "negativo"


def test_clasificar_cero():
    assert clasificar_numero(0) == "cero"

Paso 5

Volver a ejecutar:

coverage run --branch -m pytest
coverage report -m

Paso 6

Comparar el porcentaje anterior con el nuevo.

Paso 7

Generar nuevamente el reporte HTML:

coverage html

10. Pregunta para discusión

¿Tener 100% de cobertura significa que el software está libre de errores?

No necesariamente.

La cobertura indica qué código fue ejecutado por las pruebas, pero no garantiza que las pruebas sean suficientes o que todos los comportamientos posibles hayan sido validados.

Por ejemplo, una función puede tener 100% de cobertura de líneas, pero las pruebas podrían no considerar:

Valores negativos.
Cero.
Valores extremos.
Datos inválidos.
Errores esperados.
Casos límite.

Por lo tanto:

100% de cobertura no significa 100% de calidad.

La cobertura es una métrica que ayuda a identificar código que no está siendo probado.

11. Flujo completo

El flujo utilizado en esta práctica es:

Código
   ↓
Pruebas con pytest
   ↓
Ejecutar pruebas con coverage
   ↓
Medir líneas y ramas ejecutadas
   ↓
Generar reporte
   ↓
Identificar código sin cobertura
   ↓
Crear nuevas pruebas
   ↓
Volver a medir

Comandos principales
# Ejecutar pruebas
pytest

# Medir cobertura
coverage run --branch -m pytest

# Mostrar reporte en terminal
coverage report -m

# Generar reporte HTML
coverage html

Objetivo de la práctica

Al finalizar, el estudiante deberá ser capaz de:

Crear pruebas unitarias utilizando pytest.
Ejecutar pruebas automatizadas.
Medir cobertura de código.
Identificar líneas y ramas sin cobertura.
Crear pruebas adicionales para aumentar la cobertura.
Interpretar un reporte de cobertura.
Comprender las limitaciones de utilizar cobertura como métrica de calidad.
