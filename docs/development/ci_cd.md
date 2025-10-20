# CI/CD


## Overview

The project uses GitHub Actions for automated testing, building, and deployment.

## Workflows


### CI Pipeline (`.github/workflows/ci.yml`)
- Runs on every push and pull request
- Tests code quality (ruff, mypy, bandit)
- Runs test suite with pytest
- Generates coverage reports
- Supports Python 3.13, 3.12, 3.11

### Release Pipeline (`.github/workflows/release.yml`)
- Triggered by version tags (e.g., `v1.0.0`)
- Builds and tests the package
- Publishes to PyPI
- Creates GitHub releases

### Security Pipeline (`.github/workflows/security.yml`)
- Daily security scanning
- Dependency vulnerability checks
- Code security analysis


## Local Development

```bash
# Run CI checks locally
uv run ruff check .
uv run mypy .
uv run pytest
uv run pre-commit run --all-files
```

## Deployment

```bash
# Create release
git tag v1.0.0
git push origin v1.0.0
```


