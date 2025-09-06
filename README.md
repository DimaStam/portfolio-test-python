# E2E Tests (Playwright + Pytest)

End‑to‑end tests for two stores (Store 1/2) using Playwright (sync API) and Pytest, with Allure reporting and environment switching via `.env` files.

## Contents
- Technologies
- Installation
- Running: command structure and examples
- Variables used in the test command
- CI configuration
- Allure reports
- Environment variables definition

## Technologies
- Python 3.12
- Playwright (`playwright`)
- Pytest (`pytest`)
- Allure (`allure-pytest`)
- Environment variables (`python-dotenv`)
- Test data generation (`Faker`)

## Installation
1) Create and activate a virtual environment
- Windows (PowerShell):
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- Linux/macOS (bash):
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

2) Install project dependencies
```bash
pip install -r requirements.txt
```

3) Install Playwright browsers (one‑time)
```bash
playwright install
```

## Running: command structure
Basic Pytest command for a single test or a folder:
```bash
pytest <path_to_tests> --env=<dev|stage|prod> [--headed] --alluredir=allure-results
```
- `--env` – environment profile; the loader in `conftest.py` reads `.env.<env>`
- `--headed` – run the browser with UI (headless by default)
- `--alluredir` – output folder for Allure results

Examples:
- Run Store 1 (guest, courier + all payments) on `stage`:
  ```bash
  pytest tests/Store1/orders/guest_user/store_1_courier_and_all_payments_test.py \
    --env=stage --alluredir=allure-results
  ```
  With browser UI:
  ```bash
  pytest tests/Store1/orders/guest_user/store_1_courier_and_all_payments_test.py \
    --env=stage --headed --alluredir=allure-results
  ```

## Variables used in the test command
- `--env` – selects the environment profile (reads from `.env.<env>`)
- `--headed` – switches browser mode (UI vs headless)
- `--alluredir` – path for Allure results (e.g., `allure-results`)

## CI configuration
The repo contains `.gitlab-ci.yml` with a ready‑to‑use pipeline:
- Image: `mcr.microsoft.com/playwright/python:v1.44.0-jammy`
- Stages: `install` → `Store-1` → `Store-2` → `Send-report`
- Cache: `.cache`, `venv/`
- Install: create `venv`, `pip install -r requirements.txt`, `playwright install`
- Run: `pytest $STORE_TEST_PATH --env=$ENVIRONMENT --alluredir=allure-results`
- Artifacts: `screenshots/`, `allure-results`
- Publish report: `allure-server/allure-push.sh` in `Send-report`

CI variables (examples):
- `ENVIRONMENT` – passed to `--env`
- `STORE_TEST_PATH` – tests subset path (Store 1/2)
- `HEADLESS` – env flag if you want to force headless

## Allure reports
- Produce results: add `--alluredir=allure-results` to the Pytest command
- Local preview (requires Allure CLI):
  ```bash
  allure serve allure-results
  ```
- In CI: results are job artifacts; `allure-server/allure-push.sh` can publish to an external Allure server

## Environment variables definition
Tests load variables from `.env.<env>` via `python-dotenv` (see `conftest.py`).

Create environment files at the project root, e.g.:
- `.env.dev`
- `.env.stage`
- `.env.prod`

Sample content:
```env
# Entrypoints and URLs
URL_STORE_1=https://<store1-host>
URL_STORE_1_PRODUCT=https://<store1-host>/product/<sku>
URL_STORE_2=https://<store2-host>

# Users
STORE_1_USERNAME=<login>
STORE_1_PASSWORD=<password>

# Optional
HEADLESS=true
```
Note: keys are based on current usage (e.g., `URL_STORE_1_PRODUCT`, `STORE_1_USERNAME`, `STORE_1_PASSWORD`). Adjust to your environment specifics.

---
If helpful, we can also add a `.env.example` with a complete list of keys.
