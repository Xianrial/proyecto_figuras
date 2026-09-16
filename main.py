from lib import quadrado
print("Projeto figuras")
print(quadrado.get_identificador())
lado=4
print(f"A área dum {quadrado.get_identificador()} de lado {lado} é:"
    f"{quadrado.get_area(lado)} e o perémetro é {quadrado.get_perimetro(lado)}")