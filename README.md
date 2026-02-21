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
<<<<<<< ours
2. `DATABRICKS_CLIENT_ID`
   - Service Principal application/client ID.
3. `DATABRICKS_CLIENT_SECRET`
   - Service Principal OAuth client secret.

> The workflow uses `DATABRICKS_BUNDLE_ENV` to pick bundle target (`dev`, `stg`, `prd`).

## GitHub workflow variables (optional)

No repository variables are strictly required. The workflow sets `DATABRICKS_BUNDLE_ENV` automatically:

- `push` to `main` → `prd`
- `workflow_dispatch` → selected input (`dev`, `stg`, `prd`)
=======
2. `AZURE_SP_CREDS`
   - JSON credentials used by `azure/login` for your Service Principal.

## GitHub repository variables

Set these in **GitHub → Settings → Secrets and variables → Actions → Variables**:

- `APP_NAME`
- `WORKSPACE_REPO_PATH`
>>>>>>> theirs

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
<<<<<<< ours
=======


## GitHub Actions configuration (merged flow)

The workflow now merges bundle deployment with your Azure-auth + app sync/create/reboot sequence.

### Required repository secrets

- `DATABRICKS_HOST`: Databricks workspace URL (for example `https://adb-xxxx.azuredatabricks.net`)
- `AZURE_SP_CREDS`: JSON credentials for `azure/login` (service principal)

### Required repository variables

- `APP_NAME`: Databricks App name (for example `hello-world-app`)
- `WORKSPACE_REPO_PATH`: Databricks workspace path used by `databricks sync` (for example `/Workspace/Users/you@databricks.com/databricks_apps/hello-world-app`)

### Deployment sequence in workflow

1. Azure login with SP credentials.
2. Acquire Databricks token from Azure (`az account get-access-token`).
3. Bundle validate + deploy (`prd` target).
4. Sync repository code to Databricks workspace path.
5. Try to create app and deploy app code.
6. If app already exists (create step fails), stop/start the app to reboot it.
>>>>>>> theirs
