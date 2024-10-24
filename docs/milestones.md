# [ [M0] Milestone 0: Modelado del problema](https://github.com/lmchaves/OrganizarTaller/milestone/4)
- Hay que realizar un modelo inicial sobre el dominio del problema, explicado en las historias de usuario [HU1](https://github.com/lmchaves/OrganizarTaller/issues/4) y [HU2](https://github.com/lmchaves/OrganizarTaller/issues/5), incluyendo las entidades y las relaciones entre ellas, necesarias para conseguir el PMV.
- __Entregable__:
    - Código de las entidades definidas.
- __Viabilidad__:
Se considerará completado cuando el código refleje correctamente el dominio del problema descrito en las [HU1](https://github.com/lmchaves/OrganizarTaller/issues/4) y [HU2](https://github.com/lmchaves/OrganizarTaller/issues/5).

# [ [M1] Milestone 1: Implementación de la consulta de disponibilidad de piezas](https://github.com/lmchaves/OrganizarTaller/milestone/2)
- Implementar la funcionalidad que permita a Javier, el mecánico, consultar la disponibilidad de las piezas en el sistema. La información incluirá si la pieza está disponible en el taller local o si debe solicitarse desde otra sede, junto con tiempos estimados de entrega.

- __Entregable__:
    - Código con la funcionalidad de consulta de inventario para el mecánico.
- __Viabilidad__:
Se considerará completado cuando Javier pueda realizar consultas de piezas, recibir tiempos estimados de entrega, y los tests automáticos validen la funcionalidad implementada.

# [ [M2] Milestone 2:  Implementación de pedidos de piezas](https://github.com/lmchaves/OrganizarTaller/milestone/3)
- Implementar la lógica que permita gestionar las solicitudes de piezas entre las diferentes sedes, priorizando los factores de costos de transporte, tiempos estimados de entrega y la urgencia de las reparaciones.

- __Entregable__:
    - Algoritmo de optimización que seleccione la mejor sede para pedir la pieza necesaria, teniendo en cuenta los criterios de costos, tiempos de entrega.
    - Código de priorización que permita identificar las reparaciones más urgentes y asignar recursos de manera eficiente.

- __Viabilidad__:
Se considerará completado cuando el algoritmo de optimización asigne correctamente las piezas entre sedes, respetando los criterios de costos, tiempos y prioridades. 

