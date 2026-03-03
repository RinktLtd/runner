# Rinkt Runner

**One binary. Browser, desktop, Office, and API automation with durable execution.**

Rinkt Runner is a cross-platform automation engine built in Go. It executes
workflows that span Playwright-driven browsers, native desktop applications,
Microsoft Office, REST/GraphQL APIs, and Google Drive -- from a single
lightweight process. No orchestration server required for standalone use.

> **Status:** Runner is in private beta. Source code will be published here when
> the project reaches general availability. [Sign up for early access](https://rinkt.com)
> to follow progress.

---

## Why Rinkt Runner?

Most automation tools force you to choose: **browser OR desktop OR API**.
Runner handles all three in one workflow.

| | Rinkt Runner | Zapier / Make | n8n | UiPath |
|---|:---:|:---:|:---:|:---:|
| Browser automation (Playwright) | Yes | No | Plugin | Yes |
| Desktop app control | Yes | No | No | Yes |
| Office automation (Excel, Word, Outlook) | Yes | No | No | Yes |
| REST / GraphQL APIs | Yes | Yes | Yes | Yes |
| Single binary, no installer | Yes | N/A (SaaS) | Docker | No |
| Code-first workflow definitions | Yes | No | Partial | No |
| CAPTCHA solving | Built-in | No | No | Plugin |
| Deploy as system service | Yes | N/A | Docker | Yes |
| Auto-updates | Yes | N/A | Manual | Yes |
| Open source | Soon | No | Yes | No |
| Runs without cloud account | Yes | No | Yes | Yes |

## How it works

```
                        +------------------+
                        |    Rinkt API     |  (orchestration, optional)
                        +--------+---------+
                                 |
                        +--------v---------+
                        |   Dispatcher     |  (task routing)
                        +--------+---------+
                                 |
                        +--------v---------+
  You are here --->     |     Runner       |  (execution engine)
                        +------------------+
                        |  100+ activities |
                        +--+--+--+--+--+--+
                           |  |  |  |  |
              Browser  Desktop Office API  Drive
```

Runner can operate standalone or as part of the full Rinkt platform. In
standalone mode, it picks up workflow definitions from local files. In platform
mode, it receives tasks from the Dispatcher and reports results back.

## What can it automate?

**100+ built-in activity types** across these domains:

- **Browser** -- Navigate, click, fill forms, scrape data, take screenshots,
  handle authentication flows. Powered by Playwright (Chromium, Firefox, WebKit).
- **Desktop** -- Control native Windows and macOS applications. Click, type,
  read screen content, interact with UI elements.
- **Office** -- Read and write Excel workbooks, generate Word documents, send
  Outlook emails, manipulate file formats.
- **API** -- Call REST and GraphQL endpoints, handle authentication, parse
  responses, chain requests.
- **Google Drive** -- Upload, download, organise files and folders.
- **CAPTCHA** -- Solve CAPTCHAs inline during browser automation.
- **System** -- File operations, process management, environment detection.

## Example workflow

```yaml
# Scrape invoice data from a web portal, write to Excel, email the report
name: weekly-invoice-report
steps:
  - browser.navigate:
      url: https://vendor-portal.example.com/invoices
  - browser.login:
      credentials: vault://vendor-portal
  - browser.scrape:
      selector: table.invoices
      output: invoice_data
  - office.excel.write:
      file: reports/invoices-{{date}}.xlsx
      data: "{{invoice_data}}"
  - office.outlook.send:
      to: finance@company.com
      subject: "Weekly invoice report - {{date}}"
      attachments:
        - reports/invoices-{{date}}.xlsx
```

*Workflow format is illustrative. Final schema will be documented at GA.*

## Technical details

- **Language:** Go
- **UI framework:** Wails 3 (optional desktop GUI)
- **Browser engine:** Playwright (bundled)
- **Deployment:** Single binary, system service, or Docker container
- **Platforms:** Windows (amd64), macOS (amd64, arm64), Linux (amd64)
- **Observability:** Built-in metrics and structured logging
- **Updates:** Automatic self-update mechanism

## Getting started

Runner is currently in private beta.

1. **Request access** at [rinkt.com](https://rinkt.com)
2. **Download** the binary for your platform
3. **Run your first workflow** -- quickstart guide included with the download

Full documentation will be published alongside the source code at GA.

## Roadmap

- [ ] Public source release
- [ ] Plugin system for custom activity types
- [ ] Workflow marketplace
- [ ] GitHub Actions integration
- [ ] VS Code extension

## Related repositories

| Repo | Description |
|---|---|
| [dispatcher](https://github.com/RinktLtd/dispatcher) | Workflow task routing and scheduling |
| [python-interpreter](https://github.com/RinktLtd/python-interpreter) | Embedded Python runtime for workflow scripting |

## Community

- [rinkt.com](https://rinkt.com) -- Documentation and blog

## License

Source-available license. Details will be published with the public release.

---

Built by [Rinkt](https://github.com/RinktLtd).
