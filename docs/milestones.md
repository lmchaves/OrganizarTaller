# [M0] Milestone 0: Modelado del problema
- __Objetivo__ : Analizar los diferentes HUs para crear un modelo que represente los elementos del dominio del problema, reflejando la estructura del taller automotriz y los procesos de gestión logística.
Este modelo debe definir claramente las clases que intervienen en el sistema, como Piezas, Inventario, Reparaciones, Sedes, Transporte, y Clientes. Cada clase deberá incluir sus características relevantes y los comportamientos necesarios.
- __Entregable__:
    - Código que refleje los elementos del dominio, incluyendo clases para Piezas, Inventario, Reparaciones, Sedes, Transporte, Clientes y cualquier otra clase necesaria.
    - El código también debe reflejar las relaciones entre estos elementos, como la interacción entre inventario y sedes, el flujo de piezas entre diferentes localidades, y cómo los tiempos de entrega y costos afectan la distribución de piezas.

- __Viabilidad__:
Se considerará completado cuando el modelado en código esté validado y represente correctamente las interacciones del dominio, y cuando los elementos estén listos para
ser utilizados en la implementación de la lógica de negocio.

# [M1] Milestone 1: Implementación de la consulta de disponibilidad de piezas
- __Objetivo__:
Implementar la funcionalidad que permita a Javier, el mecánico, consultar la disponibilidad de las piezas en el sistema. La información incluirá si la pieza está disponible en el taller local o si debe solicitarse desde otra sede, junto con tiempos estimados de entrega.

- __Entregable__:
    - Código con la funcionalidad de consulta de inventario para el mecánico.
- __Viabilidad__:
Se considerará completado cuando Javier pueda realizar consultas de piezas, recibir tiempos estimados de entrega, y los tests automáticos validen la funcionalidad implementada.

# [M2] Milestone 2:  Implementación de pedidos de piezas
- __Objetivo__:
Implementar la lógica que permita gestionar las solicitudes de piezas entre las diferentes sedes, priorizando los factores de costos de transporte, tiempos estimados de entrega y la urgencia de las reparaciones.

- __Entregable__:
    - Algoritmo de optimización que seleccione la mejor sede para enviar la pieza, teniendo en cuenta los criterios de costos, tiempos de entrega y la prioridad de la reparación.
    - Código de priorización que permita identificar las reparaciones más urgentes y asignar recursos de manera eficiente.

- __Viabilidad__:
Se considerará completado cuando el algoritmo de optimización asigne correctamente las piezas entre sedes, respetando los criterios de costos, tiempos y prioridades. 

