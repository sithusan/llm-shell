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