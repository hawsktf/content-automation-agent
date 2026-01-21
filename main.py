import os
import asyncio
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List, Dict

# Import local services
from sheets import sheets_service
from transcriber import Transcriber
from evaluator import Evaluator
from publisher import Publisher

load_dotenv()

app = FastAPI(title="Content Automation Agent API")

# State management (simplified)
agent_state = {
    "status": "idle",
    "last_run": None,
    "active_modules": []
}

class ModuleControl(BaseModel):
    module: str
    action: str # "start", "stop"

@app.get("/")
async def root():
    return {"message": "Content Automation Agent API is running"}

@app.get("/status")
async def get_status():
    return agent_state

@app.post("/control")
async def control_module(control: ModuleControl, background_tasks: BackgroundTasks):
    module = control.module
    action = control.action
    
    if action == "start":
        if module == "discovery":
            background_tasks.add_task(run_discovery_loop)
        elif module == "transcription":
            background_tasks.add_task(run_transcription_pipeline)
        
        agent_state["active_modules"].append(module)
        return {"status": "started", "module": module}
    
    return {"status": "stopped", "module": module}

async def run_discovery_loop():
    """Poll sources from Google Sheets."""
    print("Starting discovery loop...")
    sources = sheets_service.get_sources()
    for source in sources:
        # Check YouTube/X for new content
        print(f"Checking source: {source.get('Identifier')}")
        await asyncio.sleep(2)

async def run_transcription_pipeline():
    """Process pending transcriptions."""
    transcriber = Transcriber()
    # Logic to fetch pending videos from sheets and transcribe
    print("Running transcription pipeline...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
