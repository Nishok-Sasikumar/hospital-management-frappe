import frappe

def todo_timeline(doc):
    """
    Runs only for ToDo doctype's timeline.
    `doc` here is the ToDo document being viewed.
    """
    entries = ["hi"]

    entries.append(
        {
            "creation": doc.creation,
            "content": f"ToDo created: {doc.description or 'No description'}",
            "icon": "check-circle",
        }
    )

    if doc.status == "Closed":
        entries.append(
            {
                "creation": doc.modified,
                "content": "This ToDo was marked as Closed.",
                "icon": "check",
            }
        )

    if doc.allocated_to:
        entries.append(
            {
                "creation": doc.creation,
                "content": f"Allocated to {doc.allocated_to}.",
                "icon": "user",
            }
        )

    return entries