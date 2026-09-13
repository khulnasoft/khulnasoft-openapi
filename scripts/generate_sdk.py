import argparse
import sys
import yaml
import json
import shutil
import subprocess
from pathlib import Path

class NoAliasDumper(yaml.Dumper):
    """
    Yaml aliases (variables prefixed with & and *) are invalid in OpenAPI
    syntax. This custom dumper will expand out all of the aliases when
    dumping the yaml into the sanitized spec file.
    """
    def ignore_aliases(self, data):
        return True

def filter_out_oai_keys(obj):
    """Filter out any custom keys that start with 'oai'."""
    oai_keys = []
    for key in obj:
        if key.startswith("oai"):
            oai_keys.append(key)
    for oai_key in oai_keys:
        del obj[oai_key]

def fix_default_null(obj):
    """
    For some reason openapi-generator fails when properties of type 'object'
    or 'array' have a default value of null, so rewrite those defaults to {}
    and [] respectively (generated code, at least for Typescript, doesn't use
    the defaults anyways).
    """
    if "default" in obj and obj["default"] is None:
        if obj.get("type") == "object":
            obj["default"] = {}
        elif obj.get("type") == "array":
            obj["default"] = []

def fix_nested_array(obj):
    """
    openapi-generator has a bug where it doesn't go past the first level of
    array nesting, so instead of outputting something like Array<Array<string>>>,
    it will just output Array<Array> (which is problematic for Typescript).
    This is a non-ideal hack to set the items of the top-level array to {},
    which will output as Array<any>.
    """
    if obj.get("type") == "array" and obj.get("items", {}).get("type") == "array":
        obj["items"] = {}

def sanitize_spec_object(obj):
    """
    Recursively iterate through the given spec and perform any necessary
    rewrites/sanitization for the spec that will be used to generate SDKs.
    """
    if isinstance(obj, dict):
        filter_out_oai_keys(obj)
        fix_default_null(obj)
        fix_nested_array(obj)
        for item in obj.values():
            sanitize_spec_object(item)
    elif isinstance(obj, list):
        for item in obj:
            sanitize_spec_object(item)

def generate_sanitized_spec(sanitized_spec_path):
    """
    Create sanitized versions of the spec (both YAML and JSON)
    that can be used to generate SDKs.
    """
    root_dir = Path(__file__).parent.parent
    input_path = root_dir / "openapi.yaml"
    
    if not input_path.exists():
        print(f"Error: openapi.yaml not found at {input_path}")
        sys.exit(1)

    print(f"Reading spec from {input_path}...")
    with open(input_path, "r") as input_file:
        spec = yaml.safe_load(input_file)
        sanitize_spec_object(spec)

    sanitized_yaml_path = Path(str(sanitized_spec_path) + ".yaml")
    sanitized_json_path = Path(str(sanitized_spec_path) + ".json")

    with open(sanitized_yaml_path, "w") as output_file:
        yaml.dump(spec, output_file, Dumper=NoAliasDumper, sort_keys=False)
    print(f"Sanitized YAML spec written to {sanitized_yaml_path}")

    with open(sanitized_json_path, "w") as output_file:
        json.dump(spec, output_file, indent=2)
    print(f"Sanitized JSON spec written to {sanitized_json_path}")

    return sanitized_yaml_path, sanitized_json_path

def check_dependencies():
    """Check if openapi-generator is installed and return the command name."""
    if shutil.which("openapi-generator"):
        return "openapi-generator"
    elif shutil.which("openapi-generator-cli"):
        return "openapi-generator-cli"
    else:
        print("Error: openapi-generator is not installed or not in PATH.")
        print("Please install it via brew or npm:")
        print("  brew install openapi-generator")
        print("  npm install -g @openapitools/openapi-generator-cli")
        sys.exit(1)

def generate_sdk(sanitized_yaml_path, sanitized_json_path, sdk_type, output_path):
    """Use openapi-generator to generate the SDK."""
    generator_cmd = check_dependencies()
    
    output_dir = Path(output_path)
    print(f"Generating {sdk_type} SDK to {output_dir}...")

    if sdk_type == "node":
        template_override_path = Path(__file__).parent.parent / "sdk-template-overrides/typescript-axios"
        command = [
            generator_cmd, "generate",
            "-i", str(sanitized_json_path),
            "-g", "typescript-axios",
            "-o", str(output_dir),
            "-p", "supportsES6=true",
            "-t", str(template_override_path)
        ]
        
        try:
            subprocess.run(command, check=True)
            print("SDK generation successful.")
        except subprocess.CalledProcessError as e:
            print(f"Error generating SDK: {e}")
            sys.exit(1)
    else:
        print(f"Unsupported SDK type {sdk_type}, skipping SDK generation")

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sdk", help="sdk type (supported types: 'node')")
parser.add_argument("-o", "--output", help="output directory for the generated sdk")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.sdk is None:
        print("Use -s to specify the SDK type")
        sys.exit(1)
    if args.output is None:
        print("Use -o to specify the output directory")
        sys.exit(1)

    sanitized_spec_path = Path("openapi-sanitized-tmp")
    
    try:
        sanitized_yaml_path, sanitized_json_path = generate_sanitized_spec(sanitized_spec_path)
        generate_sdk(sanitized_yaml_path, sanitized_json_path, args.sdk, args.output)
    finally:
        pass

    # Copy sanitized specs to output directory
    output_dir = Path(args.output)
    shutil.copy2(sanitized_yaml_path, output_dir / "openapi.yaml")
    shutil.copy2(sanitized_json_path, output_dir / "openapi.json")
    print(f"Copied sanitized spec files to {output_dir}/")
