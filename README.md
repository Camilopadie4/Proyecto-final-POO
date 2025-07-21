# Sistema de inventario para un restaurante

### Presentación

**Curso:** Programación Orientada a Objetos

**Grupo:** PythUNAL

**Docente:** Felipe Gonzales  Roldan

**Integrantes:** Jhonyer Camilo Padilla Enríquez, Andres Camilo, Diego   

------------


### ¿De qué trata este proyecto?

<p>Es un programa que implementa un sistema de inventario para gestionar un resturante o cualquier negocio pequeño de comida(heladería, cafetería , pizzría, etc.)desarrollado en Python con interfaz gráfica basada en Tkinter y persistencia de datos en SQLite.

<p>También incluye una API interna que facilita automatizaciones o futuras integraciones con otras aplicaciones, como sistemas POS o plataformas en línea.

------------



### Objetivo general

<p>El objetivo principal del programa es facilitar la administración eficiente de productos almacenados o en bodega, permitiendo llevar un control detallado del stock disponible, el estado de los productos, sus fechas de vencimiento, y otras variables clave para una operación organizada y segura.

### Justificación 
<p> Decidimos crear este programa con el ánimo de crear una herramienta útil y sencilla para manejar inventarios de bodegas pequeñas. Notamos que muchos negocios manejan su inventario a mano, lo que genera desorden, desperdicio y pérdidas, por ello, con este proyecto vimos la oportunidad de automatizar esos procesos y hacerlos más eficientes.  

### Objetivos específicos

- Implementar una interfaz gráfica intuitiva utilizando Tkinter, que facilite la interacción del usuario con las funcionalidades del sistema.

- Diseñar un módulo de autenticación de usuarios que controle el acceso al sistema mediante credenciales y roles (administrador y usuario).

- Crear mecanismos de alerta automática para identificar productos con stock crítico o próximos a vencerse.

- Generar reportes detallados del inventario que incluyan estadísticas clave y se puedan guardar en archivos para su consulta posterior.

- Aplicar principios de Programación Orientada a Objetos y estructuras modulares para asegurar la mantenibilidad, escalabilidad y reutilización del código.

- Permitir la integración futura con otros sistemas, mediante la creación de una API interna que facilite automatizaciones o comunicación externa.

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

1. **Inicio del sistema**

- Se ejecuta la función main().

- Se lanza el sistema de login (LoginSystem), donde el usuario debe autenticarse.

2. **Autenticación**

- Si el usuario y contraseña son válidos (verificados contra la base de datos usuarios_restaurante.db), se carga el sistema principal.

- Si falla, se muestra un mensaje de error y se cancela el acceso.

- Acceso al sistema de inventario (RestaurantInventorySystem)

- Se abre la ventana principal del inventario con el nombre del usuario autenticado.

- Se carga la base de datos inventario_restaurante.db.

- Se construye la interfaz completa (listado, botones, filtros, campos de entrada, reportes).

3. **Gestión del inventario**

<p> El usuario puede:

- Agregar, editar o eliminar productos.

- Actualizar el stock disponible.

- Filtrar productos por nombre o categoría.

- Ver alertas por productos con stock bajo o por vencer.

- Generar reportes completos.

- Acciones de backend con InventoryAPI

- Las operaciones internas (como calcular el valor total del inventario, reducir stock, etc.) son realizadas por InventoryAPI, que actúa como una capa lógica de acceso a datos.

4. **Cierre**

- Al salir, las conexiones a la base de datos se cierran correctamente.

- El sistema queda listo para una nueva sesión.

### Casos de uso clave 

| Nº | Caso de Uso                | Actor                | Descripción                                                                       |
| -- | -------------------------- | -------------------- | --------------------------------------------------------------------------------- |
| 1  | Iniciar sesión             | Usuario (admin/user) | El usuario se autentica con nombre y contraseña.                                  |
| 2  | Ver inventario             | Usuario              | Consulta todos los productos existentes en el inventario.                         |
| 3  | Agregar producto           | Admin/usuario        | Registra un nuevo producto con datos como cantidad, unidad, precio y vencimiento. |
| 4  | Editar producto            | Admin/us             | Modifica los datos de un producto existente.                                      |
| 5  | Eliminar producto          | Admin/us             | Borra un producto del inventario.                                                 |
| 6  | Registrar entrada o salida | Usuario/Admin        | Aumenta o disminuye el stock de un producto según el tipo de movimiento.          |
| 7  | Ver alertas                | Usuario/Admin        | Consulta productos con stock crítico o próximos a vencer.                         |
| 8  | Generar reporte            | Usuario/Admin        | Crea un reporte detallado del inventario y lo guarda como `.txt`.                 |
| 9  | Filtrar productos          | Usuario/Admin        | Busca productos por nombre o categoría.                                           |


------------


### Estructura de Módulos y paquetes

------------


### Tecnologías utilizadas 

Para el desarrollo del programa, fueron útile herramientas y librerías disponibles en Python. 


| **Librería**       | **Uso** |
|--------------------|---------|
| `tkinter`          | Para construir la interfaz gráfica del sistema (ventanas, botones, etiquetas, campos, etc.). |
| `ttk (Themed Tkinter)` | Para utilizar widgets estilizados como `Treeview`, `Notebook`, `Combobox` y `Frame`. |
| `sqlite3`          | Para la gestión de la base de datos SQLite, que almacena usuarios, productos e inventario. |
| `datetime`         | Para registrar fechas y horas, generar reportes con marcas de tiempo y verificar vencimientos. |
| `timedelta`        | Para calcular diferencias entre fechas (por ejemplo, productos que vencen en 7 días). |
| `hashlib`          | Para encriptar las contraseñas de los usuarios utilizando el algoritmo SHA-256. |
| `messagebox`       | Para mostrar mensajes emergentes al usuario (alertas, errores, confirmaciones, etc.). |
| `simpledialog`     | Para pedir datos sencillos al usuario mediante ventanas emergentes (como actualizar stock). |




------------

## Explicación de métodos atributos del programa

### main() – Función de Entrada
<p>Esta función orquesta el flujo del programa:

- Llama al login.

- Si es exitoso, carga la ventana de inventario.

- Si no, termina el programa.

<img width="404" height="341" alt="Captura de pantalla 2025-07-21 001849" src="https://github.com/user-attachments/assets/cedc9163-9fc6-40a7-982d-3fee2732d583" />

<p> Cuando se ejecuta con éxito, se despliega una ventana así 



### Clase RestaurantInventorySystem
<p>Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Atributos 

- **`root`**: ventana principal Tkinter del inventario.

- **`conn`**: conexión a la base de datos `inventario_restaurante.db`.

- **`cursor`**: cursor para ejecutar sentencias SQL.


#### Métodos 

| Método                                     | Descripción                                                          |
| ------------------------------------------ | -------------------------------------------------------------------- |
| `__init__(root: Tk)`                       | Inicializa la base de datos, interfaz y carga datos.                 |
| `setup_db()`                               | Crea la tabla del inventario si no existe.                           |
| `create_ui()`                              | Construye la interfaz gráfica (botones, entradas, tablas).           |
| `load_inventory()`                         | Carga los productos de la base de datos y los muestra.               |
| `filter_items()`                           | Filtra productos por nombre o categoría.                             |
| `add_product()`                            | Abre formulario para agregar un nuevo producto.                      |
| `edit_product()`                           | Abre formulario para editar un producto existente.                   |
| `delete_product()`                         | Elimina un producto seleccionado.                                    |
| `product_dialog(data)`                     | Crea un formulario para agregar/editar productos.                    |
| `update_stock()`                           | Permite actualizar la cantidad de un producto.                       |
| `get_stock_status(cantidad, stock_minimo)` | Retorna “Suficiente”, “Bajo” o “Crítico”.                            |
| `update_stats()`                           | Actualiza métricas de inventario (valor total, número de productos). |
| `show_alerts()`                            | Muestra productos con vencimiento cercano o bajo stock.              |
| `generate_report()`                        | Abre ventana con reporte detallado del inventario.                   |
| `generate_report_content()`                | Genera el contenido textual del reporte.                             |
| `save_report(content)`                     | Guarda el reporte como archivo `.txt`.                               |
| `__del__()`                                | Cierra la conexión a la base de datos.                               |




### Clase InventoryAPI

<p>Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Atributos

- **`conn`**: conexión a la base de datos del inventario.

- **`cursor`**: cursor para ejecutar consultas SQL.

#### Métodos 

| Método                                          | Descripción                                                          |
| ----------------------------------------------- | -------------------------------------------------------------------- |
| `__init__(db_path='inventario_restaurante.db')` | Inicializa la conexión con la base de datos.                         |
| `agregar_producto(...)`                         | Inserta un nuevo producto en la base de datos.                       |
| `actualizar_stock(nombre, nueva_cantidad)`      | Actualiza la cantidad de stock de un producto.                       |
| `reducir_stock(nombre, cantidad_usar)`          | Disminuye el stock tras usar producto. Valida existencia suficiente. |
| `obtener_producto(nombre)`                      | Devuelve todos los datos del producto especificado.                  |
| `listar_productos_bajo_stock()`                 | Lista productos con cantidad ≤ stock mínimo.                         |
| `valor_total_inventario()`                      | Calcula el valor total de todos los productos (cantidad × precio).   |
| `close()`                                       | Cierra la conexión a la base de datos.                               |




### LoginSystem

#### Atributos

- **`root`**: ventana principal Tkinter del login.

- **`conn`**: conexión a la base de datos de usuarios `usuarios_restaurante.db`.

- **`cursor`**: cursor para ejecutar sentencias SQL.

- **`username_var`**: variable de texto vinculada al campo de usuario.

- **`password_var`**: variable de texto vinculada al campo de contraseña.

- **`login_successful`**: indica si el login fue exitoso (`True` o `False`).


#### Métodos

| Método                         | Descripción                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------- |
| `__init__()`                   | Constructor. Inicializa ventana, base de datos e interfaz de login.                    |
| `center_window()`              | Centra la ventana en la pantalla.                                                      |
| `init_user_database()`         | Crea la tabla de usuarios si no existe. Agrega usuarios por defecto (`admin`, `user`). |
| `hash_password(password: str)` | Devuelve el hash SHA-256 de la contraseña.                                             |
| `create_login_interface()`     | Construye la interfaz visual del login con campos y botones.                           |
| `login()`                      | Valida credenciales ingresadas contra la base de datos.                                |
| `run()`                        | Ejecuta el bucle principal de Tkinter y retorna `True` si el login fue exitoso.        |
| `get_user_info()`              | Retorna un diccionario con el `id`, `username` y `role` del usuario autenticado.       |
| `__del__()`                    | Cierra la conexión a la base de datos al destruir el objeto.                           |






















