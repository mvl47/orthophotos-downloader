# PyPI Deployment Guide

This document outlines how to deploy the orthophotos-downloader package to PyPI using GitHub Actions.

## Prerequisites

### 1. PyPI Accounts
Create accounts on:
- [PyPI](https://pypi.org/account/register/) (production)
- [TestPyPI](https://test.pypi.org/account/register/) (testing)

### 2. API Tokens
Generate API tokens for secure authentication:

#### PyPI Token:
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Navigate to "API tokens" section
3. Click "Add API token"
4. Name: `orthophotos-downloader-github-actions`
5. Scope: `Entire account` (or limit to specific project after first upload)
6. Copy the generated token (starts with `pypi-`)

#### TestPyPI Token:
1. Go to [TestPyPI Account Settings](https://test.pypi.org/manage/account/)
2. Follow the same steps as above
3. Copy the generated token

### 3. GitHub Secrets
Add the API tokens as GitHub repository secrets:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:
   - Name: `PYPI_API_TOKEN`, Value: `pypi-AgENdGVzdC5weXBpLm9yZy...`
   - Name: `TEST_PYPI_API_TOKEN`, Value: `pypi-AgENdGVzdC5weXBpLm9yZy...`

### 4. GitHub Environment (Optional but Recommended)
Create a protected environment for releases:

1. Go to **Settings** → **Environments**
2. Click **New environment**
3. Name: `release`
4. Add protection rules:
   - ✅ Required reviewers (add yourself and/or team members)
   - ✅ Deployment branches: only `main` branch

## Deployment Process

### Automated Deployment (Recommended)

The deployment process is fully automated using GitHub Actions. When you push a version tag, the workflow will:

1. **Build** the package
2. **Test** the build
3. **Verify** version consistency
4. **Publish** to PyPI
5. **Create** a GitHub release

#### Steps to Deploy:

1. **Prepare the release** (use the provided script):
   ```bash
   ./scripts/prepare-release.sh 0.1.0
   ```

2. **Push changes and tag**:
   ```bash
   git push origin main --tags
   ```

3. **Monitor the workflow**:
   - Go to **Actions** tab in GitHub
   - Watch the "Publish to PyPI" workflow
   - If using protected environments, approve the deployment

### Manual Deployment (Fallback)

If needed, you can deploy manually:

```bash
# Clean previous builds
rm -rf dist/ build/

# Build the package
python -m build

# Check the package
python -m twine check dist/*

# Upload to TestPyPI (optional)
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*
```

## Version Management

### Version Numbering
Follow [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (e.g., `1.0.0`)
- Pre-releases: `1.0.0rc1`, `1.0.0a1`, `1.0.0b1`

### Version Tags
- Production releases: `v1.0.0`, `v0.1.0`
- Pre-releases: `v1.0.0rc1`, `v0.1.0a1`

Pre-release tags (containing `rc`, `alpha`, `beta`) will be published to TestPyPI first.

## Release Workflow Features

### 🔍 Version Verification
- Automatically checks that the git tag matches the version in `pyproject.toml`
- Prevents accidental version mismatches

### 🧪 Testing Pipeline
- Runs on multiple Python versions (3.10, 3.11, 3.12)
- Builds and validates the package
- Tests installation

### 📦 Dual Publishing
- Pre-releases (`rc`, `alpha`, `beta`) → TestPyPI
- Stable releases → PyPI

### 🎉 GitHub Releases
- Automatically creates GitHub releases
- Includes installation instructions
- Marks pre-releases appropriately

## Troubleshooting

### Common Issues

#### 1. Version Mismatch Error
```
ERROR: Tag version (0.1.1) does not match pyproject.toml version (0.1.0)
```
**Solution**: Update the version in `pyproject.toml` or use the correct tag.

#### 2. PyPI Authentication Error
```
HTTP Error 403: Invalid or non-existent authentication information
```
**Solution**: Verify your API tokens in GitHub secrets.

#### 3. Package Already Exists
```
HTTP Error 400: File already exists
```
**Solution**: Increment the version number. PyPI doesn't allow re-uploading the same version.

#### 4. Build Errors
**Solution**: Test locally first:
```bash
python -m build
python -m twine check dist/*
```

### Testing Before Release

Always test your package before releasing:

```bash
# Test build
python -m build

# Install in development mode
pip install -e .

# Test import
python -c "import orthophotos_downloader; print('Success!')"

# Run tests (if available)
pytest
```

## Security Best Practices

1. **Use API tokens** instead of username/password
2. **Limit token scope** to specific projects when possible
3. **Use GitHub environments** with approval requirements
4. **Enable 2FA** on PyPI and TestPyPI accounts
5. **Regularly rotate** API tokens
6. **Never commit** API tokens to the repository

## Monitoring

After deployment, monitor:
- [PyPI project page](https://pypi.org/project/orthophotos-downloader/)
- Download statistics
- User feedback and issues
- Security advisories

## Next Steps

1. Set up the GitHub secrets with your PyPI tokens
2. Test with a pre-release version first
3. Create your first release using the provided script
4. Monitor the automated deployment process
5. Celebrate! 🎉

For questions or issues, please open a GitHub issue or contact the maintainers.

---

## Screenshots (placeholders)

Below are example screenshots that your colleagues should capture and place in `DEPLOYMENT-images/` with the suggested filenames. The PDF generator will include these images in the final PDF.

- ![Create API Token](DEPLOYMENT-images/01_pypi_create_token.png)
  - Screenshot: PyPI/TestPyPI - Create API token page

- ![Add GitHub Secret](DEPLOYMENT-images/02_github_secret.png)
  - Screenshot: GitHub - Add new repository secret

- ![Create Environment](DEPLOYMENT-images/03_github_env.png)
  - Screenshot: GitHub - Create `release` environment and protection rules

- ![Push Tag](DEPLOYMENT-images/04_tag_push.png)
  - Screenshot: GitHub - Tags / Git push confirmation

- ![Actions Run](DEPLOYMENT-images/05_actions_run.png)
  - Screenshot: GitHub - Actions run success page

---

## Generate PDF (for colleagues)

Option A — Use GitHub Actions (recommended):
- Open the repository -> Actions -> select "Build Deployment PDF" -> Run workflow
- The workflow will convert `DEPLOYMENT.md` into `DEPLOYMENT.pdf` and upload it as an artifact.

Option B — Generate locally:
- Install prerequisites (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install -y pandoc texlive-xetex texlive-fonts-recommended
  ```
- Run the helper script:
  ```bash
  chmod +x scripts/generate-pdf-locally.sh
  ./scripts/generate-pdf-locally.sh
  ```

## Notes for preparing screenshots
- Use 1280×720 resolution or similar for legibility
- Crop sensitive data (tokens) before committing
- Add screenshots to `DEPLOYMENT-images/` and commit the images so CI can include them

## Files added by this guide
- `.github/workflows/build-deployment-pdf.yml` — GitHub Action to build PDF
- `scripts/generate-pdf-locally.sh` — helper to build PDF locally
- `DEPLOYMENT-images/` — folder for screenshots

Add these files to the repository and notify colleagues to follow the instructions above.
