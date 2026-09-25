import uuid
import re

def extract_tasks_from_text(raw_text: str):
    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
    tasks = []
    for line in lines:
        t_id = f"TSK-{uuid.uuid4().hex[:4].upper()}"
        l_low = line.lower()
        urgency = "High" if any(w in l_low for w in ["urgent", "asap", "today", "immediately", "deadline"]) else "Medium"
        importance = "High" if any(w in l_low for w in ["client", "production", "investor", "revenue", "critical"]) else "Low"
        category = "Operations" if "deploy" in l_low or "fix" in l_low else "Strategy"
        tasks.append({
            "task_id": t_id,
            "title": line.lstrip("-*123456789. "),
            "urgency": urgency,
            "importance": importance,
            "category": category
        })
    return tasks

def generate_daily_standup(tasks):
    high_p = [t["title"] for t in tasks if t["urgency"] == "High" or t["importance"] == "High"]
    summary = f"Today's Focus: {len(high_p)} critical deliverables out of {len(tasks)} planned items."
    return len(tasks), high_p, summary
