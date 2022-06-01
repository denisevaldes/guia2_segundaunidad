import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class text_view(Gtk.Dialog):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("mensaje")
        self.set_default_size(500, 500)
        # ventana de dialogo ya tiene una box definida por defecto
        box = self.get_content_area()
        # se crea un grid para luego añadirlo al box
        self.grid = Gtk.Grid()
        box.add(self.grid)

        #se crea scroll y luego se expande 
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)
        #se crea text view y se añade a scroll
        #scroll se añade a grid 
        self.text_view = Gtk.TextView()
        self.textbuffer = self.text_view.get_buffer()
        self.scroll.add(self.text_view)
        self.grid.attach(self.scroll,0,1,6,4)
        self.button1 = Gtk.Button(label="GUARDAR")
        self.button1.connect("clicked", self.boton_guardar)
        self.grid.attach(self.button1,0,5,3,1) #(left,top,widht,height)(izquierda,arriba,ancho,largo)
        self.boton_archivo = Gtk.Button(label = "ABRIR ARCHIVO")
        self.boton_archivo.connect("clicked", self.abrir_archivo)
        self.grid.attach(self.boton_archivo, 3,5,3,1)
        self.show_all()

    
    def mensaje_textview(self, contenido):
        self.textbuffer.set_text(contenido)
        self.texto = self.textbuffer.props.text #sacando el texto 

    def boton_guardar(self, btn = None):
        guardar_dialog = Gtk.FileChooserDialog(parent = self, action = Gtk.FileChooserAction.SAVE)

        self.set_title("guardar archivo") 
        self.set_default_size(200, 150)
        guardar_dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK,
        )
        response = guardar_dialog.run()
        if response == Gtk.ResponseType.OK:
            path  = guardar_dialog.get_current_folder()
            nombre_archivo_texto = guardar_dialog.get_current_name()
            nombre_archivo = f"{path}/{nombre_archivo_texto}.txt"
            with open(nombre_archivo, "w") as file:
                file.write(self.texto)
        elif response == Gtk.ResponseType.CANCEL:
            guardar_dialog.destroy()

        guardar_dialog.destroy()
    
    def abrir_archivo(self, btn = None):
        #abrir archivo
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            nuevo_archivo = dialog.get_filename()
            with open(nuevo_archivo, "r") as file:
                lineas = file.readlines()
                total = ""
                for x in lineas: 
                    total += x
            self.textbuffer.set_text(total)
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

class advertencia(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(transient_for=parent, flags=0)
        self.add_buttons(
        Gtk.STOCK_OK,
        Gtk.ResponseType.OK,
        )
        self.set_title("mensaje usuario")
        self.set_default_size(200, 150)
        self.label = Gtk.Label(label = "no se han ingresado datos")
        self.vbox.pack_start(self.label,True,True,0)
        self.show_all() 

    def mensaje(self, contenido):
        self.label.set_text(contenido)

class Message_dialog(Gtk.Dialog):
    
    def __init__(self, parent):
        super().__init__(transient_for=parent)

        self.set_title("mensaje")
        self.set_default_size(200, 150)
        self.label = Gtk.Label(label = "")
        self.label1= Gtk.Label(label = "")
        self.label_titulo2 = Gtk.Label(label = "")
        self.label_titulo = Gtk.Label(label = "")
        self.vbox.pack_start(self.label_titulo,True,True,0)
        self.vbox.pack_start(self.label,True,True,0)
        self.vbox.pack_start(self.label_titulo2, True, True, 0)
        self.vbox.pack_start(self.label1,True,True,0)
        self.show_all()

    def cambiar_label(self, contenido, contenido2):
        self.label_titulo.set_text("el precio total sin iva es: ")
        self.label.set_text(contenido)
        self.label_titulo2.set_text("el precio total con iva: ")
        self.label1.set_text(contenido2)


class Ventana_principal(Gtk.Window):
    def __init__(self):
        super().__init__()
        
        self.set_title("ventana")
        self.set_default_size(400, 200)
        
        #label y entrada para ingresar nombre de cliente
        self.label_nombre = Gtk.Label(label="Nombre cliente")
        self.entrada_nombre = Gtk.Entry()
        self.entrada_nombre.connect("activate", self.entrada_d_nombre)
        
        # label y entrada para ingresar el tema de cotización 
        self.label_asunto = Gtk.Label(label="Asunto cotización")
        self.entrada_asunto = Gtk.Entry()
        self.entrada_asunto.connect("activate", self.entrada_d_asunto)

        # label y entrada para ingresar el costo por unidad de producto
        self.label_unidad = Gtk.Label(label = "costo unitario")
        #self.entrada_unidad = Gtk.Entry()
        #self.entrada_unidad.connect("activate", self.precio_unidad)
        self.entrada_unidad = Gtk.SpinButton()
        ajuste = Gtk.Adjustment(upper = 3000000, step_increment = 1)
        self.entrada_unidad.set_adjustment(ajuste)
        self.entrada_unidad.connect("value-changed", self.precio_unidad)

        # label y boton spin para ingresar la cantidad de unidades a cotizar
        self.label_cantidad = Gtk.Label(label = "cantidad de unidades")
        self.boton_cantidad = Gtk.SpinButton()
        ajuste = Gtk.Adjustment(upper = 2000000, step_increment = 1)
        self.boton_cantidad.set_adjustment(ajuste)
        self.boton_cantidad.connect("value-changed", self.valor_boton_cantidad)

        # label y boton spin para ingresar el porcentaje de iva 
        self.label_iva = Gtk.Label(label = "iva %")
        self.boton_iva = Gtk.SpinButton()
        ajuste = Gtk.Adjustment(upper = 50, step_increment = 1)
        self.boton_iva.set_adjustment(ajuste)
        self.boton_iva.connect("value-changed", self.valor_boton_iva)
        #se crea box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        #se añade el box a la ventana
        self.add(box)
        #se añaden las cosas a box
        box.pack_start(self.label_nombre,True,True,0)
        box.pack_start(self.entrada_nombre, True, True, 0)
        box.pack_start(self.label_asunto, True, True, 0)
        box.pack_start(self.entrada_asunto,True,True,0)
        box.pack_start(self.label_unidad,True,True,0)
        box.pack_start(self.entrada_unidad,True,True,0)
        box.pack_start(self.label_cantidad,True,True,0)
        box.pack_start(self.boton_cantidad,True,True,0)
        box.pack_start(self.label_iva, True, True,0)
        box.pack_start(self.boton_iva,False,False,0)

        #se crean botones para aceptar, reset y mensaje 
        #se añaden a box 
        self.button1 = Gtk.Button(label="ACEPTAR")
        self.button1.connect("clicked", self.boton_aceptar)
        self.button2 = Gtk.Button(label = "RESET")
        self.button2.connect("clicked", self.resetear)
        self.button_mensaje = Gtk.Button(label = "Mensaje")
        self.button_mensaje.connect("clicked", self.mensaje)
        box.pack_start(self.button1,True,True,0)
        box.pack_start(self.button_mensaje, True, True, 0)
        box.pack_start(self.button2,True,True,0)

    def precio_unidad(self, entry = None):
        self.unidades = self.entrada_unidad.get_value_as_int()

    def valor_boton_cantidad(self, entry = None):
        self.cantidad = self.boton_cantidad.get_value_as_int()

    def valor_boton_iva(self, btn= None):
        self.iva = self.boton_iva.get_value_as_int()

    def entrada_d_nombre(self, entry= None):
        self.nombre = self.entrada_nombre.get_text()
    
    def entrada_d_asunto(self, entry = None):
        self.asunto = self.entrada_asunto.get_text()

    def calcular(self):

        self.costo_total = self.unidades * self.cantidad
        self.Sol_iva  = self.iva/100
        self.costo_uni_iva = (self.Sol_iva * self.unidades) + self.unidades
        self.iva_total = self.Sol_iva * self.costo_total
        self.costo_total_c_iva = self.iva_total + self.costo_total

    def mensaje(self, btn = None):
        #si se ingresaron respuestas se muestra un mensaje predeterminado
        # de lo contrario se avisa que no hay datos 
        self.entrada_nombre.activate()
        self.entrada_asunto.activate()
        try:
            self.calcular() 
            self.contenido = ("hola "+  str(self.nombre) + ", la cotizacion de " +
                        str(self.asunto) + " ha quedado \nen un total de " + 
                        str(self.costo_total_c_iva) + " pesos, quedando cada producto a " + 
                        str(self.costo_uni_iva) + " pesos") 
            ventana_mensaje = text_view()
            ventana_mensaje.mensaje_textview(self.contenido)
            
        except:
            ventana_mensaje = advertencia(self)
        
        ventana_mensaje.run()
        ventana_mensaje.destroy()    
    

    def boton_aceptar(self, btn=None):
        # se llama a una ventana de dialogo 
        self.entrada_nombre.activate()
        self.entrada_asunto.activate()
        try: 
            self.calcular()
            ventana_dia = Message_dialog(self)
            ventana_dia.cambiar_label(str(self.costo_total),str(self.costo_total_c_iva))
        except:
            ventana_dia = advertencia(self)

        ventana_dia.run()
        ventana_dia.destroy()

    # se crea ventana de dialogo, la cual solo tiene dos botones y sus respuestas
    def resetear(self, btn= None):
        ventana_adv = Gtk.Dialog(parent=self)
        ventana_adv.set_title("advertencia")
        ventana_adv.set_default_size(200,150) 
        ventana_adv.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK,
        )

        responde = ventana_adv.run()
        if responde == Gtk.ResponseType.OK:
            self.entrada_nombre.set_text("")
            self.entrada_asunto.set_text("")
            self.entrada_unidad.set_text("")
            self.boton_cantidad.set_value(0)
            self.boton_iva.set_value(0)
            ventana_adv.destroy()
        elif responde == Gtk.ResponseType.CANCEL:
            ventana_adv.destroy()


if __name__ == "__main__":

    ventana1 = Ventana_principal()
    ventana1.show_all()
    ventana1.connect("destroy", Gtk.main_quit)
    Gtk.main()