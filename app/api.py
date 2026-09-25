from fastapi import FastAPI
from app.config import settings
from app.models import RawNoteInput, DailyBriefing, ExtractedTask
from app.services.task_extractor import extract_tasks_from_text, generate_daily_standup

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/extract-tasks")
def extract(note: RawNoteInput):
    tasks = extract_tasks_from_text(note.raw_text)
    return {"tasks": tasks}

@app.post("/daily-briefing", response_model=DailyBriefing)
def briefing(note: RawNoteInput):
    tasks = extract_tasks_from_text(note.raw_text)
    count, high_p, summary = generate_daily_standup(tasks)
    return DailyBriefing(tasks_count=count, high_priority_tasks=high_p, standup_summary=summary)
