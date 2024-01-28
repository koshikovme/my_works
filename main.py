from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        """магический метод"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """магический метод"""
        return f"{self.x}, {self.y}"

    def __repr__(self) -> str:
        """магический метод"""
        return f"{self.x}, {self.y}"

    def __add__(self, another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"

    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return Point(result_x, result_y)

    def __eq__(self, another_point: Point) -> bool:
        return self.x == another_point.x and self.y == another_point.y


p1 = Point(10, 15)
p2 = Point(10, 15)

p3 = p2 - p1
print(p3)

print(p1 == p2)


class Complex:
    def __init__(self, real: int, img: int) -> None:
        self.real = real
        self.img = img

    def __add__(self, complex: Complex) -> Complex:
        return Complex(self.real + complex.real, self.img + complex.img)

    def __repr__(self) -> str:
        return (
            f"{self.real} {str(self.img)[0] if self.img < 0 else '+'} {abs(self.img)}j"
        )


compl = Complex(5, 7)
print(compl)

compl2 = Complex(-50, -50)

print(compl + compl2)
