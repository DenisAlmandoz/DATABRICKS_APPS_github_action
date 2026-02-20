# Databricks App deployment with Databricks Asset Bundles

This repository is configured to deploy your Databricks App with:

- `databricks.yml` (bundle configuration)
- `databricks/resources/app.yml` (app resource)
- `.github/workflows/databricks-app-cd.yml` (CD workflow)

## Files included

- `databricks.yml` uses targets: `dev`, `stg`, `prd`.
- `databricks/resources/app.yml` defines the app resource `hello-world-app`.
- `.github/workflows/databricks-app-cd.yml` validates, deploys, then runs the app resource.
- `app.py`, `layout.py`, `source.py` provide a simple Dash use case (entry point, UI layout, and data helpers).

## GitHub secrets you must configure

Add these in **GitHub → Settings → Secrets and variables → Actions → Repository secrets**:

1. `DATABRICKS_HOST`
   - Workspace URL used by the workflow (for example: `https://adb-xxxx.azuredatabricks.net`).
2. `DATABRICKS_CLIENT_ID`
   - Service Principal application/client ID.
3. `DATABRICKS_CLIENT_SECRET`
   - Service Principal OAuth client secret.

> The workflow uses `DATABRICKS_BUNDLE_ENV` to pick bundle target (`dev`, `stg`, `prd`).

## GitHub workflow variables (optional)

No repository variables are strictly required. The workflow sets `DATABRICKS_BUNDLE_ENV` automatically:

- `push` to `main` → `prd`
- `workflow_dispatch` → selected input (`dev`, `stg`, `prd`)

## How to run deployments

### Automatic

- Push to `main` and changes under `databricks.yml` or `databricks/**`.
- Workflow deploys to target `prd`.

### Manual

1. Open **Actions** in GitHub.
2. Select **Deploy Databricks App via Bundle**.
3. Click **Run workflow**.
4. Pick environment: `dev`, `stg`, or `prd`.

## Local validation (optional)

```bash
export DATABRICKS_HOST="https://adb-xxxx.azuredatabricks.net"
export DATABRICKS_CLIENT_ID="<sp-client-id>"
export DATABRICKS_CLIENT_SECRET="<sp-client-secret>"

databricks bundle validate --target dev
databricks bundle deploy --target dev
databricks bundle run hello-world-app --target dev
```

## Important notes

- Place your app source code in this repo (currently `source_code_path: .`).
- If your app code is in a subfolder, change `source_code_path` in `databricks/resources/app.yml`.
- Your Service Principal must have permissions to deploy and run app resources in each workspace target.
