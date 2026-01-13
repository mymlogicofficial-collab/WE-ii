# WE-ii Deployment Guide

This guide covers multiple deployment options for the WE-ii application.

## 🌐 GitHub Pages Deployment

The repository is configured to deploy to GitHub Pages automatically.

### Live URL

Once GitHub Pages is enabled, your site will be available at:

**`https://mymlogicofficial-collab.github.io/WE-ii/`**

This is the shortest possible URL for GitHub Pages with this repository.

## ☁️ Google Cloud Platform Deployment

For deploying WE-ii to Google Cloud Platform with Infrastructure Manager and Terraform, use the provided deployment script.

### Prerequisites

- Google Cloud SDK (`gcloud`) installed and configured
- Active GCP project with billing enabled
- Required APIs enabled:
  - Infrastructure Manager API
  - Compute Engine API
  - Cloud Storage API
- `jq` command-line JSON processor installed

### Using the Deployment Script

1. **Navigate to the repository root**:
   ```bash
   cd /path/to/WE-ii
   ```

2. **Run the deployment script**:
   ```bash
   ./deploy_solution.sh
   ```

3. **Follow the prompts**:
   - The script will automatically detect your GCP project
   - Find existing Infrastructure Manager deployments
   - Assign required IAM roles to the service account
   - Generate an `input.tfvars` file for customization
   - Create a Cloud Storage bucket for staging
   - Deploy the solution using Infrastructure Manager

### What the Script Does

- **Fetches Project Configuration**: Retrieves your current GCP project ID
- **Locates Deployment**: Searches for existing deployments across supported regions (us-central1, europe-west1, asia-east1)
- **Assigns IAM Roles**: Configures necessary permissions from `roles.txt`
- **Generates Variables**: Creates `input.tfvars` with deployment parameters
- **Creates Storage**: Sets up Cloud Storage bucket for Infrastructure Manager
- **Deploys Solution**: Applies the Terraform configuration via Infrastructure Manager

### Required Roles

The following IAM roles are assigned to the service account (defined in `roles.txt`):
- `roles/compute.instanceAdmin.v1` - Manage compute instances
- `roles/compute.networkAdmin` - Configure networking
- `roles/compute.securityAdmin` - Manage security policies
- `roles/iam.serviceAccountUser` - Use service accounts
- `roles/storage.admin` - Manage Cloud Storage
- `roles/cloudbuild.builds.editor` - Build and deploy
- `roles/logging.logWriter` - Write logs
- `roles/monitoring.metricWriter` - Write metrics

### Customization

After the script generates `input.tfvars`, you can modify:
- Number of VM nodes
- Zone configuration (within the same region)
- Custom labels for resource organization

**Note**: Do not change the region as this can lead to deployment failures.

## 📋 GitHub Pages Setup Instructions

To complete the GitHub Pages deployment, follow these steps:

### 1. Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/mymlogicofficial-collab/WE-ii`
2. Click on **Settings** (top navigation bar)
3. In the left sidebar, click on **Pages**
4. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
5. Click **Save**

### 2. Merge to Main Branch

1. Merge this pull request to the `main` branch
2. The GitHub Actions workflow will automatically trigger
3. Wait for the deployment to complete (usually 1-2 minutes)

### 3. Access Your Site

Once deployed, visit: **`https://mymlogicofficial-collab.github.io/WE-ii/`**

## 🚀 How It Works

- The workflow file `.github/workflows/deploy.yml` handles automatic deployment
- It triggers on every push to the `main` branch
- You can also manually trigger it from the Actions tab
- The entire repository content is deployed, with `index.html` as the homepage

## 🔄 Future Updates

After the initial setup, any changes pushed to the `main` branch will automatically redeploy the site.

## ⚡ Manual Deployment

You can manually trigger a deployment:

1. Go to the **Actions** tab in your repository
2. Select "Deploy to GitHub Pages" workflow
3. Click **Run workflow**
4. Choose the `main` branch
5. Click **Run workflow**
