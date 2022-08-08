# Entornos de programación

Un código de Python es en última instancia un archivo de texto donde cada línea se lee como una instrucción. Podríamos, si queremos, programar usando el bloc de notas. Sin embargo hay múltiples programas que hacen la experiencia de programar mucho más amigable, ya sea porque entienden la sintaxis y resaltan colores, porque incluyen opciones de autocompletar, de visualizar los archivos que involucran el proyecto entero, porque permiten ver resultados de la ejecución o porque permiten ejecutar paso a paso e ir viendo los valores de las variables. A estos programas se los llama IDE (Integrated Development Environment) y hay muchos. Uno de los entornos de programación más comunes es el Visual Studio Code (VSC), otro muy cómodo y que es el que vamos a usar en el curso es Jupyter notebooks. 

Notar que la palabra entorno o Enviroment acá (y en programación en general) se puede utilizar para ideas vinculadas pero diferentes. Una cosa es el entorno en tanto conjunto de librerías que usa y entre las cuales se ejecuta el código (lo que vimos en el tutorial de Conda) y otra cosa es entorno de programación en tanto herramientas y software que nos ayudan a visualizar y escribir el código. A lo largo de todo el resto de este tutorial por entorno nos vamos a referir a los entornos de Conda.

![Consola Dir](./Imagenes/Jupyter_1.png)

<!-- Pero además de haber programas externos que agregan capas de funcionalidades Python tiene una herramienta que cumple algunas de esta función de manera integrada, se llama ipython. ipython permite desde la misma consola o editor de texto poner etiquetas que agreguen funcionalidad, y permite desde la consola de Python hacer acciones como repetir comandos viejos, etc. En los hechos es común que no utilicemos solo ipython sino que ipython sea una capa más de las funcionalidades integrando hacia abajo al propio Python y hacia arriba el IDE en el que trabajemos. -->

## Las notebooks

Una de las funcionalidades más útiles que vamos a ver es la de poder programar en notebooks. Esto no hace referencia a programar en un una máquina portátil tipo laptop, sino a la idea de un bloc de notas de un laboratorio, donde uno va realizando pruebas y guarda registro de cada una de las cosas que fue haciendo para poder compartirla con los demás o para poder reconstruir en proceso y poder comparar diferentes casos. 

![Consola Dir](./Imagenes/notebook.png)

Programar con notebooks tiene la gran ventaja de que permite ejecutar el código de a bloques e ir probando que pasa luego de ejecutar cada parte. Si queremos modificar algo (ya sea porque corregimos la idea o porque agregamos algo extra) no hay que volver a ejecutar todo el código sino lo que acabamos de modificar y el resto "queda ejecutado". Para completar esta idea de cuaderno de notas, las notebooks de Python permiten destinar celdas enteras a notas complementarias que vayan explicando cuál es el proceso por el que pasamos al construir nuestro código. 

La contrapartida de usar las notebooks de Python es que puede inducir a errores comunes. El primero es que al no reejecutar todo el código desde el principio cada vez que probamos algo, podemos estar pisando datos anteriores (o lo opuesto usando datos que quedaron cargados en memoria y no deberían estar). Obviamente esto se soluciona reejecutando todas las celdas de punta a punta y probando que este todo en orden. La segunda desventaja es que si bien para un trabajo tipo científico es cómodo tener segmentado y repetidos los códigos, desde un punto de vista de eficiencia y buenas prácticas de programación conviene tener todo el código ordenado de manera lógica en un mismo bloque consistente. Es la razón por lo que la herramienta no está tan difundida en proyectos más enfocados en desarrollo de software, pero para hacer ciencia de datos es una herramienta muy cómoda.

## Jupyter

Como vimos las notebooks de Python permite separar los códigos en pequeños bloques, pero sobre eso se puede agregar una funcionalidad más, que es montar el entorno de programación en un servidor web. Esto permite varias cosas interesantes. Primero, que los outputs o resultados que genera cada celda de código puedan visualizarse con todas las herramientas web, es decir, imágenes, formato de texto, botones interactivos, etc usando cualquier navegador. Segundo, que podamos ir construyendo una "página" donde se ve nuestro código intercalado con los resultados producto de su ejecución y quede un registro histórico de lo que hicimos en lugar de que se pierdan los resultados cuando terminamos de trabajar y haya que reejecutar todo cada vez que queremos ver un resultado. Tercero, que podamos compartir los códigos mediante la web haciendo público el servidor donde corremos el notebook (que de manera predeterminada es visible solo en un navegador local) o subirlo a sitios como Google Colab o GitHub que tienen su propio servidor de notebooks. 

El programa más difundido en Python para correr un servidor local que nos permita construir y leer estas notebooks se llama Jupyter que tiene una versión más sencilla que es Jupyter notebook y otra más completa que es Jupyter Lab. Nosotros en el curso vamos a usar Jupyter Lab. 

### Como ejecutar Jupyter Lab

Para poder ejecutar correctamente Jupyter lab hay dos cosas importantes a considerar, en que entorno (de Conda) queremos que se ejecute y en que carpeta queremos que se ejecute (Jupyter nos va a mostrar y va a tener acceso a todos los archivos que haya dentro de la carpeta donde lo ejecutamos). Para elegir estas dos cosas vamos a usar una consola. 

![Consola Dir](./Imagenes/Jupyter_Lab.gif)

Lo primero es movernos en la estructura de archivos hasta donde queramos trabajar. En el ejemplo de la imagen elegimos la carpeta "Setup" dentro de la capeta donde descargamos todo el material disponible del curso. Con eso indicamos a Jupyter que carpeta de trabajo vamos a usar. 

Lo segundo es seleccionar el enviroment (o entorno) de python que queremos usar para nuestro proyecto. Si no recuerdan que es esto pueden revisar la sección correspondiente a Conda del tutorial. De manera predeterminada Conda usa el entorno que se denomina 'Base' que es el compartido con todo el sistema operativo. Para cambiar de entorno tenemos que ejecutar 

```
conda activate dhdsblend2021
```

porque 'dhdsblend2021' es el nombre con el que configuramos en Conda el entorno que vamos a usar para nuestro curso.

Vamos a ver que una vez activado en entorno aparece delante del path en la consola (dhdsblend2021) indicando que cualquier cosa que ejecutemos se va a ejecutar en ese entorno.

A continuación sí estamos listos para correr Jupyter lab escribiendo 
```
jupyter lab
```

Vamos a ver que en la consola empiezan a aparecer output del Jupyter (donde podemos visualizar información de que está haciendo) pero lo más importante es que nos da un link (o directamente lo abre en el navegador predeterminado) para acceder al servidor a través del navegador que tengamos configurado en nuestra computadora.

Una vez que carga la página podemos ver a la izquierda el árbol de directorio de la carpeta donde vamos a trabajar (incluyendo los archivos) y a la derecha un espacio para visualizar los archivos que queramos abrir o para crear alguno nuevo. 

En caso de que hayamos ejecutado Jupyter en la carpeta Setup del material de curso, si hacemos doble clic en 'setup_tool.ipynb' (o en cualquier otro archivo ipynb que son los de notebooks de ipython) podemos visualizar su contenido y volver a ejecutar los códigos ya escritos que están diseñados para testear que tengamos todo bien instalado. 

A continuación y para terminar este tutorial les mostramos como se debería visualizar esa notebook si lograron instalar todo correctamente y ejecutan su contenido. 

![notebooksetup](./Imagenes/Notebooks.gif)
