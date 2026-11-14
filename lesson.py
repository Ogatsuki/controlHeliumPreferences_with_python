from pathlib import Path
import tempfile
import sys
import json
import uuid

base_pre_path = "Default/Preferences"
pre_path = Path().resolve().parents[0] / base_pre_path

if not pre_path.exists():
    print("Preferences file not found.")
    sys.exit(1)
with pre_path.open("r", encoding="utf-8") as p:
    pre_raw = p.read()
    pre_dict = json.loads(pre_raw)

random_id = uuid.uuid4().hex
temp_file = Path(tempfile.mkdtemp()) / f"Preferences_{random_id}.json"

with temp_file.open("w", encoding="utf-8") as f:
    json.dump(pre_dict, f, indent=4)