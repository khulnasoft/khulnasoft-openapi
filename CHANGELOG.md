# Changelog

## 0.2.0 (2026-04-18)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/khulnasoft/khulnasoft-openapi/compare/v0.1.0...v0.2.0)

### Features

* **internal:** implement indices array format for query and form serialization ([6f9ef5d](https://github.com/khulnasoft/khulnasoft-openapi/commit/6f9ef5d8958d57639179c2489b8a83754a99a1dd))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([b38a7dd](https://github.com/khulnasoft/khulnasoft-openapi/commit/b38a7dd2b37726727a58683f8d5a38fa41d3d1fd))
* **deps:** bump minimum typing-extensions version ([472908c](https://github.com/khulnasoft/khulnasoft-openapi/commit/472908c4305e47c8c4e714458c889f68fdf6854c))
* ensure file data are only sent as 1 parameter ([0b1dbd3](https://github.com/khulnasoft/khulnasoft-openapi/commit/0b1dbd3e5553a22adada6cdaf3eab7dd50565280))
* **pydantic:** do not pass `by_alias` unless set ([b5501a6](https://github.com/khulnasoft/khulnasoft-openapi/commit/b5501a622cf659edf54bf1f056a15b3be3abc298))
* sanitize endpoint path params ([ed285f0](https://github.com/khulnasoft/khulnasoft-openapi/commit/ed285f0d29c8cd4270bd3acb173a18dbf3f5a352))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([2916819](https://github.com/khulnasoft/khulnasoft-openapi/commit/29168199a3f0ef9ee7b2f4fa8d887324c1259ea9))


### Chores

* **ci:** bump uv version ([de8432b](https://github.com/khulnasoft/khulnasoft-openapi/commit/de8432b906ddb023821036ce754b208d256fc1be))
* **ci:** skip lint on metadata-only changes ([827b72b](https://github.com/khulnasoft/khulnasoft-openapi/commit/827b72b54c0a94c51f624bff525594274b8114a4))
* **ci:** skip uploading artifacts on stainless-internal branches ([0de31a0](https://github.com/khulnasoft/khulnasoft-openapi/commit/0de31a092b424886e973660a9c9292c2e54d823b))
* **internal:** add request options to SSE classes ([c5b2e3c](https://github.com/khulnasoft/khulnasoft-openapi/commit/c5b2e3c6903a647319d4511e783e706176ae2317))
* **internal:** codegen related update ([b29d84f](https://github.com/khulnasoft/khulnasoft-openapi/commit/b29d84f79ab072293b1314d0c82a409c9ff8bd01))
* **internal:** make `test_proxy_environment_variables` more resilient ([f5519ae](https://github.com/khulnasoft/khulnasoft-openapi/commit/f5519ae80eff377ec23f11770e4f063c0fa0dee6))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([c7e0a49](https://github.com/khulnasoft/khulnasoft-openapi/commit/c7e0a49e3337fb6e03b024d7f43d4b57f2b2c28a))
* **internal:** remove mock server code ([0b0ddbe](https://github.com/khulnasoft/khulnasoft-openapi/commit/0b0ddbe4353a7f493f0002eab01d66c2725dffdc))
* **internal:** tweak CI branches ([b3d479d](https://github.com/khulnasoft/khulnasoft-openapi/commit/b3d479d39e3547259d5f6334ca972802ce6062ab))
* **internal:** update gitignore ([508eb92](https://github.com/khulnasoft/khulnasoft-openapi/commit/508eb9281cde0483136ed2da6252de267b1fdbbd))
* update mock server docs ([8e39256](https://github.com/khulnasoft/khulnasoft-openapi/commit/8e392563c1e63d3731db0a012d9ac30191e2b913))
* update placeholder string ([7ec8f3c](https://github.com/khulnasoft/khulnasoft-openapi/commit/7ec8f3cd27d4e70f48aaf3cc17f9c333aa8bc359))

## 0.1.0 (2026-02-13)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/khulnasoft/khulnasoft-openapi/compare/v0.0.1...v0.1.0)

### Features

* add Stainless integration workflow ([c4cf11c](https://github.com/khulnasoft/khulnasoft-openapi/commit/c4cf11c6c12656c6363d55840b2516ceb15c361d))
* **client:** add custom JSON encoder for extended type support ([8dda3b4](https://github.com/khulnasoft/khulnasoft-openapi/commit/8dda3b44ec774a13c24a702c5df95ae93a3afeb4))
* enhance SDK generation with validation, CI/CD, and comprehensive documentation ([7f3cbe1](https://github.com/khulnasoft/khulnasoft-openapi/commit/7f3cbe14208ab1251d9879878323dc19fb1227df))


### Bug Fixes

* update CI workflow to use custom validation script ([39814ad](https://github.com/khulnasoft/khulnasoft-openapi/commit/39814adb162556db6886f1b65a1dbfbe92f50ec5))


### Chores

* format all `api.md` files ([d201bd4](https://github.com/khulnasoft/khulnasoft-openapi/commit/d201bd444448eacf3589e9f8c81c4864b67c74f7))
* **internal:** bump dependencies ([0b7ad58](https://github.com/khulnasoft/khulnasoft-openapi/commit/0b7ad58d2dc4f6ea903f40f62f2ade34b35ca8d1))
* **internal:** fix lint error on Python 3.14 ([f5f3d6e](https://github.com/khulnasoft/khulnasoft-openapi/commit/f5f3d6e05949475e9445acee001f523380b0ec15))
* sync repo ([3e9884f](https://github.com/khulnasoft/khulnasoft-openapi/commit/3e9884ff53367a156e6f2799ce7824b648898e30))
* update SDK settings ([5840488](https://github.com/khulnasoft/khulnasoft-openapi/commit/5840488aaadd5a5bfc9f5bcf6d5bada2f9f13995))
* update SDK settings ([e084444](https://github.com/khulnasoft/khulnasoft-openapi/commit/e084444b9834005c908af7681a994921a81c8837))
