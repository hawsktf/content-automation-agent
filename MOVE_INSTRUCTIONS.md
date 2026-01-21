# Instructions to Move Project and Set Up GitHub

## Quick Start

I've created an automated script to handle everything. Here's what to do:

### Step 1: Stop the Running Services

First, stop the backend and frontend servers:
- Go to the terminal running the backend and press `Ctrl+C`
- Go to the terminal running the frontend and press `Ctrl+C`

### Step 2: Run the Setup Script

```bash
cd /home/spoonbill/.gemini/antigravity/scratch/git/content-automation-agent
./move_and_setup_github.sh
```

The script will:
1. ✅ Create `/home/spoonbill/Projects/git/` directory
2. ✅ Move the entire project there
3. ✅ Create a proper `.gitignore` file
4. ✅ Guide you through creating a GitHub repository
5. ✅ Push the code to GitHub

### Step 3: Follow the Prompts

The script will ask you for:
- Your GitHub username
- Repository name (default: `content-automation-agent`)
- It will pause for you to create the GitHub repo online

### Step 4: Start Services from New Location

After the move:

**Terminal 1 - Backend:**
```bash
cd /home/spoonbill/Projects/git/content-automation-agent
./venv/bin/python main.py
```

**Terminal 2 - Frontend:**
```bash
cd /home/spoonbill/Projects/git/content-automation-agent/frontend
npm run dev
```

---

## Manual Alternative (If Script Doesn't Work)

If you prefer to do it manually:

### 1. Stop Services
Press `Ctrl+C` in both terminal windows

### 2. Move Project
```bash
mkdir -p /home/spoonbill/Projects/git
cp -r /home/spoonbill/.gemini/antigravity/scratch/git/content-automation-agent /home/spoonbill/Projects/git/
cd /home/spoonbill/Projects/git/content-automation-agent
```

### 3. Create .gitignore
```bash
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
git commit -m "Add .gitignore"
```

### 4. Create GitHub Repository
1. Go to https://github.com/new
2. Name it `content-automation-agent`
3. Do NOT initialize with README
4. Click "Create repository"

### 5. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/content-automation-agent.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Troubleshooting

**Permission denied when running script:**
```bash
chmod +x move_and_setup_github.sh
```

**Git authentication issues:**
You may need to set up a GitHub Personal Access Token:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with `repo` permissions
3. Use the token as your password when pushing

**Services won't start:**
Make sure you're in the new directory and the virtual environment exists:
```bash
cd /home/spoonbill/Projects/git/content-automation-agent
ls -la venv/  # Should show the virtual environment
```
