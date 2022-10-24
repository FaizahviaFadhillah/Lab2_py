# input nilai variable
a=input("masukan nilai a:")
b=input("masukan nilai b:")

# cetak nilai variable
print("variabel a=",a)
print("variabel b=",b)

# cetak hasil operasi kedua variabel dengan string format
print("hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan {1}+{0}=%s".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%s".format(a,b) %(a/b))
