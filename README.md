U-Net for Autonomous Driving Segmentation

Project ini berisi implementasi model U-Net untuk melakukan semantic segmentation pada citra berkaitan dengan lingkungan berkendara (autonomous driving). Model dibangun, dilatih, dan diuji menggunakan dataset citra jalan beserta mask segmentasinya.

Tujuan utama project ini adalah menghasilkan model yang mampu memisahkan area jalan, marka, atau objek tertentu dari gambar input.

1. Fitur Utama

Implementasi arsitektur U-Net dari nol.

Training dan evaluasi model langsung melalui notebook.

Visualisasi mask prediksi.

Modularisasi kode ke dalam file terpisah: model.py, dataset.py, dan utils.py.

2. Struktur Project
.
├── AutoDriv_U_Net.ipynb        # Notebook utama
├── model.py                     # Arsitektur U-Net
├── dataset.py                   # Dataset loader
├── utils.py                     # Visualisasi & helper
├── results/                     # (Opsional) Contoh hasil prediksi
├── weights/                     # (Opsional) Model terlatih
├── requirements.txt             # Dependency
└── README.md                    # Dokumentasi project
3. Dataset

Notebook menggunakan dataset berbasis citra jalan. Pastikan kamu memiliki:

Folder berisi gambar input.

Folder berisi mask biner (0 dan 1).

Struktur umum dataset:

Dataset/
├── images/
│   ├── img_1.png
│   ├── img_2.png
│   └── ...
└── masks/
    ├── img_1.png
    ├── img_2.png
    └── ...

Masukkan path dataset ke dalam notebook sebelum training.

4. Cara Menjalankan

1. Clone repository:

git clone <repo-url>

2. Install dependency:

pip install -r requirements.txt

3. Jalankan notebook:

jupyter notebook AutoDriv_U_Net.ipynb

Sesuaikan path dataset sebelum mulai training.

5. Training Model

Model dibangun menggunakan U-Net standard dengan encoder dan decoder block.

Notebook menyediakan:

Preprocessing gambar dan mask

Data generator

Training loop menggunakan model.fit

Visualisasi training loss

Output model akan disimpan dalam folder weights/ jika ditambahkan.

6. Evaluasi & Visualisasi

Notebook mencakup:

* Prediksi mask pada gambar uji

* Plot perbandingan image, mask, dan prediction

Fungsi tersedia di utils.py:

* plot_sample()

* visualize_training()

7. Model Architecture

File model.py menyediakan:

* Conv block

* Encoder block

* Decoder block

Fungsi build_unet() untuk menghasilkan model siap pakai.

Arsitektur sesuai dengan U-Net versi klasik.

8. Catatan

Dataset tidak disertakan dalam repository.

Untuk hasil optimal, lakukan augmentasi data (bisa ditambahkan ke dataset.py).

Pastikan GPU aktif saat mengerjakan di Google Colab.

9. Lisensi

Silakan gunakan project ini untuk pembelajaran, penelitian, atau modifikasi bebas sesuai kebutuhan.
