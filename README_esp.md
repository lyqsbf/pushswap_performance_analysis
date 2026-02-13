# Push_swap Performance Analysis

Este repositorio contiene un conjunto de scripts en Python diseñados para probar, analizar y medir el rendimiento del proyecto **push_swap** de 42.

Los scripts automatizan la generación de números aleatorios, la ejecución de tu programa y la validación con el `checker`, proporcionando estadísticas detalladas sobre la cantidad de movimientos.

## 📋 Requisitos

Asegúrate de tener los siguientes archivos en el mismo directorio donde ejecutes los scripts:

1. **`push_swap`**: Tu ejecutable compilado.
2. **`checker_linux`**: El binario del checker proporcionado por 42 (asegúrate de que tenga permisos de ejecución: `chmod +x checker_linux`).
3. **Python 3**: Para ejecutar los scripts.

> **Tip 💡:** Todos los scripts incluyen shebangs (`#!/usr/bin/env python3`). Si les das permisos de ejecución con `chmod +x *.py`, podrás ejecutarlos directamente (ej: `./performance_analysis.py`) sin escribir `python3`.

> **Nota:** Los scripts están configurados para usar `./checker_linux`. Si deseas usar el checker de MacOS, deberás modificar la línea correspondiente en los archivos `.py`.

---

## 🛠️ Scripts Disponibles

### 1. 📊 `performance_analysis.py` (Recomendado)
Este es el script principal para obtener métricas de rendimiento detalladas. Calcula el mínimo, máximo, promedio y desviación estándar de los movimientos.

**Uso por defecto (ejecuta 100 tests de 100 números y 100 tests de 500 números):**
```bash
python3 performance_analysis.py
```

**Uso personalizado:**
Puedes especificar la cantidad de números y el número de iteraciones:
```bash
# Sintaxis: python3 performance_analysis.py [CANTIDAD_NUMEROS] [ITERACIONES]

# Ejemplo: Analizar 100 números con 500 pruebas
python3 performance_analysis.py 100 500
```
*Si el programa detecta fallos (KO), guardará los casos fallidos en `ko_cases.txt`.*

### 2. 📈 `visual_analysis.py` (Visual y Gráficos)
Ejecuta multiples pruebas incrementando el tamaño del stack y genera una gráfica (`performance_graph.png`) para comprobar visualmente la complejidad de tu algoritmo.
- **Requisitos**: Necesita `matplotlib` (`pip install matplotlib`).
- **Funcionamiento**: Al ejecutarlo crea un gráfico con las medias, mínimos y máximos.

```bash
# Por defecto (de 10 a 500 elementos, paso de 50)
python3 visual_analysis.py

# Personalizado (ej: rango específico y más muestras)
python3 visual_analysis.py --min 5 --max 500 --step 50 --samples 20
```

### 3. 🧪 `fuzz_test.py`
Realiza una comprobación básica y rápida.
- Ejecuta 20 iteraciones globales.
- En cada iteración prueba: 100 números, 500 números y un tamaño aleatorio (6-100).
- Se detiene inmediatamente si encuentra un error.

```bash
python3 fuzz_test.py
```

### 3. 🌀 `fuzz_test_v2.py`
Se enfoca en pruebas intensivas de **casos pequeños** y aleatorios.
- Tests intensivos: Tamaños de 6 a 20 (50 pruebas por cada tamaño).
- Tests aleatorios: 100 pruebas con tamaños variados (6-100).

```bash
python3 fuzz_test_v2.py
```

### 4. 📉 `fuzz_test_v3.py`
Prueba **casos especiales** y extremos.
- Listas ordenadas inversamente (tamaños 6 a 100).
- Listas "casi ordenadas" (solo 2 elementos intercambiados).

```bash
python3 fuzz_test_v3.py
```

---

## 🚀 Cómo empezar

1. Compila tu proyecto `push_swap`:
   ```bash
   make
   ```
2. Asegúrate de tener el `checker_linux` en la raiz.
3. Ejecuta el análisis de rendimiento:
   ```bash
   python3 performance_analysis.py
   ```

## 📈 Métricas Explicadas

El script de análisis te dará una salida como esta:
- **Min Moves**: La mejor ejecución (menos movimientos).
- **Max Moves**: La peor ejecución. Importante para saber si pasas los límites de evaluación.
- **Mean (Avg)**: El promedio de movimientos.
- **Std Dev**: Desviación estándar (qué tanto varían tus resultados; idealmente debe ser baja).
- **Runs > Limit**: Porcentaje de pruebas que superan el límite aceptable (700 para 100 números, 5500 para 500).

---

¡Buena suerte con tu evaluación! 🐬
