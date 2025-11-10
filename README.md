🚗 U-Net Autonomous Driving Segmentation

Selamat datang di project segmentasi gambar untuk kebutuhan autonomous driving. Proyek ini membangun model U-Net dari nol untuk memprediksi mask jalan atau objek tertentu dari citra kamera. Semua dirancang biar gampang dipakai, gampang dibaca, dan tentu saja gampang dikembangkan.

✨ Kenapa Project Ini Keren?

Dibangun dari arsitektur U-Net klasik yang terbukti kuat buat tugas segmentasi.

Kode udah dipisah jadi model.py, dataset.py, dan utils.py supaya rapih.

Notebook utama langsung siap buat training, evaluasi, dan visualisasi.

Bisa kamu modifikasi bebas buat dataset lain.

📂 Struktur Repository

.
├── AutoDriv_U_Net.ipynb        # Notebook utama
├── model.py                     # Arsitektur U-Net
├── dataset.py                   # Loader dataset
├── utils.py                     # Fungsi visualisasi & helper
├── requirements.txt             # Dependency project
├── results/                     # (Opsional) Hasil prediksi
└── weights/                     # (Opsional) Model terlatih

🧠 U-Net: Singkatnya

U-Net terdiri dari dua jalur:

Encoder buat menangkap konteks

Decoder buat menebalkan detail dan memprediksi mask

Dengan skip-connection, model bisa mempertahankan informasi spatial secara akurat.

🗂 Dataset

Gunakan dataset yang punya struktur seperti ini:

Dataset/
├── images/
│   ├── img_1.png
│   ├── img_2.png
│   └── ...
└── masks/
    ├── img_1.png
    ├── img_2.png
    └── ...

Mask idealnya grayscale dengan nilai 0 dan 1.

Dataset tidak disertakan untuk menjaga ukuran repo tetap ringan.

▶ Cara Menjalankan Project

Clone repository:

git clone <repo-url>

Install dependency:

pip install -r requirements.txt

Jalankan notebook:

jupyter notebook AutoDriv_U_Net.ipynb

Sesuaikan path dataset dan mulai training.

🔍 Training & Evaluasi

Notebook menyediakan:

Training loop

Loss curve

Visualisasi perbandingan image – mask – prediction

Simpan model otomatis (opsional)

Kamu juga bisa pakai utilitas dari utils.py:

plot_sample() buat menampilkan 1 sample prediksi

visualize_training() buat grafik loss

🎯 Hasil Prediksi

Hasil prediksi bisa kamu simpan dalam folder results/.
Kalau mau, tambahkan beberapa sample ke README ini buat showcase.

🤝 Kontribusi

Feel free buat fork project ini, tambah fitur kayak:

Data augmentation

IoU / Dice evaluation

U-Net++ atau Attention U-Net

Deployment ke Streamlit / HuggingFace Spaces

📜 Lisensi

Silakan digunakan secara bebas untuk pembelajaran maupun riset.
