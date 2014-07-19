"""
Application Models
==================

this is a list of models that are being use
"""
import os

from peewee import *

from config import db as ik_db


if os.getenv('IK_IN_DEVELOPMENT'):
    db_name = ik_db['dev']['name']
    connect_kwargs = ik_db['dev']['connect_kwargs']
else:
    db_name = ik_db['production']['name']
    connect_kwargs = ik_db['dev']['connect_kwargs']

db = PostgresqlDatabase(db_name, **connect_kwargs)


class BaseModel(Model):
    class Meta:
        database = db


class Mahasiswa(BaseModel):
    niu = IntegerField()
    nama = CharField()
    angkatan = CharField(max_length=4)
    prodi = CharField()
    visited = IntegerField()

    class Meta:
        indexes = (
            (('niu'), True)
        )


class Kelas(BaseModel):
    id = PrimaryKeyField()
    kode = CharField(max_length=7)
    name = CharField()
    matakuliah = CharField()
    dosen = CharField()
    sks = IntegerField()
    tipe = CharField(max_length=1)

    # format: '{hari}:{jam}:{ruang}|{hari}:{jam}..'
    jadwal_kuliah = TextField()

    # format: '{tanggal}:{jam}:{ruang}'
    jadwal_uts = TextField()

    # format: '{tanggal}:{jam}:{ruang}'
    jadwal_uas = TextField()


class KelasMahasiswa(BaseModel):
    mahasiswa = ForeignKeyField(Mahasiswa)
    kelas = ForeignKeyField(Kelas)