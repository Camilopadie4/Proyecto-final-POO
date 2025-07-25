# Sistema de inventario para un restaurante

### Presentación

**Curso:** Programación Orientada a Objetos

**Equipo:** PythUNAL

**Docente:** Felipe Gonzales  Roldan

**Integrantes:** Jhonyer Camilo Padilla Enríquez, Andres Camilo García Caicedo, Diego Alejandro Prieto Badillo 

------------


### ¿De qué trata este proyecto?

<p>Es un programa que implementa un sistema de inventario para gestionar un resturante o cualquier negocio pequeño de comida(heladería, cafetería , pizzría, etc.)desarrollado en Python con interfaz gráfica basada en Tkinter y persistencia de datos en SQLite.

<p>También incluye una API interna que facilita automatizaciones o futuras integraciones con otras aplicaciones, como sistemas POS o plataformas en línea.

------------


### Objetivo general

<p>El objetivo principal del programa es facilitar la administración eficiente de productos almacenados o en bodega, permitiendo llevar un control detallado del stock disponible, el estado de los productos, sus fechas de vencimiento, y otras variables clave para una operación organizada y segura.

-----------
  
### Objetivos específicos

- Implementar una interfaz gráfica intuitiva utilizando Tkinter, que facilite la interacción del usuario con las funcionalidades del sistema.

- Diseñar un módulo de autenticación de usuarios que controle el acceso al sistema mediante credenciales y roles (administrador y usuario).

- Crear mecanismos de alerta automática para identificar productos con stock crítico o próximos a vencerse.

- Generar reportes detallados del inventario que incluyan estadísticas clave y se puedan guardar en archivos para su consulta posterior.

- Aplicar principios de Programación Orientada a Objetos y estructuras modulares para asegurar la mantenibilidad, escalabilidad y reutilización del código.



-----------

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


<img width="1531" height="3843" alt="Mermaid Chart - Create complex, visual diagrams with text  A smarter way of creating diagrams -2025-07-21-171604" src="https://github.com/user-attachments/assets/6bba459e-9271-4b97-bafd-8788442a3f87" /> 




-----------

### Estructura general del sistema 

El sistema está compuesto por 2 clases principales. 

| Clase                       | Rol                                      | Interacción                        |
| --------------------------- | ---------------------------------------- | ---------------------------------- |
| `LoginSystem`               | Maneja el login y la autenticación       | Interfaz gráfica de ingreso        |
| `RestaurantInventorySystem` | Control de inventario (interfaz gráfica) | CRUD, alertas, reportes            |


------------

### Lógica general del sistema

#### Flujo completo

               +--------------------+
               |   LoginSystem      |
               |--------------------|
               | Interfaz de login  |
               | Valida credenciales|
               +---------+----------+
                         |
              Si login es exitoso
                         ↓
        +-----------------------------+
        | RestaurantInventorySystem   |
        |-----------------------------|
        | Interfaz de inventario      |
        | Ver/Agregar/Editar/Borrar   |
        | Reportes y alertas          |
        +-----------------------------+
       


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


### Tecnologías utilizadas 

Para el desarrollo del programa, fueron útile herramientas y librerías disponibles en Python. 


| **Librería**       | **Uso** |
|--------------------|---------|
| `sqlite3`          | Para la gestión de la base de datos SQLite, que almacena usuarios, productos e inventario. |
| `datetime`         | Para registrar fechas y horas, generar reportes con marcas de tiempo y verificar vencimientos. |
| `timedelta`        | Para calcular diferencias entre fechas (por ejemplo, productos que vencen en 7 días). |
| `hashlib`          | Para encriptar las contraseñas de los usuarios utilizando el algoritmo SHA-256. |
| `messagebox`       | Para mostrar mensajes emergentes al usuario (alertas, errores, confirmaciones, etc.). |





------------

## Explicación de métodos atributos del programa

### `main()` – Función de Entrada
<p>Esta función orquesta el flujo del programa:

- Llama al login.

- Si es exitoso, carga la ventana de inventario.

- Si no, termina el programa.



### `Clase RestaurantInventorySystem`
<p> Esta clase es el núcleo del sistema, gestiona la interfaz gráfica del usuario. Tambien Permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

**Funcionalidad:**

- Interfaz gráfica.

- CRUD completo: agregar, editar, eliminar productos.

- Búsqueda y filtrado.

- Alertas de stock y vencimientos.

- Reportes descargables.

#### Atributos 

- **`root`**: Constructor que Inicializa la interfaz principal, conecta a la base de datos y carga los productos existentes.

- **`conn`**: conexión a la base de datos `inventario_restaurante.db`.

- **`cursor`**: cursor para ejecutar sentencias SQL.
  
- **tabla**: Componente Treeview de Tkinter que muestra los productos en una tabla.
  
- **barra_busq**: Variable asociada al campo de búsqueda, permite filtrar en tiempo real.
  
- **total_stats**: Diccionario que contiene etiquetas para mostrar estadísticas clave.


#### Métodos 

| **Método**                                   | **Descripción**                                                                                                                               |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `__init__(self, root)`                       | Inicializa la clase con la ventana raíz (`root`). Establece conexión a la base de datos, configura la interfaz gráfica y carga el inventario. |
| `setup_db(self)`                             | Crea la tabla `inventario` si no existe en la base de datos `inventario_restaurante.db`.                                                      |
| `crear_interfaz(self)`                       | Diseña visualmente la interfaz gráfica de gestión del inventario usando Tkinter.                                                              |
| `cargar_datos(self)`                         | Carga los productos existentes desde la base de datos y los muestra en la tabla principal de la interfaz.                                     |
| `filtrar_items(self)`                        | Filtra y actualiza los productos visibles en la tabla con base en el texto ingresado (nombre o categoría).                                    |
| `agregar_producto(self)`                     | Abre un formulario para ingresar un nuevo producto al inventario. Inserta en base de datos.                                                   |
| `editar_producto(self)`                      | Abre un formulario para editar los datos del producto seleccionado en la tabla. Actualiza en la base de datos.                                |
| `eliminar_producto(self)`                    | Elimina el producto seleccionado en la tabla tanto de la interfaz como de la base de datos.                                                   |
| `formulario_producto(self, data=None)`       | Crea una ventana emergente reutilizable para agregar o editar un producto. Si recibe `data`, precarga los campos.                             |
| `actualizar_stock(self)`                     | Permite modificar la cantidad en stock de un producto seleccionado. Valida y guarda cambios en la base de datos.                              |
| `estado_stock(self, cantidad, stock_minimo)` | Devuelve un texto con el estado del stock: `"Suficiente"`, `"Bajo"` o `"Crítico"`, según la diferencia entre `cantidad` y `stock_minimo`.     |
| `actualizar_estadisticas(self)`              | Calcula y actualiza en pantalla: número total de productos, valor total del inventario, y cuántos productos tienen stock bajo.                |
| `alertas_FV(self)`                           | Muestra una ventana con dos pestañas: una con productos de stock bajo y otra con productos que vencen en 15 días o menos.                     |
| `generar_reporte(self)`                      | Abre una ventana con un informe textual del inventario: resumen, productos críticos, categorías y listado general.                            |
| `reporte_inventario(self)`                   | Genera el contenido del reporte del inventario como un texto largo, estructurado y completo.                                                  |
| `reporte_en_txt(self, content)`              | Guarda el contenido del reporte en un archivo `.txt` en el equipo del usuario.                                                                |
| `__del__(self)`                              | Destructor. Cierra la conexión con la base de datos al eliminar la instancia para liberar recursos.                                           |



### `Clase LoginSystem`

Gestiona el acceso al sistema. Tiene usuarios por defecto (admin y user) y protege las credenciales con hash SHA256

**Funcionalidades**

- Muestra una ventana gráfica de login con campos de usuario y contraseña.

- Conecta con una base de datos SQLite llamada usuarios_restaurante.db.

- Crea automáticamente dos usuarios si no existen:

- admin / admin123

- user / user123

- Protege las contraseñas usando hash SHA256.

- Si el login es exitoso, cierra la ventana y da acceso al inventario.

#### Atributos

- **`root`**: ventana principal Tkinter del login.

- **`conn`**: conexión a la base de datos de usuarios `usuarios_restaurante.db`.

- **`cursor`**: cursor para ejecutar sentencias SQL.

- **`username_var`**: variable de texto vinculada al campo de usuario.

- **`password_var`**: variable de texto vinculada al campo de contraseña.

- **`login_successful`**: indica si el login fue exitoso (`True` o `False`).
  
- **`self.user_id, self.username, self.user_role`**: Información del usuario autenticado (ID, nombre y rol).


#### Métodos

| Método                     | Descripción                                                                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `center_window()`          | Centra la ventana del sistema en la pantalla del usuario. Mejora la presentación visual.                                                               |
| `init_user_database()`     | Crea la base de datos de usuarios (si no existe), define su estructura y añade dos usuarios por defecto: un **administrador** y un **usuario normal**. |
| `hash_password(password)`  | Cifra la contraseña con `SHA-256` para mayor seguridad al almacenarla.                                                                                 |
| `create_login_interface()` | Crea la interfaz gráfica del login, incluyendo campos de entrada, títulos, botones y mensajes explicativos sobre usuarios predeterminados.             |
| `login()`                  | Lógica de autenticación: valida campos, compara credenciales con las de la base de datos y gestiona mensajes y estado del usuario autenticado.         |
| `run()`                    | Ejecuta el ciclo de eventos (`mainloop()`) de la interfaz y devuelve si el login fue exitoso o no.                                                     |
| `get_user_info()`          | Devuelve la información del usuario autenticado como un diccionario (`id`, `username`, `role`).                                                        |
| `__del__()`                | Método destructor: cierra la conexión con la base de datos al finalizar el programa para liberar recursos.                                             |

---------

### Conclusión 

El flujo de todo el sistema es sencillo pero efectivo:

- El usuario se autentica en el login.

- Accede a la interfaz principal.

- Puede realizar operaciones como agregar productos, editar, eliminar, filtrar.

- El sistema detecta automáticamente alertas de stock y vencimientos.  

- Se puede generar un reporte completo con un clic.

- Todo se guarda en una base de datos SQLite para persistencia.

















