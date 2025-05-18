import math  #*Importamos math porque necesitamos calcular la pendiente en grados con math.atan() y math.degrees(). 

class Point:
    """Entidad geométrica abstracta que representa una ubicación en un espacio."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    """Representa una línea definida por dos puntos."""
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self):
        """Calcula la longitud de la línea usando la distancia euclidiana."""
        return ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) ** 0.5

    def compute_slope(self):
        """Calcula la pendiente de la línea en grados desde la horizontal."""
        if self.start.x == self.end.x:
            return None  # Línea vertical: pendiente indefinida
        radians = math.atan((self.end.y - self.start.y) / (self.end.x - self.start.x))
        return math.degrees(radians)  # Convertir de radianes a grados

    def compute_horizontal_cross(self):
        """Calcula el cruce con el eje X, si existe."""
        slope = self.compute_slope()
        if slope is None or self.start.y * self.end.y > 0:  # No cruza el eje X
            return None
        return -self.start.y / slope + self.start.x

    def compute_vertical_cross(self):
        """Calcula el cruce con el eje Y, si existe."""
        slope = self.compute_slope()
        if slope is None or self.start.x * self.end.x > 0:  # No cruza el eje Y
            return None
        return -self.start.x / slope + self.start.y

    def discretize_line(self, n: int):
        """Genera un arreglo de 'n' puntos equidistantes sobre la línea."""
        if n < 2:
            return [self.start, self.end]  # Si n < 2, solo devuelve los extremos

        step_x = (self.end.x - self.start.x) / (n - 1)
        step_y = (self.end.y - self.start.y) / (n - 1)
        points = [Point(self.start.x + i * step_x, self.start.y + i * step_y) for i in range(n)]
        return points

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"


class Rectangle:
    """Representa un rectángulo definido por cuatro líneas."""
    def __init__(self, line1: Line, line2: Line, line3: Line, line4: Line):
        self.lines = [line1, line2, line3, line4]

        # Definir puntos clave a partir de las líneas
        self.bottom_left = line1.start
        self.bottom_right = line1.end
        self.top_left = line3.start
        self.top_right = line3.end

        # Calcular dimensiones
        self.width = line1.compute_length()
        self.height = line3.compute_length()

        # Calcular centro
        self.center = Point((self.bottom_left.x + self.top_right.x) / 2,
                            (self.bottom_left.y + self.top_right.y) / 2)

    @classmethod
    def from_corners(cls, corner1: Point, corner2: Point):
        """Inicializa un rectángulo a partir de dos esquinas opuestas."""
        bottom_left = Point(min(corner1.x, corner2.x), min(corner1.y, corner2.y))
        top_right = Point(max(corner1.x, corner2.x), max(corner1.y, corner2.y))

        # Crear las cuatro líneas del rectángulo
        line1 = Line(bottom_left, Point(top_right.x, bottom_left.y))  # Línea inferior
        line2 = Line(Point(top_right.x, bottom_left.y), top_right)  # Línea derecha
        line3 = Line(Point(bottom_left.x, top_right.y), top_right)  # Línea superior
        line4 = Line(bottom_left, Point(bottom_left.x, top_right.y))  # Línea izquierda

        return cls(line1, line2, line3, line4)

    def compute_area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def compute_perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)

    def contains_point(self, point: Point):
        """Determina si un punto está dentro del rectángulo."""
        return (self.bottom_left.x <= point.x <= self.top_right.x) and \
               (self.bottom_left.y <= point.y <= self.top_right.y)

    def __repr__(self):
        return f"Rectangle(lines={self.lines}, center={self.center}, width={self.width}, height={self.height})"


class Square(Rectangle):
    """Representa un cuadrado basado en un rectángulo."""
    def __init__(self, bottom_left: Point, side_length: float):
        # Crear las cuatro líneas del cuadrado
        line1 = Line(bottom_left, Point(bottom_left.x + side_length, bottom_left.y))  # Inferior
        line2 = Line(Point(bottom_left.x + side_length, bottom_left.y), Point(bottom_left.x + side_length, bottom_left.y + side_length))  # Derecha
        line3 = Line(Point(bottom_left.x, bottom_left.y + side_length), Point(bottom_left.x + side_length, bottom_left.y + side_length))  # Superior
        line4 = Line(bottom_left, Point(bottom_left.x, bottom_left.y + side_length))  # Izquierda

        super().__init__(line1, line2, line3, line4)

    @classmethod
    def from_center(cls, center: Point, side_length: float):
        """Inicializa un cuadrado usando su centro."""
        bottom_left = Point(center.x - side_length / 2, center.y - side_length / 2)
        return cls(bottom_left, side_length)

    @classmethod
    def from_corners(cls, corner1: Point, corner2: Point):
        """Inicializa un cuadrado usando dos esquinas opuestas (asegurando lados iguales)."""
        side_length = min(abs(corner1.x - corner2.x), abs(corner1.y - corner2.y))
        bottom_left = Point(min(corner1.x, corner2.x), min(corner1.y, corner2.y))
        return cls(bottom_left, side_length)

    def __repr__(self):
        return f"Square(lines={self.lines}, center={self.center}, side={self.width})"
