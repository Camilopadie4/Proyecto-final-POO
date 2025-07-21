# Sistema de inventario para un restaurante

### Presentación

**Curso:** Programación Orientada a Objetos

**Grupo:** PythUNAL

**Docente:** Felipe Gonzales  Roldan

**Integrantes:** Jhonyer Camilo Padilla Enríquez, Andres Camilo, Diego   

------------


### ¿De qué trata este proyectoh

<p>Es un programa que implementa un sistema de inventario para gestionar un resturante o cualquier negocio pequeño de comida(heladería, cafetería , pizzría, etc.)desarrollado en Python con interfaz gráfica basada en Tkinter y persistencia de datos en SQLite.

------------



### Objetivo

<p>El objetivo principal del programa es facilitar la administración eficiente de productos almacenados o en bodega, permitiendo llevar un control detallado del stock disponible, el estado de los productos, sus fechas de vencimiento, y otras variables clave para una operación organizada y segura.

### Justificación 
<p> Decidimos crear este programa con el ánimo de crear una herramienta útil y sencilla para manejar inventarios de bodegas pequeñas. Notamos que muchos negocios manejan su inventario a mano, lo que genera desorden, desperdicio y pérdidas, por ello, con este proyecto vimos la oportunidad de automatizar esos procesos y hacerlos más eficientes.   


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


<img width="1446" height="3840" alt="Mermaid Chart - Create complex, visual diagrams with text  A smarter way of creating diagrams -2025-07-21-013002" src="https://github.com/user-attachments/assets/36c37419-d2cc-4043-977f-e9350195cbb4" />




------------

### Lógica general del sistema

1. **Autenticación de Usuario**

- Se inicia con la ventana de login (LoginSystem).

- El usuario debe ingresar su nombre y contraseña.

- El sistema verifica los datos en la base de datos usuarios_restaurante.db.

- Si es válido, se muestra la ventana principal del sistema con su rol (admin o user).

2. **Gestión del Inventario (RestaurantInventorySystem)** 
   
- Una vez autenticado, el usuario puede:

- Visualizar el inventario completo (en un Treeview).

- Agregar, editar o eliminar productos del inventario.

- Filtrar productos por nombre o categoría.

- Registrar entradas o salidas de productos (actualización de stock).

- Ver alertas automáticas:

- Productos con stock bajo.

- Productos próximos a vencer.

- Generar y guardar reportes detallados del inventario.

- Cerrar sesión al terminar.

### Casos de uso clave 

| Nº | Caso de Uso                | Actor                | Descripción                                                                       |
| -- | -------------------------- | -------------------- | --------------------------------------------------------------------------------- |
| 1  | Iniciar sesión             | Usuario (admin/user) | El usuario se autentica con nombre y contraseña.                                  |
| 2  | Ver inventario             | Usuario              | Consulta todos los productos existentes en el inventario.                         |
| 3  | Agregar producto           | Admin                | Registra un nuevo producto con datos como cantidad, unidad, precio y vencimiento. |
| 4  | Editar producto            | Admin                | Modifica los datos de un producto existente.                                      |
| 5  | Eliminar producto          | Admin                | Borra un producto del inventario.                                                 |
| 6  | Registrar entrada o salida | Usuario/Admin        | Aumenta o disminuye el stock de un producto según el tipo de movimiento.          |
| 7  | Ver alertas                | Usuario/Admin        | Consulta productos con stock crítico o próximos a vencer.                         |
| 8  | Generar reporte            | Usuario/Admin        | Crea un reporte detallado del inventario y lo guarda como `.txt`.                 |
| 9  | Filtrar productos          | Usuario/Admin        | Busca productos por nombre o categoría.                                           |


------------


### Estructura de Módulos y paquetes

------------


### Tecnologías utilizadas 

Para el desarrollo del programa, fueron útile herramientas y librerías disponibles en Python. 


<img width="650" height="360" alt="Captura de pantalla 2025-07-20 165330" src="https://github.com/user-attachments/assets/83f12f36-8d51-4672-adec-b387071d4781" />



------------

## Explicación de métodos y atributos

### main() – Función de Entrada
<p>Esta función orquesta el flujo del programa:

- Llama al login.

- Si es exitoso, carga la ventana de inventario.

- Si no, termina el programa.



### Clase RestaurantInventorySystem
<p>Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Atributos 

- **root:** ventana principal Tkinter del inventario.

- **conn:** conexión a la base de datos inventario_restaurante.db.

- **cursor:** cursor para ejecutar SQL.  


#### Métodos 

- **__init__(root):** Inicializa todo: conecta a BD, crea interfaz, carga inventario.

- **setup_db():** Crea la tabla inventario si no existe.

- **create_ui():** Diseña visualmente la interfaz de gestión del inventario.

- **load_inventory():** Carga los productos existentes desde la base de datos y los muestra en la tabla principal.

- **filter_items():** Filtra productos por texto ingresado (por nombre o categoría).

- **add_product()**: Abre un formulario para añadir un producto nuevo.

- **edit_product():** Abre un formulario para modificar un producto seleccionado.

- **delete_product():** Elimina un producto seleccionado de la base de datos.

- **product_dialog(data):** Crea un formulario reutilizable para agregar o editar productos.

- **update_stock():** Permite actualizar la cantidad de un producto desde la interfaz.

- **get_stock_status(cantidad, stock_minimo):** Retorna el estado del stock: “Suficiente”, “Bajo” o “Crítico”.

- **update_stats():** Actualiza los valores estadísticos: número total, valor total, productos críticos.

- **show_alerts():** Muestra pestañas con productos de stock bajo y con fechas de vencimiento cercanas.

- **generate_report():** Muestra una ventana con un informe detallado del inventario (resumen, categorías, productos críticos, tabla general).

- **generate_report_content()**: Crea el texto del reporte, consultando la base de datos.

- **save_report(content):** Guarda el reporte generado como archivo .txt.

- **__del__():** Cierra conexión a base de datos al destruir el objeto.


### Clase InventoryAPI

<p>Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Atributos

- **conn:** conexión a la base de datos del inventario.

- **cursor:** cursor para ejecutar consultas SQL.

#### Métodos 

- **__init__(db_path):** Conecta con la base de datos.

- **agregar_producto(...):** Inserta un nuevo producto en la base de datos.

- **actualizar_stock(nombre, nueva_cantidad):** Cambia la cantidad actual de un producto por una nueva.

- **reducir_stock(nombre, cantidad_usar):** Disminuye la cantidad de un producto al ser utilizado. Valida que haya suficiente stock.

- **obtener_producto(nombre):** Devuelve todos los datos de un producto específico.

- **listar_productos_bajo_stock():** Lista todos los productos cuya cantidad es menor o igual al stock mínimo.

- **valor_total_inventario():** Calcula el valor total del inventario (precio unitario × cantidad por producto).

- **close():** Cierra la conexión a la base de datos.

### LoginSystem

#### Atributos

- **root:** ventana principal Tkinter del login.

- **conn:** conexión a la base de datos de usuarios usuarios_restaurante.db.

- **cursor:** cursor para ejecutar sentencias SQL.

- **username_var:** variable de texto vinculada al campo de usuario.

- **password_var:** variable de texto vinculada al campo de contraseña.

- **login_successful:** indica si el login fue exitoso (True o False).


#### Métodos

- **__init__():** Constructor. Inicializa ventana, conecta a la BD, y crea la interfaz.

- **center_window():** Centra la ventana de login en la pantalla.

- **init_user_database():** Crea la tabla usuarios si no existe. Agrega dos usuarios por defecto: admin (admin123) y user(user123).

- **hash_password(password: str):** Convierte la contraseña a un hash SHA-256. Evita guardar contraseñas en texto plano.

- **create_login_interface()**: Diseña visualmente la interfaz de login usando tkinter con estilos personalizados.

- **login():** Verifica si el usuario y la contraseña ingresados coinciden con los registros de la base de datos.

- **run()**: Inicia el mainloop() de Tkinter y espera el intento de login. Retorna True si fue exitoso.

- **get_user_info()**: Devuelve la información del usuario autenticado (id, nombre, rol).

- **__del__():** Cierra la conexión a la base de datos cuando se destruye el objeto.

























