def judul(file):
    f = open(file, "r")
    isi = f.readlines()
    judul = isi[0]
    return judul

def tgl(file):
    f = open(file, "r")
    isi = f.readlines()
    tgl = isi[1]
    return tgl


