# README.md - Tugas 4 PBP 
*Nama*: Ahmad Fatahillah

*NPM*: 2106653741

*Kelas*: PBP F

**Link Aplikasi Django:**
https://tugas2fattah.herokuapp.com/todolist

## 1️⃣ **Apa kegunaan {% csrf_token %} pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**

Melansir dari gudangssl.id, CSRF (Cross Site Request Foregry) merupakan serangan yang membuat pengguna internet tanpa sadar mengirimkan request kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. Sehingga, penyerang dapat melakukan suatu tindakan yang tidak dikehendaki oleh pengguna tersebut.

Pada Django memiliki tag `{% csrf_token %}` yang berfungsi untuk dapat mencegah serangan tersebut dapat terjadi. Token tersebut dihasilkan dari sisi server ketika sedang me-render halaman dan memastikan untuk memeriksa ulang token tersebut dari setiap request yang ada. Jika request tidak memiliki token atau token tidak valid, maka request tidak akan dieksekusi.

Sehingga jika di dalam elemen form tidak terdapat potongan tag `{% csrf_token %}`, maka bisa saja penyerangan CSRF dapat terjadi dan apabila serangan tersebut berhasil dilakukan oleh penyerang, resiko yang dapat muncul bisa sangat berisiko besar seperti pencurian akun dan lainnya.


## 2️⃣ **Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.**

Bisa, kita dapat membuat elemen `<form>` secara manual dengan gambaran besarnya yakni dengan cara di dalam file html membuat tag `<form>` yang di mana di dalam tag tersebut akan memiliki dua atribut yakni `action` dan `method`. Di dalam elemen `<form>` tersebut kita dapat secara manual untuk memberikan ruang untuk pengguna dalam memasukkan teks, memasukkan password, menekan tombol 'submit' ketika formnya telah selesai diisi, dan lainnya. Berikut adalah gambaran bagaimana bentuk kodenya di dalam file berekstensi html:
```shell
    <form action="/your-name/" method="post">
        <label for="your_name">Your name: </label>
        <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
        <input type="submit" value="OK">
    </form>
```
Kode diatas diambil dari dokumentasi Django mengenai Form

## 3️⃣ **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Data yang disubmisi oleh pengguna melalui HTML form diambil dari kode yang ada di fungsi di dalam `views.py` dengan syntax ```request.POST.get('nama-pada-html')``` dan akan disimpan ke dalam database dengan menggunakan model yang telah dibuat lalu disave. Lalu data-data tersebut dapat kita tampilkan ke dalam bentuk html dengan memanfaatkan fungsi `show_todolist` yang ada di dalam file `views.py` lalu list_of_task tersebut dapat di looping isinya dan disesuaikan dengan task masing-masing pengguna dengan memfilternya.

1. Dalam hal akun pengguna, jika pengguna belum pernah membuat akun maka akan diarahkan untuk membuat akun baru terlebih dahulu dengan memasukkan data yang dibutuhkan pada kali ini adalah nama dan password dari akun baru tersebut. Ketika pengguna telah berhasil melakukan submisi terkait registrasi akun barunya tersebut, maka data-data yang telah dimasukkan pada form registrasi tersebut akan disimpan di dalam database. Lalu, sekarang pengguna telah memiliki akun dan dapat langsung untuk mencoba login dengan username dan password yang sesuai. Ketika pengguna mencoba login dengan memasukkan username dan password miliknya, maka akan mencocokan ke dalam database apakah username dan password yang dimasukkan pengguna tersebut sudah terdaftar apa belum? Jika sudah maka pengguna berhasil login dan dapat melakukan proses-proses selanjutnya. Ketika pengguna telah sampai di halaman utama dari todolist maka akan terlihat username yang sesuai dengan akun miliknya.

2. Dalam hal to-do list yang dimiliki dari suatu akun pengguna, hal yang pertama kali dilakukan adalah akan masuk ke dalam form create_task melalui button `Add New Task` yang ada di halaman utama to-do list. Dalam membuat task baru, pengguna akan memasukkan judul dan deskripsi dari tugas tersebut dan ketika pengguna telah selesai mengisi data yang diminta lalu menekan button `tambah` maka data tersebut akan dikirim ke dalam database terlebih dahulu. Agar tasks yang dimiliki pengguna dapat muncul pada halaman utama, maka kita perlu menuliskan kode di dalam file `todolist.html` dengan melakukan looping dari setiap object yang ada di dalam database. Sehingga nantinya pada halaman `todolist.html` dapat terlihat kumpulan tasks yang dimiliki oleh pengguna tersebut dengan menampilkan detail tugas yakni waktu pembuatan tugas, judul, deskripsi, dan status tugas (selesai atau belum selesai)

## 4️⃣ **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat aplikasi `todolist` baru terlebih dahulu dan mendaftarkannya ke dalam variabel INSTALLED_APPS yang ada di `settings.py` yang ada di dalam folder project_django

2. Membuat fungsi `show_todolist` di dalam `views.py` untuk menampilkan tasks pengguna sekaligus menambahkan path url nya di dalam `urls.py` dalam folder project_django agar dapat diakses.

3. Membuat model dalam file `models.py` sebagai model dari data setiap task yakni user, date, title, description, dan status.

4. Melakukan makemigrations dan migrate terlebih dahulu agar model dapat diimplementasikan.

5. Membuat fungsi dalam `views.py` agar pengguna dapat registrasi, login, maupun logout serta  membuat halaman html untuk pengguna dapat melakukan registrasi dan login akun miliknya. (sesuai dengan tutorial 3)

6. Membuat fungsi create_task untuk pengguna membuat sebuah task baru dengan input judul dan deskripsi task tersebut di dalam `views.py`. Lalu juga mengimplementasikan pada halaman `create_task.html` agar form yang di dalam html tersebut dapat dipakai di dalam fungsi create_task.

7. Membuat fungsi untuk delete dan update agar pengguna dapat menghapus dan mengupdate setiap task yang dimilikinya dan juga membuatkan button untuk setiap task di dalam file `todolist.html`

8. Menambahkan informasi username yang sedang login pada file `todolist.html` dengan perintah {{ user.username }}

9. Melakukan routing pada `urls.py` dengan setiap fungsi yang dibuat pada `views.py` agar dapat digunakan.

10. Melakuakn git add, commit, dan push pada github dengan repositori yang masih sama dengan tugas 2. Sehingga aplikasi heroku yang masih dipakai masih sama.

# README.md - Tugas 5 PBP 

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- **Inline CSS** yakni langsung menuliskan kode CSS ke dalam atribut elemen HTML dengan menambahkan tag atribut `<style>`. Kelebihan dari style ini dapat langsung mengubah style setiap elemen tanpa harus membuat semacam selector. Sedangkan kekurangannya adalah karena biasanya setiap elemen di HTML memiliki style yang berbeda maka harus menulis ulang style-nya di setiap atribut HTML tersebut

- **Internal CSS** yakni kode CSS yang dibuat untuk styling HTML dituliskan di dalam satu file HTML yang sama. Kode CSS pada style ini dituliskan di luar tag kode HTML dengan menggunakan tag `<style>`. Kelebihan dari style ini dapat merubah kode CSS dalam satu file sehingga lebih cepat jika ingin merubah design style. Sedangkan kekurangannya adalah kode dalam HTMl menjadi tidak rapih karena langsung terdapat kode CSS dan kode HTML di satu tempat, bayangkan jika jumlah kode CSS bisa mencapai 1000 line sendiri.

- **External CSS** yakni kumpulan kode CSS yang dibuat di luar file HTML. Jadi file HTML dan CSS menjadi kedua file yang terpisah. Kelebihannya membuat file HTML menjadi lebih rapih dan terstruktur karena tidak tercampur dengan kode CSS. Kekurangannya mungkin ketika file CSS yang diambil tidak tersedia sehingga HTML yang nantinya akan ditampilkan tidak memiliki style.

## Jelaskan tag HTML5 yang kamu ketahui.

`<title>` -> membuat judul dari sebuah halaman

`<body>` -> sebagai tubuh dari sebuah halaman

`<p>` -> untuk membuat paragraf

`<table>` -> untuk membuat format table

`<tr>` -> membuat baris dalam sebuah table

`<td>` -> membuat sel dalam sebuah table

dan lain-lainnya.


## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

1. Tag selector

Selector ini ditunjuk secara langsung dari tag html yang ada.

2. ID selector

Cara menunjuk selector ini berdasarkan id yang dipasangkan dari sebuah tag HTML

3. Class selector

Cara menunjuk selector ini berdasarkan class yang dipasangkan dari sebuah tag HTML


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Meng-import link eksternal bootstrap agar bootstrap dapat berfungsi

2. Merubah penampilan todolist  yang sebelumnya dalam format table menjadi dalam bentuk card.

3. Mengimplementasikan styling bootstrap sesuai style yang kita inginkan.
