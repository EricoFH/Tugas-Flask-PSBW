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


