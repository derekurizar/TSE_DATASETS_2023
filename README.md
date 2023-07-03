# TSE_DATASETS_2023
¡Hola Voluntario! Queremos expresar nuestro más sincero agradecimiento por tu compromiso y entusiasmo al unirte a nuestro proyecto por una democracia transparente y tecnológica.

Nuestro objetivo es asegurar la transparencia y precisión en el conteo de votos de las elecciones generales de Guatemala. como voluntario, formarás parte de un equipo dedicado a procesar los resultados electorales.

Nos estamos comunicando através del grupo de telegram: https://t.co/XuiUvsLedI ¡No dudes en unirte!

## Proceso:
El proceso cuenta con 2 fases, una de análisis y otra de verificación.

### Análisis

Hay 2 carpetas: actas_procesadas y actas_malas.
La carpeta que nos interesa es "actas_malas", esta carpeta se encuentra en el siguiente enlace [enlace](https://drive.google.com/drive/folders/1W2-Hrdddcv8vuL9oznThOgQzWAjdr-5c?usp=drive_link) y debes descargarla.

Una vez tienes descargada la carpeta "actas_malas" selecciona una acta según la tabla de abajo y revisan el acta con su data digitada, tienes dos formas de hacerlo:
1) Revisar el Acta
2) Comparar con lo que salga en el trep. https://www.trep.gt/#!/tc1/ENT digitado o bien comparar con el archivo JSON.
3) Si la información es congruente y correcta debes buscar y completar los datos en la siguiente google sheet: https://docs.google.com/spreadsheets/d/1ZxZNTH3659u_GpTNM4AiyZviqq2NvHCh2MZdMfYY6aw/edit#gid=1617022974 Debes dejar en blanco los campos de verificación, ya que, estos serán los que utilizarán quienes estén haciendo el trabajo de verificadores.

4) Luego de completar los datos en la sheet, alguien del resto del grupo revisará esa misma acta y verificará que los que los datos son congruentes, dicha acta se incluirá al listado de actas procesadas, si en cambio, los datos no son correctos, marcará como incorrecta dentro de la misma sheet.

5) Como último paso, el administrador hara una doble revisión para dar el visto bueno y completar con dicha acta.


### Verificación

El proceso lo estamos llevando a cabo mediante trabajo colaborativo en la siguiente google sheet: https://docs.google.com/spreadsheets/d/1ZxZNTH3659u_GpTNM4AiyZviqq2NvHCh2MZdMfYY6aw/edit#gid=1617022974 En este archivo debes verificar que actas están correctas y cuales no, el trabajo es bastante intuitivo, dentro de la hoja hay un selector donde colocarás su estado de incorrecta o correcta y luego un verificador corrobora lo que pusiste.

Puedas ser verificador de las actas de los demás, pero no de las tuyas.
dentro del campo de "Verificación 1" debes seleccionar si los datos del acta son congruentes.
El campo "Verificación 2" es para la doble verificación por parte del administrador, esto para que cada acta cuente con una doble verificación.

Para proporcionar una descripción adecuada de los nuevos archivos agregados en el repositorio en tu pull request, puedes incluir lo siguiente en el archivo README:

## Integridad

En este repositorio, hemos agregado una carpeta llamada `integrity` que contiene archivos relacionados con la integridad de las actas. Aquí se encuentra una breve descripción de cada archivo:

- `integrity.json`: Este archivo es un objeto JSON que mapea el número de acta con el enlace de integridad correspondiente. Puedes utilizar este archivo para obtener rápidamente los enlaces de integridad asociados con cada acta.

- `integrity.txt`: Este archivo es un archivo de texto plano que incluye una lista de todas las actas, tanto aquellas que tienen el enlace de integridad como aquellas que no lo tienen. Es útil para tener una visión general de todas las actas en un solo lugar.

- `no_hash.txt`: Este archivo de texto plano contiene una lista de todas las actas que no tienen el enlace de integridad asociado. Puede ser útil para identificar rápidamente las actas que aún necesitan asignarles un enlace de integridad.

Estos archivos han sido agregados para mejorar la transparencia y garantizar la integridad de las actas en este repositorio. Si tienes alguna pregunta o sugerencia relacionada con estos archivos, no dudes en comunicarte con nosotros.

La motivación de agregar esto es para tener un backup si el TSE decide no mostrar más esta URL para cada acta.

### Disclaimer
El siguiente contenido y los resultados de este proyecto tienen fines informativos y no constituyen ninguna información oficial o legal. Este proyecto hace uso de datos abiertos al público, los cuales se obtienen de conformidad con el Decreto número 57-2008 del Congreso de la República de Guatemala, promulgado el 23 de septiembre de 2008, conocido como Ley de Acceso a la Información Pública.

La Ley de Acceso a la Información Pública tiene como objetivo garantizar a toda persona interesada, sin discriminación alguna, el derecho a solicitar y tener acceso a la información pública en posesión de las autoridades y sujetos obligados por esta ley.

Sin embargo, es importante tener en cuenta que la información obtenida de fuentes de datos abiertos está sujeta a posibles actualizaciones, modificaciones o errores. No asumimos ninguna responsabilidad por la exactitud, integridad o actualidad de los datos utilizados en este proyecto.
