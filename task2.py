def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    if a == b == c:
        return "Равносторонний треугольник"
    elif a == b or a == c or b == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))

triangle_type = check_triangle(a, b, c)

if triangle_type:
    print("Треугольник существует.")
    print("Тип треугольника:", triangle_type)
else:
    print("Треугольник с такими сторонами не существует.")
