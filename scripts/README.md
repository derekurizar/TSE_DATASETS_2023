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
