#!/bin/bash

# Script to move project to /home/spoonbill/Projects/git and set up GitHub

set -e  # Exit on error

echo "=========================================="
echo "Content Automation Agent - Move & GitHub Setup"
echo "=========================================="
echo ""

# Configuration
SOURCE_DIR="/home/spoonbill/.gemini/antigravity/scratch/git/content-automation-agent"
TARGET_DIR="/home/spoonbill/Projects/git/content-automation-agent"

# Step 1: Create target directory
echo "Step 1: Creating target directory..."
mkdir -p /home/spoonbill/Projects/git
echo "✓ Directory created"
echo ""

# Step 2: Stop running services
echo "Step 2: Stopping running services..."
echo "Please press Ctrl+C in the terminals running the backend and frontend"
echo "Press Enter when ready to continue..."
read

# Step 3: Move project
echo "Step 3: Moving project files..."
if [ -d "$TARGET_DIR" ]; then
    echo "Warning: Target directory already exists!"
    echo "Do you want to remove it and continue? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        rm -rf "$TARGET_DIR"
    else
        echo "Aborted."
        exit 1
    fi
fi

cp -r "$SOURCE_DIR" "$TARGET_DIR"
echo "✓ Project moved to $TARGET_DIR"
echo ""

# Step 4: Set up .gitignore
echo "Step 4: Creating .gitignore..."
cd "$TARGET_DIR"
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# Frontend
frontend/node_modules/
frontend/dist/
frontend/.vite/
frontend/.env.local

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Downloaded content
downloads/
transcripts/
EOF
echo "✓ .gitignore created"
echo ""

# Step 5: Add .gitignore to git
echo "Step 5: Updating git repository..."
git add .gitignore
git commit -m "Add .gitignore" || echo "No changes to commit"
echo "✓ Git repository updated"
echo ""

# Step 6: GitHub setup
echo "Step 6: GitHub Repository Setup"
echo "================================"
echo ""
echo "Please provide your GitHub information:"
echo ""
read -p "GitHub username: " GITHUB_USERNAME
read -p "Repository name (default: content-automation-agent): " REPO_NAME
REPO_NAME=${REPO_NAME:-content-automation-agent}
echo ""

echo "Now, please:"
echo "1. Go to https://github.com/new"
echo "2. Create a new repository named: $REPO_NAME"
echo "3. Do NOT initialize with README, .gitignore, or license"
echo "4. Press Enter when the repository is created..."
read

# Step 7: Add remote and push
echo "Step 7: Adding GitHub remote and pushing..."
GITHUB_URL="git@github.com:$GITHUB_USERNAME/$REPO_NAME.git"

# Remove existing remote if it exists
git remote remove origin 2>/dev/null || true

# Add new remote
git remote add origin "$GITHUB_URL"

# Rename branch to main if needed
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" = "master" ]; then
    git branch -M main
fi

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo ""
echo "Project location: $TARGET_DIR"
echo "GitHub repository: $GITHUB_URL"
echo ""
echo "To start the services:"
echo "  Terminal 1 (Backend):"
echo "    cd $TARGET_DIR"
echo "    ./venv/bin/python main.py"
echo ""
echo "  Terminal 2 (Frontend):"
echo "    cd $TARGET_DIR/frontend"
echo "    npm run dev"
echo ""
