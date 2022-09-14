# README.md - Tugas 2 PBP Poin 5
*Nama*: Ahmad Fatahillah

*NPM*: 2106653741

*Kelas*: PBP F

## Bagan ---
**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**

![bagan-tugas2](https://user-images.githubusercontent.com/92851260/190225519-1c29bff4-64c8-4923-8e6f-c04b947dcc3a.jpg)

## Virtual Environment ---
**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Seperti namanya, virtual environment berfungsi untuk dapat membuat sebuah lingkungan virtual yang terisolasi. Jika terdapat dua project yang berbeda di mana setiap project tersebut juga memakai jenis modul yang berbeda. Pada kondisi ini mengakibatkan salah satu dari kedua project tersebut tidak bisa digunakan kembali karena project tersebut memakai modul yang berbeda versi dengan versi terbarunya yang sekarang dipakai. Sehingga virtual environment pada kondisi seperti ini dapat memiliki peran yang sangat berarti. Virtual Environment mampu memisahkan masing-masing dari kedua project tersebut sesuai dengan modul yang dipakainya. Sehingga masalah project yang memakai modul yang versi lama dapat terselesaikan dengan bantuan tools virtual environment.

Apakah bisa jika kita dalam membuat aplikasi web berbasis Django **tanpa** menggunakan virtual environment? Jawabannya adalah bisa saja. Namun, jika ditemukan pada kasus sebelumnya maka akan terjadi permasalahan yakni yang biasa disebut issue dependency. Hal tersebut diakibatkan setiap project yang berbeda menggunakan modul-modul yang berbeda juga. Sehingga dalam membuat aplikasi web menggunakan Django alangkah baiknya kita tetap memanfaatkan tools virtual environment agar kita tidak menghadapi seperti masalah-masalah di atas.


## Implementasi --- 
**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Hal yang pertama kali saya lakukan adalah melakukan git clone dari template pada tugas kali ini yang telah disediakan pada github PBP Fasilkom UI. Ketika saya melihat isi dari template tersebut bahwa sudah banyak tahapan-tahapan yang telah dilakukan sehingga saya hanya harus menambahkan bagian-bagian yang belum diselesaikan saja. Hal-hal yang saya lakukan adalah sebagai berikut:
1. Membuat fungsi di dalam file views.py yang di dalam folder katalog dengan kode berikut:

    ```shell
    def show_katalog(request):
        data_barang_wishlist = CatalogItem.objects.all()
        context = {
            'list_barang': data_barang_wishlist,
            'nama': 'Fattah',
            'npm' : '2106653741'
        }

        return render(request, "katalog.html", context)
    ```
    Tak lupa juga meng-import model yang telah dibuat agar dapat melakukan pengambilan data dari database dengan menambahkan:

    ```shell
    from katalog.models import CatalogItem
    ```

2. Memodifikasi file urls.py yang ada di dalam folder katalog agar dapat melakukan routing terhadap fungsi views sehingga halaman HTML dapat ditampilkan menjadi:


    ```shell
    from django.urls import path
    from katalog.views import show_katalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_katalog, name='show_katalog'),
    ]
    ```
    Lalu setelah itu juga menambahkan aplikasi katalog ke dalam urls.py yang ada di dalam folder project_django dengan menambahkan kode berikut pada variabel urlpatterns.
    ```shell
    ...
    path('katalog/', include('katalog.urls')),
    ...
    ```

3. Setelah melakukan routing, selanjutnya adalah melakukan mapping terhadap data yang telah di-render pada fungsi views agar dapat muncul di HTML dengan cara menggunakan syntax {{data}} dan disesuaikan dengan nama variabel yang telah saya buat di dalam views.py:
    ```shell
    <h5>Name: </h5>
    <p>{{nama}}</p>

    <h5>Student ID: </h5>
    <p>{{npm}}</p>
    ```

    Agar dapat menampilkan daftar barang, kita dapat mengiterasi terhadap list_barang yang sebelumnya telah di-render ke dalam HTML. Sehingga saya memodifikasi dan menambahkan potongan kode untuk memanggil atribut yang spesifik dari setiap objek yang ada di dalam list dengan cara:

    ```shell
    {% comment %} Add the data below this line {% endcomment %}
    {% for barang in list_barang %}
      <tr>
          <th>{{barang.item_name}}</th>
          <th>{{barang.item_price}}</th>
          <th>{{barang.item_stock}}</th>
          <th>{{barang.description}}</th>
          <th>{{barang.rating}}</th>
          <th>{{barang.item_url}}</th>
      </tr>   
    {% endfor %}
    </table>
    ```

Setelah selesai melakukan semua tahapan di atas, saya ingin mencoba melihat bagaimana hasilnya sejauh ini dalam local sebelum saya melakukan add, commit, dan push ke dalam repositori github miliki saya dengan cara di antaranya:
1. Membuat virtual environment terlebih dahulu dengan syntax:
    ```shell
    python -m venv env
    ```

2. Menyalakan virtual environment yang telah dibuat.
    ```shell
    # Windows:
    env\Scripts\activate.bat
    ```

3. Meng-install dependecies yang diperlukan agar proyek Django dapat berjalan dengan cara:
    ```shell
    pip install -r requirements.txt
    ```
4. Lalu setelah itu membuka http://localhost:8000 untuk melihat apakah aplikasi yang kita buat sudah terlihat atau belum.

Jika dirasa aplikasi sudah berjalan dan terlihat semestinya. Hal selanjutnya yang saya lakukan adalah melakukan add, commit, dan push ke dalam repositori github milik saya agar seluruh progress yang telah saya kerjakan dapat tersimpan di dalam repositori tersebut.

**Tahap Deploy**
1. Membuat aplikasi baru di dalam Heroku dengan akun milik saya pribadi.
2. Salin API Key dari Setting akun Heroku milik saya yang digunakan pada tahap selanjutnya.
3. Masuk ke dalam Actions yang ada di dalam (Settings -> Security -> Secrets -> Actions)
4. Membuat 2 variabel repository secret yakni HEROKU_API_KEY dengan value API Key yang telah disalin dan HEROKU_API_NAME dengan value nama aplikasi yang baru saya buat di Heroku pada tahap 1. Dan simpan kedua variabel tersebut.
5. Buka Actions yang di halaman utama repositori dan jalankan ulang workflow yang mungkin pertama kali dilihat akan gagal.
6. Setelah berhasil, aplikasi Django pada kali ini telah berhasil saya bangun dan dapat diakses oleh siapapun melalui link https://tugas2fattah.herokuapp.com/katalog/


**Sumber Referensi:**
Dokumentasi Django - https://docs.djangoproject.com/id/4.1/
Slides Week 3 MTV Django Architecture - https://scele.cs.ui.ac.id/pluginfile.php/160675/mod_resource/content/1/Slides-3%20MTV%20Django%20Architecture.pdf
Tutorial Lab 1 PBP Ganjil 2023 - https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1
