ROUTE_MAP = {
    "Technical": "Tech Support Team",
    "Billing/Payments": "Billing & Payments Team",
    "Sales/Upgrade": "Customer Success Team",
    "Account Update": "Accounts/Onboarding Team"
}


def get_department(issue_type):
    return ROUTE_MAP.get(issue_type, "General Support")
