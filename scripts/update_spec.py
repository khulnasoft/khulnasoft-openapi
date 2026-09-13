#!/usr/bin/env python3
"""
Auto-update openapi.yaml from the publisher service.
Fetches the latest OpenAPI spec, preserves custom oaiMeta fields, and validates.
"""

import sys
import yaml
import json
import urllib.request
import urllib.error
import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
SPEC_PATH = ROOT_DIR / "openapi.yaml"
PUBLISHER_URL = "https://api.khulnasoft.com/v1/openapi.json"

def load_spec(path):
    """Load YAML spec."""
    with open(path, "r") as f:
        return yaml.safe_load(f)

def fetch_publisher_spec():
    """Fetch the latest spec from the publisher."""
    print(f"Fetching spec from {PUBLISHER_URL}...")
    try:
        req = urllib.request.Request(PUBLISHER_URL, headers={"User-Agent": "khulnasoft-openapi/1.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            spec = json.loads(response.read().decode("utf-8"))
        print("Publisher spec fetched successfully.")
        return spec
    except urllib.error.URLError as e:
        print(f"Error fetching publisher spec: {e}")
        sys.exit(1)

def extract_oai_meta(spec):
    """Extract all oaiMeta custom fields from the spec."""
    meta = {}
    
    # Extract from paths
    if "paths" in spec:
        for path, path_item in spec["paths"].items():
            for method, operation in path_item.items():
                if method.startswith("x-"):
                    continue
                if "oaiMeta" in operation:
                    meta.setdefault("paths", {}).setdefault(path, {})[method] = operation.pop("oaiMeta")
    
    # Extract from schemas (if any oaiMeta there)
    if "components" in spec and "schemas" in spec["components"]:
        for schema_name, schema in spec["components"]["schemas"].items():
            if isinstance(schema, dict) and "oaiMeta" in schema:
                meta.setdefault("components", {}).setdefault("schemas", {}).setdefault(schema_name, {})["oaiMeta"] = schema.pop("oaiMeta")
    
    return meta

def merge_oai_meta(fresh_spec, preserved_meta):
    """Merge preserved oaiMeta fields back into the fresh spec."""
    # Merge path-level oaiMeta
    if "paths" in preserved_meta:
        for path, path_item in preserved_meta["paths"].items():
            if path not in fresh_spec.get("paths", {}):
                print(f"Warning: Path {path} not found in fresh spec, skipping oaiMeta")
                continue
            for method, meta in path_item.items():
                if method in fresh_spec["paths"][path]:
                    fresh_spec["paths"][path][method]["oaiMeta"] = meta
    
    # Merge schema-level oaiMeta
    if "components" in preserved_meta and "schemas" in preserved_meta["components"]:
        for schema_name, schema_meta in preserved_meta["components"]["schemas"].items():
            if schema_name in fresh_spec.get("components", {}).get("schemas", {}):
                fresh_spec["components"]["schemas"][schema_name]["oaiMeta"] = schema_meta
    
    return fresh_spec

def validate_spec(spec):
    """Run our validation script on the spec."""
    temp_spec = ROOT_DIR / "openapi-temp-validate.yaml"
    with open(temp_spec, "w") as f:
        yaml.dump(spec, f, sort_keys=False)
    
    result = subprocess.run(
        ["python3", str(ROOT_DIR / "scripts" / "validate_spec.py")],
        capture_output=True, text=True
    )
    temp_spec.unlink(missing_ok=True)
    
    if result.returncode != 0:
        print(f"Validation failed:\n{result.stdout}")
        return False
    return True

def write_spec(spec):
    """Write the updated spec to openapi.yaml."""
    with open(SPEC_PATH, "w") as f:
        yaml.dump(spec, f, Dumper=yaml.Dumper, sort_keys=False, default_flow_style=False)
    print(f"Updated {SPEC_PATH}")

def main():
    print("=" * 60)
    print("Auto-update: KhulnaSoft OpenAPI Specification")
    print("=" * 60)
    
    # Step 1: Extract custom oaiMeta fields from current spec
    print("\n[1/4] Extracting custom metadata from current spec...")
    current_spec = load_spec(SPEC_PATH)
    preserved_meta = extract_oai_meta(current_spec)
    print(f"Preserved {len(preserved_meta.get('paths', {}))} path-level and {len(preserved_meta.get('components', {}).get('schemas', {}))} schema-level oaiMeta fields")
    
    # Step 2: Fetch fresh spec from publisher
    print("\n[2/4] Fetching fresh spec from publisher...")
    fresh_spec = fetch_publisher_spec()
    
    # Step 3: Merge preserved metadata
    print("\n[3/4] Merging custom metadata...")
    merged_spec = merge_oai_meta(fresh_spec, preserved_meta)
    
    # Step 4: Validate and write
    print("\n[4/4] Validating and writing updated spec...")
    if not validate_spec(merged_spec):
        print("ERROR: Validation failed. Spec not updated.")
        sys.exit(1)
    
    write_spec(merged_spec)
    
    # Step 5: Regenerate SDK
    print("\nRegenerating SDK...")
    subprocess.run(["make", "sdk"], check=True)
    print("SDK regenerated successfully.")
    
    print("\n" + "=" * 60)
    print("Auto-update complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
