import json

from robobrowser import RoboBrowser


BASE_URL = "http://kpo48.webege.com/koplak.php?angkatan={0}&prodi={1}"
ANGKATAN = ["2010", "2011", "2012", "2013"]
# PRODI = ["Matematika", "Statistika", "Fisika", "Geofisika", "Kimia",
#          "Elektronika+dan+Instrumentasi", "Ilmu+Komputer"]
PRODI = ["Kimia", "Elektronika+dan+Instrumentasi", "Ilmu+Komputer"]


def grab(browser, angkatan, prodi):
    url = BASE_URL.format(angkatan, prodi)
    browser.open(url)

    mahasiswa = browser.select('table > tr')[1:]
    marshal = []

    for entry in mahasiswa:
        data = entry.select('div')[:-1]

        obj = {}
        obj["niu"] = data[0].contents[0]
        obj["nama"] = data[1].contents[0]
        obj["angkatan"] = data[2].contents[0]

        marshal.append(obj)

    file_path = ('data/{prodi}/{angkatan}.json'
                    .format(angkatan=angkatan, prodi=prodi)
                    .replace('+', ' '))

    with open(file_path, 'w+') as fp:
        json.dump(marshal, fp, indent=2, separators=(',', ': '))


if __name__ == "__main__":
    browser = RoboBrowser()

    for prodi in PRODI:
        for angkatan in ANGKATAN:
            print "STATUS: grabbing {0} {1}".format(prodi, angkatan)
            grab(browser, angkatan, prodi)

    print "SUCCESS"