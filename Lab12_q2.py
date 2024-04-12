class LegacyRectangle:
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

class ModernShape:
    def __init__(self, area, perimeter) -> None:
        self.__area = area
        self.__perimeter = perimeter

    def get_area(self) -> int:
        return self.__area

    def get_perimeter(self) -> int:
        return self.__perimeter

class RectangleAdapter(ModernShape):
    def __init__(self, obj: LegacyRectangle) -> None:
        self.__obj = obj

    def get_area(self):
        return self.__obj.get_height() * self.__obj.get_width()

    def get_perimeter(self):
        return (self.__obj.get_height() + self.__obj.get_width()) * 2

class ShapeAdapter(LegacyRectangle):
    def __init__(self, obj: ModernShape) -> None:
        self.__obj = obj

    def get_height(self) -> float:
        return self.calculatation()[1] 
    
    def get_width(self) -> float:
        return self.calculatation()[0]
    
    def calculatation(self):
        area = self.__obj.get_area()
        perimeter = self.__obj.get_perimeter()
        with_cal_part = ((perimeter / 2) ** 2 - 4 * area) ** 0.5
        width = (perimeter / 2 - with_cal_part) / 2 
        height = area / width
        return height, width


class ShapeFactory:
    @staticmethod
    def get_shape() ->  ModernShape:
        return  RectangleAdapter(LegacyRectangle(10, 5))
    
    @staticmethod
    def get_height_width() ->  LegacyRectangle:
        return ShapeAdapter(ModernShape(50, 30))

def main():
    shape = ShapeFactory.get_shape()
    width_height = ShapeFactory.get_height_width()


    print(f"Area\t\t: {shape.get_area():.2f}")
    print(f"Perimeter\t: {shape.get_perimeter():.2f}")
    print(f"Height\t\t: {width_height.get_height():.2f}")
    print(f"Width\t\t: {width_height.get_width():.2f}")

if  __name__ == "__main__":
   main()