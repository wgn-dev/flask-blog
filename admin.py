#import re

def judul(file):
    f = open(file, "r")
    isi = f.readlines()
    judul = isi[0]
    j = judul.split(':')[1]
    return j

def tgl(file):
    f = open(file, "r")
    isi = f.readlines()
    tgl = isi[1]
    t = tgl.split(':')[1]
    return t


