"""
Task 0: Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template."""

    # Check template type
    if not isinstance(template, str):
        print(f"Error: template must be a string, got "
              f"{type(template).__name__}.")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print(f"Error: attendees must be a list, got "
              f"{type(attendees).__name__}.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # Write output file
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
