# Trading Signal Indicator Examples

Python project for analyzing and visualizing Trading Signal Indicator Examples (RSI divergence and more).

## Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

## Quick Start

```bash
# Install dependencies (creates .venv automatically)
poetry install

# Run a script (generates an image visualizing chart and indicator movements demonstrating divergence)
poetry run python RSI/divergence_signal.py
```

## Adding Dependencies

```bash
poetry add <package-name>
```

## Project Structure

```
├── RSI/                    # RSI signal analysis
│   └── divergence_signal.py
├── pyproject.toml          # Project config & dependencies
└── README.md
```
