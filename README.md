# Data and AI Production Readiness Programme

Ishangoai · 2026 cohort · Lead instructor: `shaddydevops`

A refreshed copy of the previous AIMS course. Reference lessons, sample model and
locked Python dependencies are retained. Previous students' submissions remain in
the original repository; this copy starts with `src/students/example` only.

## Instructor setup

Read [SETUP.md](SETUP.md) before the first deployment. The application uses the
existing `cloud-apps-ishango` project and registry in `europe-west2`. No OpenTofu
workflow is active here. The old infrastructure and workflow files are retained
under `docs/legacy` for reference only.

## Student workflow

1. Accept your invitation as a collaborator on this repository. Use a branch in
   this repository, not a fork, for this cohort's deployment workflow.
2. Create `feature-branch-YOUR-GITHUB-USERNAME` from `development` and open that
   branch in GitHub Codespaces with the smallest available machine.
3. Wait for dependency installation. In the terminal run:

   ```bash
   python scripts/new_student.py YOUR-GITHUB-USERNAME
   ```

4. Only edit `src/students/YOUR-GITHUB-USERNAME/`. Use the exact capitalization of
   your GitHub login when creating the folder.
5. Run your API from the repository root:

   ```bash
   PYTHONPATH=src/students/YOUR-GITHUB-USERNAME uv run --locked uvicorn api.main:app --host 0.0.0.0 --port 8080
   ```

6. In Codespaces, use the Ports tab to open port 8080. Visit `/hello`, `/docs`,
   `/gradio/` and `/heart-disease/`. The sample heart model is a teaching artifact.
7. Run `uv run --locked ruff check` and `uv run --locked pytest` before committing.
8. Push your branch and open a pull request into `development`. An instructor
   reviews and merges it. When deployment is enabled, the merged PR deploys your
   application as `dai-prp-2026-YOUR-LOWERCASE-GITHUB-USERNAME`.

## Instructor example

```bash
PYTHONPATH=src/students/example uv run --locked uvicorn api.main:app --host 0.0.0.0 --port 8080
```

The API starts without Gemini or search credentials. `/llm-chat/` is only mounted
when `ENABLE_AI=true`. For local AI lessons, configure `GOOGLE_API_KEY` and
`GOOGLE_CSE_ID` as Codespaces secrets, then set `ENABLE_AI=true`. Do not put values
in committed files. The current example uses one key for Gemini and Custom Search;
that key must be accepted by both APIs. Model/search availability needs a live pilot.

## Data and ML lessons

```bash
bash run_dagster.sh example
# Students:
bash run_dagster.sh YOUR-GITHUB-USERNAME
```

Open port 3000 for Dagster and 5000 for MLflow. The launcher uses explicit module
paths. ERA5 ingestion needs `CDS_API_KEY` and the relevant Copernicus access/terms.
The original aggregation lesson sends a Slack message and needs
`SLACK_AIMS_COURSE_BOT_TOKEN`. Its old channel `aims_course_october2025` is retained;
update it to the agreed cohort channel before running that lesson. These integrations
are not required for the introductory API pilot.

The inherited pytest configuration tests the shared examples, not every student's
individual implementation. Add assignment-specific tests as the course progresses.
Runtime registration data in the API is in memory; it is not a persistent database.

## Maintenance

`course.json` contains instructor logins and cloud connection metadata (no secrets).
Keep `uv.lock` committed. The package's historical internal name is retained to
avoid changing the dependency baseline. Review [REFRESH_NOTES.md](REFRESH_NOTES.md)
for the scope and remaining live checks.
