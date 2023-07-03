
# Scripts

Esta carpeta contiene scripts in python para poder hacer recuentos y otros utilitarios.

Compatibilidad: Python 3+

## compare_originales_procesadas.py

Ejecutar desde la carpeta raíz.  Emitirá una comparativa entre los archivos json de las `actas_originales` y `actas_procesadas` para saber cuántos votos se tienen por departamento y partido y cuál es la variación entre ambas.

Ejemplo:

```
Departamento 3:
  UNIDAD NACIONAL DE LA ESPERANZA: 2064 originales vs 1103 procesadas. Variación: -46.56%
  PARTIDO AZUL: 122 originales vs 50 procesadas. Variación: -59.02%
  VALOR UNIONISTA: 943 originales vs 409 procesadas. Variación: -56.63%
  CABAL: 1255 originales vs 463 procesadas. Variación: -63.11%
  TODOS: 291 originales vs 138 procesadas. Variación: -52.58%
  VAMOS POR UNA GUATEMALA DIFERENTE: 1493 originales vs 808 procesadas. Variación: -45.88%
Departamento 9:
  UNIDAD NACIONAL DE LA ESPERANZA: 1871 originales vs 715 procesadas. Variación: -61.79%
  PARTIDO AZUL: 244 originales vs 98 procesadas. Variación: -59.84%
  VALOR UNIONISTA: 1146 originales vs 442 procesadas. Variación: -61.43%
  CABAL: 1169 originales vs 416 procesadas. Variación: -64.41%
  TODOS: 391 originales vs 110 procesadas. Variación: -71.87%
...
```

# Script de extracción de datos de la spreedsheet de Google

Este script de Python permite extraer datos de una hoja de cálculo de Google y guardarlos en un archivo JSON. Específicamente, filtra los datos en función del campo "Verificación 1 (verificador)" y genera un archivo JSON con los números de mesa correctos e incorrectos, junto con el total de mesas contadas.

Se están obteniendo los datos de la siguiente spreadsheet: https://docs.google.com/spreadsheets/d//edit#gid=1617022974

## Instalación

1. Tener instalado Python, puedes descargarlo desde [python.org](https://www.python.org/downloads/) e instalarlo siguiendo las instrucciones para tu sistema operativo.

2. Instala la librería pandas ejecutando el siguiente comando en tu terminal:

   ```shell
   pip install pandas
   ```

2.1 O bien, puedes instalar el archivo "requirements.txt" con el siguiente comando 
   ```shell
   pip install -r requirements.txt
   ```

3. Descarga el script `dp.py` a tu directorio local.

## Uso


2. Ejecuta el script ejecutando el siguiente comando en tu terminal, desde el directorio donde se encuentra el archivo `dp.py`:

   ```shell
   python dp.py
   ```

4. El script leerá la hoja de cálculo, filtrará los datos y generará un archivo JSON llamado `numeros_mesa.json` en el mismo directorio.

## Resultado

El archivo JSON generado contendrá los siguientes datos:

```json
{
  "mesas_contadas": 5,
  "total_mesas_correctas": 100,
  "total_mesas_incorrectas": 20,
  "numeros_de_mesa_correctos": [11,233,444, ...],
  "numeros_de_mesa_incorrectos": [55, 66, 22, ...]
}
```

El array `"numeros_de_mesa_correctos"` contiene los números de mesa considerados como correctos según el campo "Verificación 1 (verificador)", mientras que el array `"numeros_de_mesa_incorrectos"` contiene los números de mesa considerados como incorrectos. El campo `"mesas_contadas"` indica el número total de mesas contadas (sumando las correctas e incorrectas).

