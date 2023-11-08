def box():
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    l = float(input("Enter length: "))

    volume = float(w * h * l)
    volume = round(volume, 2)
    
    print(f"Volume is {volume}.")


box()