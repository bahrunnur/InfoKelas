InfoKelas
=========

Overview
--------
InfoKelas (Informasi Kelas) merupakan aplikasi berbasis Web yang menampilkan informasi kelas perkuliahan yang lebih terperinci dibandingkan dengan Sistem Informasi Akademika.

Limitation
----------
InfoKelas hanya bisa digunakan bagi mahasiswa FMIPA UGM.

Development Setup
-----------------
buat Python virtual environment dan aktifkan.

    virtualenv --no-site-packages InfoKelas
    source InfoKelas/bin/activate

Install dependencies.

    pip install -r requirements.txt

Start the app.

    python wsgi.py
