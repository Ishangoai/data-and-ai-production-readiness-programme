# Data and AI Production Readiness Programme

**Ishango.ai Â· 2026 Cohort**

Build, test and deploy data and AI applications using practical software engineering
workflows. This programme connects Python development, data pipelines, machine
learning and AI agents with the tools used to deliver applications in the cloud.

Learning is hands-on: develop in your own workspace, test your changes, collaborate
through pull requests and deploy working services.

## What you will learn

- Build REST APIs with FastAPI and interactive applications with Gradio.
- Package applications with Docker and manage Python dependencies with uv.
- Use Git, code review, automated checks and CI/CD in a shared development workflow.
- Build data pipelines and data-quality checks with Dagster.
- Track machine-learning experiments and manage models with MLflow.
- Develop LLM applications and tool-using agents with Gemini, LangChain and LangGraph.
- Deploy containerised applications to Google Cloud Run.

## Before you begin

You should be comfortable with Python functions, modules and basic data handling.
You will need a GitHub account and access to this repository. GitHub Codespaces
provides the course development environment; its setup installs the project dependencies.

## Getting started

### 1. Create your working branch

Accept your repository invitation. Create a branch from `development` named:

```text
feature-branch-YOUR-GITHUB-USERNAME
```

Open that branch in GitHub Codespaces using the smallest available machine, then
wait for the environment setup to finish. Use branches within this repository
for the course submission and deployment workflow.

### 2. Create your student workspace

Run this command from the repository root, replacing `YOUR-GITHUB-USERNAME` with
your exact GitHub login, including its capitalization:

```bash
python scripts/new_student.py YOUR-GITHUB-USERNAME
```

Your workspace will be created at `src/students/YOUR-GITHUB-USERNAME/`.
Keep your assignment changes inside that folder. The `example` folder contains
reference implementations for the lessons.

### 3. Start your application

In the Codespaces terminal, run:

```bash
PYTHONPATH=src/students/YOUR-GITHUB-USERNAME uv run --locked uvicorn api.main:app --host 0.0.0.0 --port 8080
```

Open port **8080** from the **Ports** tab.

| Path | Application |
| --- | --- |
| `/hello` | Introductory API endpoint |
| `/docs` | Interactive API documentation |
| `/gradio/` | Gradio demonstration |
| `/heart-disease/` | Machine-learning prediction demonstration |

The prediction demonstration is a teaching exercise. The introductory API runs
without AI credentials; the instructor will provide configuration guidance for
AI-enabled lessons.

### 4. Check your work

```bash
uv run --locked ruff check
uv run --locked pytest
```

Ruff checks code quality. Pytest runs the configured tests. Add tests for your own
application behaviour as you work through the assignments.

### 5. Submit for review

Commit and push your branch, then open a pull request into `development`.
Explain what you changed and how you tested it. Resolve any failed checks and
respond to your instructor's review.

When course deployment is enabled, a merged student pull request deploys that
student's application to its own Cloud Run service. The deployment workflow prints
the application URL in GitHub Actions.

## Data pipelines and experiment tracking

Start the services for your workspace:

```bash
bash run_dagster.sh YOUR-GITHUB-USERNAME
```

Use port **3000** for Dagster and **5000** for MLflow. To explore the reference
pipeline instead, run `bash run_dagster.sh example`.

Lessons that retrieve external data or use integrations require additional
configuration. Your instructor will guide you through these before the relevant lab.

## Repository guide

| Location | Purpose |
| --- | --- |
| `src/students/example/` | Reference APIs, applications, pipelines and agents |
| `src/students/<username>/` | Individual student work |
| `tests/` | Shared tests |
| `scripts/` | Workspace setup and deployment helpers |
| `.github/workflows/` | Automated checks and application deployment |
| `course.json` | Course configuration |
| `pyproject.toml` and `uv.lock` | Python project settings and dependency versions |

## Working together

- Keep changes focused and use descriptive commit messages.
- Test your application before requesting a review.
- Keep credentials out of code and commits; use the configuration provided for each lab.
- Report problems with the command you ran, the error message and the relevant file.

**Lead instructor:** [Shadrack Darku](https://github.com/shaddydevops)

Instructor configuration and deployment instructions are in [SETUP.md](SETUP.md).