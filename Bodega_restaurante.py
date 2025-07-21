import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from datetime import datetime, timedelta
import hashlib


class RestaurantInventorySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")
        self.root.geometry("1200x1200")
        self.root.configure(bg="#ffffff")

        # Inicializar base de datos
        self.database()
        
        # Crear interfaz
        self.interfazTK()
        
        # Cargar datos
        self.carga_inventaroi()
        
    def database(self): #creacion base de datos con sqlite
        self.conn = sqlite3.connect('inventario.db')
        self.cursor = self.conn.cursor()
        
        # Crear tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                cantidad REAL NOT NULL,
                unidad TEXT NOT NULL,
                precio_unitario REAL NOT NULL,
                stock_minimo REAL NOT NULL,
                fecha_vencimiento TEXT NOT NULL,
                proveedor TEXT NOT NULL,
                fecha_actualizacion TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insertar datos de ejemplo si la tabla está vacía
        self.cursor.execute('SELECT COUNT(*) FROM inventario')
        if self.cursor.fetchone()[0] == 0: #si no hya ningun producto agrega los que se muetran ahi
            datos_ejemplo = [
                ('Pollo', 'Carnes', 25, 'kg', 12000, 10, '2025-06-20', 'Mc pollo'),
                ('Arroz', 'Granos', 50, 'kg', 3500, 20, '2025-12-15', 'Diana'),
                ('Tomate', 'Verduras', 8, 'kg', 4000, 15, '2025-06-18', 'Fruco'),
                ('Leche', 'Lacteos', 20, 'L', 2800, 10, '2025-06-22', 'Alpina'),
                ('Aceite', 'Condimentos', 12, 'L', 8500, 5, '2026-01-15', 'premier')
            ]
            
            self.cursor.executemany('''
                INSERT INTO inventario (nombre, categoria, cantidad, unidad, precio_unitario, 
                                      stock_minimo, fecha_vencimiento, proveedor)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
            ''', datos_ejemplo)  #posicion en la que se van a poner los items 
            
        self.conn.commit()
        
    def interfazTK(self): #interfaz grafica ATT: kevin arboleda yt, turbo codigo yt, codigo espinoza yt, programacion facil yt
        # Crear interfaz gráfica
        ventana = ttk.Frame(self.root, padding="10") #con self.root esta llamando a la ventana creada en el rpincipio, y con padding separa 10 pix del borde
        ventana.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))#se pone desde la esquina superior izq y se expande si la ventana cambia de tamaño
        
        #adaptaciones de tamaño de la pantalla para eviar problemas de vusisual
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        ventana.columnconfigure(1, weight=1)
        ventana.rowconfigure(2, weight=1)
        
        # Título
        titulo = ttk.Label(ventana, text="Sistema de Inventario PythUNAL", 
                               font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20)) #ubicacion del titulo
        
        #Estadísticas totales del inventario
        estadisticas = ttk.LabelFrame(ventana, text="Estadísticas", padding="10")
        estadisticas.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.total_stats = {}
        estadisticas_item = ['Total Items', 'Stock Bajo', 'Por Vencer', 'Valor Total'] #crear las eituqtas para las estadisticas del inventario final
        for i, item in enumerate(estadisticas_item): #un for que recorre estadisticas_item y le da un elemento grafico a cada uno
            ttk.Label(estadisticas, text=f"{item}:", font=('Arial', 10, 'bold')).grid(row=0, column=i*2, padx=(0, 5))
            self.total_stats[item] = ttk.Label(estadisticas, text="0")
            self.total_stats[item].grid(row=0, column=i*2+1, padx=(0, 20))
        
        #adaptaciones de tamaño de la pantalla para eviar problemas de vusisual
        controls_frame = ttk.Frame(ventana)
        controls_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        controls_frame.columnconfigure(1, weight=1)
        controls_frame.rowconfigure(1, weight=1)
        
        # Botones de acción
        botones = ttk.Frame(controls_frame)
        botones.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10)) #organizacion de botones
        
        #agrega los botones de las acciones que se pueden ahecr en el inventario, se uso pack por la sencilles
        ttk.Button(botones, text="Agregar Producto", 
                  command=self.Agregar_producto).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(botones, text="Editar Producto", 
                  command=self.Editar_prodcto).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(botones, text="Eliminar Producto", 
                  command=self.eliminar_producto).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(botones, text="Ver Alertas", 
                  command=self.alertas_FV).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(botones, text="Reporte", 
                  command=self.generar_reporte).pack(side=tk.LEFT, padx=(0, 5))
        
        #barra de busqueda para filtrar los objetos del inevntario
        busqueda = ttk.Frame(controls_frame)
        busqueda.grid(row=0, column=2, sticky=(tk.E), pady=(0, 10))
        
    
        ttk.Label(busqueda, text="Buscar:").pack(side=tk.LEFT, padx=(0, 5))
        self.barra_busq = tk.StringVar()
        self.barra_busq.trace('w', self.filtrar) #si el usuario escribe algo llama a la funcion filtrar
        entrada = ttk.Entry(busqueda, textvariable=self.barra_busq, width=20)
        entrada.pack(side=tk.LEFT)
        
        #tabla de inventario y acomodacion para el visual
        tabla = ttk.Frame(controls_frame)
        tabla.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        tabla.columnconfigure(0, weight=1)
        tabla.rowconfigure(0, weight=1)
        
        #creacion de las columnas
        self.tabla = ttk.Treeview(tabla, columns=('ID', 'Nombre', 'Categoría', 'Cantidad', 
                                                     'Unidad', 'Precio Unit.', 'Stock Mín.', 
                                                     'Vencimiento', 'Proveedor', 'Estado'), 
                                show='headings', height=20)
        
        #diccionario para configurar el ancho de cada columna en pix
        colum_config = {
            'ID': 50,
            'Nombre': 150,
            'Categoría': 100,
            'Cantidad': 80,
            'Unidad': 70,
            'Precio Unit.': 100,
            'Stock Mín.': 80,
            'Vencimiento': 100,
            'Proveedor': 150,
            'Estado': 100
        }
        
        for col, tam in colum_config.items(): #reocrre el diccionario para hacer el siguiente proceso
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=tam, anchor=tk.CENTER) #se define el ancho, la alineacion y el nombre de cada columna
        
        #scrollbars by nicosiored yt
        v_scrollbar = ttk.Scrollbar(tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        h_scrollbar = ttk.Scrollbar(tabla, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        #aca se le da la orientacion de las scrollbars
        self.tabla.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
    def carga_inventaroi(self):
        #limpiar tabla par que no se acumulen cada vez qeu se corra el codigo
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        #se obtienen los datos de la base de datos creada
        self.cursor.execute('''
            SELECT id, nombre, categoria, cantidad, unidad, precio_unitario, 
                   stock_minimo, fecha_vencimiento, proveedor
            FROM inventario ORDER BY nombre
        ''')
        
        items = self.cursor.fetchall()
        
        for item in items:
            estado = self.alerta_stock(item[3], item[6])  #aca determina junto a la definicion alerta_stock 
            
            #convierte el prcio de forma $xxx.xxx
            precio = f"${item[5]:,.0f}"
            
            #innsertar todo en la tabla
            item_id = self.tabla.insert('', tk.END, values=(
                item[0], item[1], item[2], item[3], item[4], 
                precio, item[6], item[7], item[8], estado
            ))
            
            #colorear segun estado critico/bajo/normal
            if estado == 'CRÍTICO':
                self.tabla.item(item_id, tags=('critical',))
            elif estado == 'BAJO':
                self.tabla.item(item_id, tags=('warning',))
        
        # Configurar colores
        self.tabla.tag_configure('critical', background='#ffcccc')
        self.tabla.tag_configure('warning', background='#fff3cd')
        
        # Actualizar estadísticas
        self.Actualizar_producto()
        
    def alerta_stock(self, cantidad, stock_minimo): #alertas para cuando un producto esta por debajo del stock minimo o cerca de llegar a el
        if cantidad <= stock_minimo:
            return 'CRÍTICO'
        elif cantidad <= stock_minimo * 1.5:
            return 'BAJO'
        else:
            return 'NORMAL'
    
    def Actualizar_producto(self):
        self.cursor.execute('SELECT COUNT(*) FROM inventario')
        total_items = self.cursor.fetchone()[0] # no de productos que hay
        
        self.cursor.execute('SELECT COUNT(*) FROM inventario WHERE cantidad <= stock_minimo')
        stock_bajo = self.cursor.fetchone()[0] # no de producto que tienen stock minimo
        
        # Items por vencer (próximos 7 días)
        fecha_limite = (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d') #Cuenta los prudctos que se vencen en los ultimos 15 dias o ya vencieron
        self.cursor.execute('SELECT COUNT(*) FROM inventario WHERE fecha_vencimiento <= ?', (fecha_limite,))
        por_vencer = self.cursor.fetchone()[0]
        
        # Valor total
        self.cursor.execute('SELECT SUM(cantidad * precio_unitario) FROM inventario') #calcula el valor total de todos los productos del inventario
        valor_total = self.cursor.fetchone()[0] or 0
        
        #Se hacen las operaciond de estadisticas_items que etsba en la primera definicion
        self.total_stats['Total Items'].config(text=str(total_items), foreground = 'red')
        self.total_stats['Stock Bajo'].config(text=str(stock_bajo), foreground='red' if stock_bajo > 0 else 'blue')
        self.total_stats['Por Vencer'].config(text=str(por_vencer), foreground='orange' if por_vencer > 0 else 'blue')
        self.total_stats['Valor Total'].config(text=f"${valor_total:,.0f}", foreground='green')
    
    def filtrar(self):
        filtrarfinal = self.barra_busq.get().lower()
        
        #elimina los elemntos de la tabla sin embargo deja los que han sido filtrados
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        #buscar en base de datos por colulta SQL ya sea por nombre, sategoria o proveedor
        query = '''
            SELECT id, nombre, categoria, cantidad, unidad, precio_unitario, 
                   stock_minimo, fecha_vencimiento, proveedor
            FROM inventario 
            WHERE LOWER(nombre) LIKE ? OR LOWER(categoria) LIKE ? OR LOWER(proveedor) LIKE ?
            ORDER BY nombre
        '''
        
        self.cursor.execute(query, (f'%{filtrarfinal}%', f'%{filtrarfinal}%', f'%{filtrarfinal}%'))
        items = self.cursor.fetchall()
        
        #actrualiza los productos filtrados en la tabla y los actualiza con los parametros de stock y precio
        for item in items:
            estado = self.alerta_stock(item[3], item[6])
            precio_fmt = f"${item[5]:,.0f}"
            
            item_id = self.tabla.insert('', tk.END, values=(
                item[0], item[1], item[2], item[3], item[4], 
                precio_fmt, item[6], item[7], item[8], estado
            ))
            
            if estado == 'CRÍTICO':
                self.tabla.item(item_id, tags=('critical',))
            elif estado == 'BAJO':
                self.tabla.item(item_id, tags=('warning',))
    
    def agregar_editar(self, product_data=None):
        emergente = tk.Toplevel(self.root) #se crea una ventana emergente
        emergente.title("Agregar Producto" if product_data is None else "Editar Producto") #si se sslecciona un rpoducto la ventana emergente sera la de editar si no era la de agregar
        emergente.geometry("500x500")
        emergente.transient(self.root) #se mantiene dobre la ventana pricipals
        emergente.grab_set()  #no se cierra si no se cierra la pricipasl
        
        #variables, atring var para variables de texto y doublevar para vairables de decimales
        in_var = {
            'nombre': tk.StringVar(),
            'categoria': tk.StringVar(),
            'cantidad': tk.DoubleVar(),
            'unidad': tk.StringVar(),
            'precio_unitario': tk.DoubleVar(),
            'stock_minimo': tk.DoubleVar(),
            'fecha_vencimiento': tk.StringVar(),
            'proveedor': tk.StringVar()
        }
        
        #si es edicion, se llena con datos existentes
        if product_data:
            in_var['nombre'].set(product_data[1])
            in_var['categoria'].set(product_data[2])
            in_var['cantidad'].set(product_data[3])
            in_var['unidad'].set(product_data[4])
            in_var['precio_unitario'].set(product_data[5])
            in_var['stock_minimo'].set(product_data[6])
            in_var['fecha_vencimiento'].set(product_data[7])
            in_var['proveedor'].set(product_data[8])
        
        #crear campos
        ventana = ttk.Frame(emergente, padding="20")
        ventana.pack(fill=tk.BOTH, expand=True)
        
        fields = [
            ('Nombre:', 'nombre', ttk.Entry),
            ('Categoría:', 'categoria', lambda parent, **kwargs: ttk.Combobox(parent, values=['Carnes', 'Verduras', 'Granos', 'Lácteos', 'Bebidas', 'Condimentos', 'Otros'], **kwargs)),
            ('Cantidad:', 'cantidad', ttk.Entry),
            ('Unidad:', 'unidad', lambda parent, **kwargs: ttk.Combobox(parent, values=['kg', 'g', 'L', 'ml', 'unidades', 'cajas'], **kwargs)),
            ('Precio Unitario:', 'precio_unitario', ttk.Entry),
            ('Stock Mínimo:', 'stock_minimo', ttk.Entry),
            ('Fecha Vencimiento (YYYY-MM-DD):', 'fecha_vencimiento', ttk.Entry),
            ('Proveedor:', 'proveedor', ttk.Entry)
        ]
        
        widgets = {}
        for i, (label, var_name, widget_class) in enumerate(fields):
            ttk.Label(ventana, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            
            widget = widget_class(ventana, textvariable=in_var[var_name], width=30)
            widget.grid(row=i, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
            widgets[var_name] = widget
        
        #botones
        botones = ttk.Frame(ventana)
        botones.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        def guardar_prodcuto():
            try:
                #validar campos obligatorios
                if not in_var['nombre'].get() or not in_var['categoria'].get():
                    messagebox.showerror("Error", "Todas las celdas son obligatoriass")
                    return
                
                values = [  #extra los valores en cada campo 
                    in_var['nombre'].get(),
                    in_var['categoria'].get(),
                    in_var['cantidad'].get(),
                    in_var['unidad'].get(),
                    in_var['precio_unitario'].get(),
                    in_var['stock_minimo'].get(),
                    in_var['fecha_vencimiento'].get(),
                    in_var['proveedor'].get()
                ]
                
                if product_data is None:  #si el producto no estaba se agrega
                    self.cursor.execute('''
                        INSERT INTO inventario (nombre, categoria, cantidad, unidad, precio_unitario, 
                                              stock_minimo, fecha_vencimiento, proveedor)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', values)
                    message = "Producto agregado correctamente"
                else:  #Si ya estaba se edita
                    self.cursor.execute('''
                        UPDATE inventario SET nombre=?, categoria=?, cantidad=?, unidad=?, 
                                            precio_unitario=?, stock_minimo=?, fecha_vencimiento=?, proveedor=?
                        WHERE id=?
                    ''', values + [product_data[0]])
                    message = "Producto actualizado correctamente"
                
                self.conn.commit()
                self.carga_inventaroi()
                emergente.destroy()
                messagebox.showinfo("Éxito", message)
                
            except Exception as error:
                messagebox.showerror("Error", f"Error al guardar: {str(error)}")
        
        ttk.Button(botones, text="Guardar", command=guardar_prodcuto).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones, text="Cancelar", command=emergente.destroy).pack(side=tk.LEFT, padx=5)
        
        # Configurar grid
        ventana.columnconfigure(1, weight=1)

    def Agregar_producto(self): #agrega el rpodcuto al inevntario
        self.agregar_editar()
    
    def Editar_prodcto(self): #edita el productoq que se selecciono
        selection = self.tabla.selection()
        if not selection:
            messagebox.showwarning("Cuidado", "Selecciona un producto para editar")
            return
        
        item = self.tabla.item(selection[0]) #toma los dos del producto seleccionado
        product_id = item['values'][0]  #toma el id para consultar el producto en la base de datos
        
        # Obtener datos completos del producto
        self.cursor.execute('SELECT * FROM inventario WHERE id = ?', (product_id,)) #edita el producto en la base de datos por el id
        product_data = self.cursor.fetchone()
        
        self.agregar_editar(product_data)
    
    def eliminar_producto(self):
        selection = self.tabla.selection()
        if not selection:
            messagebox.showwarning("Cuidado", "Selecciona un producto para eliminar")
            return
        
        item = self.tabla.item(selection[0])
        product_id = item['values'][0] #toma el id del producto
        product_name = item['values'][1] #toma el nombre dle producto
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar el producto '{product_name}'?"): #aparece un mensaje con el nombre dle producto
            self.cursor.execute('DELETE FROM inventario WHERE id = ?', (product_id,)) #elimina el producto de la base de datos por el id
            self.conn.commit()
            self.carga_inventaroi()#carga el invenatario con la nueva informacion
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")

    def alertas_FV(self):
        """Mostrar ventana de alertas"""
        alerta_vent = tk.Toplevel(self.root)
        alerta_vent.title("Alertas de Inventario")
        alerta_vent.geometry("800x600")
        alerta_vent.transient(self.root) #se mantiene la ventana principal
        
        notebook = ttk.Notebook(alerta_vent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        #primera ventana "stock bajo"
        bajo_stock = ttk.Frame(notebook)
        notebook.add(bajo_stock, text="Stock Bajo")
        
        ttk.Label(bajo_stock, text="Productos con stock bajo:", font=('Arial', 12, 'bold')).pack(pady=10)
        
        bajo_stock = ttk.Treeview(bajo_stock, columns=('Nombre', 'Cantidad', 'Stock Mín.', 'Diferencia'),show='headings', height=10) #columnas de inforamcion para las alertas
        
        for col in ['Nombre', 'Cantidad', 'Stock Mín.', 'Diferencia']:  #para poner los titulos en cada columna
            bajo_stock.heading(col, text=col)
            bajo_stock.column(col, width=150, anchor=tk.CENTER)
        
        bajo_stock.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  #se acomoda a la visual
        
        # Cargar productos con stock bajo
        self.cursor.execute('''
            SELECT nombre, cantidad, stock_minimo 
            FROM inventario 
            WHERE cantidad <= stock_minimo
            ORDER BY (cantidad - stock_minimo)
        ''')
        
        for item in self.cursor.fetchall():
            diferencia = item[1] - item[2]
            bajo_stock.insert('', tk.END, values=(item[0], item[1], item[2], f"{diferencia:.1f}"))
        
        #Segunda ventana "Proximos a vencer"
        expiracion = ttk.Frame(notebook)
        notebook.add(expiracion, text="Próximos a Vencer")
        
        ttk.Label(expiracion, text="Productos que vencieeron o vencen en los próximos 15 dias:", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        expiracion = ttk.Treeview(expiracion, columns=('Nombre', 'Cantidad', 'Vencimiento', 'Días'), show='headings', height=10)#informacion que ira en la columnas
        
        for col in ['Nombre', 'Cantidad', 'Vencimiento', 'Días']:  #texto de las columnas
            expiracion.heading(col, text=col)
            expiracion.column(col, width=150, anchor=tk.CENTER)
        
        expiracion.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Cargar productos próximos a vencer
        fecha_limite = (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d') #con datetime se obtiene la fecha acutal del sistema y se le suman 15 dias
        self.cursor.execute('''
            SELECT nombre, cantidad, fecha_vencimiento 
            FROM inventario 
            WHERE fecha_vencimiento <= ?
            ORDER BY fecha_vencimiento
        ''', (fecha_limite,)) #aca compara la fecha limite con la fecha de vencimiento de cada uno de los productos
        
        for item in self.cursor.fetchall():
            try:
                fecha_venc = datetime.strptime(item[2], '%Y-%m-%d')
                dias_restantes = (fecha_venc - datetime.now()).days  #fecha de vencimiento - dia actual
                expiracion.insert('', tk.END, values=(item[0], item[1], item[2], dias_restantes))  #inserta la alerta con los dias restantes
            except:
                expiracion.insert('', tk.END, values=(item[0], item[1], item[2], "N/A"))
    
    def generar_reporte(self):
        report_vent = tk.Toplevel(self.root)
        report_vent.title("Reporte de inventario")
        report_vent.geometry("700x700")
        report_vent.transient(self.root)
        
        #Crear ventana de texto con scroll by nicosiored yt
        text_frame = ttk.Frame(report_vent)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10) #PADX horizontal y PADY vertical 
        
        text_widget = tk.Text(text_frame, wrap=tk.WORD, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        #generar contenido del reporte
        report_content = self.reporte_inventario() #report_content es el reporte del inventario
        text_widget.insert(tk.END, report_content)
        text_widget.config(state=tk.DISABLED)
        
        #botonn para guardar reporte
        ttk.Button(report_vent, text="Guardar Reporte", 
                  command=lambda: self.reporte_en_txt(report_content)).pack(pady=10) #report_content se envia a reporte_en_txt como parametro alla como content
    
    def reporte_inventario(self): #generar la infor del reporte
        report_lst = [] #se crea una lista xq con strings son inmuutables
        report_lst.append("="*60)
        report_lst.append("REPORTE DE INVENTARIO")
        report_lst.append(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") #fecha de hoy
        report_lst.append("="*60)
        report_lst.append("")
        
        #estadisticas generales
        self.cursor.execute('SELECT COUNT(*) FROM inventario') #cantidad total de productos
        total_items = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT SUM(cantidad * precio_unitario) FROM inventario') #suma total del inventario
        valor_total = self.cursor.fetchone()[0] or 0
        
        self.cursor.execute('SELECT COUNT(*) FROM inventario WHERE cantidad <= stock_minimo') #cuantos productos estan en el minimo o debajo
        stock_bajo = self.cursor.fetchone()[0]
        
        report_lst.append("RESUMEN INVENTARIO PythUNAL:") #lo que se busco anteriormente se agrega aca
        report_lst.append(f"• Total de productos: {total_items}")
        report_lst.append(f"• Valor total del inventario: ${valor_total:,.0f}")
        report_lst.append(f"• Productos con stock bajo: {stock_bajo}")
        report_lst.append("")
        
        # Inventario por categoría
        report_lst.append("INVENTARIO POR CATEGORÍA:")
        report_lst.append("-" * 40)
        
        self.cursor.execute('''
            SELECT categoria, COUNT(*), SUM(cantidad * precio_unitario)
            FROM inventario 
            GROUP BY categoria 
            ORDER BY categoria
        ''')
        
        for categ, cantidad, valor in self.cursor.fetchall(): #recorre las stats de los prodcutos existentes en un for y los separa por categoira
            report_lst.append(f"{categ:15} | {cantidad:3} items | ${valor:>10,.0f}")   #.0f para los decimales y > para alinearlo a la derecha
        
        report_lst.append("")
        
        # Productos con stock crítico
        report_lst.append("PRODUCTOS CON STOCK CRÍTICO:")
        report_lst.append("-" * 50)
        
        self.cursor.execute('''
            SELECT nombre, cantidad, stock_minimo, unidad
            FROM inventario 
            WHERE cantidad < stock_minimo
            ORDER BY (cantidad - stock_minimo)
        ''')
        
        critical_items = self.cursor.fetchall()
        if critical_items: #si hay productos con stock bajo 
            for nombre, cantidad, stock_min, unidad in critical_items:
                report_lst.append(f"• {nombre}: {cantidad} {unidad} (El minimo es: {stock_min} {unidad})")
        else: #si no hay
            report_lst.append("• No hay productos con stock bajo")
        
        report_lst.append("")
        
        # Inventario completo
        report_lst.append("INVENTARIO COMPLETO:")
        report_lst.append("-" * 80)
        report_lst.append(f"{'Producto':<15} {'Cat.':<15} {'Cant.':<8} {'Unidad':<8} {'Precio':<12} {'Total':<12}")
        report_lst.append("-" * 80)
        
        self.cursor.execute('''
            SELECT nombre, categoria, cantidad, unidad, precio_unitario
            FROM inventario 
            ORDER BY categoria, nombre
        ''')
        
        for nombre, categoria, cantidad, unidad, precio in self.cursor.fetchall(): #toma todo el inventario disponible
            total_item = cantidad * precio
            report_lst.append(f"{nombre[:19]:<15} {categoria[:11]:<15} {cantidad:<8.0f} {unidad:<8} ${precio:<11,.0f} ${total_item:<11,.0f}")
        
        return "\n".join(report_lst) #esta linea convierte la lista creada al principio por comodidad en un string separado por \n
    
    def reporte_en_txt(self, content):
        try:
            filename = f"reporte_inventario_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" #nombre del archivo txt con la fecha actual
            with open(filename, 'w', encoding='utf-8') as f: #UTF-8 es par que acepte caracteres espciales
                f.write(content)
            messagebox.showinfo("Éxito", f"Reporte guardado como: {filename}")
        except Exception as error: #cualquier error que impida guardar el reporte se avia con una ventana emergente
            messagebox.showerror("Error", f"Error al guardar el reporte: {str(error)}")
    
    def __del__(self): #se destruye el objeto para salvar mrecursos o evitar daños en los archivos sqlite otxt
        if hasattr(self, 'conn'): #verifica si tiene conexion aun con la base de datos sqlite
            self.conn.close()


class LoginSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Acceso al Sistema - Restaurante")
        self.root.geometry("400x300")
        self.root.configure(bg='#2c3e50')
        
        # Centrar ventana
        self.center_window()
        
        # Inicializar base de datos de usuarios
        self.init_user_database()
        
        # Crear interfaz de login
        self.create_login_interface()
        
        # Variable para controlar si el login fue exitoso
        self.login_successful = False
        
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        self.root.geometry(f"400x300+{x}+{y}")
        
    def init_user_database(self):
        """Inicializar base de datos de usuarios"""
        self.conn = sqlite3.connect('usuarios_restaurante.db')
        self.cursor = self.conn.cursor()
        
        # Crear tabla de usuarios si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Crear usuario administrador por defecto si no existe
        self.cursor.execute('SELECT COUNT(*) FROM usuarios WHERE username = ?', ('admin',))
        if self.cursor.fetchone()[0] == 0:
            # Contraseña: admin123 (hasheada)
            admin_password = self.hash_password('admin123')
            self.cursor.execute('''
                INSERT INTO usuarios (username, password, role)
                VALUES (?, ?, ?)
            ''', ('admin', admin_password, 'admin'))
            
            # Usuario normal: user, contraseña: user123
            user_password = self.hash_password('user123')
            self.cursor.execute('''
                INSERT INTO usuarios (username, password, role)
                VALUES (?, ?, ?)
            ''', ('user', user_password, 'user'))
            
        self.conn.commit()
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()  #sha256 para la seguridad
        
    def create_login_interface(self):
        """Crear interfaz de login"""
        # Frame principal
        ventanalogin = tk.Frame(self.root, bg='#2c3e50')
        ventanalogin.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Título
        titulo2 = tk.Label(ventanalogin, text="Sistema de Inventario", 
                              font=('Arial', 20, 'bold'), 
                              fg='#ecf0f1', bg="#2c2d50")
        titulo2.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(ventanalogin, text="Restaurante", 
                                 font=('Arial', 14), 
                                 fg='#bdc3c7', bg='#2c3e50')
        subtitle_label.pack(pady=(0, 30))
        
        # Frame del formulario
        form_frame = tk.Frame(ventanalogin, bg='#34495e', relief='raised', bd=2)
        form_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Título del formulario
        form_title = tk.Label(form_frame, text="Iniciar Sesión", 
                             font=('Arial', 16, 'bold'), 
                             fg='#ecf0f1', bg='#34495e')
        form_title.pack(pady=20)
        
        # Campo usuario
        user_frame = tk.Frame(form_frame, bg='#34495e')
        user_frame.pack(pady=10, padx=30, fill='x')
        
        tk.Label(user_frame, text="Usuario:", font=('Arial', 12), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        self.username_var = tk.StringVar()
        self.username_entry = tk.Entry(user_frame, textvariable=self.username_var, 
                                      font=('Arial', 12), width=25, relief='flat', 
                                      bg='#ecf0f1', fg='#2c3e50')
        self.username_entry.pack(pady=(5, 0), ipady=8)
        
        # Campo contraseña
        pass_frame = tk.Frame(form_frame, bg='#34495e')
        pass_frame.pack(pady=10, padx=30, fill='x')
        
        tk.Label(pass_frame, text="Contraseña:", font=('Arial', 12), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(pass_frame, textvariable=self.password_var, 
                                      font=('Arial', 12), width=25, show='*', 
                                      relief='flat', bg='#ecf0f1', fg='#2c3e50')
        self.password_entry.pack(pady=(5, 0), ipady=8)
        
        # Boton de login
        login_button = tk.Button(form_frame, text="Iniciar Sesión", 
                               font=('Arial', 12, 'bold'), 
                               bg='#3498db', fg='white', 
                               relief='flat', cursor='hand2',
                               command=self.login)
        login_button.pack(pady=20, ipady=8, ipadx=20)
        
        # Informacion de usuarios por defecto
        info_frame = tk.Frame(form_frame, bg='#34495e')
        info_frame.pack(pady=(10, 20), padx=30, fill='x')
        
        tk.Label(info_frame, text="Usuarios por defecto:", 
                font=('Arial', 10, 'bold'), fg='#f39c12', bg='#34495e').pack()
        tk.Label(info_frame, text="Admin: usuario='admin', contraseña='admin123'", 
                font=('Arial', 9), fg='#ecf0f1', bg='#34495e').pack()
        tk.Label(info_frame, text="Usuario: usuario='user', contraseña='user123'", 
                font=('Arial', 9), fg='#ecf0f1', bg='#34495e').pack()
        
        # Bind Enter key para login
        self.root.bind('<Return>', lambda e: self.login())
        
        # Focus en el campo de usuario
        self.username_entry.focus()
        
    def login(self):
        """Proceso de autenticación"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        # Validar campos
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
            return
        
        # Hashear contraseña ingresada
        hashed_password = self.hash_password(password)
        
        # Verificar credenciales
        self.cursor.execute('''
            SELECT id, username, role FROM usuarios 
            WHERE username = ? AND password = ?
        ''', (username, hashed_password))
        
        user_data = self.cursor.fetchone()
        
        if user_data:
            self.login_successful = True
            self.user_id = user_data[0]
            self.username = user_data[1]
            self.user_role = user_data[2]
            
            messagebox.showinfo("Éxito", f"¡Bienvenido {username}!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.password_var.set("")  # Limpiar contraseña
            self.password_entry.focus()
    
    def run(self):
        """Ejecutar el sistema de login"""
        self.root.mainloop()
        return self.login_successful
    
    def get_user_info(self):
        """Obtener información del usuario autenticado"""
        if hasattr(self, 'user_id'):
            return {
                'id': self.user_id,
                'username': self.username,
                'role': self.user_role
            }
        return None
    
    def __del__(self):
        """Cerrar conexión a la base de datos"""
        if hasattr(self, 'conn'):
            self.conn.close()


def main():
    """Función principal que ejecuta primero el login y luego el inventario"""
    
    # 1. EJECUTAR SISTEMA DE LOGIN
    login_system = LoginSystem()
    login_success = login_system.run()
    
    # 2. SI EL LOGIN ES EXITOSO, ABRIR INVENTARIO
    if login_success:
        user_info = login_system.get_user_info()
        
        # Crear ventana para el sistema de inventario
        root = tk.Tk()
        app = RestaurantInventorySystem(root)
        root.mainloop()
    else:
        print("Acceso denegado - Login cancelado")

if __name__ == "__main__":
    main()






# FUNCIÓN PRINCIPAL MODIFICADA
# def main():
#     """Función principal que ejecuta primero el login y luego el inventario"""
    
#     # 1. EJECUTAR SISTEMA DE LOGIN
#     login_system = LoginSystem()
#     login_success = login_system.run()
    
#     # 2. SI EL LOGIN ES EXITOSO, ABRIR INVENTARIO
#     if login_success:
#         user_info = login_system.get_user_info()
        
#         # Crear nueva ventana raíz para el inventario
#         inventory_root = tk.Tk()
#         inventory_root.mainloop()
#         if __name__ == "__main__":
#             root = tk.Tk()
#             app = RestaurantInventorySystem(root)
#             root.mainloop()
#     else:
#         print("Acceso denegado - Login cancelado")

# if __name__ == "__main__":
#             main()
