# Keyword Argument Usage

def log_event(event, level="INFO"):
    print(f"[{level}] {event}")

log_event("Training started")  
log_event("Model crashed", level="ERROR")  
