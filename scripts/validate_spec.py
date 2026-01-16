#!/usr/bin/env python3
"""
Validate the OpenAPI specification and check for common issues.
"""

import sys
import yaml
from pathlib import Path


def load_spec(spec_path):
    """Load and parse the OpenAPI specification."""
    try:
        with open(spec_path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ File not found: {spec_path}")
        return None


def validate_structure(spec):
    """Validate basic OpenAPI structure."""
    issues = []
    
    # Check required top-level fields
    required_fields = ['openapi', 'info', 'paths']
    for field in required_fields:
        if field not in spec:
            issues.append(f"Missing required field: {field}")
    
    # Check OpenAPI version
    if 'openapi' in spec:
        version = spec['openapi']
        if not version.startswith('3.'):
            issues.append(f"OpenAPI version {version} is not 3.x")
    
    # Check info section
    if 'info' in spec:
        info = spec['info']
        if 'title' not in info:
            issues.append("Missing info.title")
        if 'version' not in info:
            issues.append("Missing info.version")
    
    return issues


def validate_paths(spec):
    """Validate path definitions."""
    issues = []
    
    if 'paths' not in spec:
        return issues
    
    paths = spec['paths']
    
    for path, path_item in paths.items():
        if not path.startswith('/'):
            issues.append(f"Path '{path}' should start with /")
        
        for method, operation in path_item.items():
            if method.startswith('x-'):
                continue  # Skip extensions
            
            if method not in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head', 'trace']:
                continue  # Skip non-HTTP methods
            
            # Check for operationId
            if 'operationId' not in operation:
                issues.append(f"Missing operationId for {method.upper()} {path}")
            
            # Check for responses
            if 'responses' not in operation:
                issues.append(f"Missing responses for {method.upper()} {path}")
            
            # Check for summary or description
            if 'summary' not in operation and 'description' not in operation:
                issues.append(f"Missing summary/description for {method.upper()} {path}")
    
    return issues


def validate_schemas(spec):
    """Validate schema definitions."""
    issues = []
    
    if 'components' not in spec or 'schemas' not in spec['components']:
        return issues
    
    schemas = spec['components']['schemas']
    
    for schema_name, schema in schemas.items():
        # Check for description
        if 'description' not in schema and 'title' not in schema:
            issues.append(f"Schema '{schema_name}' missing description/title")
        
        # Check object schemas have properties
        if schema.get('type') == 'object' and 'properties' not in schema and 'allOf' not in schema and 'oneOf' not in schema:
            issues.append(f"Object schema '{schema_name}' has no properties")
    
    return issues


def check_examples(spec):
    """Check for examples in the specification."""
    warnings = []
    
    if 'paths' not in spec:
        return warnings
    
    paths = spec['paths']
    paths_without_examples = []
    
    for path, path_item in paths.items():
        for method, operation in path_item.items():
            if method not in ['get', 'post', 'put', 'delete', 'patch']:
                continue
            
            has_example = False
            
            # Check for request body examples
            if 'requestBody' in operation:
                content = operation['requestBody'].get('content', {})
                for media_type, media_obj in content.items():
                    if 'example' in media_obj or 'examples' in media_obj:
                        has_example = True
            
            # Check for response examples
            if 'responses' in operation:
                for status, response in operation['responses'].items():
                    content = response.get('content', {})
                    for media_type, media_obj in content.items():
                        if 'example' in media_obj or 'examples' in media_obj:
                            has_example = True
            
            if not has_example:
                paths_without_examples.append(f"{method.upper()} {path}")
    
    if paths_without_examples:
        warnings.append(f"⚠️  {len(paths_without_examples)} endpoints without examples")
    
    return warnings


def main():
    """Main validation function."""
    spec_path = Path(__file__).parent.parent / 'openapi.yaml'
    
    print("🔍 Validating OpenAPI specification...")
    print(f"📄 File: {spec_path}\n")
    
    # Load spec
    spec = load_spec(spec_path)
    if spec is None:
        sys.exit(1)
    
    print("✅ YAML syntax is valid\n")
    
    # Run validations
    all_issues = []
    all_warnings = []
    
    all_issues.extend(validate_structure(spec))
    all_issues.extend(validate_paths(spec))
    all_issues.extend(validate_schemas(spec))
    all_warnings.extend(check_examples(spec))
    
    # Report results
    if all_issues:
        print("❌ ERRORS FOUND:\n")
        for issue in all_issues:
            print(f"  • {issue}")
        print()
    
    if all_warnings:
        print("⚠️  WARNINGS:\n")
        for warning in all_warnings:
            print(f"  • {warning}")
        print()
    
    if not all_issues and not all_warnings:
        print("✅ All validations passed!")
        print("🎉 OpenAPI specification looks good!\n")
        return 0
    elif not all_issues:
        print("✅ No errors found (only warnings)")
        print("💡 Consider addressing warnings for better documentation\n")
        return 0
    else:
        print(f"❌ Found {len(all_issues)} error(s)")
        print("🔧 Please fix the errors above\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
