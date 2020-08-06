import math
import time

version = "Alpha 7.0"


def main():
    print("\n\n\n")
    print("\t _____                             _      _                 ")
    time.sleep(0.3)
    print("\t/  __ \                           (_)    (_)                ")
    time.sleep(0.3)
    print("\t| /  \/ ___  _ __   ___ _ __ _ __  _  ___ _ _   _ _ __ ___  ")
    time.sleep(0.3)
    print("\t| |    / _ \| '_ \ / _ \ '__| '_ \| |/ __| | | | | '_ ` _ \ ")
    time.sleep(0.3)
    print("\t| \__/\ (_) | |_) |  __/ |  | | | | | (__| | |_| | | | | | |")
    time.sleep(0.3)
    print("\t \____/\___/| .__/ \___|_|  |_| |_|_|\___|_|\__,_|_| |_| |_|")
    time.sleep(0.3)
    print("\t            | |                                             ")
    time.sleep(1)
    print("\nBienvenido al programa. A continuación, escoja la opción que estime conveniente.")
    print("\t1 - Polígonos (2D)")
    print("\t2 - Poliedros (3D)")
    print("\t3 - Créditos")
    print("\t4 - Salir")
    opcion = int(input("Opción: "))

    # Figuras 2D
    if opcion == 1:
        def fig_2d():
            print("\nSeleccione un polígono.")
            print("1 - Cuadriláteros")
            print("2 - Circunferencia")
            print("3 - Triángulo")
            print("4 - Pentágono")
            print("5 - Volver al menú principal")
            option = int(input("Opción: "))

            # Cuadriláteros
            if option == 1:
                def cuadrilateros():
                    print("\nSeleccione una figura:")
                    print("1 - Cuadrado")
                    print("2 - Rectángulo")
                    print("3 - Rombo")
                    print("4 - Romboide")
                    print("5 - Trapecio")
                    print("6 - Trapezoide")
                    print("7 - Escoger otro polígono")
                    option = int(input("Opción: "))

                    # Cuadrado
                    if option == 1:
                        print("\nSeleccione aspecto a calcular.")
                        print("1 - Área")
                        print("2 - Perímetro")
                        print("3 - Diagonal")
                        print("4 - Escoger otro cuadrilátero")
                        option = int(input("Opción: "))

                        # Área de un cuadrado
                        if option == 1:
                            lado = float(input("Ingrese la medida de uno de sus lados: "))
                            area_sq = lado ** 2
                            if lado <= 0:
                                print("\nError: El lado alberga un valor negativo o igual a cero.")
                                time.sleep(2)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(1)
                                fig_2d()
                            else:
                                print(f"\nLa medida del área de este cuadrado es de {area_sq} unidades cuadradas.")
                                time.sleep(4)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Perímetro de un cuadrado
                        elif option == 2:
                            lado = float(input("Ingrese la medida de uno de sus lados: "))
                            perim_sq = lado * 4
                            if lado <= 0:
                                print("\nError: El lado alberga un valor negativo o igual a cero.")
                                time.sleep(3)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                            else:
                                print(f"\nEl perímetro de este cuadrado es de {perim_sq} unidades.")
                                time.sleep(4)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Diagonal de un cuadrado
                        elif option == 3:
                            lado = float(input("Ingrese la medida de uno de sus lados: "))
                            diag_sq = ((lado ** 2) + (lado ** 2))
                            diag_sq_final = (math.sqrt(diag_sq))
                            if lado <= 0:
                                print("\nError: El valor ingresado no puede tener valor negativo o igual a cero.")
                                time.sleep(3)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"\nLa diagonal de este cuadrado es de {diag_sq_final:.2f} unidades.")
                                time.sleep(4)
                                print("Volviendo al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Escoger otro cuadrilátero
                        elif option == 4:
                            cuadrilateros()

                        # Otro valor
                        else:
                            print("\nError: Operación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                    # Rectángulo
                    elif option == 2:
                        print("\nSeleccione aspecto a calcular.")
                        print("1 - Área")
                        print("2 - Perímetro")
                        print("3 - Diagonal")
                        print("4 - Escoger otro cuadrilátero")
                        option = int(input("Opción: "))

                        # Área de un rectángulo
                        if option == 1:
                            print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                            time.sleep(0.5)
                            ancho = float(input("\nAncho: "))
                            largo = float(input("Largo: "))
                            area_rect = ancho * largo
                            print(f"\nEl área de este rectángulo es de {area_rect} unidades cuadradas.")
                            time.sleep(4)
                            print("Volviendo al menú de polígonos...")
                            time.sleep(2)
                            fig_2d()

                        # Perímetro de un rectángulo
                        elif option == 2:
                            print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                            ancho = float(input("Ancho: "))
                            largo = float(input("Largo: "))
                            perim_rect = (ancho * 2) + (largo * 2)
                            print(f"\nEl perímetro de este rectángulo es de {perim_rect} unidades.")
                            time.sleep(4)
                            print("Volviendo al menú de polígonos...")
                            time.sleep(2)
                            fig_2d()

                        # Diagonal de un rectángulo
                        elif option == 3:
                            print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                            ancho = float(input("Ancho: "))
                            largo = float(input("Largo: "))
                            diag_rect = ((ancho ** 2) + (largo ** 2))
                            diag_rect_final = (math.sqrt(diag_rect))
                            print(f"\nLa diagonal aproximada de este rectángulo es de {diag_rect_final:.2f} unidades.")
                            time.sleep(4)
                            print("Volviendo al menú de polígonos...")
                            time.sleep(2)
                            fig_2d()

                        # Escoger otro cuadrilátero
                        elif option == 4:
                            cuadrilateros()

                        # Otro valor
                        else:
                            print("\nError: Operación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                    # Rombo
                    elif option == 3:
                        print("\nSeleccione aspecto a calcular.")
                        print("1 - Área")
                        print("2 - Perímetro")
                        print("3 - Escoger otro cuadrilátero")
                        option = int(input("Opción: "))

                        # Área de un rombo
                        if option == 1:
                            D = float(input("\nIngrese el valor de la diagonal mayor: "))
                            d = float(input("Ingrese el valor de la diagonal menor: "))
                            area_romb = (D * d) / 2
                            if D > 0 and d > 0:
                                print(f"\nEl área del rombo es de {area_romb:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print("\nError: Los valores ingresados no pueden albergar números negativos o iguales a"
                                      " cero.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Perímetro de un rombo
                        elif option == 2:
                            D = float(input("\nIngrese el valor de la diagonal mayor: "))
                            d = float(input("Ingrese el valor de la diagonal menor: "))
                            perim_romb = 2 * (math.sqrt((D ** 2) + (d ** 2)))
                            if D > 0 and d > 0:
                                print(f"\nEl perímetro de este rombo es de {perim_romb:.2f} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print("\nError: Los valores ingresados no pueden albergar números negativos o iguales a"
                                      " cero.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Escoger otra figura
                        elif option == 3:
                            cuadrilateros()

                        # Otro valor
                        else:
                            print("\nError: Operación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                    # Romboide
                    elif option == 4:
                        print("\nSeleccione aspecto a calcular.")
                        print("1 - Área")
                        print("2 - Perímetro")
                        print("3 - Escoger otro cuadrilátero")
                        option = int(input("Opción: "))

                        # Área de un romboide
                        if option == 1:
                            b = float(input("\nIngrese el valor del lado que actúa como base: "))
                            h = float(input("Ingrese el valor de la altura relativa: "))
                            area_romboid = b * h
                            if b <= 0 or h <= 0:
                                print("\nError: Los valores ingresados albergan números negativos o iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"\nEl área del romboide es de {area_romboid:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Perímetro de un romboide
                        elif option == 2:
                            a = float(input("\nIngrese la medida de un lado: "))
                            b = float(input("Ingrese la medida del otro lado: "))
                            perim_romboid = 2 * (a + b)
                            if a <= 0 or b <= 0:
                                print("\nError: Los valores ingresados albergan números negativos o iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"\nEl perímetro del romboide es de {perim_romboid:.2f} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de polígonos...")
                                time.sleep(2)
                                fig_2d()

                        # Escoger otra figura
                        elif option == 3:
                            cuadrilateros()

                        # Otro valor
                        else:
                            print("\nError: Operación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                    # Trapecio
                    elif option == 5:
                        print("\nEn construcción...")
                        time.sleep(2)
                        main()

                    # Trapezoide
                    elif option == 6:
                        print("\nEn construcción...")
                        time.sleep(2)
                        main()

                    # Escoger otro polígono
                    elif option == 7:
                        fig_2d()

                    # Otro valor
                    else:
                        print("\nError: Operación incorrecta.")
                        time.sleep(2)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                cuadrilateros()

            # Circunferencia
            elif option == 2:
                print("\nSeleccione aspecto a calcular.")
                print("1 - Área")
                print("2 - Perímetro")
                print("3 - Diámetro")
                print("4 - Escoger otra figura")
                option = int(input("Opción: "))

                # Área de la circunferencia
                if option == 1:
                    print("\nA continuación ingrese la medida del radio del círculo.")
                    radio = float(input("Radio: "))
                    area_cir = math.pi * (radio ** 2)
                    print(f"\nLa medida del área del círculo es de {area_cir:.3f} unidades cuadradas.")
                    print(f"Con π como incógnita: {radio ** 2}π unidades cuadradas.")
                    time.sleep(3)
                    print("Volviendo al menú de polígonos...")
                    time.sleep(2)
                    fig_2d()

                # Perímetro de la circunferencia
                elif option == 2:
                    print("\nA continuación ingrese la medida del radio del círculo.")
                    radio = float(input("Radio: "))
                    perim_circ = 2 * radio * math.pi
                    print(f"\nEl perímetro del círculo es de {perim_circ:.3f} unidades.")
                    print(f"Con π como incógnita: {(2 * radio)}π unidades.")
                    time.sleep(2)
                    print("Volviendo al menú de polígonos...")
                    time.sleep(2)
                    fig_2d()

                # Diámetro de la circunferencia
                elif option == 3:
                    print("\nA continuación ingrese la medidad del radio del círculo.")
                    radio = float(input("Radio: "))
                    print(f"\nEl diámetro del círculo es de {2 * radio} unidades.")
                    time.sleep(2)
                    print("Volviendo al menú de polígonos...")
                    time.sleep(2)
                    fig_2d()

                # Escoger otra figura
                elif option == 4:
                    fig_2d()

                # Operación no definida
                else:
                    print("\nError: Operación incorrecta.")
                    time.sleep(1)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Triángulo
            elif option == 3:
                def triangulos():
                    print("\nSeleccione la clasificación a trabajar.")
                    print("1 - Medida de sus lados")
                    print("2 - Amplitud de sus ángulos")
                    print("3 - Trigonometría (Uso de lados y ángulos)")
                    print("4 - Obtener ángulos")
                    print("5 - Escoger otra figura")
                    option = int(input("Clasificación: "))

                    # Triángulos por medida de sus lados
                    if option == 1:
                        print("\nSeleccione el tríangulo.")
                        print("1 - Equilátero")
                        print("2 - Isóceles")
                        print("3 - Escaleno")
                        option = int(input("Clasificación: "))

                        # Triángulo Equilátero
                        if option == 1:
                            print("\nSeleccione aspecto a calcular.")
                            print("1 - Área")
                            print("2 - Perímetro")
                            print("3 - Altura")
                            option = int(input("Opción: "))

                            # Área del triángulo equilátero
                            if option == 1:
                                lado = float(input("\nIngrese la medida del lado del triángulo: "))
                                area_tr_eq = (math.sqrt(3) / 4) * (lado ** 2)
                                print(f"\nEl área del triángulo es de {area_tr_eq:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Perímetro del triángulo equilátero
                            elif option == 2:
                                lado = float(input("\nIngrese la medida del lado del triángulo: "))
                                print(f"\nEl perímetro del triángulo es de {lado * 3} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Diagonal del triángulo equilatero
                            elif option == 3:
                                lado = float(input("\nIngrese la medida del lado del triángulo: "))
                                h_tr_eq = (math.sqrt(3) * lado) / 2
                                print(f"\nLa altura del triángulo es de {h_tr_eq:.2f} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Otro
                            else:
                                print("\nError: Operación incorrecta.")
                                time.sleep(1)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()

                        # Triángulo Isóceles
                        elif option == 2:
                            print("\nSeleccione aspecto a calcular.")
                            print("1 - Área")
                            print("2 - Perímetro")
                            print("3 - Altura")
                            option = int(input("Opción: "))

                            # Área de un triángulo isóceles
                            if option == 1:
                                lado1 = float(input("\nIngrese la medida de los lados iguales: "))
                                lado2 = float(input("Ingrese la medida de la base: "))
                                if lado1 * 2 <= lado2:
                                    print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                    alt_tr_is = math.sqrt(equation_h)
                                    area_tr_is = (lado2 * alt_tr_is) / 2
                                    print(
                                        f"\nEl área del triángulo isóceles es de {area_tr_is:.2f} unidades cuadradas.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Perímetro de un triángulo isóceles
                            elif option == 2:
                                lado1 = float(input("\nIngrese la medida de los lados iguales: "))
                                lado2 = float(input("Ingrese la medida del lado diferente: "))
                                if lado1 * 2 <= lado2:
                                    print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(
                                        f"\nEl perímetro de este triángulo isóceles es de {lado1 * 2 + lado2} unidades.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Altura de un triángulo isóceles
                            elif option == 3:
                                lado1 = float(input("\nIngrese la medida de los lados iguales: "))
                                lado2 = float(input("Ingrese la medida del lado diferente: "))
                                if lado1 * 2 <= lado2:
                                    print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                    alt_tr_is = math.sqrt(equation_h)
                                    print(f"\nLa altura del triángulo isóceles es de {alt_tr_is:.2f} unidades.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                            else:
                                print("\nError: Operación incorrecta.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()

                        # Triángulo Escaleno
                        elif option == 3:
                            print("\nSeleccione aspecto a calcular.")
                            print("1 - Área")
                            print("2 - Perímetro")
                            print("3 - Alturas")
                            option = int(input("Opción: "))

                            # Área de un triángulo escaleno
                            if option == 1:
                                lado1 = float(input("\nIngrese la medida del primer lado: "))
                                lado2 = float(input("Ingrese la medida del segundo lado: "))
                                lado3 = float(input("Ingrese la medida del tercer lado: "))
                                s_perim = (lado1 + lado2 + lado3) / 2
                                form_heron_sq = s_perim * (s_perim - lado1) * (s_perim - lado2) * (s_perim - lado3)
                                form_heron = math.sqrt(form_heron_sq)
                                if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                                    print(
                                        "\nError: El triángulo debe tener como valor en sus lados números mayores a 0.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 == lado2 and lado1 == lado3:
                                    print("\nError: Los tres lados ingresados son de igual valor.")
                                    print("El triángulo es equilátero.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                    print("\nLos valores ingresados no cumplen con la desigualdad triangular.")
                                    time.sleep(2)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(f"\nEl área de este triángulo escaleno es de {form_heron:.2f} unidades"
                                          f" cuadradas.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Perímetro de un triángulo escaleno
                            if option == 2:
                                lado1 = float(input("\nIngrese la medida del primer lado: "))
                                lado2 = float(input("Ingrese la medida del segundo lado: "))
                                lado3 = float(input("Ingrese la medida del tercer lado: "))
                                perim_tr_esc = lado1 + lado2 + lado3
                                if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                                    print(
                                        "\nError: El triángulo debe tener como valor en sus lados números mayores a 0.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 == lado2 and lado1 == lado3:
                                    print("\nError: Los tres lados ingresados son de igual valor.")
                                    print("El triángulo es equilatero.")
                                    print(
                                        f"\nEl perímetro de este triángulo equilátero es de {perim_tr_esc:.2f} unidades.")
                                    time.sleep(5)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 == lado2 or lado2 == lado1:
                                    print(
                                        "\nError: Lado 1 y Lado 2 comparten el mismo valor. El triángulo es isóceles.")
                                    print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                    time.sleep(5)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado2 == lado3 or lado3 == lado2:
                                    print(
                                        "\nError: Lado 2 y Lado 3 comparten el mismo valor. El triángulo es isóceles.")
                                    print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                    time.sleep(5)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 == lado3 or lado3 == lado1:
                                    print(
                                        "\nError: Lado 1 y Lado 3 comparten el mismo valor. El triángulo es isóceles.")
                                    print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                    time.sleep(5)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                    print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(
                                        f"\nEl perímetro de este triángulo escaleno es de {perim_tr_esc:.2f} unidades.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            #  Alturas de un triángulo escaleno
                            if option == 3:
                                lado1 = float(input("\nIngrese la medida del primer lado: "))
                                lado2 = float(input("Ingrese la medida del segundo lado: "))
                                lado3 = float(input("Ingrese la medida del tercer lado: "))
                                s_perim = (lado1 + lado2 + lado3) / 2
                                form_heron_sq = s_perim * (s_perim - lado1) * (s_perim - lado2) * (s_perim - lado3)
                                form_heron = math.sqrt(form_heron_sq)
                                ha = (2 / lado1) * form_heron
                                hb = (2 / lado2) * form_heron
                                hc = (2 / lado3) * form_heron
                                if ha <= 0 or hb <= 0 or hc <= 0:
                                    print("\nError: Los valores de las alturas son negativos o iguales a cero.")
                                    print("El triángulo no existe.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(f"\nLas alturas del triángulo son de {ha:.2f} unidades, {hb:.2f}"
                                          f" unidades y {hc:.2f} unidades respectivamente.")
                                    print("Estos valores se encuentran aproximados a la centésima.")
                                    time.sleep(6)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(3)
                                    triangulos()

                    # Triángulos por amplitud de sus ángulos
                    elif option == 2:
                        print("\nSeleccione el tríangulo.")
                        print("1 - Rectángulo")
                        option = int(input("Opción: "))

                        # Triángulo Rectángulo
                        if option == 1:
                            print("\nSeleccione aspecto a calcular.")
                            print("1 - Área")
                            print("2 - Perímetro")
                            print("3 - Hipotenusa por medio de Pitágoras")
                            print("4 - Cateto faltante por medio de Pitágoras")
                            option = int(input("Opción: "))

                            # Área de un triángulo rectángulo
                            if option == 1:
                                cat1 = float(input("\nIngrese la medida de un cateto: "))
                                cat2 = float(input("Ingrese la medida del otro cateto: "))
                                area_tr_rec = (cat1 + cat2) / 2
                                print(f"\nEl área del triángulo es de {area_tr_rec:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Perímetro de un triángulo rectángulo
                            elif option == 2:
                                cat1 = float(input("\nIngrese la medida de un cateto: "))
                                cat2 = float(input("Ingrese la medida del otro cateto: "))
                                hip = float(input("Ingrese la medida de la hipotenusa: "))
                                perim_tr_rect = cat1 + cat2 + hip
                                print(f"\nEl perímetro del triángulo es de {perim_tr_rect} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Hipotenusa del triángulo rectángulo
                            elif option == 3:
                                cat1 = float(input("\nIngrese la medida de un cateto: "))
                                cat2 = float(input("Ingrese la medida del otro cateto: "))
                                hip_sq = (cat1 ** 2) + (cat2 ** 2)
                                hip = math.sqrt(hip_sq)
                                print(f"\nLa hipotenusa de este triángulo tiene un valor de {hip} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Medida de un cateto del triángulo rectángulo por medio de la hipotenusa y el otro cateto
                            elif option == 4:
                                cat1 = float(input("\nIngrese la medida del cateto: "))
                                hip = float(input("Ingrese la medida de la hipotenusa: "))
                                x = hip ** 2 - cat1 ** 2
                                cat2 = math.sqrt(x)
                                print(f"\nLa medida del cateto faltante es de {cat2:.2f} unidades.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Operación no reconocida
                            else:
                                print("\nOperación incorrecta.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()

                        # Operación no reconocida
                        else:
                            print("\nOperación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                    # Trigonometría (Uso de lados y ángulos)
                    elif option == 3:
                        print("\nEstos problemas se realizan exclusivamente con triángulos rectángulos.")
                        print("Es decir, aquellos triángulos que poseen un ángulo de 90 grados en su interior.")
                        time.sleep(4)
                        print("¡OJO! Por el momento, los resultados se entregan en radianes.")
                        time.sleep(4)
                        print("\nA continuación, escoja una función trigonométrica:")
                        time.sleep(1.5)
                        print("1 - Seno")
                        print("2 - Coseno")
                        print("3 - Tangente")
                        print("4 - Cosecante")
                        print("5 - Secante")
                        print("6 - Cotangente")
                        print("7 - Volver al menú de triángulos")
                        option = int(input("Opción: "))

                        # Seno
                        if option == 1:
                            co = float(input("\nIngrese el valor del cateto opuesto: "))
                            hip = int(input("Ingrese el valor de la hipotenusa: "))
                            sin = co / hip
                            sin_f = math.sin(sin)
                            print(f"\nEl valor del seno es de {sin_f:.5f} radianes.")
                            time.sleep(3)
                            print("Regresando al menú de triángulos...")
                            time.sleep(2)
                            triangulos()

                        # Coseno
                        elif option == 2:
                            ca = float(input("\nIngrese el valor del cateto adyacente: "))
                            hip = float(input("Ingrese el valor de la hipotenusa: "))
                            cos = ca / hip
                            cos_f = math.cos(cos)
                            print(f"\nEl valor del coseno es de {cos_f:.5f} radianes.")
                            time.sleep(3)
                            print("Regresando al menú de triángulos...")
                            time.sleep(2)
                            triangulos()

                        # Tangente
                        elif option == 3:
                            co = float(input("\nIngrese el valor del cateto opuesto: "))
                            ca = float(input("Ingrese el valor del cateto adyacente: "))
                            tan = co / ca
                            tan_f = math.tan(tan)
                            print(f"\nEl valor de la tangente es de {tan_f:.5f} radianes.")
                            time.sleep(3)
                            print("Regresando al menú de triángulos...")
                            time.sleep(2)
                            triangulos()

                        # Cosecante
                        elif option == 4:
                            print("\n¿En función de qué desea realizar esta función?")
                            print("1 - De la hipotenusa y cateto opuesto")
                            print("2 - Del valor del seno del ángulo")
                            print("3 - Del ángulo")
                            en_function = int(input("Opción: "))

                            # Hipotenusa y cateto opuesto
                            if en_function == 1:
                                co = float(input("\nIngrese el valor del cateto opuesto: "))
                                hip = float(input("Ingrese el valor de la hipotenusa: "))
                                csc = hip / co
                                if co <= 0 or hip <= 0:
                                    print("Error: Los valores ingresados no puden albergar valores menores o iguales a"
                                          " cero.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(f"\nLa cosecante de este triángulo tiene un valor de {csc:.5f} radianes.")
                                    time.sleep(5)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Seno del ángulo
                            elif en_function == 2:
                                sen = float(input("\nIngrese el valor de seno: "))
                                csc = 1 / sen
                                print(f"\nLa cosecante de este triángulo tiene un valor de {csc:.5f} radianes.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Ángulo
                            elif en_function == 3:
                                a = float(input("\nIngrese el valor del ángulo en radianes: "))
                                csc = 1 / math.sin(a)
                                print(f"\nLa cosecante de este triángulo tiene un valor de {csc:.5f} radianes.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Operación incorrecta
                            else:
                                print("\nError: Operación incorrecta.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                        # Secante
                        elif option == 5:
                            print("\n¿En función de qué desea realizar esta función?")
                            print("1 - De la hipotenusa y cateto adyacente")
                            print("2 - Del valor del coseno del ángulo")
                            print("3 - Del ángulo")
                            en_function = int(input("Opción: "))

                            # Hipotenusa y cateto adyacente
                            if en_function == 1:
                                hip = float(input("\nIngrese el valor de la hipotenusa: "))
                                ca = float(input("Ingrese el valor del cateto adyacente: "))
                                sec = hip / ca
                                if hip <= 0 or ca <= 0:
                                    print("\nError: Los valores ingresados son menores o iguales a cero.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(f"\nLa secante de este triángulo tiene un valor de {sec:.5f} unidades.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Valor del coseno
                            elif en_function == 2:
                                cos = float(input("Ingrese el valor de coseno: "))
                                if cos == 0:
                                    print("No puedes dividir por cero bro jajaja")
                                else:
                                    sec = 1 / cos
                                    print(f"La secante de este triángulo tiene un valor de {sec:.5f} radianes.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                            # Ángulo
                            elif en_function == 3:
                                a = float(input("Ingrese el valor del ángulo en radianes: "))
                                sec = 1 / math.cos(a)
                                print(f"La secante de este triángulo tiene un valor de {sec:.5f} radianes.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Operación incorrecta
                            else:
                                print("\nError: Operación incorrecta.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                        # Cotangente
                        elif option == 6:
                            print("\n¿En función de qué desea realizar esta función?")
                            print("1 - Del cateto adyacente y el cateto opuesto")
                            print("2 - Del valor de la tangente del ángulo")
                            print("3 - Del ángulo")
                            en_function = int(input("Opción: "))

                            # Cateto adyacente y cateto opuesto
                            if en_function == 1:
                                ca = float(input("\nIngrese el valor del cateto adyacente: "))
                                co = float(input("Ingrese el valor del cateto opuesto: "))
                                cotg = ca / co
                                print(f"\nLa cotangente de este triángulo tiene un valor de {cotg:.5f} radianes.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                            # Valor de la tangente
                            elif en_function == 2:
                                tan = float(input("\nIngrese el valor de la tangente: "))
                                cotg = 1 / tan
                                if tan == 0 or tan > 1 or tan < -1:
                                    print("Error: El valor de la tangente debe estar entre los valores de -1 y 1.")
                                    print("Evite usar el valor cero.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()
                                else:
                                    print(f"\nEl valor de la cotangente de este triángulo es de {cotg:.5f} radianes.")
                                    time.sleep(3)
                                    print("Regresando al menú principal...")
                                    time.sleep(2)
                                    main()

                            # Ángulo
                            elif en_function == 3:
                                a = float(input("Ingrese el valor del ángulo en radianes: "))
                                sec = 1 / math.tan(a)
                                if a == 90 or a == 270:
                                    print("\nError: La tangente no se encuentra expresada en este valor.")
                                    time.sleep(3)
                                    print("Regresando al menú de polígonos...")
                                    time.sleep(2)
                                    fig_2d()
                                else:
                                    print(f"\nLa secante de este triángulo tiene un valor de {sec:.5f} radianes.")
                                    time.sleep(3)
                                    print("Regresando al menú de triángulos...")
                                    time.sleep(2)
                                    triangulos()

                        # Volver al menú de triángulos
                        elif option == 7:
                            triangulos()

                        # Operación no reconocida
                        else:
                            print("\nError: Operación incorrecta.")
                            time.sleep(2)
                            print("Regresando al menú de triángulos...")
                            time.sleep(1)
                            triangulos()

                    # Obtener ángulos
                    elif option == 4:
                        print("\nEstos cálculos se realizan exclusivamente con triángulos rectángulos.")
                        time.sleep(3)
                        print("¿Cómo desea obtener los ángulos?")
                        print("\n1 - Medida del otro ángulo")
                        option = int(input("Opción: "))

                        # Medida del otro ángulo
                        if option == 1:
                            a = float(input("\nIngrese la medida del ángulo: "))
                            if a <= 0 or a > 90:
                                print(
                                    "Error: El ángulo ingresado alberga un valor menor o igual a cero, o es mayor a "
                                    " 90 grados.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()
                            else:
                                ang_fal = 90 - a
                                print(f"\nEl ángulo faltante es de {ang_fal:.2f} grados.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()

                        # Funciones trigonométricas inversas (arcoseno, arcocoseno)
                        # Work In Progress, no listo aún
                        elif option == 2:
                            co = float(input("\nIngrese la medida del cateto opuesto: "))
                            ca = float(input("Ingrese la medida del cateto adyacente: "))
                            if ca <= 0 or co <= 0:
                                print("\nError: Los valores ingresados albergan valores menores o iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de triángulos...")
                                time.sleep(2)
                                triangulos()
                            else:
                                print("WIP")
                                time.sleep(1)
                                main()

                    # Escoger otra figura
                    elif option == 5:
                        fig_2d()

                    # Operación no reconocida
                    else:
                        print("\nError: Operación incorrecta.")
                        time.sleep(2)
                        print("Reiniciando menú de triángulos...")
                        time.sleep(1)
                        triangulos()
                triangulos()

            # Pentágono
            elif option == 4:
                print("\nEstos ejercicios se realizan con un pentágono regular.")
                time.sleep(1)
                print("\nSeleccione aspecto a calcular.")
                print("1 - Área")
                print("2 - Perímetro")
                print("3 - Apotema")
                print("4 - Escoger otra figura")
                option = int(input("Opción: "))

                # Área de un pentágono
                if option == 1:
                    lado = float(input("\nIngrese la medida de uno de los lados: "))
                    area = (lado ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4
                    if lado <= 0:
                        print("\nError: El valor del lado del pentágono no puede albergar un valor negativo o igual"
                              "a cero.")
                        time.sleep(4)
                        print("Regresando al menú de polígonos...")
                        fig_2d()
                    else:
                        print(f"El área de este pentágono es de {area:.2f} unidades cuadradas.")
                        time.sleep(4)
                        print("\nRegresando al menú principal...")
                        time.sleep(1)
                        main()

                # Perímetro de un pentágono
                elif option == 2:
                    lado = float(input("\nIngrese la medida de uno de los lados: "))
                    perim_penta = 5 * lado
                    if lado <= 0:
                        print("\nError: El valor del lado del pentágono no puede albergar un valor negativo o igual"
                              " a cero.")
                        time.sleep(4)
                        print("Regresando al menú de polígonos...")
                        time.sleep(1)
                        fig_2d()
                    else:
                        print(f"El perímetro de este pentágono es de {perim_penta} unidades.")
                        time.sleep(4)
                        print("\nRegresando al menú principal...")
                        time.sleep(1)
                        main()

                # Apotema de un pentágono
                elif option == 3:
                    lado = float(input("\nIngrese la medida de uno de los lados: "))
                    apot_pent = (lado / 2) * (math.sqrt(1 + (2 / math.sqrt(5))))
                    if lado <= 0:
                        print("\nError: El valor del lado del pentágono no puede albergar un valor negativo o igual"
                              " a cero.")
                        time.sleep(4)
                        print("Regresando al menú de polígonos...")
                        time.sleep(1)
                        fig_2d()
                    else:
                        print(f"La apotema de este pentágono es de {apot_pent} unidades.")
                        time.sleep(4)
                        print("\nRegresando al menú principal...")
                        time.sleep(1)
                        main()

                # Seleccionar otro polígono
                elif option == 4:
                    fig_2d()

                # Otro valor
                else:
                    print("\nError: Operación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú de polígonos...")
                    time.sleep(1)
                    fig_2d()

            # Menú Principal
            elif option == 5:
                main()

            # Otro valor
            else:
                print("\nError: Operación incorrecta.")
                time.sleep(2)
                print("Regresando al menú principal...")
                time.sleep(1)
                main()

        fig_2d()

    # Cuerpos 3D
    elif opcion == 2:
        def fig_3d():
            print("\nSeleccione un cuerpo.")
            print("1 - Cubo")
            print("2 - Prismas")
            print("3 - Esfera")
            print("4 - Cilindro")
            print("5 - Pirámide")
            print("6 - Volver al menú principal")
            opt = int(input("Opción: "))

            # Cubo
            if opt == 1:
                print("\nSeleccione aspecto a calcular.")
                print("1 - Área")
                print("2 - Volumen")
                print("3 - Diagonal")
                print("4 - Seleccionar otro poliedro")
                opt = int(input("Opción: "))

                # Área de un cubo
                if opt == 1:
                    a = float(input("\nIngrese la medida del arista del cubo: "))
                    area_cubo = 6 * (a ** 3)
                    print(f"\nEl área total de este cubo es de {area_cubo} unidades cuadradas.")
                    time.sleep(3)
                    print("Regresando al menú de poliedros...")
                    time.sleep(2)
                    fig_3d()

                # Volumen de un cubo
                elif opt == 2:
                    a = float(input("\nIngrese la medida del arista del cubo: "))
                    vol_cubo = a ** 3
                    print(f"\nEl volumen de este cubo es de {vol_cubo} unidades cúbicas.")
                    time.sleep(3)
                    print("Regresando al menú de poliedros...")
                    time.sleep(2)
                    fig_3d()

                # Diagonal de un cubo
                elif opt == 3:
                    a = float(input("\nIngrese la medida del arista del cubo: "))
                    diag_cubo = a * math.sqrt(3)
                    print(f"\nLa diagonal de este cubo es de {diag_cubo:.2f} unidades.")
                    time.sleep(3)
                    print("Regresando al menú de poliedros...")
                    time.sleep(2)
                    fig_3d()

                # Volver al menú de selección de poliedros
                elif opt == 4:
                    fig_3d()

                # Otro valor
                else:
                    print("\nError: Operación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Prisma
            elif opt == 2:
                print("\nEscoja el prisma con el cual desea trabajar:")
                print("1 - Prismas regulares")
                print("2 - Seleccionar otro poliedro")
                opt = int(input("Opción: "))

                # Prismas regulares
                if opt == 1:
                    print("\nEscoja una base:")
                    print("1 - Triangular")
                    print("2 - Cuadrangular")
                    opt = int(input("Opción: "))

                    # Prisma de base triangular
                    if opt == 1:
                        print("\nSeleccione aspecto a calcular: ")
                        print("1 - Áreas")
                        print("2 - Volumen")
                        opt = int(input("Opción: "))

                        # Áreas de un prisma regular de base triangular
                        if opt == 1:
                            a1 = float(input("\nIngrese la medida de una arista de la base: "))
                            a2 = float(input("Ingrese la medida de otra arista de la base: "))
                            a3 = float(input("Ingrese la medida de otra arista de la base: "))
                            h = float(input("Ingrese la altura del prisma: "))

                            # Prisma regular de base triangular equilátera y altura h
                            if (a1 + a2 + a3) / 3 == a1 and a2 and a3:
                                area_basal = (math.sqrt(3) / 4) * (a1 ** 2)
                                area_lat = a1 * h
                                area_total = 2 * area_basal + 3 * area_lat
                                print(f"\nEl área total de este prisma es de {area_total:.2f} unidades cuadradas.")
                                print(f"El área basal de este prisma es de {area_basal:.2f} unidades cuadradas.")
                                print(f"El área lateral de este prisma es de {area_lat} unidades cuadradas.")
                                print("Nota: Valores aproximados a la centésima.")
                                time.sleep(11)
                                print("Regresando al menú de poliedros...")
                                time.sleep(4)
                                fig_3d()

                            # Arista de valor negativo o igual a cero
                            elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                print("\nError: Las aristas no pueden tener valores negativos o iguales a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de poliedros...")
                                time.sleep(1)
                                fig_3d()

                            # Altura de valor negativo o igual a cero
                            elif h <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de poliedros...")
                                time.sleep(1)
                                fig_3d()

                            # Prisma regular de base triangular escalena/isóceles y altura h
                            else:
                                s = (a1 + a2 + a3) / 2
                                perim = s * 2
                                area_base = s * (s - a1) * (s - a2) * (s - a3)
                                area_basal = math.sqrt(area_base)
                                area_lat = perim * h
                                area_total = 2 * area_basal + 3 * area_lat
                                print(f"\nEl área total de este prisma es de {area_total:.2f} unidades cuadradas.")
                                print(f"El área basal de este prisma es de {area_basal:.2f} unidades cuadradas.")
                                print(f"El área lateral de este prisma es de {area_lat} unidades cuadradas.")
                                print("Nota: Valores aproximados a la centésima.")
                                time.sleep(11)
                                print("Regresando al menú de poliedros...")
                                time.sleep(4)
                                fig_3d()

                        # Volumen de un prisma regular de base triangular
                        elif opt == 2:
                            a1 = float(input("\nIngrese la medida de una arista de la base: "))
                            a2 = float(input("Ingrese la medida de otra arista de la base: "))
                            a3 = float(input("Ingrese la medida de otra arista de la base: "))
                            h = float(input("Ingrese la altura del prisma: "))

                            # Prisma regular de base triangular equilátera y altura h
                            if (a1 + a2 + a3) / 3 == a1 and a2 and a3:
                                area_basal = (math.sqrt(3) * (a1 ** 2)) / 4
                                volumen = area_basal * h
                                print(f"\nEl volumen de este prisma corresponde a {volumen} unidades cúbicas.")
                                time.sleep(7)
                                print("Regresando al menú de poliedros...")
                                time.sleep(3)
                                fig_3d()

                            # Valor negativo o igual a cero de al menos una arista
                            elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                print("\nError: Las aristas no pueden tener valores negativos o iguales a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de poliedros...")
                                time.sleep(1)
                                fig_3d()

                            # Valor negativo o igual a cero de la altura
                            elif h <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de poliedros...")
                                time.sleep(1)
                                fig_3d()

                            # Prisma regular de base triangular escalena/isóceles y altura h
                            else:
                                s = (a1 + a2 + a3) / 2
                                area_base = s * (s - a1) * (s - a2) * (s - a3)
                                area_basal = math.sqrt(area_base)
                                volumen = area_basal * h
                                print(f"\nEl volumen de este prisma corresponde a {volumen:.2f} unidades cúbicas.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                    # Prisma regular de base cuadrangular
                    elif opt == 2:
                        print("\nSeleccione aspecto a calcular: ")
                        print("1 - Áreas")
                        print("2 - Volumen")
                        print("3 - Diagonal")
                        opt = int(input("Opción: "))

                        # Áreas de un prisma de base cuadrangular
                        if opt == 1:
                            l1 = float(input("\nIngrese la medida de un lado del rectángulo de la base: "))
                            l2 = float(input("Ingrese la medida del otro lado del rectángulo de la base: "))
                            h_pr_qd = float(input("Ingrese la medida de la altura: "))
                            if l1 <= 0 or l2 <= 0:
                                print("\nError: Los lados ingresados no pueden ser valores menores o iguales a cero.")
                                time.sleep(5)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                area_pr_quad = 2 * (l1 * l2 + l1 * h_pr_qd + l2 * h_pr_qd)
                                print(f"\nEl área total de este prisma es de {area_pr_quad} unidades cuadradas.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                        # Volumen de un prisma de base cuadrangular
                        elif opt == 2:
                            l1 = float(input("\nIngrese la medida de un lado del rectángulo de la base: "))
                            l2 = float(input("Ingrese la medida del otro lado del rectángulo de la base: "))
                            h_pr_qd = float(input("Ingrese la medida de la altura: "))
                            if l1 <= 0 or l2 <= 0:
                                print("\nError: Los lados basales no pueden poseer valores menores o iguales a cero.")
                                time.sleep(5)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                print("\nError: Está calculando el volumen de un cubo.")
                                print(f"El volumen de este cubo es de {l1 * l2 * h_pr_qd} unidades cúbicas.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                vol_pr_qd = l1 * l2 * h_pr_qd
                                print(f"\nEl volumen de este prisma es de {vol_pr_qd} unidades cúbicas.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                        # Diagonal de un prisma cuadrangular
                        elif opt == 3:
                            l1 = float(input("\nIngrese la medida de un lado del rectángulo de la base: "))
                            l2 = float(input("Ingrese la medida del otro lado del rectángulo de la base: "))
                            h_pr_qd = float(input("Ingrese la medida de la altura: "))
                            if l1 <= 0 or l2 <= 0:
                                print("\nError: Los lados basales no pueden poseer valores menores o iguales a cero.")
                                time.sleep(7)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                print("\nError: Está calculando la diagonal de un cubo.")
                                print(f"La diagonal tiene una medida de {(l1 * math.sqrt(3)):.2f} unidades.")
                                time.sleep(7)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                diag_pr_qd_sq = l1 ** 2 + l2 ** 2 + h_pr_qd ** 2
                                diag_pr_qd = math.sqrt(diag_pr_qd_sq)
                                print(f"\nLa diagonal de este prisma tiene una medida de {diag_pr_qd:.2f} unidades.")
                                print("Nota: Valor aproximado a la centésima.")
                                time.sleep(7)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                    # Otro valor
                    else:
                        print("\nOperación incorrecta.")
                        time.sleep(2)
                        print("Regresando al menú de poliedros...")
                        time.sleep(1)
                        fig_3d()

                # Volver al menú de selección de poliedros
                elif opt == 2:
                    fig_3d()

                # Otro valor
                else:
                    print("\nOperación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Esfera
            elif opt == 3:
                print("\nSeleccione aspecto a calcular: ")
                print("1 - Área")
                print("2 - Volumen")
                print("3 - Seleccionar otro poliedro")
                opt = int(input("Opción: "))

                # Área de la esfera
                if opt == 1:
                    r = float(input("\nIngrese el valor del radio de la esfera: "))
                    area_sph = 4 * math.pi * (r ** 2)
                    if r <= 0:
                        print("\nError: El radio de la esfera no puede contener valores negativos o iguales a cero.")
                        time.sleep(4)
                        print("Regresando al menú de poliedros...")
                        time.sleep(1)
                        fig_3d()
                    else:
                        print(f"\nEl área de esta esfera es de {area_sph:.2f} unidades cuadradas.")
                        print(f"Número pi como incógnita: {4 * (r ** 2)}π unidades cuadradas.")
                        time.sleep(7)
                        print("Regresando al menú de poliedros...")
                        time.sleep(2)
                        fig_3d()

                # Volumen de la esfera
                elif opt == 2:
                    r = float(input("\nIngrese el valor del radio de la esfera: "))
                    vol_sph = (4 / 3) * math.pi * (r ** 3)
                    if r <= 0:
                        print("\nError: El radio de la esfera no puede contener valores negativos o iguales a cero.")
                        time.sleep(4)
                        print("Regresando al menú de poliedros...")
                        time.sleep(1)
                        fig_3d()
                    else:
                        print(f"\nEl volumen de esta esfera es de {vol_sph:.2f} unidades cúbicas.")
                        print(f"Número pi como incógnita: {(4 / 3) * (r ** 3):.2f}π unidades cúbicas.")
                        time.sleep(7)
                        print("Regresando al menú de poliedros...")
                        time.sleep(2)
                        fig_3d()

                # Volver al menú de selección de poliedros
                elif opt == 3:
                    fig_3d()

                # Otro valor
                else:
                    print("\nOperación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Cilindro
            elif opt == 4:
                print("\nSeleccione el tipo de cilindro con el cual desea trabajar:")
                print("1 - Recto (Eje del cilindro es perpendicular a las bases)")
                print("2 - Seleccionar otro poliedro")
                cho = int(input("Opción: "))

                # Cilindro recto
                if cho == 1:
                    print("\nSeleccione aspecto a calcular:")
                    print("1 - Áreas")
                    print("2 - Volumen")
                    choice = int(input("Opción: "))

                    # Áreas de un cilindro recto
                    if choice == 1:
                        r = float(input("\nIngrese el valor del radio de la base del cilindro: "))
                        h = float(input("Ingrese el valor de la altura del cilindro: "))

                        # Valores negativos para el radio o la altura
                        if r <= 0 or h <= 0:
                            print("\nError: Los valores ingresados son negativos o iguales a cero.")
                            time.sleep(5)
                            print("Volviendo al menú de selección de poliedros...")
                            time.sleep(3)
                            fig_3d()

                        # Valores positivos para el radio y la altura
                        else:
                            ar_bas = math.pi * (r ** 2)
                            ar_lat = 2 * math.pi * r * h
                            ar_total = ar_lat + 2 * ar_bas
                            print(f"\nEl área total de este cilindro es de {ar_total:.2f} unidades cuadráticas.")
                            print(f"El área lateral de este cilindro es de {ar_lat:.2f} unidades cuadráticas.")
                            print(f"El área basal de este cilindro es de {ar_bas:.2f} unidades cuadráticas.")
                            time.sleep(12)
                            print("Regresando al menú de poliedros...")
                            time.sleep(2)
                            fig_3d()

                    # Volumen de un cilindro recto
                    elif choice == 2:
                        r = float(input("\nIngrese el valor del radio de la base del cilindro: "))
                        h = float(input("Ingrese el valor de la altura del cilindro: "))

                        # Valores negativos para el radio o la altura
                        if r <= 0 or h <= 0:
                            print("\nError: Los valores ingresados son negativos o iguales a cero.")
                            time.sleep(5)
                            print("Volviendo al menú de selección de poliedros...")
                            time.sleep(3)
                            fig_3d()

                        # Valores positivos para el radio y la altura
                        else:
                            vol = math.pi * (r ** 2) * h
                            print(f"\nEl volumen de este cilindro es de {vol:.2f} unidades cúbicas.")
                            time.sleep(5)
                            print("Regresando al menú de poliedros...")
                            time.sleep(2)
                            fig_3d()

                # Volver al menú de poliedros
                elif cho == 2:
                    fig_3d()

                # Otro valor
                else:
                    print("\nOperación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Pirámide
            elif opt == 5:
                print("\nSeleccione el tipo de pirámide con el que desea trabajar:")
                print("1 - Pirámides rectas regulares")
                print("2 - Pirámides oblicuas irregulares")
                print("3 - Seleccionar otro poliedro")
                opt = int(input("Opción: "))

                # Pirámides rectas
                if opt == 1:
                    print("\nSeleccione la base de la pirámide: ")
                    print("1 - Cuadrada")
                    print("2 - Rectangular")
                    opt = int(input("Opción: "))

                    # Pirámide recta de base cuadrada
                    if opt == 1:
                        print("\nSeleccione aspecto a calcular: ")
                        print("1 - Área")
                        print("2 - Volumen")
                        opt = int(input("Opción: "))

                        # Área de una pirámide recta de base cuadrada
                        if opt == 1:
                            lado = float(input("Ingrese la medida de una arista de la base: "))
                            ap = float(input("Ingrese la medida del apotema: "))
                            ar_pir_qd = lado * (2 * ap + lado)

                            # Valores negativos o iguales a cero para apotema y/o lado
                            if lado <= 0 or ap <= 0:
                                print("\nError: Los valores ingresados no pueden contener valores negativos o"
                                      " iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                print(f"\nEl área de esta pirámide es de {ar_pir_qd:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                        # Volumen de una pirámide recta de base cuadrada
                        elif opt == 2:
                            lado = float(input("Ingrese la medida de una arista de la base: "))
                            h = float(input("Ingrese la medida de la altura de la pirámide: "))
                            vol = 1 / 3 * (lado ** 2) * h
                            # Valores negativos o iguales a cero para altura y/o lado
                            if lado <= 0 or h <= 0:
                                print("\nError: Los valores ingresados no pueden contener valores negativos o"
                                      " iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                print(f"\nEl volumen de esta pirámide es de {vol} unidades cúbicas.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                    # Pirámide recta de base rectangular
                    elif opt == 2:
                        print("\nSeleccione aspecto a calcular: ")
                        print("1 - Área")
                        print("2 - Volumen")
                        opt = int(input("Opción: "))

                        # Área de la pirámide recta de base cuadrangular
                        if opt == 1:
                            a = float(input("\nIngrese la medida de un lado de la base: "))
                            b = float(input("Ingrese la medida de otro lado de la base: "))
                            h = float(input("Ingrese la medida de la altura de la pirámide: "))
                            if a <= 0 or b <= 0 or h <= 0:
                                print("\nError: Los valores ingresados no pueden contener valores negativos o"
                                      " iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                area = a * b + a * math.sqrt(h ** 2 + (b ** 2 / 4)) + b * math.sqrt(
                                    h ** 2 + (a ** 2 / 4))
                                print(f"\nEl área de esta pirámide es de {area:.2f} unidades cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

                        # Volumen de pirámide de base cuadrangular
                        elif opt == 2:
                            a = float(input("\nIngrese la medida de un lado de la base: "))
                            b = float(input("Ingrese la medida de otro lado de la base: "))
                            h = float(input("Ingrese la medida de la altura de la pirámide: "))
                            if a <= 0 or b <= 0 or h <= 0:
                                print("\nError: Los valores ingresados no pueden contener valores negativos o"
                                      " iguales a cero.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                vol = (a * b * h) / 3
                                print(f"\nEl volumen de esta pirámide es de {vol:.2f} unidades cúbicas.")
                                time.sleep(3)
                                print("Regresando al menú de poliedros...")
                                time.sleep(2)
                                fig_3d()

                    # Otro valor
                    else:
                        print("\nOperación incorrecta.")
                        time.sleep(2)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Pirámides oblicuas
                elif opt == 2:
                    print("En construcción...")
                    main()

                # Seleccionar otro poliedro
                elif opt == 3:
                    fig_3d()

                # Otro valor
                else:
                    print("\nOperación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Volver al menú principal
            elif opt == 5:
                main()

            # Otro valor
            else:
                print("\nOperación incorrecta.")
                time.sleep(2)
                print("Regresando al menú principal...")
                time.sleep(1)
                main()

        fig_3d()

    # Créditos
    elif opcion == 3:
        print(f"\n\tVersión actual: {version}")
        print("\t--- Codename Copernicium ---")
        print("\tProgramado en Python 3.8")
        time.sleep(3)
        print("\nProgramación: Qm_Dev")
        time.sleep(3)
        print("Diseño: Qm_Dev")
        time.sleep(3)
        print("Testeo: Qm_Dev")
        time.sleep(3)
        print("Código fuente: https://github.com/Qm-Dev/figures-calculator")
        time.sleep(3)
        print("Agradecimientos especiales: "
              "\n-Alejandro Taboada Sánchez"
              "\n-Patorjk")
        time.sleep(5)
        main()

    # Salir del programa
    elif opcion == 4:
        time.sleep(0.2)
        print("\nSaliendo del programa...")
        time.sleep(0.8)
        exit()

    # Easter
    elif opcion == 2082019:
        time.sleep(3)
        print("\n\t'Si puedes imaginarlo, puedes programarlo.'")
        time.sleep(3)
        print("\t\t- Alejandro Taboada Sánchez")
        time.sleep(5)
        main()

    # Otro valor
    else:
        print("\nError: Operación incorrecta.")
        print("Reiniciando programa...")
        time.sleep(1)
        main()


main()
