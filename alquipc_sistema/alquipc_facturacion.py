import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from datetime import datetime

class AlquipcFacturacion:
    def __init__(self, root):
        self.root = root
        self.root.title("ALQUIPC - Sistema de Facturación")
        self.root.geometry("1400x1000")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.num_equipos = tk.IntVar(value=2)
        self.dias_iniciales = tk.IntVar(value=1)
        self.dias_adicionales = tk.IntVar(value=0)
        self.tipo_alquiler = tk.StringVar(value="dentro_ciudad")
        self.id_cliente = tk.StringVar()
        
        # Variables para datos del cliente
        self.nombre_cliente = tk.StringVar()
        self.correo_cliente = tk.StringVar()
        self.telefono_cliente = tk.StringVar()
        
        # Variable para controlar si el código está generado
        self.codigo_generado = False
        
        # Variable para controlar si ya se generó una factura con este ID
        self.factura_generada = False
        
        # Precio base por día
        self.precio_dia = 35000
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título principal
        titulo = tk.Label(self.root, text="ALQUIPC - Sistema de Facturación", 
                         font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=10)
        
        subtitulo = tk.Label(self.root, text="Alquiler de Computadores", 
                            font=("Arial", 12), bg='#f0f0f0', fg='#7f8c8d')
        subtitulo.pack(pady=5)
        
        # Frame principal con dos columnas
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Frame izquierdo - Formulario
        left_frame = tk.Frame(main_frame, bg='#f0f0f0', width=450)
        left_frame.pack(side='left', fill='both', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Frame derecho - Factura
        right_frame = tk.Frame(main_frame, bg='#f0f0f0')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        
        
        # === FRAME IZQUIERDO - FORMULARIO ===
        # ID Cliente
        id_frame = tk.Frame(left_frame, bg='#f0f0f0')
        id_frame.pack(fill='x', pady=5)
        
        # Frame superior para ID
        id_info_frame = tk.Frame(id_frame, bg='#f0f0f0')
        id_info_frame.pack(fill='x', pady=2)
        tk.Label(id_info_frame, text="ID Cliente:", font=("Arial", 10, "bold"), 
                bg='#f0f0f0').pack(side='left')
        self.label_id_cliente = tk.Label(id_info_frame, text="[Sin generar]", font=("Arial", 10), 
                bg='#f0f0f0', fg='#e74c3c')
        self.label_id_cliente.pack(side='left', padx=10)
        
        # Frame para botón de generar código
        btn_codigo_frame = tk.Frame(id_frame, bg='#f0f0f0')
        btn_codigo_frame.pack(fill='x', pady=5)
        
        self.btn_generar_codigo = tk.Button(btn_codigo_frame, text="Generar Código Cliente", 
                                           command=self.generar_codigo_cliente, bg='#e74c3c', 
                                           fg='white', font=("Arial", 10, "bold"), 
                                           padx=15, pady=5)
        self.btn_generar_codigo.pack(side='left')
        
        # Mensaje informativo
        info_frame = tk.Frame(left_frame, bg='#f0f0f0')
        info_frame.pack(fill='x', pady=10)
        tk.Label(info_frame, text="⚠️ IMPORTANTE: Debe generar un código de cliente primero", 
                font=("Arial", 9), bg='#f0f0f0', fg='#e67e22').pack(anchor='w')
        
        # Datos del Cliente
        cliente_frame = tk.LabelFrame(left_frame, text="Datos del Cliente", 
                                     font=("Arial", 10, "bold"), bg='#f0f0f0', 
                                     fg='#2c3e50', padx=10, pady=10)
        cliente_frame.pack(fill='x', pady=10)
        
        # Nombre del cliente
        nombre_frame = tk.Frame(cliente_frame, bg='#f0f0f0')
        nombre_frame.pack(fill='x', pady=5)
        tk.Label(nombre_frame, text="Nombre completo:", 
                font=("Arial", 9, "bold"), bg='#f0f0f0').pack(anchor='w')
        self.entry_nombre = tk.Entry(nombre_frame, textvariable=self.nombre_cliente, 
                                    font=("Arial", 9), width=35)
        self.entry_nombre.pack(anchor='w', pady=2)
        
        # Correo del cliente
        correo_frame = tk.Frame(cliente_frame, bg='#f0f0f0')
        correo_frame.pack(fill='x', pady=5)
        tk.Label(correo_frame, text="Correo electrónico:", 
                font=("Arial", 9, "bold"), bg='#f0f0f0').pack(anchor='w')
        self.entry_correo = tk.Entry(correo_frame, textvariable=self.correo_cliente, 
                                    font=("Arial", 9), width=35)
        self.entry_correo.pack(anchor='w', pady=2)
        
        # Teléfono del cliente
        telefono_frame = tk.Frame(cliente_frame, bg='#f0f0f0')
        telefono_frame.pack(fill='x', pady=5)
        tk.Label(telefono_frame, text="Teléfono:", 
                font=("Arial", 9, "bold"), bg='#f0f0f0').pack(anchor='w')
        self.entry_telefono = tk.Entry(telefono_frame, textvariable=self.telefono_cliente, 
                                      font=("Arial", 9), width=35)
        self.entry_telefono.pack(anchor='w', pady=2)
        
        # Número de equipos
        equipos_frame = tk.Frame(left_frame, bg='#f0f0f0')
        equipos_frame.pack(fill='x', pady=10)
        tk.Label(equipos_frame, text="Número de equipos (mín. 2):", 
                font=("Arial", 10, "bold"), bg='#f0f0f0').pack(anchor='w')
        equipos_spinbox = tk.Spinbox(equipos_frame, from_=2, to=50, 
                                   textvariable=self.num_equipos, width=10)
        equipos_spinbox.pack(anchor='w', pady=5)
        
        # Días iniciales
        dias_frame = tk.Frame(left_frame, bg='#f0f0f0')
        dias_frame.pack(fill='x', pady=10)
        tk.Label(dias_frame, text="Días iniciales de alquiler:", 
                font=("Arial", 10, "bold"), bg='#f0f0f0').pack(anchor='w')
        dias_spinbox = tk.Spinbox(dias_frame, from_=1, to=365, 
                                textvariable=self.dias_iniciales, width=10)
        dias_spinbox.pack(anchor='w', pady=5)
        
        # Días adicionales
        dias_adicionales_frame = tk.Frame(left_frame, bg='#f0f0f0')
        dias_adicionales_frame.pack(fill='x', pady=10)
        tk.Label(dias_adicionales_frame, text="Días adicionales (descuento 2% por día):", 
                font=("Arial", 10, "bold"), bg='#f0f0f0').pack(anchor='w')
        dias_adicionales_spinbox = tk.Spinbox(dias_adicionales_frame, from_=0, to=365, 
                                            textvariable=self.dias_adicionales, width=10)
        dias_adicionales_spinbox.pack(anchor='w', pady=5)
        
        # Tipo de alquiler
        tipo_frame = tk.Frame(left_frame, bg='#f0f0f0')
        tipo_frame.pack(fill='x', pady=10)
        tk.Label(tipo_frame, text="Tipo de alquiler:", 
                font=("Arial", 10, "bold"), bg='#f0f0f0').pack(anchor='w')
        
        opciones_frame = tk.Frame(tipo_frame, bg='#f0f0f0')
        opciones_frame.pack(anchor='w', pady=5)
        
        tk.Radiobutton(opciones_frame, text="Dentro de la ciudad", 
                      variable=self.tipo_alquiler, value="dentro_ciudad",
                      bg='#f0f0f0').pack(anchor='w')
        tk.Radiobutton(opciones_frame, text="Fuera de la ciudad (+5% servicio domicilio)", 
                      variable=self.tipo_alquiler, value="fuera_ciudad",
                      bg='#f0f0f0').pack(anchor='w')
        tk.Radiobutton(opciones_frame, text="Dentro del establecimiento (-5% descuento)", 
                      variable=self.tipo_alquiler, value="establecimiento",
                      bg='#f0f0f0').pack(anchor='w')
        









        
        # === FRAME DERECHO - FACTURA ===
        # Título y botones en la parte superior
        header_frame = tk.Frame(right_frame, bg='#f0f0f0')
        header_frame.pack(fill='x', pady=(0, 10))
        
        # Título de factura
        titulo_factura = tk.Label(header_frame, text="Factura:", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0')
        titulo_factura.pack(side='left')
        
        # Frame para botones en la parte superior derecha
        botones_header = tk.Frame(header_frame, bg='#f0f0f0')
        botones_header.pack(side='right')
        
        self.btn_calcular = tk.Button(botones_header, text="🚀 GENERAR", 
                                     command=self.generar_factura, bg='#3498db', 
                                     fg='white', font=("Arial", 11, "bold"), 
                                     padx=15, pady=8)
        self.btn_calcular.pack(side='right', padx=(5, 0))
        
        self.btn_limpiar = tk.Button(botones_header, text="🧹 LIMPIAR", 
                                    command=self.limpiar_formulario, bg='#95a5a6', 
                                    fg='white', font=("Arial", 11, "bold"), 
                                    padx=15, pady=8)
        self.btn_limpiar.pack(side='right', padx=(5, 0))
        
        # Área de texto para la factura
        
        self.texto_resultado = scrolledtext.ScrolledText(right_frame, height=25, 
                                                        width=80, font=("Courier", 9))
        self.texto_resultado.pack(fill='both', expand=True, pady=5)














        
        
        # Deshabilito campos inicialmente hasta que se genere código
        self.deshabilitar_campos()
        
    def generar_id_cliente(self):
        # Generamos ID aleatorio de 6 dígitos
        id_numero = random.randint(100000, 999999)
        self.id_cliente.set(f"ALQPC-{id_numero}")
    
    def generar_codigo_cliente(self):
        """Genera un nuevo código de cliente y habilita los campos"""
        # Deshabilior el botón inmediatamente
        self.btn_generar_codigo.config(state='disabled', bg='#95a5a6')

        self.generar_id_cliente()
        self.codigo_generado = True
        self.factura_generada = False  # Resetear estado de factura

        # Actualizar la interfaz
        self.label_id_cliente.config(text=self.id_cliente.get(), fg='#27ae60')

        # Habilito todos los campos
        self.habilitar_campos()

        messagebox.showinfo("Código Generado", f"Código de cliente generado: {self.id_cliente.get()}\n\nAhora puede completar los datos del cliente.")
    
    def habilitar_campos(self):
        """Habilita todos los campos del formulario"""
        # Habilitar campos de datos del cliente
        self.entry_nombre.config(state='normal')
        self.entry_correo.config(state='normal')
        self.entry_telefono.config(state='normal')
        
        # Habilitar campos de alquiler (estos ya los dejo habilitados por defecto pero aun asi no funcionarann)
        
    
    def deshabilitar_campos(self):
        """Deshabilita todos los campos del formulario"""
        # Deshabilitar campos de datos del cliente
        self.entry_nombre.config(state='disabled')
        self.entry_correo.config(state='disabled')
        self.entry_telefono.config(state='disabled')
    
    def validar_nombre(self, nombre):
        """Valida que el nombre no esté vacío y contenga solo letras y espacios"""
        if not nombre or nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        
        # Verificar que solo contenga letras y espacios
        import re
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$", nombre.strip()):
            return False, "El nombre solo puede contener letras y espacios"
        
        if len(nombre.strip()) < 2:
            return False, "El nombre debe tener al menos 2 caracteres"
        
        return True, "Nombre válido"
    
    def validar_correo(self, correo):
        """Valida que el correo tenga formato válido"""
        if not correo or correo.strip() == "":
            return False, "El correo no puede estar vacío"
        
        import re
        # Patrón básico para validar email
        patron_correo = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        if not re.match(patron_correo, correo.strip()):
            return False, "El formato del correo electrónico no es válido. Ejemplo: usuario@dominio.com"
        
        return True, "Correo válido"
    
    def validar_telefono(self, telefono):
        """Valida que el teléfono tenga formato válido"""
        if not telefono or telefono.strip() == "":
            return False, "El teléfono no puede estar vacío"
        
        # Remover espacios y caracteres especiales para validar
        import re
        telefono_limpio = re.sub(r'[\s\-\(\)\+]', '', telefono.strip())
        
        # Verificar que solo contenga dígitos
        if not telefono_limpio.isdigit():
            return False, "El teléfono solo puede contener números, espacios, guiones, paréntesis y el símbolo +"
        
        # Verificar longitud mínima (7 dígitos) y máxima (15 dígitos)
        if len(telefono_limpio) < 7:
            return False, "El teléfono debe tener al menos 7 dígitos"
        
        if len(telefono_limpio) > 15:
            return False, "El teléfono no puede tener más de 15 dígitos"
        
        return True, "Teléfono válido"
    
    def validar_datos_cliente(self):
        """Valida todos los datos del cliente y retorna mensajes de error"""
        errores = []
        
        # Validar nombre
        es_valido, mensaje = self.validar_nombre(self.nombre_cliente.get())
        if not es_valido:
            errores.append(f"Nombre: {mensaje}")
        
        # Validar correo
        es_valido, mensaje = self.validar_correo(self.correo_cliente.get())
        if not es_valido:
            errores.append(f"Correo: {mensaje}")
        
        # Validar teléfono
        es_valido, mensaje = self.validar_telefono(self.telefono_cliente.get())
        if not es_valido:
            errores.append(f"Teléfono: {mensaje}")
        
        return errores
        
    def calcular_precios(self):
        equipos = self.num_equipos.get()
        dias_iniciales = self.dias_iniciales.get()
        dias_adicionales = self.dias_adicionales.get()
        tipo = self.tipo_alquiler.get()
        
        # Cálculo base
        total_dias = dias_iniciales + dias_adicionales
        subtotal = equipos * total_dias * self.precio_dia
        
        # Aplicar modificadores según tipo de alquiler
        modificador_tipo = 0
        descripcion_modificador = ""
        
        if tipo == "fuera_ciudad":
            modificador_tipo = 0.05  # 5% incremento
            descripcion_modificador = "Servicio de domicilio (+5%)"
        elif tipo == "establecimiento":
            modificador_tipo = -0.05  # 5% descuento
            descripcion_modificador = "Descuento establecimiento (-5%)"
        else:  # dentro_ciudad
            modificador_tipo = 0
            descripcion_modificador = "Sin modificador"
        
        # Calcular modificador por tipo
        valor_modificador_tipo = subtotal * modificador_tipo
        
        # Calcular descuento por días adicionales (2% por día adicional)
        descuento_dias_adicionales = 0
        if dias_adicionales > 0:
            # Aplicar descuento del 2% por cada día adicional al subtotal
            porcentaje_descuento = dias_adicionales * 0.02  # 2% por cada día adicional
            descuento_dias_adicionales = subtotal * porcentaje_descuento
        
        # Total final
        total_final = subtotal + valor_modificador_tipo - descuento_dias_adicionales
        
        return {
            'equipos': equipos,
            'dias_iniciales': dias_iniciales,
            'dias_adicionales': dias_adicionales,
            'total_dias': total_dias,
            'precio_dia': self.precio_dia,
            'subtotal': subtotal,
            'tipo': tipo,
            'descripcion_modificador': descripcion_modificador,
            'valor_modificador_tipo': valor_modificador_tipo,
            'descuento_dias_adicionales': descuento_dias_adicionales,
            'total_final': total_final
        }
    
    def generar_factura(self):
        try:
            # Validar que el código de cliente esté generado
            if not self.codigo_generado:
                messagebox.showerror("Código Requerido", 
                    "Debe generar un código de cliente antes de continuar.\n\n"
                    "Presione el botón 'Generar Código Cliente' para continuar.")
                return
            
            # Validar que no se haya generado ya una factura con este ID
            if self.factura_generada:
                messagebox.showerror("ID ya utilizado",
                    f"No es posible usar el mismo ID ({self.id_cliente.get()}) dos veces.\n\n"
                    "Debe presionar el botón '🧹 LIMPIAR' para:\n"
                    "• Limpiar el formulario actual\n"
                    "• Generar un nuevo código de cliente\n"
                    "• Crear una nueva factura")
                return
            
            # Validar datos del cliente
            errores_cliente = self.validar_datos_cliente()
            if errores_cliente:
                mensaje_error = "Por favor corrija los siguientes errores en los datos del cliente:\n\n" + "\n".join(errores_cliente)
                messagebox.showerror("Error en datos del cliente", mensaje_error)
                return
            
            # Validar datos del alquiler
            if self.num_equipos.get() < 2:
                messagebox.showerror("Error", "El mínimo de equipos es 2")
                return
                
            if self.dias_iniciales.get() < 1:
                messagebox.showerror("Error", "Los días iniciales deben ser al menos 1")
                return
            
            # Calcular precios
            datos = self.calcular_precios()
            
            # Generar factura
            fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            factura = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ALQUIPC - FACTURA                              ║
║                        Alquiler de Computadores                             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Fecha: {fecha_actual:<65} ║
║ ID Cliente: {self.id_cliente.get():<57} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ DATOS DEL CLIENTE:                                                           ║
║                                                                              ║
║ • Nombre: {self.nombre_cliente.get():<67} ║
║ • Correo: {self.correo_cliente.get():<66} ║
║ • Teléfono: {self.telefono_cliente.get():<64} ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ DETALLES DEL ALQUILER:                                                       ║
║                                                                              ║
║ • Número de equipos: {datos['equipos']:<56} ║
║ • Días iniciales: {datos['dias_iniciales']:<58} ║
║ • Días adicionales: {datos['dias_adicionales']:<56} ║
║ • Total de días: {datos['total_dias']:<60} ║
║ • Precio por día: ${datos['precio_dia']:,.0f} ║
║                                                                              ║
║ TIPO DE ALQUILER:                                                            ║
║ • {self.get_descripcion_tipo(datos['tipo']):<74} ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ CÁLCULO DETALLADO:                                                           ║
║                                                                              ║
║ Subtotal ({datos['equipos']} equipos × {datos['total_dias']} días × ${self.precio_dia:,.0f}): ${datos['subtotal']:>12,.0f} ║
"""
            
            if datos['valor_modificador_tipo'] != 0:
                factura += f"║ {datos['descripcion_modificador']}: ${datos['valor_modificador_tipo']:>12,.0f} ║\n"
            
            if datos['descuento_dias_adicionales'] > 0:
                porcentaje_total = datos['dias_adicionales'] * 2
                factura += f"║ Descuento días adicionales ({porcentaje_total}% por {datos['dias_adicionales']} días): -${datos['descuento_dias_adicionales']:>8,.0f} ║\n"
            
            factura += f"""
╠══════════════════════════════════════════════════════════════════════════════╣
║ TOTAL A PAGAR: ${datos['total_final']:>55,.0f} ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║ NOTA: Este recibo será enviado por correo electrónico.                      ║
║       ALQUIPC contribuye con el reciclaje de papel.                         ║
║                                                                              ║
║ ¡Gracias por elegir ALQUIPC!                                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
            
            # Mostrar en el área de texto
            self.texto_resultado.delete(1.0, tk.END)
            self.texto_resultado.insert(1.0, factura)
            
            # Marcar que se generó una factura con este ID
            self.factura_generada = True
            
            messagebox.showinfo("Éxito", "Factura generada correctamente. El recibo será enviado por email.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar la factura: {str(e)}")
    
    def get_descripcion_tipo(self, tipo):
        if tipo == "dentro_ciudad":
            return "Dentro de la ciudad (sin modificador)"
        elif tipo == "fuera_ciudad":
            return "Fuera de la ciudad (incremento 5%)"
        else:
            return "Dentro del establecimiento (descuento 5%)"
    
    def limpiar_formulario(self):
        self.num_equipos.set(2)
        self.dias_iniciales.set(1)
        self.dias_adicionales.set(0)
        self.tipo_alquiler.set("dentro_ciudad")

        # Limpiar datos del cliente
        self.nombre_cliente.set("")
        self.correo_cliente.set("")
        self.telefono_cliente.set("")

        # Resetear estado del código y factura
        self.codigo_generado = False
        self.factura_generada = False
        self.label_id_cliente.config(text="[Sin generar]", fg='#e74c3c')
        self.btn_generar_codigo.config(text="Generar Código Cliente", bg='#e74c3c', state='normal')

        # Deshabilitar campos
        self.deshabilitar_campos()

        self.texto_resultado.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = AlquipcFacturacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()
