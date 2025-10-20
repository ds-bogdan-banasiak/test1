# Project Structure

## Directory Structure

```
test1/
├── .github/workflows/         # CI/CD workflows
├── packages/                 # Workspace packages (apps/libs)
│   └── <pkg>/
│       ├── pyproject.toml        # Package configuration
│       └── src//   # Package sources
├── docs/                      # Documentation
├── site/                      # Built docs (generated)
├── scripts/                   # Utility scripts
├── mkdocs.yml                 # Docs configuration
├── mise.toml                  # Tool versions and tasks
├── pyproject.toml             # Workspace configuration
└── README.md
```
