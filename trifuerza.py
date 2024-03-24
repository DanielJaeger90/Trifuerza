import turtle
import tkinter

def dibujar_triangulo(size):
    # Dibuja un triángulo equilátero de lado size
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def dibujar_trifuerza(n):
    # Calcula el tamaño del triángulo grande
    size = 2 * n - 1
    
    # Dibuja el triángulo grande
    dibujar_triangulo(size)
    
    # Mueve la tortuga a la posición para dibujar los triángulos pequeños
    turtle.penup()
    turtle.left(60)
    turtle.forward(size / 2)
    turtle.right(60)
    turtle.forward(size / 2)
    turtle.left(180)
    turtle.pendown()
    
    # Calcula el tamaño de los triángulos pequeños
    small_size = size // 2
    
    # Dibuja los triángulos pequeños
    for _ in range(2):
        dibujar_triangulo(small_size)
        turtle.penup()
        turtle.forward(small_size)
        turtle.pendown()
    
    # Muestra el dibujo
    turtle.done()

def main():
    try:
        n = int(input("Introduce el número de filas de los triángulos: "))
        if n <= 0:
            raise ValueError("El número de filas debe ser un entero positivo.")
        dibujar_trifuerza(n)
    except ValueError as e:
        print("Error:", e)
        print("Por favor, introduce un número entero positivo.")

if __name__ == "__main__":
    main()
