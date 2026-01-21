# Content Automation Agent

A full-stack application for automating content discovery, evaluation, transcription, and publishing workflows.

## Project Structure

```
content-automation-agent/
├── backend/               # Python FastAPI backend
│   ├── main.py           # API server
│   ├── discovery.py      # Content discovery module
│   ├── evaluator.py      # On-brand evaluation
│   ├── transcriber.py    # YouTube transcription
│   ├── publisher.py      # Content publishing
│   ├── sheets.py         # Google Sheets integration
│   ├── sheet_init.py     # Database initialization
│   └── requirements.txt  # Python dependencies
└── frontend/             # React frontend
    ├── src/
    └── package.json
```

## Prerequisites

- **Python 3.8+**
- **Node.js 16+** and npm
- **Google Cloud Service Account** with Sheets API access
- **Google AI API Key** (Tier 1 recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd content-automation-agent
```

### 2. Backend Setup

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the root directory with the following:

```env
# Google AI API
GOOGLE_API_KEY=your_google_ai_api_key_here

# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS_FILE=path/to/service-account.json
SPREADSHEET_ID=your_spreadsheet_id_here

# Optional: Additional configuration
BRAND_NAME=YourBrandName
```

#### Initialize Google Sheets Database

```bash
python sheet_init.py
```

This will create the necessary sheets structure in your Google Spreadsheet.

### 3. Frontend Setup

#### Navigate to Frontend Directory

```bash
cd frontend
```

#### Install Dependencies

```bash
npm install
```

#### Configure Frontend Environment (if needed)

Create `frontend/.env` if you need to configure the API endpoint:

```env
VITE_API_URL=http://localhost:8000
```

## Running the Application

### Start the Backend Server

From the project root directory:

```bash
python main.py
```

The backend API will be available at `http://localhost:8000`

### Start the Frontend Development Server

In a separate terminal, from the `frontend` directory:

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173` (or the port shown in the terminal)

## Quick Start Commands

### Terminal 1 - Backend
```bash
cd /path/to/content-automation-agent
python main.py
```

### Terminal 2 - Frontend
```bash
cd /path/to/content-automation-agent/frontend
npm run dev
```

## API Endpoints

- `GET /` - API health check
- `GET /status` - Get agent status
- `POST /control` - Control modules (start/stop)

## Modules

- **Discovery**: Monitors content sources from Google Sheets
- **Transcription**: Processes YouTube videos with Whisper
- **Evaluator**: Assesses content for brand alignment
- **Publisher**: Publishes approved content

## Google Sheets Structure

The application uses Google Sheets as a database with the following sheets:

- **Sources**: Content sources to monitor
- **Content**: Discovered content items
- **Transcripts**: Processed transcriptions
- **Published**: Published content tracking

## Development

### Backend Development

The backend uses FastAPI with hot-reload enabled by default when running via `uvicorn`.

### Frontend Development

The frontend uses Vite with hot module replacement (HMR) for fast development.

## Deployment

### Backend Deployment

For production, use a production-grade ASGI server:

```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Deployment

Build the frontend for production:

```bash
cd frontend
npm run build
```

The built files will be in `frontend/dist/` and can be served by any static file server.

## Troubleshooting

### Backend Issues

- **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Google Sheets access**: Verify your service account JSON file path and permissions
- **API key errors**: Check that your `GOOGLE_API_KEY` is valid and has sufficient quota

### Frontend Issues

- **Connection refused**: Ensure the backend is running on port 8000
- **Build errors**: Delete `node_modules` and run `npm install` again

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
