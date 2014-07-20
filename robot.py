"""
Robot Scrapper
==============

This robot has mission to scrap your body.
"""
from robobrowser import RoboBrowser

from models import *


class Robot(object):
    """This robot have two functionality, which is to grab matakuliah data
    and to grab KRS of each mahasiswa. This robot also need username and
    password for authorization.

    :param str username: username for login
    :param str password: password for login

    """
    def __init__(self, username, password):
        self.browser = RoboBrowser()
        self.username = username
        self.password = password
        self.matakuliah = []

    def update_matakuliah(self):
        self.matakuliah = self._get_matakuliah()
        for obj in self.matakuliah:
            detail = self._get_matakuliah_detail(obj['link_detail'])
            obj['jadwal_kuliah'] = detail['jadwal_kuliah']
            # obj['jadwal_uts'] = detail['jadwal_uts']
            # obj['jadwal_uas'] = detail['jadwal_uas']
        self._persist_matakuliah()

    def _persist_matakuliah(self,):
        for obj in self.matakuliah:
            try:
                kelas = (Kelas.select()
                         .where(Kelas.nama == obj['nama_kelas']).get())
            except Kelas.DoesNotExist:
                kelas = Kelas()

            kelas.kode_mk = obj['kode_mk']
            kelas.nama = obj['nama_kelas']
            kelas.matakuliah = obj['matakuliah']
            kelas.dosen = obj['dosen']
            kelas.sks = obj['sks']
            kelas.tipe = obj['tipe']
            kelas.jadwal_kuliah = obj['jadwal_kuliah']
            kelas.save()

    def __login(self):
        self.browser.open('http://akademika.ugm.ac.id')
        login_form = self.browser.get_form(id='form-login')
        login_form['username'].value = self.username
        login_form['password'].value = self.password
        self.browser.submit_form(login_form)

    def _get_matakuliah(self):
        self.__login()

        # go to 'informasi matakuliah' page
        link_matakuliah = self.browser.select('#navigation li a')[3]
        self.browser.follow_link(link_matakuliah)

        marshal = []
        matakuliah_raw = browser.select('.table-common > tr')[1:]
        for raw in matakuliah_raw:
            data = raw.select('td')

            obj = {}
            obj['kode_mk'] = data[1].contents[0]
            obj['matakuliah'] = data[2].contents[0]
            obj['dosen'] = data[3].contents[0]
            obj['link_detail'] = data[4].contents[0]
            obj['nama_kelas'] = data[4].contents[0].get_text()
            obj['tipe'] = data[5].contents[0]
            obj['sks'] = data[6].contents[0]
            marshal.append(obj)

        return marshal

    def _get_matakuliah_detail(self, link):
        self.browser.follow_link(link)
        jadwal_row = self.browser.select('table > tr')

        # for brevity
        obj = {}
        obj['jadwal_kuliah'] = ""
        obj['jadwal_uts'] = ""
        obj['jadwal_uas'] = ""

        jadwal_kuliah_row = jadwal_row[0].select('table tr')[1:]
        for row in jadwal_kuliah_row:
            contents = [x.contents[0] for x in row.select('td')]
            data_string = "$".join(contents)
            obj['jadwal_kuliah'] = "|".join([data_string])

        # TODO: find a way to get 'tanggal'
        # jadwal_uts_row = jadwal_row[1].select('table tr')[1:]
        # jadwal_uas_row = jadwal_row[2].select('table tr')[1:]

        return obj