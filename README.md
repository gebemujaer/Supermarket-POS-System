# Supermarket-POS-System

## Latar Belakang
- Peningkatan Efisiensi Transaksi: Sistem yang akan dikembangkan akan membuat proses transaksi menjadi lebih cepat dan efisien dengan adanya fitur untuk membuat ID transaksi customer.
- Kemudahan Input Data: Dengan adanya form untuk memasukkan detail item, customer dapat dengan mudah memasukkan data item yang dibeli seperti nama, jumlah, dan harga.
- Perbaikan Data Tanpa Menghapus Item: Sistem akan menyediakan opsi untuk memperbaiki item yang salah diinput tanpa harus menghapus item, sehingga akan mengurangi resiko kesalahan dan mempermudah proses transaksi.

## Tujuan
- Menciptakan fitur untuk membuat ID transaksi customer.
- Menyediakan form untuk memasukkan detail item seperti nama, jumlah, dan harga.
- Menyediakan opsi untuk memperbaiki item yang salah diinput tanpa menghapus item.
- Menyediakan fitur untuk membatalkan item yang dibeli.
- Menyediakan fitur untuk memeriksa ulang harga dan nama item yang diinput.
- Menyediakan fitur untuk menghitung total belanja.

## Requirements/Objectives
- Implementasi class Transaction untuk membuat ID transaksi customer
- Implementasi method add_item untuk memasukkan nama item, jumlah item, dan harga barang
- Implementasi method update_item_name, update_item_qty, dan update_item_price untuk memperbaiki kesalahan input item
- Implementasi method delete_item untuk menghapus item belanjaan dan method reset_transaction untuk mereset transaksi
- Implementasi method check_order untuk memeriksa input data dan mengeluarkan pesan "Pemesanan sudah benar" atau "Terdapat kesalahan input data"
- Implementasi method total_price untuk menghitung total belanja dan memberikan diskon sesuai ketentuan.

## Flow chart
![Flowchart](https://github.com/gebemujaer/Supermarket-POS-System/blob/main/Flowchart.jpeg?raw=true)

## Penjelasan Fungsi
### Method
- add_item() yang berfungsi untuk menambahkan item ke list items.
- update_item_name() yang berfungsi untuk mengupdate nama item.
- update_item_qty() yang berfungsi untuk mengupdate jumlah item.
- update_item_price() yang berfungsi untuk mengupdate harga item.
- delete_item() yang berfungsi untuk menghapus item dari list items.
- reset_transaction() yang berfungsi untuk mengosongkan list items.
- check_order() yang berfungsi untuk memeriksa apakah terdapat kesalahan input data atau tidak.
- total_price() yang berfungsi untuk menghitung total harga belanja dan memberikan diskon jika memenuhi syarat.
