import numpy as np

def mle_bernoulli(data):
    data = np.asarray(data)
    if data.size == 0:
        raise ValueError("data is empty")
    if data.dtype == bool:
        data = data.astype(int)
    uniques = np.unique(data)
    if not np.all(np.isin(uniques, [0, 1])):
        raise ValueError("data must contain only 0/1 or boolean values")
    k = int(np.sum(data))
    n = int(data.size)
    theta_hat = k / n
    return {"theta_hat": theta_hat, "k": k, "n": n}

def mle_poisson(data):
    data = np.asarray(data)
    if data.size == 0:
        raise ValueError("data is empty")
    if np.any(data < 0):
        raise ValueError("data must contain non-negative counts")
    lambda_hat = float(np.mean(data))
    return {"lambda_hat": lambda_hat, "n": int(data.size), "sum": float(np.sum(data))}

def beta_posterior(k, m):
    alpha = k + 1
    beta_param = m + 1
    mean = alpha / (alpha + beta_param)
    if alpha > 1 and beta_param > 1:
        mode = (alpha - 1) / (alpha + beta_param - 2)
    else:
        mode = np.nan
    return {"alpha": alpha, "beta": beta_param, "mode": mode, "mean": mean}

def log_likelihood_bernoulli(theta, k, n):
    theta = np.clip(theta, 1e-12, 1 - 1e-12)
    return k * np.log(theta) + (n - k) * np.log(1 - theta)

def log_likelihood_poisson(theta, data):
    data = np.asarray(data)
    theta = np.clip(theta, 1e-12, None)
    n = int(data.size)
    return np.sum(data) * np.log(theta) - n * theta