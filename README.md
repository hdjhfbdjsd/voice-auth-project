# Secure Voice Authentication System

## Overview
Project to build a voice-based authentication system with anti-spoofing detection.
Stack: Python, PyTorch, SpeechBrain, FastAPI, Dash.

## Structure
- data/: raw and processed audio
- models/: training scripts
- models_saved/: checkpoints
- src/: source code (preprocessing, models, api, dashboard)
- notebooks/: experiments
- docs/: documentation

## Quick start (dev)
1. Create virtualenv and activate:
   - `python -m venv venv`
   - `source venv/bin/activate` (Windows: `venv\\Scripts\\activate`)
2. Install requirements:
   - `pip install -r requirements.txt`
3. Run backend server (example):
   - `uvicorn src.api.app:app --reload --port 8000`
4. Run dashboard:
   - `python src.dashboard.app.py`

## Dataset
We will use subsets of VoxCeleb + small custom recordings for enrollment/testing.

## Team & Workflow
- Weekly sprints. See docs/sprint-plan.md for details.
