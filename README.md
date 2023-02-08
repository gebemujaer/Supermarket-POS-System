# Supermarket-POS-System

## Latar Belakang
- Peningkatan Efisiensi Transaksi: Sistem yang akan dikembangkan akan membuat proses transaksi menjadi lebih cepat dan efisien dengan adanya fitur untuk membuat ID transaksi customer;
- Kemudahan Input Data: Dengan adanya form untuk memasukkan detail item, customer dapat dengan mudah memasukkan data item yang dibeli seperti nama, jumlah, dan harga;
- Perbaikan Data Tanpa Menghapus Item: Sistem akan menyediakan opsi untuk memperbaiki item yang salah diinput tanpa harus menghapus item, sehingga akan mengurangi resiko kesalahan dan mempermudah proses transaksi.

## Tujuan
- Menciptakan fitur untuk membuat ID transaksi customer;
- Menyediakan form untuk memasukkan detail item seperti nama, jumlah, dan harga;
- Menyediakan opsi untuk memperbaiki item yang salah diinput tanpa menghapus item;
- Menyediakan fitur untuk membatalkan item yang dibeli;
- Menyediakan fitur untuk memeriksa ulang harga dan nama item yang diinput;
- Menyediakan fitur untuk menghitung total belanja.

## Requirements/Objectives
- Implementasi `class Transaction` untuk membuat ID transaksi customer;
- Implementasi method `add_item` untuk memasukkan nama item, jumlah item, dan harga barang;
- Implementasi method `update_item_name`, `update_item_qty`, dan `update_item_price` untuk memperbaiki kesalahan input item;
- Implementasi method `delete_item` untuk menghapus item belanjaan dan method `reset_transaction` untuk mereset transaksi;
- Implementasi method `check_order` untuk memeriksa input data dan mengeluarkan pesan "`Pemesanan sudah benar`" atau "`Terdapat kesalahan input data`";
- Implementasi method `total_price` untuk menghitung total belanja dan memberikan diskon sesuai ketentuan.

## Alur Program
1. Membuat `class Transaction`.
2. Membuat method `init` yang menentukan atribut class seperti ID transaksi dan list item belanjaan.
3. Membuat method `add_item` untuk memasukkan item belanjaan ke list item belanjaan.
4. Membuat method `update_item_name` untuk memperbaiki nama item belanjaan.
5. Membuat method `update_item_qty` untuk memperbaiki jumlah item belanjaan.
6. Membuat method `update_item_price` untuk memperbaiki harga item belanjaan.
7. Membuat method `delete_item` untuk menghapus item belanjaan.
8. Membuat method `reset_transaction` untuk mereset transaksi.
9. Membuat method `check_order` untuk memeriksa input data.
10. Membuat method `total_price` untuk menghitung total belanja dan memberikan diskon sesuai ketentuan.

## Penjelasan Fungsi
### Method
- `__init__` : method ini akan dijalankan saat instance dari class Transaction dibuat. Method ini menetapkan atribut transaction_id dengan nilai "trnsct_123" dan menetapkan atribut items sebagai list kosong.
- `add_item` : method ini akan menambahkan item ke dalam list items. Parameter yang diterima adalah item.
- `update_item_name` : method ini akan mengupdate nama item dalam list items. Parameter yang diterima adalah name dan update_name. Method akan mencari item dengan nama name dan mengubah namanya menjadi update_name.
- `update_item_qty` : method ini akan mengupdate jumlah item dalam list items. Parameter yang diterima adalah name dan update_qty. Method akan mencari item dengan nama name dan mengubah jumlahnya menjadi update_qty.
- `update_item_price` : method ini akan mengupdate harga item dalam list items. Parameter yang diterima adalah name dan update_price. Method akan mencari item dengan nama name dan mengubah harganya menjadi update_price.
- `delete_item` : method ini akan menghapus item dalam list items. Parameter yang diterima adalah name. Method akan mencari item dengan nama name dan menghapusnya.
- `reset_transaction` : method ini akan menghapus semua item dalam list items.
- `check_order` : method ini akan memeriksa kebenaran data dalam list items. Method akan mengembalikan string "Terdapat kesalahan input data" jika ada item dalam list yang memiliki nilai None. Jika tidak, method akan mengembalikan string "Pemesanan sudah benar".
- `total_price` : method ini akan menghitung total harga dari semua item dalam list items dan memberikan diskon jika total harga melebihi batas tertentu. Method akan mengembalikan nilai total harga setelah diskon.

Dari semua method tersebut, kita dapat melakukan berbagai proses transaksi seperti menambahkan item, mengupdate item, menghapus item, memeriksa data transaksi, dan menghitung total harga setelah diskon.

## Test Case
### Test 1 – `add_item()`
_Customer_ ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
- Nama item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama item: Pasta Gigi, Qty: 3, Harga: 15000

**Output**:
![Test Case 1](https://github.com/gebemujaer/Supermarket-POS-System/blob/main/Images/Test%20Case%201.png)

### Test 2 – `delete_item()`
Ternyata _Customer_ salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka _Customer_ menggunakan method `delete_item()` untuk menghapus item. Item yang ingin dihapuskan adalah **Pasta Gigi**.

**Output**:
![Test Case 2](https://github.com/gebemujaer/Supermarket-POS-System/blob/main/Images/Test%20Case%202.png)

### Test 3 – `reset_transaction()`
Ternyata setelah dipikir-pikir _Customer_ salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu per satu, maka _Customer_ cukup menggunakan method `reset_transaction()` untuk menghapuys semua item yang sudah ditambahkan.

**Output**:
![Test Case 3](https://github.com/gebemujaer/Supermarket-POS-System/blob/main/Images/Test%20Case%203.png)

### Test 4 – `total_price()`
Setelah selesai berbelanja, _Customer_ akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

**Output**:
![Test Case 4](https://github.com/gebemujaer/Supermarket-POS-System/blob/main/Images/Test%20Case%204.png)

## Kesimpulan
1. Project Super Cashier adalah sebuah aplikasi kasir sederhana yang memiliki fungsi untuk menyimpan item belanjaan dan menghitung total harga.
2. Fungsi-fungsi seperti add_item, delete_item, dan reset_transaction telah diterapkan untuk mempermudah pengguna dalam menambahkan, menghapus, dan mereset item belanjaan.
3. Output dari aplikasi ini terstruktur dan mempermudah pengguna dalam memantau item belanjaan dan total harga yang harus dibayarkan.
4. Project Super Cashier dapat menjadi pilihan yang baik bagi mereka yang mencari aplikasi kasir sederhana dan mudah digunakan.
5. Walaupun masih banyak ruang untuk pengembangan lebih lanjut, Project Super Cashier sudah memberikan solusi dasar yang efektif untuk mengelola transaksi belanja.

## _Possible Improvements_
1. Penambahan Fitur Pembayaran: Proyek ini dapat ditingkatkan dengan menambahkan fitur pembayaran seperti pembayaran melalui kartu kredit atau e-wallet.
2. Integrasi dengan Sistem Inventory: Integrasi dengan sistem inventory akan mempermudah proses pencatatan stok dan pemantauan stok barang.
3. Laporan Penjualan: Proyek ini juga bisa ditingkatkan dengan menambahkan fitur laporan penjualan yang dapat mencakup data penjualan harian, mingguan, bulanan dan tahunan.
4. Penambahan Fitur Diskon: Fitur diskon bisa ditambahkan untuk memberikan pengalaman belanja yang lebih menyenangkan bagi pelanggan.
5. User Management System: Proyek ini dapat ditingkatkan dengan menambahkan sistem manajemen pengguna untuk memantau dan mengelola akses pengguna ke sistem.
6. Akses Dari Berbagai Platform: Proyek ini dapat ditingkatkan dengan menambahkan akses dari berbagai platform seperti mobile atau web untuk mempermudah pelanggan melakukan transaksi.
