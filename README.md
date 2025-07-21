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


<img width="1446" height="3840" alt="Mermaid Chart - Create complex, visual diagrams with text  A smarter way of creating diagrams -2025-07-21-013002" src="https://github.com/user-attachments/assets/36c37419-d2cc-4043-977f-e9350195cbb4" />




------------


### Estructura de Módulos y paquetes

------------


### Tecnologías utilizadas 

Para el desarrollo del programa, fueron útile herramientas y librerías disponibles en Python. 


<img width="650" height="360" alt="Captura de pantalla 2025-07-20 165330" src="https://github.com/user-attachments/assets/83f12f36-8d51-4672-adec-b387071d4781" />



------------

### Explicación del código


#### Clase RestaurantInventorySystem
Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).

#### Atributo principal
_ def __init__(self, root): 
**root** El constructor recibe root, que es la ventana principal de Tkinter (tk.Tk()).

#### Métodos 
- 

#### Clase InventoryAPI
Clase auxiliar que permite manipular el inventario de forma programática, útil para integraciones futuras (API REST, scripts automáticos, etc).
#### Atributos
#### Métodos 

### main() – Función de Entrada

Esta función orquesta el flujo del programa:

2. Llama al login.

3. Si es exitoso, carga la ventana de inventario.

4. Si no, termina el programa.



---------


#### LoginSystem



















