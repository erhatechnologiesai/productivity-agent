from pydantic import BaseModel
from typing import List, Optional

class RawNoteInput(BaseModel):
    raw_text: str

class ExtractedTask(BaseModel):
    task_id: str
    title: str
    urgency: str # High, Medium, Low
    importance: str # High, Low
    category: str

class DailyBriefing(BaseModel):
    tasks_count: int
    high_priority_tasks: List[str]
    standup_summary: str
