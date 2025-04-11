import uuid

def create_ticket(message, category, department):
    ticket_id = f"REQ-{str(uuid.uuid4())[:6].upper()}"
    return {
        "ticket_id": ticket_id,
        "message": message,
        "category": category,
        "assigned_to": department
    }
