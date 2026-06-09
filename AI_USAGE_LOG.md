# AI Usage Log - moby/moby Statistical Audit

# Summary
| Member | Peran | Tools | ~% Kode AI-assisted | Interpretation AI-assisted? |
|--------|-------|-------|--------------------|-----------------------------|
| Muhamad Fharis Arradhien | Data Engineer | Claude | 45 % | No |
| Kevindra Raditya Luthfiansyah | Estimation Analyst | Claude | 45 % | No |
| Adhinda Zahra Dinanti | Inference Analyst | Gemini | 40 % | No |
| Nayla Andhini Novia Dewani | Hypothesis Analyst | Gemini | 47 % | No |
| Bram Radhitya Riezky Prayoga | Computation Analyst | ChatGPT | 45 % | No |

# Per-Member Detail
# Member A - Muhamad Fharis Arradhien
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Data Collecting | Claude | Ubahkan Logic dari Codingan diatas agar Mendapatkan Issues & PRs sesuai dengan tergat yang diinginkan | Mengambil referensi code untuk Colleting Data | Kode dieksekusi untuk memastikan data Issues dan PRs yang ditarik dari API/sumber sesuai dengan kriteria target (jumlah, status, rentang waktu) dan berjalan tanpa error |
| 2 | EDA | Claude | Buatkan Analogi Mengenai Pembuatan Grafik untuk pengerjaan EDA | Mengambil referensi Aalogi Code untuk Grafik pada EDA | Kode referensi diuji coba pada dataset untuk memastikan grafik/visualisasi berhasil di-render, representatif, dan jelas dalam menampilkan polanya |

# Member B - Kevindra Raditya Luthfiansyah
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Tambah validasi input (data kosong, negatif) | Claude | Cara menambahkan pengecekan input yang proper untuk fungsi numpy | diintegrasikan ke fungsi yang sudah ada | Diuji dengan input tidak valid (kosong/negatif) untuk memastikan error handling berfungsi tanpa crash |
| 2 | Implementasi Clopper–Pearson CI | Claude | Cara implementasi Clopper-Pearson CI menggunakan scipy | edge case k=0 dan k=n ditambahkan sendiri | Hasil CI dicocokkan dengan kalkulator statistik standar, dan edge case (k=0, k=n) diuji agar tidak error |

# Member C - Adhinda Zahra Dinanti
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Bagaimana rumus bekerja | Gemini | "buatkan analogi dari rumus rumus yang saya berikan dengan bahasa yang mudah" | Digunakan sebagai brainstorming | Saya tidak menjadikan AI patokan 100%, hanya menjadi referensi bagaimana cara menganalogikan kode secara mudah |
| 2 | Pengecekan apakah kode sudah benar | Gemini | "apakah kode yang saya beri sudah benar?" | Digunakan sebagai validasi kode | Gemini menyarankan pergantian kode untuk beberapa bagian, namun saya mendiskusikan dengan tim dan tetap menggunakan konsep awal |

# Member D - Nayla Andhini Novia Dewani
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Formulasi logika fungsi statistik modular Poisson Z-test | Gemini | "tolong buatkan kerangka fungsi modular python untuk rumus uji satu sempel dan dua sampel berbasis asumsi distribusi Poisson" | Digunakan sebagai basis pengembangan logika kode pada file sc/hypothesis.py sebelum diintegerasikan ke dalam eksekusi notebook 04 | Dievaluasi dengan mencocokkan hasil return value fungsi terhadap kalkulasi manual, serta memastikan tidak ada error saat di-import ke notebook |
| 2 | Sinkronisasi visualisasi kurva distribusi dua arah (Subplot VS Code) | Gemini | "Tolong rapikan kode matplotlib subplots untuk memetakan z-score aktual dan daerah kritis z=1.96 secara berdampingan" | Digunakan untuk memperbaiki bug tata letak grafik di lingkungan lokal sehingga menghasilkan visualisasi kurva yang presisi dan bersih| Dievaluasi berdasarkan kejelasan posisi garis z-critical, area rejection region berwarna merah, dan ketepatan render plot saat cell dijalankan |

# Member E - Bram Radhitya Riezky Prayoga
| # | Task | Tool | Prompt (ringkas) | Cara output digunakan | Bagaimana hasil dievaluasi |
|---|------|------|------------------|----------------------|---------------------------|
| 1 | Memahami fungsi Monte Carlo Estimation | ChatGPT | gimana cara kerja fungsi estimate_probability pada monte carlo simulation | Digunakan sebagai referensi untuk memahami cara kerja fungsi estimasi probabilitas pada Monte Carlo Simulation | Penjelasan dicocokkan dengan logika kode simulasi yang dibuat untuk memastikan tidak ada miskonsepsi |
| 2 | Memahami pengaruh parameter terhadap performa Bloom Filter | ChatGPT | ap dampak pemilihan nilai m dan k yang terlalu besar atau terlalu kecil terhadap performa dan false positive rate bloom filter | Digunakan untuk memahami hubungan antarparameter Bloom Filter sebelum implementasi pada tugas | Teori divalidasi melalui eksperimen kode dengan mengubah nilai m dan k lalu mengamati perubahan false positive rate |
| 3 | Memahami mekanisme acceptance probability pada MCMC Knapsack | ChatGPT | knp algoritma mcmc ttp menerima solusi yang lebih buruk pada kondisi tertentu dan bagaimana hal tersebut membantu pencarian solusi optimal | Digunakan untuk memahami mekanisme acceptance probability pada algoritma MCMC Knapsack | Pemahaman divalidasi dengan memantau log eksekusi algoritma untuk memastikan ia bisa keluar dari local optimum |

# Group Reflection
Selama tiga minggu pengerjaan projek ini, pemanfaatan AI dalam tim kami berkembang secara bertahap dan semakin terarah. Pada minggu pertama, kami lebih cenderung menggunakan AI secara exploratif terutama untuk memahami cara kerja API GitHub serta struktur data yang siap diaudit. AI memberikan dukungan besar kepada Member A dalam merumuskan logika pengambilan data, tetapi keputusan mengenai parameter seperti jangka waktu dan jumlah data tetap kami tentukan sendiri sesuai kebutuhan analisis.

Memasuki minggu kedua, penggunaan AI mulai lebih terfokus pada validasi kode. Member C dan D memanfaatkan AI untuk memeriksa apakah rumus yang diterapkan sudah sesuai, tetapi interpretasi hasil dan formulasi hipotesis tetap dilakukan secara mandiri. Terdapat satu momen ketika AI merekomendasikan perubahan pendekatan untuk interval kepercayaan, namun setelah berdiskusi tim kami memutuskan untuk tetap bertahan dengan metode yang awal karena lebih sesuai dengan referensi Tsun (2020).

Pada minggu ketiga, Member E menggunakan AI untuk memahami konsep MCMC dan Bloom Filter secara mendalam sebelum melaksanakan implementasi bukan untuk menciptakan kode, melainkan untuk membangun pemahaman intuitif yang tepat tentang algoritma tersebut.

AI sangat bagus dalam mengelola scaffolding kode dan penjelasan konsep. Namun, kami menemukan bahwa keluaran AI perlu divalidasi secara kritis beberapa rekomendasi tidak sesuai dengan konteks dataset kami atau spesifikasi tugas yang ada. Ada kalanya kami memilih untuk tidak menggunakan AI, contohnya ketika merumuskan pertanyaan penelitian dan menulis interpretasi hasil karena bagian tersebut memerlukan pemahaman kontekstual tentang pandas-dev/pandas yang tidak bisa diserahkan kepada AI.