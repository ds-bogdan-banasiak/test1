# test1

Repository is created with deepsense.ai project template boilerplate. Adapt to your needs.
Documentation is available at [https://deepsense-ai.github.io/ds-template/](https://deepsense-ai.github.io/ds-template/).

This is a uv workspace project containing multiple packages.

## Quick Start

### Setup with uv

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then setup the project:

```bash
uv sync
```

### Initialize Git and Pre-commit

```bash
git init
git add .
git commit -m "chore: initial commit"
uv run pre-commit install
```

### Running Tests

```bash
uv run pytest
```

### Building Documentation

This project uses MkDocs for documentation. To build and serve the documentation locally:

```bash
# Build documentation
uv run mkdocs build

# Serve documentation locally (with auto-reload)
uv run mkdocs serve
```

The documentation will be available at `http://127.0.0.1:8000` when using `mkdocs serve`.

## Development

### Dev Tools

- uv (dependency and task runner)
- mise (toolchain/version manager)
- ruff (lint + format)
- mypy (type checking)
- pytest (tests)
- mkdocs (docs)

### Code Quality

Run all code quality checks:

```bash
uv run pre-commit run --all-files
```

### Individual Tools

```bash
# Linting
uv run ruff check .

# Formatting
uv run ruff format .

# Type checking
uv run mypy packages/
```

## Project Structure

```
test1/
├── .github/workflows/     # CI workflows
├── packages/              # Workspace packages (apps/libs)
│   └── <pkg>/
│       ├── pyproject.toml     # Package config
│       └── src/<pkg>/         # Package sources
├── docs/                  # Documentation sources
├── site/                  # Built docs (generated)
├── scripts/               # Utility scripts
├── mkdocs.yml             # Docs configuration
├── mise.toml              # Tool versions and tasks
└── pyproject.toml         # Workspace + tooling config
```

### pyproject.toml

- Defines uv workspace, dependencies, tool configs (ruff, mypy, pytest)
- Per-package `pyproject.toml` lives under each `packages/<pkg>/`

### mise

- Manage toolchain and tasks
- Install tools: `mise install`
- Run tasks (if defined): `mise run <task>`

## Documentation

The documentation is built using MkDocs with the Material theme. Key features:

- **Modern UI**: Clean, responsive design
- **Search**: Full-text search across all documentation
- **Navigation**: Easy navigation with tabs and sections
- **Code highlighting**: Syntax highlighting for code blocks
- **Mermaid diagrams**: Support for creating diagrams

### Adding Documentation

1. Add new `.md` files to the `docs/` directory
2. Update `mkdocs.yml` to include them in the navigation
3. Run `uv run mkdocs serve` to preview changes
4. Commit your changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and quality checks
5. Submit a pull request
