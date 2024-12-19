## Descripción del Problema
Un taller de coches con varias sedes en distintas ciudades de España está enfrentando problemas para gestionar de manera eficiente la distribución y disponibilidad de las piezas necesarias para las reparaciones. El taller necesita un sistema que no solo identifique qué sede tiene la pieza requerida, sino que también optimice el proceso considerando factores como:

- Costos de transporte entre sedes.
- Tiempos de entrega estimados de las piezas.
- Priorización de las reparaciones según la urgencia del cliente y la disponibilidad de las piezas.

Para ello, disponemos de los datos de costos de transporte y tiempos estimados de entrega entre las sedes, lo que nos permitirá optimizar estos procesos de manera eficiente y realizar pruebas sobre la mejora en la gestión del flujo de piezas.

## Clases Principales

### Sede.py
La clase **Sede** representa cada una de las sedes del taller, que pueden estar ubicadas en diferentes ciudades. Esta clase se encarga de gestionar la información relacionada con las sedes, como su ubicación, inventario de piezas disponibles y el transporte entre sedes. 

### Pedido.py
La clase **Pedido** es responsable de gestionar las solicitudes de piezas para reparaciones. Cada pedido incluye detalles sobre la pieza solicitada, la urgencia de la reparación y la sede en la que se realiza la solicitud.

## Comprobación
Para ver si la sintaxis es correcta ejcuta:
make check 

Y ejecuta make help para ver todas las opciones.

## Documentación adicional
- [Historias de usuario](./docs/user-stories.md)
- [Viajes de usuario](./docs/user-journeys.md)
- [Milestones](./docs/milestones.md)
- [Gestor Dependecias](./docs/gestor_dependencias.md)
- [Gestor Tareas](./docs/gestor_tareas.md) 


