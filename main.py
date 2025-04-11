from src.ticket_creator import create_ticket
from src.router import get_department
import joblib

def classify_and_route(user_message):
    model = joblib.load("models/classifier.pkl")
    prediction = model.predict([user_message])[0]
    dept = get_department(prediction)
    ticket = create_ticket(user_message, prediction, dept)
    return ticket

if __name__ == "__main__":
    print("=== Customer Service Agent ===")
    print("Type 'exit' to quit.\n")

    while True:
        msg = input("Enter your message: ").strip()
        if msg.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        ticket = classify_and_route(msg)
        print("\n🎫 Ticket Raised:")
        print(f"Ticket ID    : {ticket['ticket_id']}")
        print(f"Issue Type   : {ticket['category']}")
        print(f"Assigned To  : {ticket['assigned_to']}")
        print(f"Message      : {ticket['message']}\n")
