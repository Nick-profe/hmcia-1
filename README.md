# HMCIA

Repositorio de apoyo para la asignatura Herramientas Matematicas y
Computacionales para la IA. El proyecto contiene ejemplos practicos en Python
para trabajar conceptos matematicos usados en inteligencia artificial.

Actualmente el repositorio incluye un modulo de operaciones basicas con
matrices usando NumPy.

## Contenido actual

- Suma de matrices.
- Resta de matrices.
- Multiplicacion matricial.
- Transpuesta de una matriz.
- Lectura de matrices desde archivos CSV.
- Pruebas unitarias con Pytest.

## Estructura del proyecto

```text
.
├── data/
│   ├── matrix_A.csv
│   └── matrix_B.csv
├── src/
│   ├── __init__.py
│   └── matrix_operations.py
├── tests/
│   └── test_matrix_operations.py
├── main.py
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10 o superior.
- pip.

Las dependencias principales estan definidas en `requirements.txt`:

- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter
- Pytest

## Instalacion

Desde la raiz del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

Ejecuta el archivo principal para cargar las matrices de `data/` y mostrar los
resultados de las operaciones:

```bash
python main.py
```

El script lee:

- `data/matrix_A.csv`
- `data/matrix_B.csv`

y calcula:

- `A + B`
- `A - B`
- `A x B`
- `A^T`

## Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

## Modulo principal

Las funciones disponibles estan en `src/matrix_operations.py`:

```python
add_matrices(A, B)
subtract_matrices(A, B)
multiply_matrices(A, B)
transpose_matrix(A)
```

Estas funciones esperan matrices compatibles, normalmente creadas como arreglos
de NumPy.

## Proximos pasos sugeridos

- Agregar mas pruebas para resta, multiplicacion y transpuesta.
- Incorporar notebooks con ejemplos guiados.
- Crear nuevos modulos para calculo, estadistica y probabilidad.
- Agregar validaciones para dimensiones incompatibles entre matrices.
