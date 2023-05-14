try:
    raise NameError('nama')
except NameError:
    print("Variabel yang diminta belum didefinisikan!")
    raise