# khulnasoft-openapi

📘 OpenAPI specification for the KhulnaSoft API, providing a clear, standardized contract for developers. Includes endpoints, schemas, authentication, and examples to enable seamless integration, testing, and SDK generation. 🚀

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Manual SDK Generation](#manual-sdk-generation)
  - [Cleaning Generated Files](#cleaning-generated-files)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains the OpenAPI 3.0 specification for the KhulnaSoft API and tools to generate client SDKs in various programming languages. The specification defines all available endpoints, request/response schemas, authentication methods, and provides examples for easy integration.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** - For running the SDK generation script
- **PyYAML** - Python YAML parser (install via `pip3 install pyyaml`)
- **OpenAPI Generator** - Tool for generating SDKs from OpenAPI specs

### Installing OpenAPI Generator

You can install OpenAPI Generator using either **Homebrew** or **npm**:

#### Option 1: Homebrew (macOS/Linux)
```bash
brew install openapi-generator
```

#### Option 2: npm (Cross-platform)
```bash
npm install -g @openapitools/openapi-generator-cli
```

The SDK generation script automatically detects which installation method you used.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/khulnasoft/khulnasoft-openapi.git
cd khulnasoft-openapi
```

2. Install Python dependencies:
```bash
pip3 install pyyaml
```

3. Install OpenAPI Generator (see [Prerequisites](#prerequisites))

## Usage

### Quick Start

Generate a TypeScript SDK using the Makefile:

```bash
make sdk
```

This will create a TypeScript/Axios SDK in `generated_sdks/typescript/`.

### Manual SDK Generation

You can also use the Python script directly for more control:

```bash
python3 scripts/generate_sdk.py --sdk node --output ./my-custom-output
```

**Arguments:**
- `-s, --sdk` - SDK type to generate (currently supported: `node`)
- `-o, --output` - Output directory for the generated SDK

### Cleaning Generated Files

Remove all generated SDK files:

```bash
make clean
```

## Project Structure

```
khulnasoft-openapi/
├── openapi.yaml                    # Main OpenAPI 3.0 specification
├── scripts/
│   └── generate_sdk.py            # SDK generation script
├── sdk-template-overrides/
│   └── typescript-axios/          # Custom templates for TypeScript SDK
│       ├── apiInner.mustache
│       └── configuration.mustache
├── generated_sdks/                # Generated SDKs (gitignored)
├── Makefile                       # Convenience commands
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Development

### How the SDK Generation Works

1. **Sanitization**: The script reads `openapi.yaml` and performs sanitization:
   - Removes custom `oai*` keys (used for documentation)
   - Fixes null defaults for objects/arrays
   - Handles nested array types

2. **Generation**: Uses OpenAPI Generator to create SDK code from the sanitized spec

3. **Cleanup**: Removes temporary files automatically

### Modifying the OpenAPI Spec

Edit `openapi.yaml` to add or modify API endpoints. The spec follows OpenAPI 3.0 standards.

Custom metadata can be added using keys starting with `oai` - these will be automatically filtered out during SDK generation.

### Adding Support for New Languages

To add support for additional SDK languages, modify `scripts/generate_sdk.py`:

1. Add a new condition in the `generate_sdk()` function
2. Specify the appropriate OpenAPI Generator language flag
3. Optionally add custom templates in `sdk-template-overrides/`

Example:
```python
elif sdk_type == "python":
    command = [
        generator_cmd, "generate",
        "-i", str(sanitized_spec_path),
        "-g", "python",
        "-o", str(output_dir),
    ]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

See the [LICENSE](LICENSE) file for details.
