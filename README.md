# AutoPrima - Website Dealer Mobil (Flask)

Website dealer mobil sederhana yang dibuat dengan **Flask** dan **Bootstrap 5**. Proyek ini dibuat sebagai tugas pembelajaran untuk mengintegrasikan template HTML ke dalam Flask menggunakan route, template inheritance, dan komponen Flask lainnya.

## Fitur

- Halaman beranda dengan banner dan mobil pilihan
- Daftar mobil dengan filter berdasarkan tipe (MPV, Hatchback, SUV, dll.)
- Halaman detail untuk setiap mobil
- Formulir kontak dengan notifikasi (flash message)
- Halaman 404 kustom
- Format harga otomatis dalam Rupiah

## Teknologi

- Python 3
- Flask
- Jinja2 (template engine bawaan Flask)
- Bootstrap 5 (via CDN)

## Struktur Proyek

```
dealer/
├── app.py                  # Aplikasi Flask: route dan data mobil
├── requirements.txt        # Daftar dependensi
├── static/
│   ├── style.css           # CSS kustom
│   └── img/                # Foto mobil dan banner
└── templates/
    ├── base.html           # Layout utama (navbar, footer)
    ├── index.html          # Beranda
    ├── cars.html           # Daftar mobil + filter
    ├── car_detail.html     # Detail mobil
    ├── contact.html        # Form kontak
    ├── 404.html            # Halaman tidak ditemukan
    └── _card.html          # Komponen kartu mobil
```

## Komponen Flask yang Digunakan

| Komponen | Penggunaan |
|---|---|
| `@app.route` | Halaman beranda, daftar mobil, dan kontak |
| Dynamic route `<int:car_id>` | Halaman detail (`/mobil/1`) |
| `methods=["GET", "POST"]` | Pengiriman form kontak |
| `render_template` dan `{% extends %}` | Template inheritance dari `base.html` |
| `url_for` | Link antar halaman dan file static |
| `flash` | Pesan notifikasi setelah form dikirim |
| `@app.errorhandler(404)` | Halaman 404 kustom |
| `@app.template_filter` | Filter `rupiah` untuk format harga |
| `request.args` | Filter tipe mobil lewat query string |

## Cara Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/EricoFH/Flask.git
cd Flask
```

### 2. Buat dan aktifkan virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi

```bash
python app.py
```

Buka `http://127.0.0.1:5000` di browser.

## Daftar Halaman

| URL | Halaman |
|---|---|
| `/` | Beranda |
| `/mobil` | Daftar semua mobil |
| `/mobil?tipe=SUV` | Daftar mobil dengan filter tipe |
| `/mobil/<id>` | Detail mobil |
| `/kontak` | Formulir kontak |

## Menambah Mobil Baru

Tambahkan satu blok data di list `CARS` pada `app.py`:

```python
{"id": 5, "name": "Suzuki Ertiga", "year": 2022, "price": 225000000,
 "type": "MPV", "trans": "Manual", "color": "#718096",
 "img": "ertiga.jpg",
 "desc": "MPV hemat bahan bakar dengan kabin lega."},
```

Simpan fotonya di `static/img/` dengan nama file yang sama. Pastikan `id` unik.

## Screenshot

> Ganti bagian ini dengan screenshot aplikasi Anda.

| Langkah | Screenshot |
|---|---|
| Instalasi Python | `screenshots/01-python.png` |
| Pembuatan venv | `screenshots/02-venv.png` |
| Instalasi Flask | `screenshots/03-flask.png` |
| Aplikasi di browser | `screenshots/04-browser.png` |

Contoh cara menampilkan gambar:

```markdown
![Aplikasi berjalan di browser](screenshots/04-browser.png)
```

## Keterbatasan

- Data mobil disimpan dalam list Python, bukan database.
- Formulir kontak hanya menampilkan notifikasi dan tidak menyimpan atau mengirim pesan.
- `secret_key` dan `debug=True` hanya untuk pengembangan, jangan dipakai saat deploy.

## Pengembangan Selanjutnya

- Menyimpan data mobil di database (SQLite dengan Flask-SQLAlchemy)
- Halaman admin untuk menambah dan mengubah mobil
- Menyimpan atau mengirim pesan dari formulir kontak lewat email
- Fitur pencarian dan pengurutan harga

## Kredit

- Framework CSS: [Bootstrap 5](https://getbootstrap.com)
- Foto: *(isi sumber foto, misalnya Unsplash atau Pexels, dan nama fotografer jika ada)*

## Penulis

Erico - [@EricoFH](https://github.com/EricoFH)
