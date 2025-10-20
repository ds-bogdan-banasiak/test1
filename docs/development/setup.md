# Development Setup

Initial setup and environment configuration for development.

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- [mise](https://mise.jdx.dev/) toolchain manager
- Git


## Initial Setup

```bash
# Clone the repository
git clone <GIT-SSH>
cd test1

# Trust the project with mise
mise trust

# Install dependencies
uv sync

# Enable pre-commit hooks
uv run pre-commit install
```

## Verification

Verify your setup is working:

```bash
# Check tool versions
mise current

# Run code quality checks
uv run pre-commit run --all-files

# Run tests
uv run pytest

# Build documentation
uv run mkdocs build
```

## Next Steps

- [Project Structure](project_structure.md) - Understanding the codebase
