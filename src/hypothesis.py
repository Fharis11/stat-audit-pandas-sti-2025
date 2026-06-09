import numpy as np
from scipy import stats

def z_test_one_sample(x_bar, mu0, sigma, n, alternative="two-sided", alpha=0.05):
    """
    Fungsi untuk melakukan Uji Z Satu Sampel (One-Sample Z-Test)
    """
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))
 
    if alternative == "two-sided":
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == "greater":
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == "less":
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("alternative harus 'two-sided', 'greater', atau 'less'")
 
    decision = "Tolak H₀" if p_value < alpha else "Gagal Tolak H₀"
 
    interpretation = (
        f"Dengan z={z_stat:.4f} dan p-value={p_value:.4f}, "
        f"pada a={alpha}, kita {decision}. "
        f"{'Terdapat' if p_value < alpha else 'Tidak terdapat'} "
        f"bukti statistik yang signifikan."
    )
 
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }
 
def z_test_two_sample(x_bar1, x_bar2, sigma1, sigma2, n1, n2, alternative="two-sided", alpha=0.05):
    """
    Fungsi untuk melakukan Uji Z Dua Sampel (Two-Sample Z-Test)
    Menggunakan rumus standard error untuk dua kelompok independen.
    """
    se = np.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))
    z_stat = (x_bar1 - x_bar2) / se
 
    if alternative == "two-sided":
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == "greater":
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == "less":
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("alternative harus 'two-sided', 'greater', atau 'less'")
 
    decision = "Tolak H₀" if p_value < alpha else "Gagal Tolak H₀"
 
    interpretation = (
        f"Dengan z={z_stat:.4f} dan p-value={p_value:.4f}, "
        f"pada a={alpha}, kita {decision}. "
        f"{'Terdapat' if p_value < alpha else 'Tidak terdapat'} "
        f"perbedaan yang signifikan antara dua kelompok."
    )
 
    return {
        "z_stat": z_stat,
        "p_value": p_value,
        "decision": decision,
        "interpretation": interpretation
    }