# README.md - Tugas 3 PBP 
*Nama*: Ahmad Fatahillah

*NPM*: 2106653741

*Kelas*: PBP F

## 1️⃣
**Jelaskan perbedaan antara JSON, XML, dan HTML!**
Pertama akan membahas antara JSON dan XML terlebih dahulu. Sebenarnya antara JSON dan XML memiliki fungsi yang sama yakni sebagai format untuk pertukaran data. Lalu perbedaannya berada di: (1) Ekstensi file JSON adalah .json dan ekstensi file dari XML adalah .xml, (2) JSON jauh lebih sederhana dibandingkan dengan XML yang lebih kompleks, (3)  Data pada XML lebih terstruktur dibanding JSON, (4) JSON lebih efisien dibanding XML. Jika disimpulkan, JSON dapat menyimpan data dengan lebih efisien tetapi tidak rapi jika dilihat, sedangkan XML data yang disimpan lebih terstruktur, mudah dibaca, tetapi kurang efisien.

Lalu HTML merupakan bahasa markup yang digunakan sebagai pondasi utama dalam pembuatan halaman website. Jika diumpamakan pada seorang manusia, HTML merupakanlah tulang-tulang atau kerangka tubuh. Jadi setelah data-data yang telah di format menggunakan JSON atau XML, HTML berfungsi untuk menampilkan data-data tersebut dengan gaya tertentu.

## 2️⃣
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data Delivery dalam pengimplementasian sebuah platform bersifat fleksibel agar dapat terus saling bertukar informasi secara up-to-date. Jika terdapat client yang ingin mengakses platform tersebut maka pada saat itu akan terjadi transaksi data dan pada saat ini lah data delivery berperan agar komunikasi antar server dapat berjalan dengan baik dan data yang telah di-request bersifat konsisten.

## 3️⃣
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
Dalam mengimplementasikan checklist di atas, saya berpacu dengan semua hal yang ada di tutorial-tutorial sebelumnya. Hal yang pertama kali saya lakukan adalah membuat aplikasi Django terlebih dahulu yang bernama `mywatchlist`. Selanjutnya saya mendaftarkan aplikasi yang baru dibuat tersebut ke dalam variabel `INSTALLED_APPS` yang ada di `settings.py` pada folder `project_django`. Selanjutnya saya mempersiapkan terkait 10 data tontonan yang akan ditampilkan nantinya pada halaman HTML termasuk menyiapkan isi konten 10 tontonan pada file `initial_watchlist_data.json` pada folder `fixtures`. Selanjutnya saya menyelesaikan dan melengkapi hal-hal lainnya seperti menyelesaikan `views.py` pada `mywatchlist` agar dapat berfungsi sesuai dengan aturan pada soal serta pada bagian implementasi fitur untuk penyajian data dalam bentuk HTML, XML, dan JSON. Pada file tersebut lah saya juga melengkapi potongan kode agar ketiga url ini dapat diakses:
    -  http://localhost:8000/mywatchlist/html/
    -  http://localhost:8000/mywatchlist/xml/
    -  http://localhost:8000/mywatchlist/json/
Selanjutnya saya juga melengkapi file `urls.py` untuk menyambungkan request client ke dalam file sebelumnya yang saya buat yakni pada file `views.py`. Setelah saya merasa semuanya sudah berhasil diimplemntasikan dan sebelum melakukan `git push` terhadap repositori saya, saya mencoba menjalankan aplikasi yang telah saya bangun pada lokal terlebih dahulu. Setelah semuanya sudah sesuai, barulah saya melakukan git add, commit, serta push terhadap repositori saya

## 4️⃣
**Screenshot Postman**
    1. HTML

    2. XML

    3. JSON



