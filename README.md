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
### Funcionalidades principales

------------
### Explicación del código 

**Clase LoginSystem**


**Función:** Gestiona el proceso de autenticación de usuarios usando SHA-256 para validar contraseñas. Si las credenciales son correctas, guarda los datos del usuario y cierra la ventana del login.

-----------

**Clase RestaurantInventorySystem**


        
**Función:** Obtiene todos los productos desde SQLite y los muestra en la tabla principal de la interfaz gráfica. También determina el estado del stock (normal, bajo o crítico).
        
**Detección del estado del stock**


        
**Función:** Determina el estado del producto para generar alertas visuales. Cuando la cantidad está por debajo del mínimo o es igual, el estado es crítico. 

**Generación de reportes**


    
**Función:** Genera un reporte detallado del inventario, que incluye estadísticas generales, productos críticos, y una tabla con todos los productos.

-----------

**Clase InventoryAPI**


    
**Función:** Permite agregar productos desde otras interfaces o scripts usando esta API en lugar de la interfaz gráfica. Facilita integraciones externas.

**Función principal "main"**

# FUNCIÓN PRINCIPAL QUE INICIA EL SISTEMA




