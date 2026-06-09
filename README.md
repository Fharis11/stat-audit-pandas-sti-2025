#  Statistical Health Audit - pandas-dev/pandas

# Project Description
Repositori ini berisi audit statistik menyeluruh terhadap proyek open-source pandas-dev/pandas salah satu library Python paling banyak digunakan di dunia untuk analisis data. Audit ini menerapkan teknik statistik dari Minggu 11–14 (estimasi, inferensi, uji hipotesis, simulasi komputasional) untuk menjawab pertanyaan nyata tentang kesehatan proyek yang berguna bagi para maintainer-nya. Dataset diambil melalui GitHub REST API v3 pada tanggal 24 Mei 2026, mencakup issues dan pull requests dari rentang waktu 2020–2025.

# Research Questions
| # | Research Question | Technique | Week |
|---|-------------------|-----------|------|
| RQ1 | Berapa probabilitas estimasi sebuah PR akan di-merge, dan seberapa tidak pasti estimasi tersebut? | MLE Bernoulli + Confidence Interval | W11–12 |
| RQ2 | Apakah rata-rata tingkat bug report berubah secara signifikan setelah rilis major terakhir (pandas 2.0)? | MLE Poisson + Z-test satu sampel | W11–13 |
| RQ3 | Berapa probabilitas bahwa sebuah issue yang dipilih secara acak membutuhkan lebih dari 30 hari untuk ditutup, diestimasi tanpa formula analitik? | Monte Carlo Simulation | W14 |

# Struktur Repositori
- stat-audit-pandas-sti-2025/
- ├── README.md
- ├── AI_USAGE_LOG.md
- ├── data/
- │   ├── raw/
- │   │   ├── fetch_data.py
- │   │   ├── issues_raw.json
- │   │   └── pulls_raw.json
- │   └── clean/
- │       ├── clean_data.py
- │       ├── dataset.csv
- │       ├── issues.csv
- │       └── pulls.csv
- ├── notebooks/
- │   ├── 01_eda.ipynb
- │   ├── 02_estimation.ipynb
- │   ├── 03_confidence_interval.ipynb
- │   ├── 04_hypothesis_testing.ipynb
- │   └── 05_simulation.ipynb
- ├── presentation/
- │   └── video_link.md
- ├── report/
- │   └── statistical_health_report.pdf
- ├── src/
- │   ├── estimator.py
- │   ├── hypothesis.py
- │   ├── inference.py
- │   └── simulation.py
- └── requirements.txt

# Tim
| Anggota | Peran | Noteboook |
|---------|-------|----------|
| Muhamad Fharis Arradhien      | Data Engineer      (Member A) | 01_eda.ipynb                 |
| Kevindra Raditya Luthfiansyah | Estimation Analyst (Member B) | 02_estimation.ipynb          |
| Adhinda Zahra Dinanti         | Inference Analyst  (Member C) | 03_confidence_interval.ipynb |
| Nayla Andhini Novia Dewani    | Hypothesis Analyst (Member D) | 04_hypothesis_testing.ipynb  |
| Bram Radhitya Riezky Prayoga  | Computation Analyst(Member E) | 05_simulation.ipynb          |

# Cara Menjalankan
# 1. Clone repositori
git clone https://github.com/Fharis11/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025

# 2. Install dependensi
pip install -r requirements.txt

# 3. Ambil data (opsional, data sudah tersedia di data/clean/)
python data/raw/fetch_data.py
python data/clean/clean_data.py

# 4. Jalankan notebook secara berurutan
jupyter notebook

# Temuan Utama
Berdasarkan audit statistik yang dilakukan terhadap data issues dan pull requests dari repositori pandas, berikut adalah kesimpulan utama yang kami peroleh :
- Penerimaan Pull Request (RQ1): 
Angka probabilitas sebuah Pull Request (PR) di-merge ke dalam repositori pandas saat ini sedang dihitung menggunakan metode Maximum Likelihood Estimation (MLE) Bernoulli di dalam 02_estimation.ipynb oleh Kevindra. Selanjutnya, tingkat ketidakpastian dari estimasi tersebut akan divalidasi menggunakan Confidence Interval di 03_confidence_interval.ipynb oleh Adhinda, untuk memberikan rentang persentase penerimaan PR yang paling representatif.

- Dampak Rilis pandas 2.0 terhadap Bug Reports (RQ2):
Perubahan rata-rata tingkat laporan bug sebelum dan sesudah rilis major pandas 2.0 sedang diuji di dalam 04_hypothesis_testing.ipynb oleh Nayla. Melalui pemodelan MLE Poisson dan uji hipotesis statistik (Z-test satu sampel), Notebook ini akan menghasilkan nilai p-value yang akan menentukan apakah terdapat lonjakan atau penurunan bug yang signifikan secara statistik pasca-rilis.

- Estimasi Waktu Resolusi Issue (RQ3):
Probabilitas bahwa sebuah issue memakan waktu lebih dari 30 hari untuk ditutup sedang diestimasi tanpa menggunakan formula analitik, melainkan melalui komputasi numerik di 05_simulation.ipynb oleh Bram. Notebook ini menjalankan Simulasi Monte Carlo dengan ribuan iterasi untuk melihat pola distribusi waktu resolusi issue secara empiris, sehingga menghasilkan persentase probabilitas yang mendekati kondisi nyata di lapangan.

# Dataset
Sumber: GitHub REST API v3
Repo diaudit: pandas-dev/pandas
Tanggal pengambilan data: 24 - 05 - 2026
Rentang waktu: 2020–2025
Jumlah issues:5.650
Jumlah PRs: 2.500
Keterbatasan yang diketahui : API GitHub membatasi 5.000 request/jam, data diambil dengan pagination dan retry logic. Issues yang dibuka kembali diperlakukan sebagai satu entri berdasarkan tanggal penutupan terakhir.