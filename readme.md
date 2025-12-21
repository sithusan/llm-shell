# Warning
Do **not** run this program unless you have reviewed the source code and set up an isolated environment.

This project **does not include the security, safety, or guardrails** expected from a production-grade AI agent. Running it without understanding the code may expose your system or data to risk.

This project is intended **strictly for educational purposes**.

# Setup (uv)

This project uses **uv** to manage an isolated Python virtual environment and package management, keeping dependencies separate from other projects.

## Prerequisites

- Python installed
- `uv` installed

## Create Virtual Environment

From the project root:
```shell
uv venv
```
This will create a .venv directory.

## Activate Virtual Environment

```shell
source .venv/bin/activate
```