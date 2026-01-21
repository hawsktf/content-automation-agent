#!/bin/bash

# Quick script to move project and set up GitHub with SSH

set -e

SOURCE_DIR="/home/spoonbill/.gemini/antigravity/scratch/git/content-automation-agent"
TARGET_DIR="/home/spoonbill/Projects/git/content-automation-agent"

echo "Moving project to $TARGET_DIR..."
mkdir -p /home/spoonbill/Projects/git
cp -r "$SOURCE_DIR" "$TARGET_DIR"

cd "$TARGET_DIR"

# Create .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
venv/
.env
frontend/node_modules/
frontend/dist/
.DS_Store
*.log
EOF

git add .gitignore
git commit -m "Add .gitignore" || true

echo ""
echo "Project moved successfully!"
echo ""
echo "Now, to push to GitHub:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Name it: content-automation-agent"
echo "3. Do NOT initialize with README"
echo ""
echo "Then run these commands:"
echo ""
echo "  cd $TARGET_DIR"
echo "  git remote add origin git@github.com:YOUR_USERNAME/content-automation-agent.git"
echo "  git branch -M main"
echo "  git push -u origin main"
echo ""
echo "Replace YOUR_USERNAME with your GitHub username"
echo ""
