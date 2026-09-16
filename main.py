from lib import quadrado, rectangulo
print("Projeto figuras")
print(quadrado.get_identificador())
lado=4
print(f"A área dum {quadrado.get_identificador()} de lado {lado} é:\
      {quadrado.get_area(lado)} e o perémetro é {quadrado.get_perimetro(lado)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"A área dum {rectangulo.get_identificador()} de base {base}\
      e altura {altura} é: {rectangulo.get_area(base, altura)} \
        e o perímetro é: {rectangulo.get_perimetro(base, altura)}")