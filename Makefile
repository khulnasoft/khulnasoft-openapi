.PHONY: sdk clean validate help update

help:
	@echo "Available targets:"
	@echo "  make sdk       - Generate TypeScript SDK (openapi.json + openapi.yaml)"
	@echo "  make validate  - Validate OpenAPI specification"
	@echo "  make clean     - Remove generated SDK files"
	@echo "  make update    - Auto-update openapi.yaml from publisher"

validate:
	python3 scripts/validate_spec.py

sdk:
	python3 scripts/generate_sdk.py --sdk node --output generated_sdks/typescript

update:
	python3 scripts/update_spec.py

clean:
	rm -rf generated_sdks/
