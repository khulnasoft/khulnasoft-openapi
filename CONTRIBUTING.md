# Contributing to khulnasoft-openapi

Thank you for your interest in contributing to the KhulnaSoft OpenAPI specification! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **OpenAPI Generator version** and SDK language
- **Error messages** or logs

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** explaining why this enhancement would be useful
- **Examples** of how the enhancement would work

### Adding New Endpoints

To add a new endpoint to the OpenAPI specification:

1. Follow the OpenAPI 3.0 specification format
2. Include complete request/response schemas
3. Add examples for all operations
4. Document authentication requirements
5. Test SDK generation with your changes

### Adding Support for New SDK Languages

To add support for a new programming language:

1. Update `scripts/generate_sdk.py` with the new language
2. Add any custom templates to `sdk-template-overrides/`
3. Update the README with the new language
4. Test the SDK generation thoroughly

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/khulnasoft-openapi.git
   cd khulnasoft-openapi
   ```

2. **Install dependencies**
   ```bash
   pip3 install pyyaml
   npm install -g @openapitools/openapi-generator-cli
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Making Changes

### Modifying the OpenAPI Specification

1. Edit `openapi.yaml` following OpenAPI 3.0 standards
2. Validate your changes:
   ```bash
   openapi-generator-cli validate -i openapi.yaml
   ```
3. Test SDK generation:
   ```bash
   make sdk
   ```

### OpenAPI Best Practices

- **Use descriptive operationIds** - These become method names in SDKs
- **Include examples** - Helps developers understand the API
- **Document all parameters** - Include descriptions and constraints
- **Use schemas** - Define reusable components in `#/components/schemas`
- **Add response codes** - Document all possible HTTP responses
- **Security schemes** - Clearly define authentication methods

### Custom Metadata

You can add custom metadata for documentation using keys starting with `oai`:

```yaml
paths:
  /example:
    get:
      operationId: getExample
      oaiMeta:
        name: Get Example
        group: examples
        examples:
          curl: |
            curl https://api.khulnasoft.com/v1/example
```

These keys are automatically filtered out during SDK generation.

## Submitting Changes

### Pull Request Process

1. **Update documentation** - Ensure README and other docs reflect your changes
2. **Test thoroughly** - Run `make sdk` to verify SDK generation works
3. **Commit with clear messages** - Follow conventional commit format:
   ```
   feat: add new endpoint for user management
   fix: correct response schema for completions
   docs: update README with new examples
   ```
4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request** - Provide a clear description of changes

### PR Checklist

- [ ] OpenAPI spec validates successfully
- [ ] SDK generation works without errors
- [ ] Documentation updated (README, inline comments)
- [ ] Examples provided for new endpoints
- [ ] Commit messages are clear and descriptive
- [ ] No breaking changes (or clearly documented if necessary)

## Style Guidelines

### YAML Style

- Use 2 spaces for indentation
- Keep lines under 100 characters when possible
- Use descriptive names for schemas and operations
- Order properties alphabetically within objects (when logical)
- Add comments for complex schemas

### Example

```yaml
paths:
  /users/{userId}:
    get:
      operationId: getUser
      summary: Retrieve a user by ID
      parameters:
        - in: path
          name: userId
          required: true
          schema:
            type: string
          description: The unique identifier for the user
      responses:
        "200":
          description: User retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        "404":
          description: User not found
```

### Python Style

For changes to `scripts/generate_sdk.py`:

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to functions
- Keep functions focused and single-purpose
- Use pathlib for file operations

## Questions?

Feel free to open an issue with the `question` label if you need help or clarification.

Thank you for contributing! 🚀
