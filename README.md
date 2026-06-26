# Playwright Workshop Demo - 26 - 6 -2026


(Internal Use only to try playwright in Local, read attached .pptx for the basic info)
A tiny, self-contained app + test suite that puts the concepts from the
**"Playwright for Everyone"** deck into actually-runnable code. No backend,
no signup, no real AI tool required — just a simple login `index.html` and a handful of
Playwright tests pointed at it.

## Quick start (Windows)

Double-click **`run.bat`**. First run will:

1. Create a `.venv` virtual environment
2. `pip install` Playwright + pytest + pytest-html
3. Download the Chromium browser
4. Run the full test suite with the browser visible (`--headed`)
5. Generate `report.html` and open it in your browser

Re-running it later just runs the tests again (the setup steps are skipped
if already done).

### Manual / other OS

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests --headed --html=report.html --self-contained-html
```

## Test credentials

The app validates against two hardcoded users — the same ones used
throughout the deck:

| Username           | Password       | Result                          |
|---------------------|----------------|----------------------------------|
| `standard_user`      | `secret_sauce` | Logs in, lands on **Products**  |
| `locked_out_user`    | `secret_sauce` | "Sorry, this user has been locked out." |
| anything else        | anything       | "Username and password do not match." |

## What's in here, and which deck module it demos

| File | Deck module | What it shows |
|---|---|---|
| `hello_world.py` | Module 4 — Core Concepts | Standalone script (no pytest) showing Browser → Context → Page explicitly |
| `tests/test_login.py` | Modules 4–6 | Basic login/logout/cart flow with `expect()` assertions |
| `tests/test_actions_cheatsheet.py` | Module 6 | Every action from the cheat-sheet: `click`, `fill`, `check`, `select_option`, `press` |
| `tests/test_red_flags_demo.py` | **Module 5** | The 3 red flags, paired BAD vs GOOD, run against this exact app — brittle CSS path vs `get_by_role`, hardcoded sleep vs `expect()`, missing assertion vs explicit one |
| `tests/test_debug_me.py` | Module 6 | **Fails on purpose** — use it to practice `--headed`, `page.pause()`, and the trace viewer |
| `pages/login_page.py`, `pages/inventory_page.py` | Module 7 | Page Object Model |
| `tests/test_login_pom.py` | Module 7 | Same login tests, refactored to use the POM above — compare to `test_login.py` |

`index.html` is the app under test: a login form (with a "Remember me"
checkbox) and a Products page (search box, sort dropdown, add-to-cart
buttons, cart badge). The "Add Backpack to cart" button is deliberately
buried under a few wrapper `<div>`s — that's the target for the brittle
CSS/XPath locator in `test_red_flags_demo.py`.

## Expected result

18 tests should pass. **1 test fails on purpose** —
`tests/test_debug_me.py::test_login_with_wrong_button_name_fails_on_purpose`.
If anything else fails, that's a real bug — please report it rather than
assuming it's intentional.

## Project structure

```
demo/
├── index.html                 # the app under test
├── hello_world.py             # Module 4 standalone script
├── conftest.py                # lets tests/ import pages/
├── requirements.txt
├── run.bat                    # setup + run everything
├── run_hello_world.bat
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
└── tests/
    ├── test_login.py
    ├── test_actions_cheatsheet.py
    ├── test_red_flags_demo.py
    ├── test_debug_me.py
    └── test_login_pom.py
```
