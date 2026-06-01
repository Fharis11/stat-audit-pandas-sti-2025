import numpy as np
from scipy import stats

def confidence_interval(theta_hat, sigma, n, confidence=0.95):
    z = stats.norm.ppf((1 + confidence) / 2)
    moe = z * sigma / np.sqrt(n)
    return {
        "lower": theta_hat - moe,
        "upper": theta_hat + moe,
        "margin_of_error": moe,
        "z": z
    }

def ci_bernoulli(k, n, confidence=0.95):
    theta_hat = k / n
    sigma = np.sqrt(theta_hat * (1 - theta_hat))
    result = confidence_interval(theta_hat, sigma, n, confidence)
    result["theta_hat"] = theta_hat
    return result

def ci_poisson(data, confidence=0.95):
    data = np.array(data)
    n = len(data)
    lambda_hat = np.sum(data) / n
    sigma = np.sqrt(lambda_hat)
    result = confidence_interval(lambda_hat, sigma, n, confidence)
    result["lambda_hat"] = lambda_hat
    return result

def credible_interval(alpha, beta, confidence=0.95):
    lower_p = (1 - confidence) / 2
    upper_p = 1 - lower_p
    lower = stats.beta.ppf(lower_p, alpha, beta)
    upper = stats.beta.ppf(upper_p, alpha, beta)
    mean = alpha / (alpha + beta)
    mode = (alpha - 1) / (alpha + beta - 2) if (alpha + beta - 2) > 0 else 0.5
    return {
        "lower": lower,
        "upper": upper,
        "mean":  mean,
        "mode":  mode
    }