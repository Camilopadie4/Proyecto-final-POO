<img width="592" height="339" alt="Captura de pantalla 2025-07-20 200519" src="https://github.com/user-attachments/assets/598e40fe-99cb-42cd-a0c2-cceb056735af" /># Sistema de inventario para un restaurante




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

#### Clase LoginSystem
Clase principal del sistema de inventario. Maneja toda la lógica y la interfaz de gestión de productos.

#### Clase RestaurantInventorySystem
Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Clase InventoryAPI
Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

### main() – Función de Entrada

Esta función orquesta el flujo del programa:

2. Llama al login.

3. Si es exitoso, carga la ventana de inventario.

4. Si no, termina el programa.

<img width="1087" height="455" alt="Captura de pantalla 2025-07-20 203715" src="https://github.com/user-attachments/assets/c08c3244-1540-4a4b-9266-b030c508eca6" />


---------

### Métodos clave de cada clase 

#### LoginSystem

<img width="205" height="46" alt="Captura de pantalla 2025-07-20 194307" src="https://github.com/user-attachments/assets/e590711c-04c9-455c-81b8-57e1d874f96b" />

**Función:**  Inicializa la ventana, configura estilo, base de datos y crea la interfaz gráfica.


<img width="242" height="36" alt="Captura de pantalla 2025-07-20 194346" src="https://github.com/user-attachments/assets/be164605-a89f-49af-b9c8-0ab5e93d6a1b" />

**Función:** Crea y gestiona la base de datos de usuarios. Incluye usuarios por defecto.

<img width="634" height="398" alt="Captura de pantalla 2025-07-20 200459" src="https://github.com/user-attachments/assets/c0bfe444-56f9-4805-b8bc-21800c7d9533" />  


<img width="592" height="339" alt="Captura de pantalla 2025-07-20 200519" src="https://github.com/user-attachments/assets/3bfa8128-bbb2-40ce-b00a-79eb3c3e0313" />
      

**Función:** Verifica credenciales. Usa SHA-256 para comparar contraseñas.


<img width="421" height="192" alt="Captura de pantalla 2025-07-20 194627" src="https://github.com/user-attachments/assets/817d29f6-54c3-42f3-a7cf-d279231c4bc0" />

**Función:** Retorna info del usuario autenticado para usarla en otras clases



#### RestaurantInventorySystem

<img width="269" height="36" alt="Captura de pantalla 2025-07-20 192446" src="https://github.com/user-attachments/assets/43a70fc3-0779-44c1-96bc-d545343f9209" />

**Función:** Inicia la interfaz principal, base de datos e inventario.

<img width="577" height="283" alt="Captura de pantalla 2025-07-20 194827" src="https://github.com/user-attachments/assets/5c5cdb8b-115f-4f92-8aaf-56c3607b8b9a" />

**Función:** Carga los datos desde la base de datos y los muestra en pantalla.

<img width="267" height="72" alt="Captura de pantalla 2025-07-20 194953" src="https://github.com/user-attachments/assets/6a4f4a96-620c-44d8-aaf8-473a08783283" />

<img width="662" height="300" alt="Captura de pantalla 2025-07-20 195001" src="https://github.com/user-attachments/assets/c9d7cc58-4a15-4514-988a-135e7e334823" />

<img width="691" height="318" alt="Captura de pantalla 2025-07-20 195013" src="https://github.com/user-attachments/assets/7ba75805-fa8c-410d-8f68-327df92ed9d6" />

**Función:** CRUD completo. Usan formularios Tkinter para registrar/modificar productos.

<img width="392" height="129" alt="image" src="https://github.com/user-attachments/assets/22a43249-c74f-44f1-8c81-428b8c29c71e" />

**Función:** Muestra productos con bajo stock o por vencer.

<img width="314" height="55" alt="Captura de pantalla 2025-07-20 190325" src="https://github.com/user-attachments/assets/0b65fe35-6ee7-43f9-a15f-d5a723c68720" />

**Función:** Genera reporte con resumen, categorías y valores.


#### InventoryAPI

<img width="267" height="72" alt="Captura de pantalla 2025-07-20 194953" src="https://github.com/user-attachments/assets/1161f3b9-343e-40e8-8784-97e9ee87d67d" />

**Función:** Inserta un nuevo producto en la BD.

<img width="610" height="290" alt="Captura de pantalla 2025-07-20 195541" src="https://github.com/user-attachments/assets/8ca0ecbe-23a6-41c4-a70e-b6014635e6b4" />

**Función:** Cambia el valor del stock actual.

<img width="434" height="51" alt="image" src="https://github.com/user-attachments/assets/1f7711f7-c790-4528-b550-82893a01fe4d" />

**Función:** Disminuye el stock cuando un producto se consume. Incluye validaciones.

<img width="354" height="58" alt="Captura de pantalla 2025-07-20 203420" src="https://github.com/user-attachments/assets/014ff616-10d2-402c-b7ce-1a3502a45210" />

**Función:** Devuelve lista de productos críticos.












