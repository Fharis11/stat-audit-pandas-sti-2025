# AI Usage Log — moby/moby Statistical Audit

## Summary

| Member | Peran | Tools | ~% Kode AI-assisted | Interpretation AI-assisted? |
|--------|-------|-------|--------------------|-----------------------------|
| Muhamad Fharis Arradhien | Data Engineer | Claude | 45 % | No |
| Kevindra Raditya Luthfiansyah | Estimation Analyst | Claude | 45 % | No |
| Adhinda Zahra Dinanti | Inference Analyst | Gemini | 40 % | No |
| Nayla Andhini Novia Dewani | Hypothesis Analyst | Gemini | 47 % | No |
| Bram Radhitya Riezky Prayoga | Computation Analyst | - | - % | No |

# Per-Member Detail
# Member A —  Muhamad Fharis Arradhien
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|------|------|------------------|----------------------|
| 1 | Data Collecting | Claude | Ubahkan Logic dari Codingan diatas agar Mendapatkan Issues & PRs sesuai dengan tergat yang diinginkan | Mengambil referensi code untuk Colleting Data |
| 2 | EDA | Claude | Buatkan Analogi Mengenai Pembuatan Grafik untuk pengerjaan EDA | Mengambil referensi Aalogi Code untuk Grafik pada EDA |

# Member B — Kevindra Raditya Luthfiansyah
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|------|------|------------------|----------------------|
| 1 | Tambah validasi input (data kosong, negatif) | Claude | Cara menambahkan pengecekan input yang proper untuk fungsi numpy | diintegrasikan ke fungsi yang sudah ada |
| 2 | Implementasi Clopper–Pearson CI | Claude | Cara implementasi Clopper-Pearson CI menggunakan scipy | edge case k=0 dan k=n ditambahkan sendiri |

# Member C — Adhinda Zahra Dinanti
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|
| 1 | Bagaimana rumus bekerja | Gemini | "buatkan analogi dari rumus rumus yang saya berikan dengan bahasa yang mudah" | Digunakan sebagai brainstorming | Saya tidak menjadikan AI patokan 100%, hanya menjadi referensi bagaimana cara menganalogikan kode secara mudah |
| 2 | Pengecekan apakah kode sudah benar | Gemini | "apakah kode yang saya beri sudah benar?" | Digunakan sebagai validasi kode | Gemini menyarankan pergantian kode untuk beberapa bagian, namun saya mendiskusikan dengan tim dan tetap menggunakan konsep awal |

# Member D — Nayla Andhini Novia Dewani
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Formulasi logika fungsi statistik modular Poisson Z-test | Gemini | "tolong buatkan kerangka fungsi modular python untuk rumus uji satu sempel dan dua sampel berbasis asumsi distribusi Poisson" | Digunakan sebagai basis pengembangan logika kode pada file sc/hypothesis.py sebelum diintegerasikan ke dalam eksekusi notebook 04 | Dievaluasi dengan mencocokkan hasil return value fungsi terhadap kalkulasi manual, serta memastikan tidak ada error saat di-import ke notebook |
| 2 | Sinkronisasi visualisasi kurva distribusi dua arah (Subplot VS Code) | Gemini | "Tolong rapikan kode matplotlib subplots untuk memetakan z-score aktual dan daerah kritis z=1.96 secara berdampingan" | Digunakan untuk memperbaiki bug tata letak grafik di lingkungan lokal sehingga menghasilkan visualisasi kurva yang presisi dan bersih| Dievaluasi berdasarkan kejelasan posisi garis z-critical, area rejection region berwarna merah, dan ketepatan render plot saat cell dijalankan |

# Member E — Bram Radhitya Riezky Prayoga
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan |
|---|------|------|------------------|----------------------|
| 1 | | | | |

# Group Reflection
