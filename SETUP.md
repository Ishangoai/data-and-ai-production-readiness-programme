# Instructor setup — existing GCP resources

Target: https://github.com/Ishangoai/data-and-ai-production-readiness-programme

## 1. Publish the prepared files

Extract the ZIP. Open a terminal inside its `data-and-ai-production-readiness-programme`
folder (the folder containing this file). Run:

```bash
git init -b main
git add .
git commit -m "Prepare 2026 course baseline"
git remote add origin https://github.com/Ishangoai/data-and-ai-production-readiness-programme.git
git push -u origin main
git switch -c development
git push -u origin development
```

These commands assume the target is still empty. If it has changed, do not force
push; inspect and reconcile the new contents first. Authenticate through your
normal GitHub credential manager. The push creates CI runs but no deployment,
because deployment only runs after a merged PR and an explicit repository toggle.
Use `main` as the initial default branch; student work targets `development`.

## 2. GitHub configuration

Under Settings → Environments, create `production`.
Under Settings → Secrets and variables → Actions → Variables, set:

| Name | Initial value |
| --- | --- |
| COURSE_DEPLOY_ENABLED | false |
| COURSE_ENABLE_AI | false |

Cloud metadata is already populated in `course.json`:

- Project: `cloud-apps-ishango`, number `898784939110`
- Region: `europe-west2`
- Registry: `cloud-apps-ishango-gcr`
- Provider: `projects/898784939110/locations/global/workloadIdentityPools/github/providers/github-actions-provider`
- Deployer: `tf-provision@cloud-apps-ishango.iam.gserviceaccount.com`
- Runtime identity: `cloud-run-service@cloud-apps-ishango.iam.gserviceaccount.com`

The provider and registry have been confirmed from the console information supplied.
The runtime account, exact deployment permissions, organisation workflow policies,
quotas and billing remain to be verified by the first pilot. No GCP credentials are
required as GitHub secrets for federation.

Set branch rules for `development` to require instructor review and the `checks`
status. Add students as collaborators who work on branches in this repository.
GitHub fork PRs are not the supported deployment route in this starter.

## 3. Local / Codespaces check

Open a Codespace and run:

```bash
uv sync --locked
uv run --locked ruff check
uv run --locked pytest
PYTHONPATH=src/students/example uv run --locked uvicorn api.main:app --host 0.0.0.0 --port 8080
```

Open port 8080 and test `/hello` and `/gradio/` before enabling deployments.

## 4. First Cloud Run deployment

1. Change repository variable `COURSE_DEPLOY_ENABLED` to `true`.
2. As `shaddydevops`, create a small README change on a feature branch and open a
   PR into `development`.
3. Wait for code checks, review, then merge it.
4. In Actions, open `Deploy Course Application`. It selects the `example` folder
   for an instructor PR and creates/updates `dai-prp-2026-example`.
5. Open the URL printed by the final deployment step. Confirm `/hello`, `/docs`,
   `/gradio/` and `/heart-disease/`.

This intentionally uses a `pull_request` event. The existing identity provider
accepts `push` and `pull_request`; a `workflow_dispatch` authentication attempt
would not satisfy its current condition. There is no Run workflow button here.

The pilot builds and pushes an image, creates a new public course service, and may
incur GCP charges. It sets 1 CPU, 1 GiB RAM, minimum zero and maximum two instances
per service. Those settings are not a spending cap. Other existing app names are
not targeted. Turn `COURSE_DEPLOY_ENABLED` back to `false` to stop future deployment
jobs; that does not stop or delete services already running.

If authentication fails, capture the failed step's error without secrets and ask
an infrastructure maintainer to verify the existing binding. Do not run the legacy
OpenTofu scripts as a troubleshooting shortcut.

## 5. AI lessons later

Keep `COURSE_ENABLE_AI=false` until model and search calls have been tested.
When ready, add `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` to the `production` environment
secrets, set `COURSE_ENABLE_AI=true`, and merge another instructor PR. Secrets from
last year's GitHub repo are not automatically copied. An authorised maintainer
needs to supply their values; do not use the old secret-revealing workflow.
The inherited chatbot uses `gemini-2.5-flash` and Google Custom Search. Their current
availability and your account's access are not validated by the local smoke test.

## 6. Pilot one student

Have one student create their folder, run locally, submit a PR and obtain review.
Check that their merged PR deploys the correct folder and has its own service URL.
Only then onboard the full cohort. Deployment packages the repository but selects
one student's API at runtime, consistent with the original course model.
