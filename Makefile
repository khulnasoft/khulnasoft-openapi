.PHONY: sdk clean validate help

help:
	@echo "Available targets:"
	@echo "  make sdk       - Generate TypeScript SDK"
	@echo "  make validate  - Validate OpenAPI specification"
	@echo "  make clean     - Remove generated SDK files"

validate:
	python3 scripts/validate_spec.py

sdk:
	python3 scripts/generate_sdk.py --sdk node --output generated_sdks/typescript

clean:
	rm -rf generated_sdks/
