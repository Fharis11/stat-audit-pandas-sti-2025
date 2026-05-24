import json
import pandas as pd
import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw")
CLEAN_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(CLEAN_DIR, exist_ok=True)

print("Memuat data raw...")
with open(os.path.join(RAW_DIR, "issues_raw.json")) as f:
    issues_raw = json.load(f)
with open(os.path.join(RAW_DIR, "pulls_raw.json")) as f:
    pulls_raw = json.load(f)
print(f"  issues_raw : {len(issues_raw)} item")
print(f"  pulls_raw  : {len(pulls_raw)} item")

def parse_issues(raw):
    rows = []
    for item in raw:
        created   = pd.to_datetime(item["created_at"], utc=True)
        closed    = pd.to_datetime(item["closed_at"],  utc=True) if item.get("closed_at") else None
        days_open = (closed - created).days if closed else None
        labels    = [l["name"] for l in item.get("labels", [])]
        rows.append({
            "id"           : item["number"],
            "type"         : "issue",
            "state"        : item["state"],
            "created_at"   : created,
            "closed_at"    : closed,
            "days_to_close": days_open,
            "label_names"  : ",".join(labels),
            "is_bug"       : int(any("bug" in l.lower() for l in labels)),
            "is_merged"    : 0,
            "year_month"   : created.strftime("%Y-%m"),
            "year"         : created.year,
        })
    return pd.DataFrame(rows)

def parse_pulls(raw):
    rows = []
    for item in raw:
        created   = pd.to_datetime(item["created_at"], utc=True)
        closed    = pd.to_datetime(item["closed_at"],  utc=True) if item.get("closed_at") else None
        days_open = (closed - created).days if closed else None
        labels    = [l["name"] for l in item.get("labels", [])]
        rows.append({
            "id"           : item["number"],
            "type"         : "pull_request",
            "state"        : item["state"],
            "created_at"   : created,
            "closed_at"    : closed,
            "days_to_close": days_open,
            "label_names"  : ",".join(labels),
            "is_bug"       : int(any("bug" in l.lower() for l in labels)),
            "is_merged"    : int(item.get("merged_at") is not None),
            "year_month"   : created.strftime("%Y-%m"),
            "year"         : created.year,
        })
    return pd.DataFrame(rows)

print("\nMemproses...")
df_issues = parse_issues(issues_raw)
df_pulls  = parse_pulls(pulls_raw)
df_all    = pd.concat([df_issues, df_pulls], ignore_index=True)

before = len(df_all)
df_all = df_all.dropna(subset=["days_to_close"])
df_all = df_all[df_all["days_to_close"] >= 0]
print(f"  Baris dihapus (anomali): {before - len(df_all)}")

df_all.to_csv(   os.path.join(CLEAN_DIR, "dataset.csv"), index=False)
df_issues.to_csv(os.path.join(CLEAN_DIR, "issues.csv"),  index=False)
df_pulls.to_csv( os.path.join(CLEAN_DIR, "pulls.csv"),   index=False)

print("\nSELESAI!")
print(f"   dataset.csv → {len(df_all)} baris")
print(f"   issues.csv  → {len(df_issues)} baris")
print(f"   pulls.csv   → {len(df_pulls)} baris")
print(f"\nKolom:")
print(df_all.dtypes)