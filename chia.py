def chia():
    x = float(input("Nhap so thu nhat: "))
    y = float(input("Nhap so thu hai: "))

    if y == 0:
        print("Khong the chia cho 0")
    else:
        ket_qua = x / y
        print("Ket qua:", ket_qua)
