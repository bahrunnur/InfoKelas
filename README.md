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
- Create Python virtual environment and activate it.

    	virtualenv --no-site-packages InfoKelas
    	source InfoKelas/bin/activate

- Install dependencies.

    	pip install -r requirements.txt

- Set `IK_IN_DEVELOPMENT` environment variable, or you can add it in your `.bashrc` file.

    	export IK_IN_DEVELOPMENT=yes

- Create a database that has name `info_kelas_db` or you can create with anything else name and edit the configuration in `config.py`.

- Start the app.

    	python wsgi.py
