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

### Funcionalidades principales

<img width="1083" height="422" alt="Captura de pantalla 2025-07-20 184901" src="https://github.com/user-attachments/assets/454c6808-f23c-4e3e-abd3-d05009ccc99e" /> 

**Función:**  Es el punto de entrada del sistema. Primero solicita autenticación con LoginSystem. Si las credenciales son válidas, lanza la GUI del inventario.

**Interfaz gráfica del login** 

<img width="487" height="294" alt="Captura de pantalla 2025-07-20 185412" src="https://github.com/user-attachments/assets/1c2b6ea9-1eed-4144-9a9c-ce8c7646d659" />  

**Función:** Este fragmento asegura que la tabla de usuarios exista. Además, crea usuarios por defecto (admin y user) con contraseñas hasheadas.

**Interfaz gráfica del inventario**

<img width="629" height="68" alt="Captura de pantalla 2025-07-20 185844" src="https://github.com/user-attachments/assets/89625a12-8e29-47da-b4e1-f6efa085e28a" /> 

**Función:** Permite visualizar alertas en tiempo real para controlar el inventario. Es una funcionalidad crítica de gestión.


**Generación de reportes**

<img width="314" height="55" alt="image" src="https://github.com/user-attachments/assets/ce27f430-95e1-44ca-b954-94baacb613b7" />

**Función:** Este método genera un reporte listo para ser guardado o impreso, mostrando una radiografía completa del estado del inventario.

**Función auxiliar** 

<img width="453" height="80" alt="Captura de pantalla 2025-07-20 190608" src="https://github.com/user-attachments/assets/251509ed-43c5-42e8-a7cb-7447cfc1e99c" />

**Función:** Función usada para proteger contraseñas. Se aplica al registrar o verificar un usuario.



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




