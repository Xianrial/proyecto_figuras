from lib import quadrado, triangulo, rectangulo
print("Projeto figuras")
print(quadrado.get_identificador())
lado=4
print(f"A área dum {quadrado.get_identificador()} de lado {lado} é:"
    f"{quadrado.get_area(lado)} e o perémetro é {quadrado.get_perimetro(lado)}")

base=4
altura=2
print(triangulo.get_identificador())
print(f"A área dum {triangulo.get_identificador()} de base\
      {base} e altura {altura} é: {triangulo.get_area(base, altura)} e o\
        perímetro é {triangulo.get_perimetro(base, altura)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"A área dum {rectangulo.get_identificador()} de base {base}\
      e altura {altura} é: {rectangulo.get_area(base, altura)} \
        e o perímetro é: {rectangulo.get_perimetro(base, altura)}")
