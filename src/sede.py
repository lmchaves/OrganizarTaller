from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2



@dataclass()
class Sede:
    """
    Representa una sede del taller, con información de ubicación y detalles del inventario de piezas.

    Atributos:
        nombre (str): Nombre de la sede.
        ubicacion_latitude (float): Latitud de la ubicación de la sede.
        ubicacion_longitude (float): Longitud de la ubicación de la sede.
        inventario (dict[Pieza, int]): Diccionario que mapea el nombre de la pieza pieza 
        (única fuente de verdad) su cantidad y el costo unitario.
    """
    nombre: str
    ubicacion_latitude: float
    ubicacion_longitude: float
    inventario: dict[str, tuple[int, float]]

    def __post_init__(self):
        if not isinstance(self.inventario, dict):
            raise ValueError("El inventario debe ser un diccionario.")

        if self.ubicacion_latitude < -90 or self.ubicacion_latitude > 90:
            raise ValueError("La latitud debe estar en el rango [-90, 90].")
        if self.ubicacion_longitude < -180 or self.ubicacion_longitude > 180:
            raise ValueError("La longitud debe estar en el rango [-180, 180].")

        for pieza, (cantidad, _) in self.inventario.items():
            if cantidad < 0:
                raise ValueError("Las cantidades de la pieza " + pieza + " en el inventario no pueden ser negativas.")   
            

    def get_inventario(self, pieza: str = None) -> dict | tuple:
        """
        Obtiene el inventario completo o la información de una pieza específica.

        Args:
            pieza (str): Nombre de la pieza para consultar (opcional).

        Returns:
            dict | tuple: Si `pieza` es None, devuelve el inventario completo como un diccionario.
                          Si se especifica `pieza`, devuelve una tupla con (cantidad, precio) o 
                          lanza un ValueError si la pieza no existe.
        """
        if pieza is None:
            return self.inventario
        elif pieza in self.inventario:
            return self.inventario[pieza]
        else:
            raise ValueError(f"La pieza '{pieza}' no está disponible en el inventario.")
          
        
    def añadir_piezas(self, piezas_requeridas: dict[str, int]):
        """
        Añade nuevas piezas al inventario o actualiza las cantidades si ya existen.

        Args:
            piezas_requeridas (dict[str, int]): Diccionario con las piezas requeridas y sus cantidades.
        """
        for pieza, cantidad in piezas_requeridas.items():
            if cantidad < 0:
                raise ValueError(f"La cantidad de la pieza {pieza} no puede ser negativa.")
            
            if pieza in self.inventario:
                cantidad_existente, costo_unitario = self.inventario[pieza]
                nueva_cantidad = cantidad_existente + cantidad
                self.inventario[pieza] = (nueva_cantidad, costo_unitario)
            else:
                costo_unitario = 0.0  
                self.inventario[pieza] = (cantidad, costo_unitario)
    
    
    def calcular_distancia(self, otra_sede: 'Sede') -> float:
        """
        Calcula la distancia entre la sede actual y otra sede utilizando la fórmula del haversine.

        Args:
            otra_sede (Sede): La otra sede.

        Returns:
            float: Distancia en kilómetros.
        """
        R = 6371.0  

        dlat = radians(otra_sede.ubicacion_latitude - self.ubicacion_latitude)
        dlon = radians(otra_sede.ubicacion_longitude - self.ubicacion_longitude)
        a = sin(dlat / 2) ** 2 + cos(radians(self.ubicacion_latitude)) * cos(radians(otra_sede.ubicacion_latitude)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distancia = R * c

        return distancia
    
    def tiene_pieza_disponible(self, pieza: str, cantidad_requerida: int) -> bool:
        """
        Verifica si la sede tiene una cantidad suficiente de una pieza específica.

        Args:
            pieza (str): Nombre de la pieza a verificar.
            cantidad_requerida (int): Cantidad requerida de la pieza.

        Returns:
            bool: True si la pieza está disponible en cantidad suficiente, False en caso contrario.
        """
        if pieza in self.inventario:
            cantidad_disponible, _ = self.inventario[pieza]
            return cantidad_disponible >= cantidad_requerida
        return False
    
    def calcular_costo_transporte(self, sede_destino) -> float:
        """
        Calcula el costo de transporte entre la sede actual y otra sede basado en la distancia.

        Args:
            sede_destino (Sede): La sede de destino a la que se enviarán las piezas.
            coste_km (float): Costo por kilómetro de transporte. Por defecto es 0.5.

        Returns:
            float: El costo de transporte calculado.
        """
        coste_km=0.5
        distancia = self.calcular_distancia(sede_destino)  
        return distancia * coste_km


def crear_inventario(dataframe, cantidad_fija):
    """
    Convierte un DataFrame de Excel en un diccionario de inventario.

    Args:
        dataframe (pd.DataFrame): DataFrame con las columnas 'Pieza' y 'Precio (€)'.
        cantidad_fija (int): Cantidad fija asignada a cada pieza.

    Returns:
        dict: Inventario con nombre de la pieza como clave y una tupla (cantidad, precio) como valor.
    """
    inventario = {}
    for _, row in dataframe.iterrows():
        pieza = row['Pieza']
        precio = row['Precio (€)']
        inventario[pieza] = (cantidad_fija, precio)
    return inventario

