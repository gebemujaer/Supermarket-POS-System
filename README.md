# Supermarket-POS-System

## Tujuan
1. Membangun sistem kasir otomatis yang akan membuat pelanggan dapat dengan cepat melakukan transaksi di supermarket.
2. Mengintegrasikan sistem kasir otomatis dengan layanan e-commerce sehingga pelanggan yang berada di luar kota juga dapat melakukan pembelian dari supermarket.
3. Memastikan bahwa sistem kasir otomatis dapat berfungsi dengan baik dan lancar.
4. Memastikan bahwa informasi pelanggan yang masuk ke sistem kasir otomatis aman dan terlindungi.
5. Memastikan bahwa pembayaran yang diterima dari pelanggan melalui sistem kasir otomatis dapat diproses dengan cepat dan efektif.

## Flow chart
```flow
st=>start: Start
op1=>operation: Collect Customer Data
op2=>operation: Calculate Total
op3=>operation: Process Payments & E-Commerce
op4=>operation: Authenticate Customers & Secure Data
op5=>operation: Handle Errors & Logs
e=>end

st->op1->op2->op3->op4->op5->e

