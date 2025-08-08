#!/bin/bash

# Release preparation script for orthophotos-downloader
# Usage: ./scripts/prepare-release.sh <version>
# Example: ./scripts/prepare-release.sh 0.1.0

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <version>"
    echo "Example: $0 0.1.0"
    exit 1
fi

VERSION=$1
TAG="v${VERSION}"

echo "🚀 Preparing release ${TAG}"

# Check if we're on the main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "⚠️  Warning: You are not on the main branch (current: $CURRENT_BRANCH)"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if working directory is clean
if ! git diff-index --quiet HEAD --; then
    echo "❌ Working directory is not clean. Please commit your changes first."
    exit 1
fi

# Update version in pyproject.toml
echo "📝 Updating version in pyproject.toml to ${VERSION}"
sed -i "s/^version = .*/version = \"${VERSION}\"/" pyproject.toml

# Verify the change
NEW_VERSION=$(grep '^version = ' pyproject.toml | cut -d '"' -f 2)
if [ "$NEW_VERSION" != "$VERSION" ]; then
    echo "❌ Failed to update version in pyproject.toml"
    exit 1
fi

echo "✅ Version updated to ${VERSION}"

# Build and test the package
echo "🔨 Building package..."
python -m build

echo "🧪 Testing package..."
python -m twine check dist/*

echo "✅ Package built and tested successfully"

# Create commit and tag
echo "📝 Creating commit and tag..."
git add pyproject.toml
git commit -m "Bump version to ${VERSION}"
git tag -a "${TAG}" -m "Release ${TAG}"

echo "✅ Release ${TAG} prepared successfully!"
echo ""
echo "Next steps:"
echo "1. Push the changes: git push origin main"
echo "2. Push the tag: git push origin ${TAG}"
echo "3. The GitHub Actions workflow will automatically publish to PyPI"
echo ""
echo "Or push everything at once:"
echo "git push origin main --tags"
