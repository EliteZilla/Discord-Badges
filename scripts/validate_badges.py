#!/usr/bin/env python3
from pathlib import Path
import json, re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "badges.json"
VALID_STATUS = {"active","experimental","legacy","retired"}
VALID_SOURCE = {"official","community","historical"}
ID_RE = re.compile(r"^[a-z0-9-]+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

data = json.loads(DATA.read_text(encoding="utf-8"))
errors, seen = [], set()

for i, badge in enumerate(data.get("badges", [])):
    p = f"badges[{i}] ({badge.get('id','missing-id')})"
    for field in ("id","name","category","classification","status","obtainability","description","how_to_obtain","primary_source","source_type","last_verified"):
        if not badge.get(field):
            errors.append(f"{p}: missing {field}")
    bid = badge.get("id","")
    if not ID_RE.match(bid): errors.append(f"{p}: invalid id")
    if bid in seen: errors.append(f"{p}: duplicate id")
    seen.add(bid)
    if badge.get("status") not in VALID_STATUS: errors.append(f"{p}: invalid status")
    if badge.get("source_type") not in VALID_SOURCE: errors.append(f"{p}: invalid source_type")
    if not DATE_RE.match(badge.get("last_verified","")): errors.append(f"{p}: invalid date")
    u = urlparse(badge.get("primary_source",""))
    if u.scheme not in ("http","https") or not u.netloc: errors.append(f"{p}: invalid source URL")
    if badge.get("asset") and not (ROOT / badge["asset"]).exists():
        errors.append(f"{p}: missing asset {badge['asset']}")

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    raise SystemExit(1)

print(f"Validated {len(data['badges'])} badge entries successfully.")
