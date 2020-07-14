import math
import time

version = "Alpha 6.1"


def main():
    print("\nBienvenido al programa. A continuación, escoja la opción que estime conveniente.")
    print("\t1 - Polígonos (2D)")
    print("\t2 - Poliedros (3D)")
    print("\t3 - Créditos")
    print("\t4 - Salir")
    opcion = int(input("Opción: "))

    # Figuras 2D
    if opcion == 1:
        def fig_2d():
            print("\nSeleccione una figura.")
            print("1 - Cuadrado")
            print("2 - Rectángulo")
            print("3 - Circunferencia")
            print("4 - Triángulo")
            print("5 - Pentágono")
            print("6 - Volver al menú principal")
            option = int(input("Opción: "))

            # Cuadrado
            if option == 1:
                print("\nSeleccione aspecto a calcular.")
                print("1 - Área")
                print("2 - Perímetro")
                print("3 - Diagonal")
                print("4 - Escoger otra figura")
                option = int(input("Opción: "))

                # Área de un cuadrado
                if option == 1:
                    print("\nA continuación ingrese la medida del lado del cuadrado.")
                    lado = float(input("Medida: "))
                    area_sq = lado * lado
                    if lado <= 0:
                        print("\nError: El valor ingresado no puede tener valor negativo o igual a cero.")
                        time.sleep(0.5)
                        print("Volviendo al menú de polígonos...")
                        time.sleep(1)
                        fig_2d()
                    else:
                        print(f"\nLa medida del área de este cuadrado es de {area_sq} unidades cuadradas.")
                        time.sleep(4)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Perímetro de un cuadrado
                elif option == 2:
                    print("\nA continuación ingrese la medida del lado del cuadrado.")
                    lado = float(input("Medida: "))
                    perim_sq = lado * 4

                    if lado <= 0:
                        print("\nError: El valor ingresado no puede tener valor negativo o igual a cero.")
                        time.sleep(3)
                        print("Volviendo al menú de polígonos...")
                        time.sleep(2)
                        fig_2d()

                    else:
                        print(f"\nEl perímetro de este cuadrado es de {perim_sq} unidades.")
                        time.sleep(4)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Diagonal de un cuadrado
                elif option == 3:
                    print("\nA continuación ingrese la medida del lado del cuadrado.")
                    lado = float(input("Medida: "))
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
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Escoger otra figura
                elif option == 4:
                    fig_2d()

                # Operación no definida
                else:
                    print("\nError: Operación incorrecta.")
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Rectángulo
            elif option == 2:
                print("\nSeleccione aspecto a calcular.")
                print("1 - Área")
                print("2 - Perímetro")
                print("3 - Diagonal")
                print("4 - Escoger otra figura")
                option = int(input("Opción: "))

                # Área de un rectángulo
                if option == 1:
                    print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                    ancho = float(input("Ancho: "))
                    largo = float(input("Largo: "))
                    area_rect = ancho * largo
                    print(f"\nEl área de este rectángulo es de {area_rect} unidades cuadradas.")
                    time.sleep(4)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

                # Perímetro de un rectángulo
                elif option == 2:
                    print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                    ancho = float(input("Ancho: "))
                    largo = float(input("Largo: "))
                    perim_rect = (ancho * 2) + (largo * 2)
                    print(f"\nEl perímetro de este rectángulo es de {perim_rect} unidades.")
                    time.sleep(4)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

                # Diagonal de un rectángulo
                elif option == 3:
                    print("\nA continuación ingrese las medidas de ancho y largo del rectángulo.")
                    ancho = float(input("Ancho: "))
                    largo = float(input("Largo: "))
                    diag_rect = ((ancho ** 2) + (largo ** 2))
                    diag_rect_final = (math.sqrt(diag_rect))
                    print(f"\nLa diagonal aproximada de este rectángulo es de {diag_rect_final:.2f} unidades.")
                    time.sleep(4)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

                # Escoger otra figura
                elif option == 4:
                    fig_2d()

                # Otro
                else:
                    print("\nError: Operación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Circunferencia
            elif option == 3:
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
                    print(f"\nLa medida del área del círculo es de {area_cir:.2f} unidades cuadradas.")
                    print(f"Con π como incógnita: {radio ** 2}π unidades cuadradas.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

                # Perímetro de la circunferencia
                elif option == 2:
                    print("\nA continuación ingrese la medida del radio del círculo.")
                    radio = float(input("Radio: "))
                    perim_circ = 2 * radio * math.pi
                    print(f"\nEl perímetro del círculo es de {perim_circ:.2f} unidades.")
                    print(f"Con π como incógnita: {(2 * radio)}π unidades.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

                # Diámetro de la circunferencia
                elif option == 3:
                    print("\nA continuación ingrese la medidad del radio del círculo.")
                    radio = float(input("Radio: "))
                    print(f"\nEl diámetro del círculo es de {2 * radio} unidades.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

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
            elif option == 4:
                print("\nSeleccione la clasificación a trabajar.")
                print("1 - Medida de sus lados")
                print("2 - Amplitud de sus ángulos")
                print("3 - Trigonometría (Uso de lados y ángulos)")
                print("4 - Escoger otra figura")
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
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                        # Perímetro del triángulo equilátero
                        elif option == 2:
                            lado = float(input("\nIngrese la medida del lado del triángulo: "))
                            print(f"\nEl perímetro del triángulo es de {lado * 3} unidades.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

                        # Diagonal del triángulo equilatero
                        elif option == 3:
                            lado = float(input("\nIngrese la medida del lado del triángulo: "))
                            h_tr_eq = (math.sqrt(3) * lado) / 2
                            print(f"\nLa altura del triángulo es de {h_tr_eq:.2f} unidades.")
                            time.sleep(2)
                            print("Regresando al menú principal...")
                            time.sleep(1)
                            main()

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
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()
                            else:
                                equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                alt_tr_is = math.sqrt(equation_h)
                                area_tr_is = (lado2 * alt_tr_is) / 2
                                print(f"\nEl área del triángulo isóceles es de {area_tr_is:.2f} unidades cuadradas.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()

                        # Perímetro de un triángulo isóceles
                        elif option == 2:
                            lado1 = float(input("\nIngrese la medida de los lados iguales: "))
                            lado2 = float(input("Ingrese la medida del lado diferente: "))
                            if lado1 * 2 <= lado2:
                                print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()
                            else:
                                print(f"\nEl perímetro de este triángulo isóceles es de {lado1 * 2 + lado2} unidades.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()

                        # Altura de un triángulo isóceles
                        elif option == 3:
                            lado1 = float(input("\nIngrese la medida de los lados iguales: "))
                            lado2 = float(input("Ingrese la medida del lado diferente: "))
                            if lado1 * 2 <= lado2:
                                print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                time.sleep(2)
                                print("Regresando al menú principal...")
                                time.sleep(1)
                                main()
                            else:
                                equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                alt_tr_is = math.sqrt(equation_h)
                                print(f"\nLa altura del triángulo isóceles es de {alt_tr_is:.2f} unidades.")
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
                                print("\nError: El triángulo debe tener como valor en sus lados números mayores a 0.")
                                time.sleep(3)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            elif lado1 == lado2 and lado1 == lado3:
                                print("\nError: Los tres lados ingresados son de igual valor.")
                                print("El triángulo es equilátero.")
                                time.sleep(3)
                                print("Regresando al menú de selección de figuras...")
                                time.sleep(2)
                                fig_2d()
                            elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                print("\nLos valores ingresados no cumplen con la desigualdad triangular.")
                                time.sleep(2)
                                print("Regresando al menú de selección de figuras...")
                                time.sleep(1)
                                fig_2d()
                            else:
                                print(f"\nEl área de este triángulo escaleno es de {form_heron:.2f} unidades"
                                      f" cuadradas.")
                                time.sleep(3)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

                        # Perímetro de un triángulo escaleno
                        if option == 2:
                            lado1 = float(input("\nIngrese la medida del primer lado: "))
                            lado2 = float(input("Ingrese la medida del segundo lado: "))
                            lado3 = float(input("Ingrese la medida del tercer lado: "))
                            perim_tr_esc = lado1 + lado2 + lado3
                            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                                print("\nError: El triángulo debe tener como valor en sus lados números mayores a 0.")
                                time.sleep(3)
                                print("Regresando al menú de selección de figuras...")
                                time.sleep(2)
                                fig_2d()
                            elif lado1 == lado2 and lado1 == lado3:
                                print("\nError: Los tres lados ingresados son de igual valor.")
                                print("El triángulo es equilatero.")
                                print(f"\nEl perímetro de este triángulo equilátero es de {perim_tr_esc:.2f} unidades.")
                                time.sleep(5)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            elif lado1 == lado2 or lado2 == lado1:
                                print("\nError: Lado 1 y Lado 2 comparten el mismo valor. El triángulo es isóceles.")
                                print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                time.sleep(5)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            elif lado2 == lado3 or lado3 == lado2:
                                print("\nError: Lado 2 y Lado 3 comparten el mismo valor. El triángulo es isóceles.")
                                print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                time.sleep(5)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            elif lado1 == lado3 or lado3 == lado1:
                                print("\nError: Lado 1 y Lado 3 comparten el mismo valor. El triángulo es isóceles.")
                                print(f"El perímetro de este triángulo isóceles es de {perim_tr_esc:.2f} unidades.")
                                time.sleep(5)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                print("\nError: Los valores ingresados no cumplen con la desigualdad triangular.")
                                time.sleep(3)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            else:
                                print(f"\nEl perímetro de este triángulo escaleno es de {perim_tr_esc:.2f} unidades.")
                                time.sleep(3)
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

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
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()
                            else:
                                print(f"\nLas alturas del triángulo son de {ha:.2f} unidades, {hb:.2f}"
                                      f"unidades y {hc:.2f} unidades respectivamente.")
                                print("Estos valores se encuentran aproximados a la centésima.")
                                time.sleep(6)
                                print("Regresando al menú principal...")
                                time.sleep(4)
                                main()

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
                            print("Regresando al menú principal...")
                            time.sleep(2)
                            main()

                        # Perímetro de un triángulo rectángulo
                        elif option == 2:
                            cat1 = float(input("\nIngrese la medida de un cateto: "))
                            cat2 = float(input("Ingrese la medida del otro cateto: "))
                            hip = float(input("Ingrese la medida de la hipotenusa: "))
                            perim_tr_rect = cat1 + cat2 + hip
                            print(f"\nEl perímetro del triángulo es de {perim_tr_rect} unidades.")
                            time.sleep(3)
                            print("Regresando al menú principal...")
                            time.sleep(2)
                            main()

                        # Hipotenusa del triángulo rectángulo
                        elif option == 3:
                            cat1 = float(input("\nIngrese la medida de un cateto: "))
                            cat2 = float(input("Ingrese la medida del otro cateto: "))
                            hip_sq = (cat1 ** 2) + (cat2 ** 2)
                            hip = math.sqrt(hip_sq)
                            print(f"\nLa hipotenusa de este triángulo tiene un valor de {hip} unidades.")
                            time.sleep(3)
                            print("Regresando al menú principal...")
                            time.sleep(2)
                            main()

                        # Medida de uno de los catetos del triángulo rectángulo por medio de la hipotenusa y otro cateto
                        elif option == 4:
                            cat1 = float(input("\nIngrese la medida del cateto: "))
                            hip = float(input("Ingrese la medida de la hipotenusa: "))
                            x = hip ** 2 - cat1 ** 2
                            cat2 = math.sqrt(x)
                            print(f"\nLa medida del cateto faltante es de {cat2:.2f} unidades.")
                            time.sleep(3)
                            print("Regresando al menú principal...")
                            time.sleep(2)
                            main()

                        # Cálculo no identificable
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
                    print("\nEstos problemas se realizan con un triángulo rectángulo.")
                    print("Es decir, aquellos triángulos que poseen un ángulo de 90º grados.")
                    time.sleep(5)
                    print("\nA continuación, escoja un parámetro a calcular:")
                    print("\n1 - Seno (Se necesita los valores del ángulo visto desde el cateto opuesto y "
                          "de la hipotenusa)")
                    print("2 - Coseno (Se necesita los valores del ángulo visto desde el cateto adyacente y de la "
                          "hipotenusa)")
                    print("3 - Tangente (Se necesitan los valores de los dos catetos)")
                    print("4 - Arcotangente (Se necesitan los valores de los dos catetos)")
                    option = int(input("Opción: "))

                    # Seno
                    if option == 1:
                        hip = float(input("\nIngrese el valor de la hipotenusa: "))
                        ang_degree = int(input("Ingrese el valor del ángulo: "))
                        ang_rad = math.radians(ang_degree)
                        sin = math.sin(ang_rad)
                        co = sin * hip
                        print(f"\nEl valor del cateto opuesto es de {co:.2f} unidades.")
                        time.sleep(3)
                        print("Regresando al menú principal...")
                        time.sleep(2)
                        main()
                    # Coseno
                    elif option == 2:
                        hip = float(input("\nIngrese el valor de la hipotenusa: "))
                        ang_degree = int(input("Ingrese el valor del ángulo: "))
                        ang_rad = math.radians(ang_degree)
                        cos = math.cos(ang_rad)
                        ca = cos * hip
                        print(f"\nEl valor del cateto adyacente es de {ca:.2f} unidades.")
                        time.sleep(3)
                        print("Regresando al menú principal...")
                        time.sleep(2)
                        main()

                    # Tangente
                    elif option == 3:
                        co = float(input("\nIngrese el valor del cateto opuesto: "))
                        ca = float(input("Ingrese el valor del cateto adyacente: "))
                        tan = co / ca
                        print(f"\nEl valor de la tangente para un ángulo desconocido es de {tan:.2f} unidades.")
                        time.sleep(8)
                        print("\nRegresando al menú principal...")
                        time.sleep(2)
                        main()

                    # Arcotangente
                    elif option == 4:
                        co = float(input("\nIngrese el valor del cateto opuesto: "))
                        ca = float(input("Ingrese el valor del cateto adyacente: "))
                        if co / ca == 90 or co / ca == 270:
                            print("\nError: La función no se encuentra definida para este punto.")
                            print("Regresando al menú de polígonos...")
                            time.sleep(5)
                            fig_2d()
                        else:
                            tan = co / ca
                            arctan = math.degrees(math.atan(tan))
                            arctan_rad = math.atan(tan)
                            print(f"\nEl ángulo presente en este triángulo tiene una medida de {arctan:.2f} grados.")
                            print(f"Su equivalente en radianes es de {arctan_rad:.2f} rad.")
                            time.sleep(10)
                            print("\nRegresando al menú principal...")
                            time.sleep(5)
                            main()

                    # Operación no reconocida
                    else:
                        print("\nError: Operación incorrecta.")
                        time.sleep(2)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Escoger otra figura
                elif option == 4:
                    fig_2d()

                # Operación no reconocida
                else:
                    print("\nError: Operación incorrecta.")
                    time.sleep(2)
                    print("Regresando al menú principal...")
                    time.sleep(1)
                    main()

            # Pentágono
            elif option == 5:
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

            # Menú Principal
            elif option == 6:
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
                    print("Regresando al menú principal...")
                    time.sleep(2)
                    main()

                # Volumen de un cubo
                elif opt == 2:
                    a = float(input("\nIngrese la medida del arista del cubo: "))
                    vol_cubo = a ** 3
                    print(f"\nEl volumen de este cubo es de {vol_cubo} unidades cúbicas.")
                    time.sleep(3)
                    print("Regresando al menú principal...")
                    time.sleep(2)
                    main()

                # Diagonal de un cubo
                elif opt == 3:
                    a = float(input("\nIngrese la medida del arista del cubo: "))
                    diag_cubo = a * math.sqrt(3)
                    print(f"\nLa diagonal de este cubo es de {diag_cubo:.2f} unidades.")
                    time.sleep(3)
                    print("Regresando al menú principal...")
                    time.sleep(2)
                    main()

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
                                print("\nRegresando al menú principal...")
                                time.sleep(4)
                                main()

                            # Arista de valor negativo o igual a cero
                            elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                print("\nError: Las aristas no pueden tener valores negativos o iguales a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de cuerpos...")
                                time.sleep(1)
                                fig_3d()

                            # Altura de valor negativo o igual a cero
                            elif h <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de cuerpos...")
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
                                print("\nRegresando al menú principal...")
                                time.sleep(4)
                                main()

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
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()

                            # Valor negativo o igual a cero de al menos una arista
                            elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                print("\nError: Las aristas no pueden tener valores negativos o iguales a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de cuerpos...")
                                time.sleep(1)
                                fig_3d()

                            # Valor negativo o igual a cero de la altura
                            elif h <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(2)
                                print("Regresando al menú de selección de cuerpos...")
                                time.sleep(1)
                                fig_3d()

                            # Prisma regular de base triangular escalena/isóceles y altura h
                            else:
                                s = (a1 + a2 + a3) / 2
                                area_base = s * (s - a1) * (s - a2) * (s - a3)
                                area_basal = math.sqrt(area_base)
                                volumen = area_basal * h
                                print(f"\nEl volumen de este prisma corresponde a {volumen:.2f} unidades cúbicas.")
                                print("Nota: Valor aproximado a la centésima.")
                                time.sleep(10)
                                print("\nRegresando al menú principal...")
                                time.sleep(3)
                                main()

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
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()
                            else:
                                area_pr_quad = 2 * (l1 * l2 + l1 * h_pr_qd + l2 * h_pr_qd)
                                print(f"\nEl área total de este prisma es de {area_pr_quad} unidades cuadradas.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()

                        # Volumen de un prisma de base cuadrangular
                        elif opt == 2:
                            l1 = float(input("\nIngrese la medida de un lado del rectángulo de la base: "))
                            l2 = float(input("Ingrese la medida del otro lado del rectángulo de la base: "))
                            h_pr_qd = float(input("Ingrese la medida de la altura: "))
                            if l1 <= 0 or l2 <= 0:
                                print("\nError: Los lados basales no pueden poseer valores menores o iguales a cero.")
                                time.sleep(5)
                                print("Regresando al menú principal...")
                                main()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()
                            elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                print("\nError: Está calculando el volumen de un cubo.")
                                print(f"El volumen de este cubo es de {l1 * l2 * h_pr_qd} unidades cúbicas.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()
                            else:
                                vol_pr_qd = l1 * l2 * h_pr_qd
                                print(f"\nEl volumen de este prisma es de {vol_pr_qd} unidades cúbicas.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()

                        # Diagonal de un prisma cuadrangular
                        elif opt == 3:
                            l1 = float(input("\nIngrese la medida de un lado del rectángulo de la base: "))
                            l2 = float(input("Ingrese la medida del otro lado del rectángulo de la base: "))
                            h_pr_qd = float(input("Ingrese la medida de la altura: "))
                            if l1 <= 0 or l2 <= 0:
                                print("\nError: Los lados basales no pueden poseer valores menores o iguales a cero.")
                                time.sleep(7)
                                print("Regresando al menú principal...")
                                time.sleep(3)
                                main()
                            elif h_pr_qd <= 0:
                                print("\nError: La altura no puede albergar un valor negativo o igual a cero.")
                                time.sleep(10)
                                print("Regresando al menú principal...")
                                main()
                            elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                print("\nError: Está calculando la diagonal de un cubo.")
                                print(f"La diagonal tiene una medida de {(l1 * math.sqrt(3)):.2f} unidades.")
                                time.sleep(7)
                                print("Regresando al menú principal...")
                                time.sleep(3)
                                main()
                            else:
                                diag_pr_qd_sq = l1 ** 2 + l2 ** 2 + h_pr_qd ** 2
                                diag_pr_qd = math.sqrt(diag_pr_qd_sq)
                                print(f"\nLa diagonal de este prisma tiene una medida de {diag_pr_qd:.2f} unidades.")
                                print("Nota: Valor aproximado a la centésima.")
                                time.sleep(7)
                                print("Regresando al menú principal...")
                                time.sleep(3)
                                main()

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
                        print("\nRegresando al menú principal...")
                        time.sleep(3)
                        main()

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
                        print("\nRegresando al menú principal...")
                        time.sleep(3)
                        main()

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
                            print("Regresando al menú principal...")
                            time.sleep(3)
                            main()

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
                            print("Volviendo al menú principal...")
                            time.sleep(3)
                            main()

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
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

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
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

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
                                print("Regresando al menú principal...")
                                time.sleep(2)
                                main()

                    # Otro valor
                    else:
                        print("\nOperación incorrecta.")
                        time.sleep(2)
                        print("Regresando al menú principal...")
                        time.sleep(1)
                        main()

                # Pirámides oblicuas
                elif opt == 2:
                    print("en desarrollo")
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
        print("\tProgramado en Python 3.8")
        time.sleep(3)
        print("\nProgramación: Qm_Dev")
        time.sleep(3)
        print("Diseño: Qm_Dev")
        time.sleep(3)
        print("Testeo: Qm_Dev")
        time.sleep(3)
        print("Agradecimientos especiales: Alejandro Taboada Sánchez")
        time.sleep(5)
        main()

    # Salir del programa
    elif opcion == 4:
        time.sleep(0.2)
        print("\nSaliendo del programa...")
        time.sleep(0.8)
        exit()

    # pascua
    elif opcion == 2082019:
        time.sleep(3)
        print("\n\t'Si puedes imaginarlo, puedes programarlo.'")
        time.sleep(3)
        print("\t- Alejandro Taboada Sánchez")
        time.sleep(5)
        main()

    # Otro valor
    else:
        time.sleep(0.1)
        print("\nError: Operación incorrecta.")
        print("Reiniciando programa...")
        time.sleep(2)
        main()


main()
