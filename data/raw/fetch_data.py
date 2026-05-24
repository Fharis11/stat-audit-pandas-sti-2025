import requests
import json
import time
import os

GITHUB_TOKEN = "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"
REPO         = "pandas-dev/pandas"
HEADERS      = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept":        "application/vnd.github.v3+json"
}

def fetch_all_pages(url, params, label="data", max_pages=50):
    all_items = []
    page = 1
    while True:
        params["page"] = page
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code == 403:
            reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset_time - time.time(), 0) + 5
            print(f"Rate limit! Tunggu {wait:.0f} detik...")
            time.sleep(wait)
            continue

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text[:200]}")
            break

        items = response.json()
        if not items:
            break

        all_items.extend(items)
        print(f"{label} — hal. {page}: {len(items)} item (total: {len(all_items)})")

        if "next" not in response.headers.get("Link", ""):
            break

        page += 1
        if page > max_pages:
            print(f"Batas {max_pages} halaman tercapai")
            break

        time.sleep(0.5)

    return all_items


def main():
    os.makedirs("data/raw", exist_ok=True)

    print("\nMengambil issues murni via Search API (per tahun)...")
    issues_only = []

    tahun_range = [
        ("2020-01-01", "2020-12-31"),
        ("2021-01-01", "2021-12-31"),
        ("2022-01-01", "2022-12-31"),
        ("2023-01-01", "2023-12-31"),
        ("2024-01-01", "2024-12-31"),
        ("2025-01-01", "2025-12-31"),
    ]

    for start, end in tahun_range:
        page = 1
        print(f"\n  Periode: {start} s/d {end}")
        while True:
            url = "https://api.github.com/search/issues"
            params = {
                "q":        f"repo:{REPO} is:issue is:closed created:{start}..{end}",
                "per_page": 100,
                "page":     page,
                "sort":     "created",
                "order":    "desc"
            }
            response = requests.get(url, headers=HEADERS, params=params)

            if response.status_code == 403:
                reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
                wait = max(reset_time - time.time(), 0) + 5
                print(f"  Rate limit! Tunggu {wait:.0f} detik...")
                time.sleep(wait)
                continue

            if response.status_code != 200:
                print(f"  Error {response.status_code}: {response.text[:200]}")
                break

            data  = response.json()
            items = data.get("items", [])
            if not items:
                break

            issues_only.extend(items)
            total = data.get("total_count", "?")
            print(f"  hal. {page}: {len(items)} item (tersedia: {total}, terkumpul: {len(issues_only)})")

            if "next" not in response.headers.get("Link", ""):
                break

            page += 1
            if page > 10:
                break

            time.sleep(2)

    # Deduplikasi
    seen = set()
    unique_issues = []
    for i in issues_only:
        if i["number"] not in seen:
            seen.add(i["number"])
            unique_issues.append(i)
    issues_only = unique_issues

    print(f"\nTotal issues unik: {len(issues_only)}")
    with open("data/raw/issues_raw.json", "w") as f:
        json.dump(issues_only, f, indent=2)
    print("Disimpan: data/raw/issues_raw.json")

    print("\nMengambil pull requests...")
    pulls = fetch_all_pages(
        url       = f"https://api.github.com/repos/{REPO}/pulls",
        params    = {"state": "closed", "per_page": 100},
        label     = "pulls",
        max_pages = 25
    )
    print(f"Total pull requests: {len(pulls)}")
    with open("data/raw/pulls_raw.json", "w") as f:
        json.dump(pulls, f, indent=2)
    print("Disimpan: data/raw/pulls_raw.json")

    print("\nSelesai!")
    print(f"   issues_raw.json → {len(issues_only)} issues")
    print(f"   pulls_raw.json  → {len(pulls)} pull requests")


if __name__ == "__main__":
    main()