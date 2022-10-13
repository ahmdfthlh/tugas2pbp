# README.md - Tugas 6 PBP 
*Nama*: Ahmad Fatahillah

*NPM*: 2106653741

*Kelas*: PBP F

**Link Aplikasi Django:**
https://tugas2fattah.herokuapp.com/todolist

## 1️⃣ **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

Asynchronous Programming tidak terikat dengan proses I/O sedangkan Synchronous Programming terikat dengan proses I/O. Hal tersebut mengakibatkan bahwa task-task yang ada pada Asysnchronous Programming dapat berjalan secara pararel sehingga kemungkinan selesainya akan lebih cepat, sedangkan task-task pada Synchronous Programming harus diselesaikan secara satu-satu sehingga kemungkinan selesainya bakal lebih lambat.

## 2️⃣ **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Event-Driven Programming merupakan salah satu teknik yang digunakan dalam melakukan pemrograman. Sesuai namanya, konsep dari Event-Driven Programming hanya bekerja sesuai dengan suatu kejadian atau event yang terjadi. Salah satu contoh penerapannya pada tugas ini adalah pada button `Add New Task`. Pada button tersebut akan memunculkan modal form ketika ditekan oleh user. Event-Driven pada button ini terjadi ketika ada seorang pengguna yang menekan tombol tersebut, maka barulah akan muncul modal form yang berisikan detail tugas yang ingin ditambahkan. Sehingga event pada kali ini adalah ketika button tersebut ditekan maka akan melanjutkan proses selanjutnya.

## 3️⃣ **Jelaskan penerapan asynchronous programming pada AJAX.**

Penerapan Asynchronous Programming pada AJAX adalah ketika terdapat client yang membuka halaman HTML maka pada saat itu juga akan membaca data yang ada di database. Asynchronous berguna pada kali ini adalah ketika terdapat suatu data baru yang ditambahkan, maka data-data yang ada di database akan juga ikut terbarui tanpa me-refresh halaman HTML tersebut. 

Dalam program ini AJAX digunakan dalam mengambil data dan event-driven ketika menambahkan task baru, kedua hal tersebut akan memakai data dalam bentuk JSON. Dengan memanfaatkan JQuery juga memudahkan dalam melakukan proses pengerjaan karena sudah tersedia berbagai function seperti saat success ataupun error.

## 4️⃣ **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas**

1. Membuat fungsi `show_json` pada `views.py` yang berguna untuk mengambil data model dalam bentuk JSON serta memetakan fungsi tersebut ke dalam `urls.py`

2. Merubah cara penampilan card to-do list dengan menggunakan AJAX sesuai dengan fungsi `show_json` yang telah dibuat sebelumnya.

3. Setelah to-do list yang ada berhasil ditampilkan, baru lah mengimplementasikan Add New Task dengan AJAX POST. Selanjutnya membuat fungsi `create_task_ajax` pada `views.py` yang berguna untuk mengambil value input dari user ketika menambahkan task baru serta memetakan fungsi tersebut ke dalam `urls.py`.

4. Merubah button tambah task baru dengan bentuk modal. Lalu ketika user menekan button submit pada modal tersebut maka akan memanggil fungsi `new_task()` pada todolist.html dengan tipe AJAX POST agar data baru yang ditambahkan tersebut tersimpan.