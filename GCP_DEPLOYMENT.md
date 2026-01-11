# Google Cloud Deployment Script

This directory contains the deployment automation script for deploying WE-ii to Google Cloud Platform using Infrastructure Manager and Terraform.

## Files

- **`deploy_solution.sh`**: Main deployment script
- **`roles.txt`**: List of IAM roles required for deployment

## Quick Start

```bash
./deploy_solution.sh
```

## Prerequisites

### Required Tools

1. **Google Cloud SDK**: Install from https://cloud.google.com/sdk/docs/install
   ```bash
   gcloud --version
   ```

2. **jq**: JSON processor for parsing responses
   ```bash
   # Ubuntu/Debian
   sudo apt-get install jq
   
   # macOS
   brew install jq
   
   # Verify installation
   jq --version
   ```

### Required GCP Configuration

1. **Authenticated Account**:
   ```bash
   gcloud auth login
   ```

2. **Set Active Project**:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Enable Required APIs**:
   ```bash
   gcloud services enable \
     config.googleapis.com \
     compute.googleapis.com \
     storage.googleapis.com \
     cloudbuild.googleapis.com
   ```

4. **Billing**: Ensure your GCP project has billing enabled

## Script Workflow

### Step 1: Project Detection
- Retrieves the currently active GCP project ID
- Validates project configuration

### Step 2: Deployment Discovery
- Searches for existing Infrastructure Manager deployments
- Checks supported regions: `us-central1`, `europe-west1`, `asia-east1`
- Filters by solution ID: `we-ii-chat-app`

### Step 3: IAM Role Assignment
- Retrieves the service account from the deployment
- Checks current IAM policy bindings
- Assigns missing roles from `roles.txt`
- Skips roles that are already assigned

### Step 4: Terraform Variables Generation
- Extracts current deployment parameters
- Creates `input.tfvars` file with:
  - Region (locked to prevent migration issues)
  - Zone
  - Number of nodes
  - Project ID
  - Solution labels

### Step 5: User Review
- Pauses for user to review and customize `input.tfvars`
- Allows modifications to zone, nodes, and other parameters
- **Warning**: Do not change the region

### Step 6: Storage Bucket Creation
- Creates Cloud Storage bucket for Infrastructure Manager staging
- Bucket name format: `${PROJECT_ID}_infra_manager_staging`
- Skips if bucket already exists

### Step 7: Deployment Application
- Applies the Terraform configuration
- Uses Infrastructure Manager for state management
- Tags deployment with solution labels

## IAM Roles Explained

| Role | Purpose |
|------|---------|
| `roles/compute.instanceAdmin.v1` | Create and manage VM instances |
| `roles/compute.networkAdmin` | Configure VPC networks and load balancers |
| `roles/compute.securityAdmin` | Manage firewall rules and security policies |
| `roles/iam.serviceAccountUser` | Attach service accounts to resources |
| `roles/storage.admin` | Manage Cloud Storage buckets |
| `roles/cloudbuild.builds.editor` | Create and manage Cloud Build jobs |
| `roles/logging.logWriter` | Write application logs |
| `roles/monitoring.metricWriter` | Write monitoring metrics |

## Customizable Parameters

After the script generates `input.tfvars`, you can modify:

```hcl
# Change the zone within the same region
zone = "us-central1-b"  # or us-central1-c, us-central1-f

# Adjust number of VM nodes
nodes = "3"  # default is from existing deployment

# Add custom labels
labels = {
  "environment" = "production"
  "team" = "we-ii"
  # ... existing labels are preserved
}
```

**⚠️ Warning**: Do NOT change the `region` parameter as it can cause deployment failures.

## Error Handling

The script includes robust error handling:

- **Exits on errors**: Uses `set -o pipefail` and error trap
- **Validates deployment existence**: Fails if no deployment found
- **Checks bucket creation**: Handles existing buckets gracefully
- **Verifies IAM bindings**: Prevents duplicate role assignments

## Troubleshooting

### "Failed to find the existing deployment"

**Cause**: No Infrastructure Manager deployment exists with the solution ID `we-ii-chat-app`

**Solution**: 
1. Create an initial deployment via Google Cloud Console
2. Ensure it's labeled with `goog-solutions-console-solution-id: we-ii-chat-app`
3. Verify it's in one of the supported regions

### "Permission denied" errors

**Cause**: Insufficient permissions to assign IAM roles

**Solution**:
1. Ensure you have `roles/resourcemanager.projectIamAdmin` or `roles/owner`
2. Run: `gcloud projects get-iam-policy PROJECT_ID` to verify

### "jq: command not found"

**Cause**: JSON processor not installed

**Solution**: Install jq as described in Prerequisites

### Storage bucket already exists

**Status**: This is normal and expected. The script will continue.

## Security Considerations

1. **Service Account Least Privilege**: Only assigns required roles
2. **Conditional IAM Checks**: Avoids overwriting existing conditions
3. **Project Isolation**: Works within the configured project only
4. **No Hardcoded Credentials**: Uses gcloud authentication

## Integration with CI/CD

This script can be integrated into automated pipelines:

```yaml
# Example for GitHub Actions
- name: Deploy to GCP
  run: |
    echo "${GCP_SA_KEY}" | gcloud auth activate-service-account --key-file=-
    gcloud config set project ${{ secrets.GCP_PROJECT_ID }}
    ./deploy_solution.sh
```

## Support

For issues or questions:
1. Check the main [DEPLOYMENT.md](DEPLOYMENT.md) guide
2. Review GCP Infrastructure Manager documentation
3. Verify all prerequisites are met
4. Check Cloud Console for deployment status

## License

Copyright 2026 WE-ii Project

Licensed under the Apache License, Version 2.0
