#  Statistical Health Audit — pandas-dev/pandas
> Final Group Assignment | Probability & Statistics | STI 2025
Deskripsi Proyek
Repositori ini berisi audit statistik menyeluruh terhadap proyek open-source pandas-dev/pandas — salah satu library Python paling banyak digunakan di dunia untuk analisis data. Audit ini menerapkan teknik statistik dari Minggu 11–14 (estimasi, inferensi, uji hipotesis, simulasi komputasional) untuk menjawab pertanyaan nyata tentang kesehatan proyek yang berguna bagi para maintainer-nya.
Dataset diambil melalui GitHub REST API v3 pada tanggal 24 Mei 2026, mencakup issues dan pull requests dari rentang waktu 2020–2025.

# Research Questions
| # | Research Question | Technique | Week |
|---|-------------------|-----------|------|
| RQ1 | Berapa probabilitas estimasi sebuah PR akan di-merge, dan seberapa tidak pasti estimasi tersebut? | MLE Bernoulli + Confidence Interval | W11–12 |
| RQ2 | Apakah rata-rata tingkat bug report berubah secara signifikan setelah rilis major terakhir (pandas 2.0)? | MLE Poisson + Z-test satu sampel | W11–13 |
| RQ3 | Berapa probabilitas bahwa sebuah issue yang dipilih secara acak membutuhkan lebih dari 30 hari untuk ditutup, diestimasi tanpa formula analitik? | Monte Carlo Simulation | W14 |

# Struktur Repositori
stat-audit-pandas-sti-2025/
├── README.md
├── AI_USAGE_LOG.md
├── data/
│   ├── raw/     
│   └── clean/
├── src/
│   ├── estimator.py  
│   ├── inference.py  
│   ├── hypothesis.py 
│   └── simulation.py 
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_confidence_interval.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
├── report/statistical_health_report.pdf
├── presentation/video_link.md
└── requirements.txt

# Tim
| Anggota | Peran | Notebook |
|---------|-------|----------|
| Muhamad Fharis Arradhien      | Data Engineer      (Member A) | 01_eda.ipynb                 |
| Kevindra Raditya Luthfiansyah | Estimation Analyst (Member B) | 02_estimation.ipynb          |
| Nayla Andhini Novia Dewani    | Inference Analyst  (Member C) | 03_confidence_interval.ipynb |
| Adhinda Zahra Dinanti         | Hypothesis Analyst (Member D) | 04_hypothesis_testing.ipynb  |
| Bram Radhitya Riezky Prayoga  | Computation Analyst(Member E) | 05_simulation.ipynb          |

# Cara Menjalankan
# 1. Clone repositori
git clone https://github.com/<username>/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan notebook secara berurutan
jupyter notebook

# Dataset
Sumber: GitHub REST API v3
Repo diaudit: `pandas-dev/pandas`
Tanggal pengambilan data: 24 - 05 - 2026
Rentang waktu: 2020–2025
Keterbatasan yang diketahui : API GitHub membatasi 5.000 request/jam; data diambil dengan pagination dan retry logic. Issues yang dibuka kembali (reopened) diperlakukan sebagai satu entri berdasarkan tanggal penutupan terakhir.