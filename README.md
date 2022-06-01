# guia2_segundaunidad

# Descripción del programa 
  Este programa realiza cotizaciones de productos dando como resultado el precio total con y sin iva, además de realizar un mensaje predeterminado, el cual   se puede modificar y guardar, para poder ir guardando las cotizaciones y mensajes realizados. 
 
# Descripción código 
  En este código se cuenta con cuatro clases
  
  1) Clase principal 

    - Se crea ventana principal, la cual contiene botones, label, y entradas en las cuales el usuario puede 
      ingresar el nombre del comprador,la descripción de la cotización, el costo unitario del producto, la
      cantidad de unidades y el porcentaje de iva aplicado.
      En los métodos creados se incluye la creación de una ventana de diálogo, la cual tiene como función resetear
      los botones y entradas para poder ingresar una nueva cotización. 
 
  2) Clase diálogo "advertencia"
 
    - ventana de diálogo compuesta por un label con un mensaje predeterminado en el cual se advierte 
      que falta ingresar datos

  3) Clase diálogo "mensaje"
  
    - Ventana de diálogo compuesta por 4 labels y una función encargada de darle
      nuevos valores a los labels, mostrando en pantalla el precio total con o sin
      iva del producto a cotizar 
      
  4) clase dialogo "text_view"

    - ventana de dialogo en la que se abre un textview, el cual tiene de forma predeterminada un texto
      creado con la finalidad de poder enviarse al comprador.
      Dentro de esta clase también se tienen dos ventanas de dialogo de tipo filechoooser, las cuales se
      activan al momento de apretar el boton "guardar" o "abrir archivo" y que tienen la funcionalidad de guardar el 
      archivo que se esta editando o mostrar un archivo nuevo en pantalla.

# Lenguajes utilizados 
  - python

# Construido con 
  - Gtk
 
# Autores 
 - Denise Valdés 
 - Sebastian Benavides 
