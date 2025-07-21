# Sistema de inventario para un restaurante




### Presentación

**Curso:** Programación Orientada a Objetos

**Grupo:** PythUNAL

**Docente:** Felipe Gonzales  Roldan

**Integrantes:** Jhonyer Camilo Padilla Enríquez, Andres Camilo, Diego 

------------



### ¿De qué trata este proyectoh

<p>Es un programa que implementa un sistema de inventario para gestionar un resturante o cualquier negocio pequeño de comida(heladería, cafetería , pizzría, etc.)desarrollado en Python con interfaz gráfica basada en Tkinter y persistencia de datos en SQLite

------------



### Objetivo

<p>Facilitar la administración eficiente de productos almacenados o en bodega, permitiendo llevar un control detallado del stock disponible, el estado de los productos, sus fechas de vencimiento, y otras variables clave para una operación organizada y segura.

------------



### Características 

•  Autenticación de usuarios con roles (admin / user).

•  Carga, edición y eliminación de productos con validaciones.

•  Actualización de stock y control de inventario en tiempo real.

•  Alertas automáticas para productos en estado crítico(con stock mínimo fuera de límite).

•  Filtrado y búsqueda inteligente de ítems.

•  Generación de reportes con estadísticas, categorías y detalle completo del inventario.

•  Acceso programático (API interna) para operaciones automatizadas sobre el inventario.

------------



###  Diagrama UML del sistema

------------


### Estructura de Módulos y paquetes

------------


### Tecnologías utilizadas 

Para el desarrollo del programa, fueron útile herramientas y librerías disponibles en Python. 

------------
### Explicación del código 

**Clase LoginSystem**

def login(self):
    """Proceso de autenticación"""
    username = self.username_var.get().strip()
    password = self.password_var.get().strip()
    hashed_password = self.hash_password(password)
    

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
        self.root.destroy()
        
**Función:** Gestiona el proceso de autenticación de usuarios usando SHA-256 para validar contraseñas. Si las credenciales son correctas, guarda los datos del usuario y cierra la ventana del login.

-----------

**Clase RestaurantInventorySystem**

def load_inventory(self):
    """Cargar todos los productos del inventario en la tabla"""
    self.cursor.execute('SELECT * FROM inventario ORDER BY nombre')
    for item in self.cursor.fetchall():
        estado = self.get_stock_status(item[3], item[6])
        self.tree.insert('', tk.END, values=(...))
        
**Función:** Obtiene todos los productos desde SQLite y los muestra en la tabla principal de la interfaz gráfica. También determina el estado del stock (normal, bajo o crítico).
        
**Detección del estado del stock**

def get_stock_status(self, cantidad, stock_minimo):
    if cantidad <= stock_minimo:
        return 'CRÍTICO'
    elif cantidad <= stock_minimo * 1.5:
        return 'BAJO'
    else:
        return 'NORMAL'
        
**Función:** Determina el estado del producto para generar alertas visuales. Cuando la cantidad está por debajo del mínimo o es igual, el estado es crítico. 

**Generación de reportes**

def generate_report_content(self):
    self.cursor.execute('SELECT COUNT(*) FROM inventario')
    total_items = self.cursor.fetchone()[0]
    ...
    report.append(f"• Total de productos: {total_items}")
    report.append(f"• Valor total del inventario: ${valor_total:,.0f}") 
    
**Función:** Genera un reporte detallado del inventario, que incluye estadísticas generales, productos críticos, y una tabla con todos los productos.

-----------

**Clase InventoryAPI**

def agregar_producto(self, nombre, categoria, cantidad, unidad, precio_unitario, 
                    stock_minimo, fecha_vencimiento=None, proveedor=None):
    self.cursor.execute('''
        INSERT INTO inventario (...)
    ''', (nombre, categoria, cantidad, unidad, precio_unitario, stock_minimo, fecha_vencimiento, proveedor))
    self.conn.commit()
    
**Función:** Permite agregar productos desde otras interfaces o scripts usando esta API en lugar de la interfaz gráfica. Facilita integraciones externas.

**Función principal "main"**

# FUNCIÓN PRINCIPAL QUE INICIA EL SISTEMA
def main():
    """Función principal que ejecuta primero el login y luego el inventario"""
    
    # 1. Ejecutar sistema de login
    login_system = LoginSystem()
    login_success = login_system.run()
    
    # 2. Si el login es exitoso, abrir la interfaz de inventario
    if login_success:
        user_info = login_system.get_user_info()
        inventory_root = tk.Tk()
        
        # Inicializar el sistema de inventario
        app = RestaurantInventorySystem(inventory_root, user_info)
        inventory_root.mainloop()
    else:
        print("Acceso denegado - Login cancelado")


if __name__ == "__main__":
    main()

**Función:** Marca el inicio del sistema. Su finalidad es ejecutar la interfaz de login usando la clase LoginSystem y verificar las credenciales del usuario. Si el login es exitoso se lanza la interfaz principal del sistema de inventario con RestaurantInventorySystem.




