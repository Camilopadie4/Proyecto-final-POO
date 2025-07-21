# Sistema de invenatrio para un restaurante

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

class LoginSystem:
    def __init__(self): 
    
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



---------

### Métodos clave de cada clase 

#### LoginSystem



**Función:**  Inicializa la ventana, configura estilo, base de datos y crea la interfaz gráfica.




**Función:** Crea y gestiona la base de datos de usuarios. Incluye usuarios por defecto.





      

**Función:** Verifica credenciales. Usa SHA-256 para comparar contraseñas.




**Función:** Retorna info del usuario autenticado para usarla en otras clases



#### RestaurantInventorySystem



**Función:** Inicia la interfaz principal, base de datos e inventario.

>

**Función:** Carga los datos desde la base de datos y los muestra en pantalla.





**Función:** CRUD completo. Usan formularios Tkinter para registrar/modificar productos.



**Función:** Muestra productos con bajo stock o por vencer.



**Función:** Genera reporte con resumen, categorías y valores.


#### InventoryAPI



**Función:** Inserta un nuevo producto en la BD.



**Función:** Cambia el valor del stock actual.



**Función:** Disminuye el stock cuando un producto se consume. Incluye validaciones.

<

**Función:** Devuelve lista de productos críticos.












