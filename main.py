from lib import quadrado, triangulo, rectangulo, circunferencia
print("Projeto figuras")
print(quadrado.get_identificador())
lado=4
print(f"A área dum {quadrado.get_identificador()} de lado {lado} é:"
    f"{quadrado.get_area(lado)} e o perémetro é {quadrado.get_perimetro(lado)}")

base=4
altura=2
lado_a=2
lado_b=3
lado_c=3
print(triangulo.get_identificador())
print(f"A área dum {triangulo.get_identificador()} de base {base} e altura {altura} é: {triangulo.get_area(base, altura)} e o perímetro é {triangulo.get_perimetro(lado_a, lado_b, lado_c)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"A área dum {rectangulo.get_identificador()} de base {base} e altura {altura} é: {rectangulo.get_area(base, altura)} e o perímetro é: {rectangulo.get_perimetro(base, altura)}")

radio=3
print(f"A área dumha circunferencia de radio {radio} é: {circunferencia.get_area(radio)}")