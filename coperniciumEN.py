import math
import time

version = "Alpha 7.1"
lang = "EN"
redo = 0

while redo == 0:

    try:
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
            print("\nWelcome to the program. Please, select an option.")
            print("\t1 - Polygons (2D)")
            print("\t2 - Polyhedra (3D)")
            print("\t3 - Credits")
            print("\t4 - Exit")
            option = int(input("Option: "))

            # 2D Figures
            if option == 1:
                def fig_2d():
                    print("\nSelect a polygon.")
                    print("1 - Quadrilaterals")
                    print("2 - Circumference")
                    print("3 - Triangles")
                    print("4 - Pentagons")
                    print("5 - Return to main menu")
                    option = int(input("Option: "))

                    # Quadrilaterals
                    if option == 1:
                        def quadrilaterals():
                            print("\nChoose a figure:")
                            print("1 - Square")
                            print("2 - Rectangle")
                            print("3 - Rhombus")
                            print("4 - Romboide")
                            print("5 - Trapezium")
                            print("6 - Trapezoid")
                            print("7 - Choose another polygon")
                            option = int(input("Option: "))

                            # Square
                            if option == 1:
                                print("\nChoose an aspect to calculate.")
                                print("1 - Area")
                                print("2 - Perimeter")
                                print("3 - Diagonal")
                                print("4 - Choose another quadrilateral")
                                option = int(input("Option: "))

                                # Square area
                                if option == 1:
                                    side = float(input("Input the value of the side: "))
                                    area_sq = side ** 2
                                    if side <= 0:
                                        print("\nError: Sides can't have negative or equal to zero values.")
                                        time.sleep(2)
                                        print("Returning to the polygons menu...")
                                        time.sleep(1)
                                        fig_2d()
                                    else:
                                        print(f"\nThe square area of this square is {area_sq} square units.")
                                        time.sleep(4)
                                        print("Returning to the polygons menu...")
                                        time.sleep(2)
                                        fig_2d()

                                # Perimeter of square
                                elif option == 2:
                                    side = float(input("Input the value of the side: "))
                                    perim_sq = side * 4
                                    if side <= 0:
                                        print("\nError: Sides can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to the polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print(f"\nThe perimeter of this square is {perim_sq} units.")
                                        time.sleep(4)
                                        print("Returning to the polygons menu...")
                                        time.sleep(2)
                                        fig_2d()

                                # Diagonal of square
                                elif option == 3:
                                    side = float(input("Input the value of the side: "))
                                    diag_sq = ((side ** 2) + (side ** 2))
                                    diag_sq_final = (math.sqrt(diag_sq))
                                    if side <= 0:
                                        print("\nError: Sides can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to the polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print(f"\nThe diagonal of this square is {diag_sq_final:.2f} units.")
                                        time.sleep(4)
                                        print("Returning to the polygons menu...")
                                        time.sleep(2)
                                        fig_2d()

                                # Choose another quadrilateral
                                elif option == 4:
                                    quadrilaterals()

                                # Other value
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Rectangle
                            elif option == 2:
                                print("\nChoose an aspect to calculate.")
                                print("1 - Area")
                                print("2 - Perimeter")
                                print("3 - Diagonal")
                                print("4 - Choose another quadrilateral")
                                option = int(input("Option: "))

                                # Rectangle area
                                if option == 1:
                                    print("\nInput the width and length of the rectangle:")
                                    width = float(input("\nWidth: "))
                                    length = float(input("Length: "))
                                    area_rect = width * length
                                    print(f"\nThe area of this rectangle is {area_rect} square units.")
                                    time.sleep(4)
                                    print("Returning to polygons menu...")
                                    time.sleep(2)
                                    fig_2d()

                                # Rectangle perimeter
                                elif option == 2:
                                    print("\nInput the width and length of the rectangle:")
                                    width = float(input("Width: "))
                                    length = float(input("Length: "))
                                    perim_rect = (width * 2) + (length * 2)
                                    print(f"\nThe perimeter of this rectangle is {perim_rect} units.")
                                    time.sleep(4)
                                    print("Returning to polygons menu...")
                                    time.sleep(2)
                                    fig_2d()

                                # Rectangle diagonal
                                elif option == 3:
                                    print("\nInput the width and length of the rectangle:")
                                    width = float(input("Width: "))
                                    length = float(input("Length: "))
                                    diag_rect = (width ** 2) + (length ** 2)
                                    diag_rect_final = (math.sqrt(diag_rect))
                                    print(f"\nThe diagonal of this rectangle is {diag_rect_final:.2f} units.")
                                    time.sleep(4)
                                    print("Returning to the polygons menu...")
                                    time.sleep(2)
                                    fig_2d()

                                # Choose another quadrilateral
                                elif option == 4:
                                    quadrilaterals()

                                # Other value
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Rhombus
                            elif option == 3:
                                print("\nChoose an aspect to calculate.")
                                print("1 - Area")
                                print("2 - Perimeter")
                                print("3 - Choose another quadrilateral")
                                option = int(input("Option: "))

                                # Rhombus area
                                if option == 1:
                                    D = float(input("\nInput the value of the longest diagonal: "))
                                    d = float(input("Input the value of the shortest diagonal: "))
                                    area_romb = (D * d) / 2
                                    if D > 0 and d > 0:
                                        print(f"\nThe area of this rhombus is {area_romb:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print("\nError: The input values can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to quadrilaterals menu...")
                                        time.sleep(2)
                                        quadrilaterals()

                                # Rhombus perimeter
                                elif option == 2:
                                    D = float(input("\nInput the value of the longest diagonal: "))
                                    d = float(input("Input the value of the shortest diagonal: "))
                                    perim_romb = 2 * (math.sqrt((D ** 2) + (d ** 2)))
                                    if D > 0 and d > 0:
                                        print(f"\nThe perimeter of this rhombus is {perim_romb:.2f} units.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print("\nError: The input values can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to quadrilaterals menu...")
                                        time.sleep(2)
                                        quadrilaterals()

                                # Choose another quadrilateral
                                elif option == 3:
                                    quadrilaterals()

                                # Other value
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Rhomboid
                            elif option == 4:
                                print("\nChoose an aspect to calculate.")
                                print("1 - Area")
                                print("2 - Perimeter")
                                print("3 - Choose another quadrilateral")
                                option = int(input("Option: "))

                                # Rhomboid area
                                if option == 1:
                                    b = float(input("\nInput the value of the side that acts as the base: "))
                                    h = float(input("Input the value of the relative height: "))
                                    area_rhomboid = b * h
                                    if b <= 0 or h <= 0:
                                        print("\nError: The input values can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print(f"\nThe area of the rhomboid is {area_rhomboid:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()

                                # Rhomboid perimeter
                                elif option == 2:
                                    a = float(input("\nInput the value of one side: "))
                                    b = float(input("Ingput the value of another side: "))
                                    perim_rhomboid = 2 * (a + b)
                                    if a <= 0 or b <= 0:
                                        print("\nError: The input values can't have negative or equal to zero values.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()
                                    else:
                                        print(f"\nThe perimeter of the rhomboid is {perim_rhomboid:.2f} units.")
                                        time.sleep(3)
                                        print("Returning to polygons menu...")
                                        time.sleep(2)
                                        fig_2d()

                                # Choose another figure
                                elif option == 3:
                                    quadrilaterals()

                                # Other value
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Trapecio
                            elif option == 5:
                                print("\nWIP...")
                                time.sleep(2)
                                main()

                            # Trapezoide
                            elif option == 6:
                                print("\nWIP...")
                                time.sleep(2)
                                main()

                            # Choose another polygon
                            elif option == 7:
                                fig_2d()

                            # Another value
                            else:
                                print("\nError: Wrong operation.")
                                time.sleep(2)
                                print("Returning to main menu...")
                                time.sleep(1)
                                main()

                        quadrilaterals()

                    # Circumference
                    elif option == 2:
                        print("\nChoose an aspect to calculate.")
                        print("1 - Area")
                        print("2 - Perimeter")
                        print("3 - Diameter")
                        print("4 - Choose another polygon")
                        option = int(input("Option: "))

                        # Circumference area
                        if option == 1:
                            print("\nInput the value of the radio of the circumference.")
                            radio = float(input("Radio: "))
                            area_cir = math.pi * (radio ** 2)
                            print(f"\nThe area of this circumference is {area_cir:.3f} square units.")
                            print(f"'π' as an X: {radio ** 2}π square units.")
                            time.sleep(3)
                            print("Returning to polygons menu...")
                            time.sleep(2)
                            fig_2d()

                        # Circumference perimeter
                        elif option == 2:
                            print("\nInput the value of the radio of the circumference.")
                            radio = float(input("Radio: "))
                            perim_circ = 2 * radio * math.pi
                            print(f"\nThe perimeter of this circumference is {perim_circ:.3f} units.")
                            print(f"'π' as an X: {(2 * radio)}π units.")
                            time.sleep(2)
                            print("Returning to polygons menu...")
                            time.sleep(2)
                            fig_2d()

                        # Circumference diameter
                        elif option == 3:
                            print("\nInput the value of the radio of the circumference.")
                            radio = float(input("Radio: "))
                            print(f"\nThe diameter of this circumference is {2 * radio} units.")
                            time.sleep(2)
                            print("Returning to polygons menu...")
                            time.sleep(2)
                            fig_2d()

                        # Choose another polygon
                        elif option == 4:
                            fig_2d()

                        # Another value
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Triangles
                    elif option == 3:
                        def triangle():
                            print("\nChoose a classification to work with.")
                            print("1 - Side measurement")
                            print("2 - Angle width")
                            print("3 - Trigonometry (Sides & Angles)")
                            print("4 - Obtain angles")
                            print("5 - Choose another polygon")
                            option = int(input("Classification: "))

                            # Triangles by side measurement
                            if option == 1:
                                print("\nChoose the triangle.")
                                print("1 - Equilateral")
                                print("2 - Isosceles")
                                print("3 - Scalene")
                                print("4 - Return to the triangles menu")
                                option = int(input("Classification: "))

                                # Equilateral Triangle
                                if option == 1:
                                    print("\nChoose an aspect to calculate.")
                                    print("1 - Area")
                                    print("2 - Perimeter")
                                    print("3 - Height")
                                    option = int(input("Option: "))

                                    # Area - Equilateral triangle
                                    if option == 1:
                                        lado = float(input("\nInput the value of the side: "))
                                        area_tr_eq = (math.sqrt(3) / 4) * (lado ** 2)
                                        print(f"\nThe area of the triangle is {area_tr_eq:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Perimeter - Equilateral triangle
                                    elif option == 2:
                                        lado = float(input("\nInput the value of the side: "))
                                        print(f"\nThe perimeter of the triangle is {lado * 3} units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Height - Equilateral Triangle
                                    elif option == 3:
                                        lado = float(input("\nInput the value of the side: "))
                                        h_tr_eq = (math.sqrt(3) * lado) / 2
                                        print(f"\nThe height of the triangle is {h_tr_eq:.2f} units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Other
                                    else:
                                        print("\nError: Wrong operation.")
                                        time.sleep(2)
                                        print("Returning to main menu...")
                                        time.sleep(1)
                                        main()

                                # Isosceles Triangle
                                elif option == 2:
                                    print("\nChoose an aspect to calculate.")
                                    print("1 - Area")
                                    print("2 - Perimeter")
                                    print("3 - Height")
                                    option = int(input("Option: "))

                                    # Area - Isosceles Triangle
                                    if option == 1:
                                        lado1 = float(input("\nInput the value of the equal sides: "))
                                        lado2 = float(input("Input the value of the base: "))
                                        if lado1 * 2 <= lado2:
                                            print("\nError: The input values don't meet the triangle inequality.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                            alt_tr_is = math.sqrt(equation_h)
                                            area_tr_is = (lado2 * alt_tr_is) / 2
                                            print(
                                                f"\nThe area of the triangle is {area_tr_is:.2f} square units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Perimeter - Isosceles Triangle
                                    elif option == 2:
                                        lado1 = float(input("\nInput the value of the equal sides: "))
                                        lado2 = float(input("Input the value of the base: "))
                                        if lado1 * 2 <= lado2:
                                            print("\nError: The input values don't meet the triangle inequality.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(f"\nThe perimeter of this triangle is {lado1 * 2 + lado2} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Height - Isosceles Triangle
                                    elif option == 3:
                                        lado1 = float(input("\nInput the value of the equal sides: "))
                                        lado2 = float(input("Input the value of the base: "))
                                        if lado1 * 2 <= lado2:
                                            print("\nError: The input values don't meet the triangle inequality.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            equation_h = lado1 ** 2 - (lado2 ** 2 / 4)
                                            alt_tr_is = math.sqrt(equation_h)
                                            print(f"\nThe height of the triangle is {alt_tr_is:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                    else:
                                        print("\nError: Wrong operation.")
                                        time.sleep(2)
                                        print("Returning to main menu...")
                                        time.sleep(1)
                                        main()

                                # Scalene Triangle
                                elif option == 3:
                                    print("\nChoose an aspect to calculate.")
                                    print("1 - Area")
                                    print("2 - Perimeter")
                                    print("3 - Heights")
                                    option = int(input("Option: "))

                                    # Area - Scalene Triangle
                                    if option == 1:
                                        lado1 = float(input("\nInput the value of the first side: "))
                                        lado2 = float(input("Input the value of the second side: "))
                                        lado3 = float(input("Input the value of the third side: "))
                                        s_perim = (lado1 + lado2 + lado3) / 2
                                        form_heron_sq = s_perim * (s_perim - lado1) * (s_perim - lado2) * (s_perim - lado3)
                                        form_heron = math.sqrt(form_heron_sq)
                                        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                                            print("\nError: Input values must be greater than zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 == lado2 and lado1 == lado3:
                                            print("\nError: The sides are equal.")
                                            print("This is an equilateral triangle.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                            print("\nError: The input values don't meet the triangle inequality.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(f"\nThe area of this triangle is {form_heron:.2f} square units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Perimeter - Scalene Triangle
                                    if option == 2:
                                        lado1 = float(input("\nInput the value of the first side: "))
                                        lado2 = float(input("Input the value of the second side: "))
                                        lado3 = float(input("Input the value of the third side: "))
                                        perim_tr_esc = lado1 + lado2 + lado3
                                        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                                            print("\nError: Input values must be greater than zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 == lado2 and lado1 == lado3:
                                            print("\nError: The sides are equal.")
                                            print("This is an equilateral triangle.")
                                            print(f"\nThe perimeter of this triangle is {perim_tr_esc:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 == lado2 or lado2 == lado1:
                                            print("\nError: Side 1 and 2 share the same value. "
                                                  "This is an isosceles triangle.")
                                            print(f"The perimeter of this triangle is {perim_tr_esc:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado2 == lado3 or lado3 == lado2:
                                            print(
                                                "\nError: Side 2 and 3 share the same value. "
                                                "This is an isosceles triangle.")
                                            print(f"The perimeter of this triangle is {perim_tr_esc:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 == lado3 or lado3 == lado1:
                                            print(
                                                "\nError: Side 1 and 3 share the same value. "
                                                "This is an isosceles triangle.")
                                            print(f"The perimeter of this triangle is {perim_tr_esc:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        elif lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
                                            print("\nError: The input values don't meet the triangle inequality.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(
                                                f"\nThe perimeter of this triangle is {perim_tr_esc:.2f} units.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    #  Heights - Scalene Triangle
                                    if option == 3:
                                        lado1 = float(input("\nInput the value of the first side: "))
                                        lado2 = float(input("Input the value of the second side: "))
                                        lado3 = float(input("Input the value of the third side: "))
                                        s_perim = (lado1 + lado2 + lado3) / 2
                                        form_heron_sq = s_perim * (s_perim - lado1) * (s_perim - lado2) * (s_perim - lado3)
                                        form_heron = math.sqrt(form_heron_sq)
                                        ha = (2 / lado1) * form_heron
                                        hb = (2 / lado2) * form_heron
                                        hc = (2 / lado3) * form_heron
                                        if ha <= 0 or hb <= 0 or hc <= 0:
                                            print("\nError: Input values must be greater than zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(f"\nThe heights of the triangle are {ha:.2f} units, {hb:.2f}"
                                                  f" units and {hc:.2f} units respectively.")
                                            print("These values are rounded to the hundredth.")
                                            time.sleep(6)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                # Return
                                elif option == 4:
                                    triangle()

                                # Wrong operation
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Triangles by angle width
                            elif option == 2:
                                print("\nChoose the triangle.")
                                print("1 - Rectangular")
                                print("2 - Return to the triangles menu")
                                option = int(input("Option: "))

                                # Rectangular Triangle
                                if option == 1:
                                    print("\nChoose an aspect to calculate.")
                                    print("1 - Area")
                                    print("2 - Perimeter")
                                    print("3 - Hypotenuse by Pythagoras Theorem")
                                    print("4 - Missing cathetus by Pythagoras Theorem")
                                    option = int(input("Option: "))

                                    # Area - Rectangular triangle
                                    if option == 1:
                                        cat1 = float(input("\nInput the value from one cathetus: "))
                                        cat2 = float(input("Input the value from the other cathetus: "))
                                        area_tr_rec = (cat1 + cat2) / 2
                                        print(f"\nThe area of this triangle is {area_tr_rec:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Perimeter - Rectangular triangle
                                    elif option == 2:
                                        cat1 = float(input("\nInput the value from one cathetus: "))
                                        cat2 = float(input("Input the value from the other cathetus: "))
                                        hip = float(input("Input the value of the hypotenuse: "))
                                        perim_tr_rect = cat1 + cat2 + hip
                                        print(f"\nThe perimeter of the triangle is {perim_tr_rect} units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Hypotenuse - Rectangular triangle
                                    elif option == 3:
                                        cat1 = float(input("\nInput the value from one cathetus: "))
                                        cat2 = float(input("Input the value from the other cathetus: "))
                                        hip_sq = (cat1 ** 2) + (cat2 ** 2)
                                        hip = math.sqrt(hip_sq)
                                        print(f"\nThe hypotenuse of this triangle is {hip} units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Find the missing cathetus
                                    elif option == 4:
                                        cat1 = float(input("\nInput the value of the cathetus: "))
                                        hip = float(input("Input the value of the hypotenuse: "))
                                        x = hip ** 2 - cat1 ** 2
                                        cat2 = math.sqrt(x)
                                        print(f"\nThe size of the missing cathetus is {cat2:.2f} units.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Operación no reconocida
                                    else:
                                        print("\nError: Wrong operation.")
                                        time.sleep(2)
                                        print("Returning to main menu...")
                                        time.sleep(1)
                                        main()

                                # Volver atrás
                                elif option == 2:
                                    triangle()

                                # Wrong operation
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Trigonometry (Sides & Angles)
                            elif option == 3:
                                print("\nThese problems are done exclusively with rectangular triangles.")
                                print("That means, triangles with a 90 degrees angle on them.")
                                time.sleep(4)
                                print("WARNING! At the moment, the results are in radian.")
                                time.sleep(4)
                                print("\nChoose a trigonometric function:")
                                time.sleep(1.5)
                                print("1 - Sine")
                                print("2 - Cosine")
                                print("3 - Tangent")
                                print("4 - Cosecant")
                                print("5 - Secant")
                                print("6 - Cotangent")
                                print("7 - Return to the triangles menu")
                                option = int(input("Option: "))

                                # Sine
                                if option == 1:
                                    co = float(input("\nInput the value of the opposite cathetus: "))
                                    hip = float(input("Input the value of the hypotenuse: "))
                                    sin = co / hip
                                    sin_f = math.sin(sin)
                                    print(f"\nThe value of the sine is {sin_f:.5f} radians.")
                                    time.sleep(3)
                                    print("Returning to the triangles menu...")
                                    time.sleep(2)
                                    triangle()

                                # Cosine
                                elif option == 2:
                                    ca = float(input("\nInput the value of the adjacent cathetus: "))
                                    hip = float(input("Input the value of the hypotenuse: "))
                                    cos = ca / hip
                                    cos_f = math.cos(cos)
                                    print(f"\nThe value of the cosine is {cos_f:.5f} radians.")
                                    time.sleep(3)
                                    print("Returning to the triangles menu...")
                                    time.sleep(2)
                                    triangle()

                                # Tangent
                                elif option == 3:
                                    co = float(input("\nInput the value of the opposite cathetus: "))
                                    ca = float(input("Input the value of the adjacent cathetus: "))
                                    tan = co / ca
                                    tan_f = math.tan(tan)
                                    print(f"\nThe value of the tangent is {tan_f:.5f} radians.")
                                    time.sleep(3)
                                    print("Returning to the triangles menu...")
                                    time.sleep(2)
                                    triangle()

                                # Cosecant
                                elif option == 4:
                                    print("\nDepending on what would you do this?")
                                    print("1 - Hypotenuse and opposite cathetus")
                                    print("2 - Value of sine of the angle")
                                    print("3 - Angle")
                                    en_function = int(input("Option: "))

                                    # Hypotenuse and Opposite cathetus
                                    if en_function == 1:
                                        co = float(input("\nInput the value of the opposite cathetus: "))
                                        hip = float(input("Input the value of the hypotenuse: "))
                                        csc = hip / co
                                        if co <= 0 or hip <= 0:
                                            print("\nError: Input values must be greater than zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(f"\nThe cosecant of this triangle is {csc:.5f} radians.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Sine of the angle
                                    elif en_function == 2:
                                        sen = float(input("\nInput the value of the sin: "))
                                        csc = 1 / sen
                                        print(f"\nThe cosecant of this triangle is {csc:.5f} radians.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Angle
                                    elif en_function == 3:
                                        a = float(input("\nInput the value of the angle in radians: "))
                                        csc = 1 / math.sin(a)
                                        print(f"\nThe cosecant of this triangle is {csc:.5f} radians.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Wrong Operation
                                    else:
                                        print("\nError: Wrong operation.")
                                        time.sleep(2)
                                        print("Returning to main menu...")
                                        time.sleep(1)
                                        main()

                                # Secant
                                elif option == 5:
                                    print("\nDepending on what would you do this?")
                                    print("1 - Hypotensue and adjacent cathetus")
                                    print("2 - Value of the cosine of the angle")
                                    print("3 - Angle")
                                    en_function = int(input("Option: "))

                                    # Hypotenuse and adjacent cathetus
                                    if en_function == 1:
                                        hip = float(input("Input the value of the hypotenuse: "))
                                        ca = float(input("\nInput the value of the adjacent cathetus: "))
                                        sec = hip / ca
                                        if hip <= 0 or ca <= 0:
                                            print("\nError: Input values must be greater than zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            print(f"\nThe secant of this triangle is {sec:.5f} radians.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Cosine value
                                    elif en_function == 2:
                                        cos = float(input("Ingrese el valor de coseno: "))
                                        if cos == 0:
                                            print("You can't divide by zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            sec = 1 / cos
                                            print(f"\nThe secant of this triangle is {sec:.5f} radians.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Angle
                                    elif en_function == 3:
                                        a = float(input("\nInput the value of the angle in radians: "))
                                        sec = 1 / math.cos(a)
                                        print(f"The secant of this triangle is {sec:.5f} radians.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Wrong Operation
                                    else:
                                        print("\nError: Wrong operation.")
                                        time.sleep(2)
                                        print("Returning to the triangle menu..")
                                        time.sleep(2)
                                        triangle()

                                # Cotangent
                                elif option == 6:
                                    print("\nDepending on what would you do this?")
                                    print("1 - Adjacent cathetus and opposite cathetus")
                                    print("2 - Value of the tangent of the angle")
                                    print("3 - Angle")
                                    en_function = int(input("Option: "))

                                    # Adjacent cathetus and opposite cathetus
                                    if en_function == 1:
                                        ca = float(input("\nInput the value of the adjacent cathetus: "))
                                        co = float(input("Input the value of the opposite cathetus: "))
                                        cotg = ca / co
                                        print(f"\nThe cotangent of this triangle is {cotg:.5f} radians.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                    # Tangent value
                                    elif en_function == 2:
                                        tan = float(input("\nInput the value of the tangent: "))
                                        if tan == 0 or tan > 1 or tan < -1:
                                            print("Error: Input value must be between -1 and 1, excluding zero.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            cotg = 1 / tan
                                            print(f"\nThe value of the cotangent is {cotg:.5f} radians.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                    # Angle
                                    elif en_function == 3:
                                        a = float(input("Input the value of the angle in radians: "))
                                        if a == 90 or a == 270:
                                            print("\nError: The tangent is not expressed in this value.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()
                                        else:
                                            sec = 1 / math.tan(a)
                                            print(f"\nThe cotangent of this triangle is {sec:.5f} radians.")
                                            time.sleep(3)
                                            print("Returning to the triangles menu...")
                                            time.sleep(2)
                                            triangle()

                                # Return to triangle menu
                                elif option == 7:
                                    triangle()

                                # Wrong operation
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to triangle menu...")
                                    time.sleep(1)
                                    triangle()

                            # Obtain angles
                            elif option == 4:
                                print("\nThese calculations are exclusively done with rectangular triangles.")
                                time.sleep(3)
                                print("How you want to obtain the angle?")
                                print("\n1 - Measure of the other angle")
                                option = int(input("Option: "))

                                # Measure of the other angle
                                if option == 1:
                                    a = float(input("\nInput the value of the angle in degrees: "))
                                    if a <= 0 or a > 90:
                                        print("Error: Input angle is lower or equal to zero, or greater than 90.")
                                        time.sleep(3)
                                        print("Returning to triangles menu...")
                                        time.sleep(2)
                                        triangle()
                                    else:
                                        ang_fal = 90 - a
                                        print(f"\nThe missing angle is {ang_fal:.2f} degrees.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()

                                # Inverse trigonometric functions (arcosine, arcocosine)
                                # Work In Progress
                                elif option == 9:
                                    co = float(input("\nInput the value of the opposite cathetus: "))
                                    ca = float(input("\nInput the value of the adjacent cathetus: "))
                                    if ca <= 0 or co <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the triangles menu...")
                                        time.sleep(2)
                                        triangle()
                                    else:
                                        print("WIP")
                                        time.sleep(1)
                                        main()

                                # Wrong operation
                                else:
                                    print("\nError: Wrong operation.")
                                    time.sleep(2)
                                    print("Returning to main menu...")
                                    time.sleep(1)
                                    main()

                            # Return to Fig_2d menu
                            elif option == 5:
                                fig_2d()

                            # Wrong operation
                            else:
                                print("\nError: Wrong operation.")
                                time.sleep(2)
                                print("Returning to triangles menu...")
                                time.sleep(1)
                                triangle()

                        triangle()

                    # Pentagon
                    elif option == 4:
                        print("\nThese calculations are done with a regular pentagon.")
                        time.sleep(1)
                        print("\nChoose an aspect to calculate.")
                        print("1 - Area")
                        print("2 - Perimeter")
                        print("3 - Apothem")
                        print("4 - Choose another polygon")
                        option = int(input("Option: "))

                        # Area - Pentagon
                        if option == 1:
                            lado = float(input("Input the value of one of the sides: "))
                            area = (lado ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4
                            if lado <= 0:
                                print("\nError: Input values must be greater than zero.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"The area of this pentagon is {area:.2f} square units.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()

                        # Perimeter - Pentagon
                        elif option == 2:
                            lado = float(input("Input the value of one of the sides: "))
                            perim_penta = 5 * lado
                            if lado <= 0:
                                print("\nError: Input values must be greater than zero.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"The perimeter of this pentagon is {perim_penta} units.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()

                        # Apothem - Pentagon
                        elif option == 3:
                            lado = float(input("Input the value of one of the sides: "))
                            apot_pent = (lado / 2) * (math.sqrt(1 + (2 / math.sqrt(5))))
                            if lado <= 0:
                                print("\nError: Input values must be greater than zero.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()
                            else:
                                print(f"The apothem of this pentagon is {apot_pent} units.")
                                time.sleep(3)
                                print("Returning to polygons menu...")
                                time.sleep(2)
                                fig_2d()

                        # Choose another polygon
                        elif option == 4:
                            fig_2d()

                        # Wrong Operation
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Main Menu
                    elif option == 5:
                        main()

                    # Other value
                    else:
                        print("\nError: Wrong operation.")
                        time.sleep(2)
                        print("Returning to main menu...")
                        time.sleep(1)
                        main()

                fig_2d()

            # Polyhedra (3D)
            elif option == 2:
                def fig_3d():
                    print("\nChoose a polyhedron.")
                    print("1 - Cube")
                    print("2 - Prisms")
                    print("3 - Sphere")
                    print("4 - Cylinder")
                    print("5 - Pyramid")
                    print("6 - Return to main menu")
                    opt = int(input("Option: "))

                    # Cube
                    if opt == 1:
                        print("\nChoose an aspect to calculate.")
                        print("1 - Area")
                        print("2 - Volume")
                        print("3 - Diagonal")
                        print("4 - Choose another polyhedron")
                        opt = int(input("Option: "))

                        # Area - Cube
                        if opt == 1:
                            a = float(input("\nInput the value of the edge of the cube: "))
                            area_cubo = 6 * (a ** 2)
                            print(f"\nThe total area of this cube is {area_cubo} square units.")
                            time.sleep(3)
                            print("Returning to the polyhedra menu...")
                            time.sleep(2)
                            fig_3d()

                        # Volume - Cube
                        elif opt == 2:
                            a = float(input("\nInput the value of the edge of the cube: "))
                            vol_cubo = a ** 3
                            print(f"\nThe volume of this cube is {vol_cubo} cubic units.")
                            time.sleep(3)
                            print("Returning to the polyhedra menu...")
                            time.sleep(2)
                            fig_3d()

                        # Diagonal - Cube
                        elif opt == 3:
                            a = float(input("\nInput the value of the edge of the cube: "))
                            diag_cubo = a * math.sqrt(3)
                            print(f"\nThe diagonal of this cube is {diag_cubo:.2f} units.")
                            time.sleep(3)
                            print("Returning to the polyhedra menu...")
                            time.sleep(2)
                            fig_3d()

                        # Return to the polyhedra menu
                        elif opt == 4:
                            fig_3d()

                        # Other value
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Prism
                    elif opt == 2:
                        print("\nChoose the prism to work with:")
                        print("1 - Regular prism")
                        print("2 - Choose another polyhedron")
                        opt = int(input("Option: "))

                        # Regular Prism
                        if opt == 1:
                            print("\nChoose a base:")
                            print("1 - Triangular")
                            print("2 - Quadrangular")
                            opt = int(input("Option: "))

                            # Triangular base
                            if opt == 1:
                                print("\nChoose an aspect to calculate: ")
                                print("1 - Areas")
                                print("2 - Volume")
                                opt = int(input("Option: "))

                                # Areas - Triangular base prism
                                if opt == 1:
                                    a1 = float(input("\nInput the value of one edge of the base: "))
                                    a2 = float(input("Input the value of other edge from the base: "))
                                    a3 = float(input("Input the value of other edge from the base: "))
                                    h = float(input("Input the height of the prism: "))

                                    # Triangular base prism equilateral and height h
                                    if (a1 + a2 + a3) / 3 == a1 and a2 and a3:
                                        area_basal = (math.sqrt(3) / 4) * (a1 ** 2)
                                        area_lat = a1 * h
                                        area_total = 2 * area_basal + 3 * area_lat
                                        print(f"\nThe total area of this prism is {area_total:.2f} square units.")
                                        print(f"The basal area of this prism is {area_basal:.2f} square units.")
                                        print(f"The lateral area of the prism is {area_lat} square units.")
                                        time.sleep(7)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(3)
                                        fig_3d()

                                    # Edge <= 0
                                    elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(2)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(1)
                                        fig_3d()

                                    # Height <= 0
                                    elif h <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(2)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(1)
                                        fig_3d()

                                    # Triangular base prism scalene or isosceles and height h
                                    else:
                                        s = (a1 + a2 + a3) / 2
                                        perim = s * 2
                                        area_base = s * (s - a1) * (s - a2) * (s - a3)
                                        area_basal = math.sqrt(area_base)
                                        area_lat = perim * h
                                        area_total = 2 * area_basal + 3 * area_lat
                                        print(f"\nThe total area of this prism is {area_total:.2f} square units.")
                                        print(f"The basal area of this prism is {area_basal:.2f} square units.")
                                        print(f"The lateral area of the prism is {area_lat} square units.")
                                        time.sleep(7)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(3)
                                        fig_3d()

                                # Volume - Triangular base prism
                                elif opt == 2:
                                    a1 = float(input("\nInput the value of one edge of the base: "))
                                    a2 = float(input("Input the value of other edge from the base: "))
                                    a3 = float(input("Input the value of other edge from the base: "))
                                    h = float(input("Input the height of the prism: "))

                                    # Triangular base prism equilateral and height h
                                    if (a1 + a2 + a3) / 3 == a1 and a2 and a3:
                                        area_basal = (math.sqrt(3) * (a1 ** 2)) / 4
                                        volumen = area_basal * h
                                        print(f"\nThe volume of this prism is {volumen} cubic units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                                    # Edge <= 0
                                    elif a1 <= 0 or a2 <= 0 or a3 <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(2)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(1)
                                        fig_3d()

                                    # Height <= 0
                                    elif h <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(2)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(1)
                                        fig_3d()

                                    # Triangular base prism scalene or isosceles and height h
                                    else:
                                        s = (a1 + a2 + a3) / 2
                                        area_base = s * (s - a1) * (s - a2) * (s - a3)
                                        area_basal = math.sqrt(area_base)
                                        volumen = area_basal * h
                                        print(f"\nThe volume of this prism is {volumen:.2f} cubic units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                            # Quadrangular base
                            elif opt == 2:
                                print("\nChoose an aspect to calculate: ")
                                print("1 - Areas")
                                print("2 - Volume")
                                print("3 - Diagonal")
                                opt = int(input("Option: "))

                                # Areas - Quadrangular base prism
                                if opt == 1:
                                    l1 = float(input("\nEnter the measurement of one side of the base rectangle: "))
                                    l2 = float(input("Enter the measurement of another side of the base rectangle: "))
                                    h_pr_qd = float(input("Input the height: "))
                                    if l1 <= 0 or l2 <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    elif h_pr_qd <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        area_pr_quad = 2 * (l1 * l2 + l1 * h_pr_qd + l2 * h_pr_qd)
                                        print(f"\nThe total area of this prism is {area_pr_quad} square units.")
                                        time.sleep(4)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(1)
                                        fig_3d()

                                # Volume - Quadrangular base prism
                                elif opt == 2:
                                    l1 = float(input("\nEnter the measurement of one side of the base rectangle: "))
                                    l2 = float(input("Enter the measurement of another side of the base rectangle: "))
                                    h_pr_qd = float(input("Input the height: "))
                                    if l1 <= 0 or l2 <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    elif h_pr_qd <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                        print("\nError: You're calculating the volume of a cube.")
                                        print(f"The volume of this cube is {l1 * l2 * h_pr_qd} cubic units.")
                                        time.sleep(8)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        vol_pr_qd = l1 * l2 * h_pr_qd
                                        print(f"\nThe volume of this prism is {vol_pr_qd} cubic units.")
                                        time.sleep(8)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                                # Diagonal - Quadrangular prism
                                elif opt == 3:
                                    l1 = float(input("\nEnter the measurement of one side of the base rectangle: "))
                                    l2 = float(input("Enter the measurement of another side of the base rectangle: "))
                                    h_pr_qd = float(input("Input the height: "))
                                    if l1 <= 0 or l2 <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    elif h_pr_qd <= 0:
                                        print("\nError: Input values must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    elif l1 and l2 and h_pr_qd == l1 or l2 or h_pr_qd:
                                        print("\nError: You're calculating the diagonal of a cube.")
                                        print(f"The size of the diagonal is {(l1 * math.sqrt(3)):.2f} units.")
                                        time.sleep(8)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        diag_pr_qd_sq = l1 ** 2 + l2 ** 2 + h_pr_qd ** 2
                                        diag_pr_qd = math.sqrt(diag_pr_qd_sq)
                                        print(f"\nThe diagonal of this prism is {diag_pr_qd:.2f} units.")
                                        time.sleep(8)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                            # Wrong operation
                            else:
                                print("\nError: Wrong operation.")
                                time.sleep(2)
                                print("Returning to main menu...")
                                time.sleep(1)
                                main()

                        # Return to polyhedra menu
                        elif opt == 2:
                            fig_3d()

                        # Other value
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Sphere
                    elif opt == 3:
                        print("\nChoose an aspect to calculate: ")
                        print("1 - Area")
                        print("2 - Volume")
                        print("3 - Choose another polyhedron")
                        opt = int(input("Option: "))

                        # Area - Sphere
                        if opt == 1:
                            r = float(input("\nInput the value of the radius from the sphere: "))
                            area_sph = 4 * math.pi * (r ** 2)
                            if r <= 0:
                                print("\nError: Input value must be greater than zero.")
                                time.sleep(3)
                                print("Returning to the polyhedra menu...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                print(f"\nThe area of this sphere is {area_sph:.2f} square units.")
                                print(f"Unknown value of pi: {4 * (r ** 2)}π unidades cuadradas.")
                                time.sleep(3)
                                print("Returning to the polyhedra menu...")
                                time.sleep(2)
                                fig_3d()

                        # Volume - Sphere
                        elif opt == 2:
                            r = float(input("\nInput the value of the radius from the sphere: "))
                            vol_sph = (4 / 3) * math.pi * (r ** 3)
                            if r <= 0:
                                print("\nError: Input value must be greater than zero.")
                                time.sleep(3)
                                print("Returning to the polyhedra menu...")
                                time.sleep(2)
                                fig_3d()
                            else:
                                print(f"\nThe volume of the sphere is {vol_sph:.2f} cubic units.")
                                print(f"Unknown value of pi: {(4 / 3) * (r ** 3):.2f}π cubic units.")
                                time.sleep(7)
                                print("Returning to the polyhedra menu...")
                                time.sleep(2)
                                fig_3d()

                        # Return to polyhedra menu
                        elif opt == 3:
                            fig_3d()

                        # Wrong operation
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Cylinder
                    elif opt == 4:
                        print("\nChoose the cylinder you are working with:")
                        print("1 - Right")
                        print("2 - Choose another polyhedron")
                        cho = int(input("Option: "))

                        # Right cylinder
                        if cho == 1:
                            print("\nChoose an aspect to calculate:")
                            print("1 - Areas")
                            print("2 - Volume")
                            choice = int(input("Option: "))

                            # Areas - Right cylinder
                            if choice == 1:
                                r = float(input("\nInput the radius of the base from the cylinder: "))
                                h = float(input("Input the height of the cylinder: "))

                                # Radius or Height <= 0
                                if r <= 0 or h <= 0:
                                    print("\nError: Input value must be greater than zero.")
                                    time.sleep(3)
                                    print("Returning to the polyhedra menu...")
                                    time.sleep(2)
                                    fig_3d()

                                # Radius and Height > 0
                                else:
                                    ar_bas = math.pi * (r ** 2)
                                    ar_lat = 2 * math.pi * r * h
                                    ar_total = ar_lat + 2 * ar_bas
                                    print(f"\nThe total area of this cylinder is {ar_total:.2f} square units.")
                                    print(f"The lateral area of this cylinder is {ar_lat:.2f} square units.")
                                    print(f"The basal area of this cylinder is {ar_bas:.2f} square units.")
                                    time.sleep(8)
                                    print("Returning to the polyhedra menu...")
                                    time.sleep(2)
                                    fig_3d()

                            # Volume - Right Cylinder
                            elif choice == 2:
                                r = float(input("\nInput the radius of the base from the cylinder: "))
                                h = float(input("Input the height of the cylinder: "))

                                # Radius or Height <= 0
                                if r <= 0 or h <= 0:
                                    print("\nError: Input value must be greater than zero.")
                                    time.sleep(3)
                                    print("Returning to the polyhedra menu...")
                                    time.sleep(2)
                                    fig_3d()

                                # Radius and Height > 0
                                else:
                                    vol = math.pi * (r ** 2) * h
                                    print(f"\nThe volume of this cylinder is {vol:.2f} cubic units.")
                                    time.sleep(5)
                                    print("Returning to the polyhedra menu...")
                                    time.sleep(2)
                                    fig_3d()

                        # Return to polyhedra menu
                        elif cho == 2:
                            fig_3d()

                        # Wrong operation
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Pyramids
                    elif opt == 5:
                        print("\nChoose the type of pyramid you want to work with:")
                        print("1 - Right regular pyramids")
                        print("2 - Irregular oblique pyramids")
                        print("3 - Choose another polyhedron")
                        opt = int(input("Option: "))

                        # Right pyramids
                        if opt == 1:
                            print("\nChoose the base of the pyramid: ")
                            print("1 - Square")
                            print("2 - Rectangular")
                            opt = int(input("Option: "))

                            # Right pyramid - Square base
                            if opt == 1:
                                print("\nChoose an aspect to calculate: ")
                                print("1 - Area")
                                print("2 - Volume")
                                opt = int(input("Option: "))

                                # Area - Right pyramid, square base
                                if opt == 1:
                                    lado = float(input("Input the value of one edge of the base: "))
                                    ap = float(input("Input the value of the apothem: "))
                                    ar_pir_qd = lado * (2 * ap + lado)

                                    # Edge or Ap <= 0
                                    if lado <= 0 or ap <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        print(f"\nThe area of this pyramid is {ar_pir_qd:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                                # Volume - Right pyramid, square base
                                elif opt == 2:
                                    lado = float(input("Input the value of one edge of the base: "))
                                    h = float(input("Input the height of the pyramid: "))
                                    vol = (1 / 3) * (lado ** 2) * h

                                    # Edge or Height <= 0
                                    if lado <= 0 or h <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        print(f"\nThe volume of this pyramid is {vol} cubic units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                            # Right pyramid - Rectangular base
                            elif opt == 2:
                                print("\nChoose an aspect to calculate: ")
                                print("1 - Area")
                                print("2 - Volume")
                                opt = int(input("Option: "))

                                # Area - Right pyramid, rectangular base
                                if opt == 1:
                                    a = float(input("\nInput the value of one side of the base: "))
                                    b = float(input("Input the value of another side of the base: "))
                                    h = float(input("Input the height of the pyramid: "))
                                    if a <= 0 or b <= 0 or h <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        area = a * b + a * math.sqrt(h ** 2 + (b ** 2 / 4)) + b * math.sqrt(
                                            h ** 2 + (a ** 2 / 4))
                                        print(f"\nThe area of this pyramid is {area:.2f} square units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                                # Volume - Right pyramid, rectangular base
                                elif opt == 2:
                                    a = float(input("\nInput the value of one side of the base: "))
                                    b = float(input("Input the value of another side of the base: "))
                                    h = float(input("Input the height of the pyramid: "))
                                    if a <= 0 or b <= 0 or h <= 0:
                                        print("\nError: Input value must be greater than zero.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()
                                    else:
                                        vol = (a * b * h) / 3
                                        print(f"\nThe volume of this pyramid is {vol:.2f} cubic units.")
                                        time.sleep(3)
                                        print("Returning to the polyhedra menu...")
                                        time.sleep(2)
                                        fig_3d()

                            # Wrong operation
                            else:
                                print("\nError: Wrong operation.")
                                time.sleep(2)
                                print("Returning to main menu...")
                                time.sleep(1)
                                main()

                        # Oblique pyramids
                        elif opt == 2:
                            print("WIP")
                            main()

                        # Choose another polyhedron
                        elif opt == 3:
                            fig_3d()

                        # Wrong operation
                        else:
                            print("\nError: Wrong operation.")
                            time.sleep(2)
                            print("Returning to main menu...")
                            time.sleep(1)
                            main()

                    # Return to main menu
                    elif opt == 5:
                        main()

                    # Wrong operation
                    else:
                        print("\nError: Wrong operation.")
                        time.sleep(2)
                        print("Returning to main menu...")
                        time.sleep(1)
                        main()

                fig_3d()

            # Credits
            elif option == 3:
                print(f"\n\tCurrent version: {version} {lang}")
                print("\t--- Codename Copernicium ---")
                print("\tProgrammed on Python 3.8")
                time.sleep(3)
                print("\nProgramming: Qm_Dev")
                time.sleep(3)
                print("Design: Qm_Dev")
                time.sleep(3)
                print("Testing: Qm_Dev")
                time.sleep(3)
                print("Source code: https://github.com/Qm-Dev/figures-calculator")
                time.sleep(3)
                print("Special thanks to: "
                      "\n-Alejandro Taboada Sánchez"
                      "\n-Patorjk")
                time.sleep(5)
                main()

            # Exit
            elif option == 4:
                time.sleep(0.2)
                print("\nQuitting...")
                time.sleep(0.8)
                exit()

            # Other value
            else:
                print("\nError: Wrong operation.")
                print("Restarting...")
                time.sleep(1)
                main()
        main()

    except ValueError:
        redo += 1
        print(f"\nError {redo}")
        time.sleep(1)
        redo -= 1
