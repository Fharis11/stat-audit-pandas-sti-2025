# 📊 Statistical Health Audit — pandas-dev/pandas

> Final Group Assignment | Probability & Statistics | STI 2025

## 🔬 Research Questions

| # | Research Question | Technique | Week |
|---|-------------------|-----------|------|
| RQ1 | Berapa probabilitas estimasi sebuah PR akan di-merge, dan seberapa tidak pasti estimasi tersebut? | MLE Bernoulli + Confidence Interval | W11–12 |
| RQ2 | Apakah rata-rata tingkat bug report berubah secara signifikan setelah rilis major terakhir (pandas 2.0)? | MLE Poisson + Z-test satu sampel | W11–13 |
| RQ3 | Berapa probabilitas bahwa sebuah issue yang dipilih secara acak membutuhkan lebih dari 30 hari untuk ditutup, diestimasi tanpa formula analitik? | Monte Carlo Simulation | W14 |

## 📁 Struktur Repositori

stat-audit-pandas-sti-2025/
├── README.md
├── AI_USAGE_LOG.md
├── data/
│   ├── raw/          ← data asli dari GitHub API, tidak dimodifikasi
│   └── clean/        ← dataset.csv hasil pembersihan
├── src/
│   ├── estimator.py  ← MLE & Beta posterior
│   ├── inference.py  ← Confidence & credible intervals
│   ├── hypothesis.py ← Z-test
│   └── simulation.py ← Monte Carlo, Bloom Filter, MCMC
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_confidence_interval.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
├── report/statistical_health_report.pdf
├── presentation/video_link.md
└── requirements.txt

## 👥 Tim

| Anggota | Peran | Notebook |
|---------|-------|----------|
| Member A | Data Engineer | 01_eda.ipynb |
| Member B | Estimation Analyst | 02_estimation.ipynb |
| Member C | Inference Analyst | 03_confidence_interval.ipynb |
| Member D | Hypothesis Analyst | 04_hypothesis_testing.ipynb |
| Member E | Computation Analyst | 05_simulation.ipynb |

## ▶️ Cara Menjalankan

```bash
pip install -r requirements.txt
jupyter notebook
```

## 📌 Dataset

- **Sumber:** GitHub REST API v3
- **Repo diaudit:** `pandas-dev/pandas`
- **Tanggal pengambilan data:** [isi nanti]
- **Rentang waktu:** 2017–2025