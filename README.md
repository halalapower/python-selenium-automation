# Amazon UI Test Automation (Python · Selenium · Behave)

BDD UI tests against amazon.com, built during a test-automation course (2021–2022). The suite uses the Page Object Model, Gherkin scenarios and explicit waits, and handles multiple browser windows.

**Stack:** Python · Selenium 4 · Behave (Gherkin) · Page Object Model

## Scenarios
| Feature | What it checks | Status |
|---|---|---|
| Amazon Prime | The Prime page shows the expected number of benefit boxes | Implemented |
| Bestsellers | There are 5 bestseller category links and each one opens | Implemented |
| Hamburger menu | The menu icon is present | Implemented |
| Product details | Each color option of a product can be selected and is shown as selected | Implemented |
| Window handles | Opens the Privacy Notice in a new window, verifies it, closes it and switches back | Implemented |
| Search, sign-in, cancel order, Google search | Earlier exercises with unfinished steps | `@wip`, skipped by default |

## Project layout
```
app/application.py        # wires page objects onto the Behave context
pages/                    # Page Object Model (base page, header, main, product, search results, sign-in, Prime)
features/
├── environment.py        # browser setup and teardown per scenario
├── steps/                # step definitions
└── tests/*.feature       # Gherkin scenarios
exercises/                # early standalone Selenium scripts from the course
behave.ini                # skips @wip scenarios by default
```

## Run it
```bash
pip install -r requirements.txt
python -m behave                              # Chrome, visible window
HEADLESS=1 python -m behave                   # headless
BROWSER=firefox HEADLESS=1 python -m behave   # Firefox
```
Selenium Manager (Selenium 4.6+) downloads the matching driver automatically.

## Notes
- Amazon changes its markup often and uses bot detection, so some locators may need refreshing before a live run.
- 2026 cleanup: removed the committed driver binary, replaced hard-coded local paths with Selenium Manager, merged duplicate step definitions, fixed the window-handle and color-selection steps, tagged unfinished scenarios `@wip`, and moved the loose scripts into `exercises/`.
