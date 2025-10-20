# Quick Start

Get up and running with test1 in minutes.

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- [mise](https://mise.jdx.dev/) toolchain manager
- Git

## Setup

### 1. Trust the project with mise

This project uses mise for toolchain management. Trust the project to install the required tools:

```bash
mise trust
```

### 2. Install dependencies

```bash
uv sync --dev
```

### 3. Enable pre-commit hooks

```bash
uv run pre-commit install
```

## Development

### Package Management

```bash
# Install dependencies
uv sync

# Add new dependency
uv add package-name

# Add dev dependency
uv add --dev package-name
```

### Code Quality

```bash
# Lint and format code
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy packages/

# Run all quality checks
uv run pre-commit run --all-files
```

### Testing

```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov
```

### Documentation

```bash
# Serve docs locally (auto-reload)
uv run mkdocs serve

# Build static site
uv run mkdocs build
```

## Next Steps

- [Development Setup](development/setup.md) - Initial environment setup
- [Project Structure](development/project_structure.md) - Understanding the codebase
- [CI/CD](development/ci_cd.md) - Continuous integration and deployment

> For details on how projects are generated from the template, see the [ds-template documentation](https://deepsense-ai.github.io/ds-template/).
