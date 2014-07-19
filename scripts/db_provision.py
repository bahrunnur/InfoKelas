import json

from models import *


ANGKATAN = ["2010", "2011", "2012", "2013"]
PRODI = ["Matematika", "Statistika", "Fisika", "Geofisika", "Kimia",
         "Elektronika+dan+Instrumentasi", "Ilmu+Komputer"]


def seed_mahasiswa():
    for prodi in PRODI:
        for angkatan in ANGKATAN:
            file_path = ('data/{prodi}/{angkatan}.json'
                            .format(angkatan=angkatan, prodi=prodi)
                            .replace('+', ' '))

            with open(file_path, 'r') as fp:
                mahasiswa = json.load(fp)
                for entry in mahasiswa:
                    nama = entry['nama'].rstrip()
                    niu = entry['niu'].rstrip()
                    Mahasiswa.create(nama=nama,
                                     niu=niu,
                                     angkatan=angkatan,
                                     prodi=prodi,
                                     visited=0)


if __name__ == "__main__":
    Mahasiswa.create_table()
    Kelas.create_table()
    KelasMahasiswa.create_table()
    seed_mahasiswa()
    print "SUCCESS"