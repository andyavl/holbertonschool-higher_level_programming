#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Input type validation
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Empty content checks
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process and write output
    for i, attendee in enumerate(attendees, start=1):
        # Safely get each value or fallback to "N/A"
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        content = template.replace("{name}", name)
        content = content.replace("{event_title}", title)
        content = content.replace("{event_date}", date)
        content = content.replace("{event_location}", location)

        # Write to file
        filename = f"output_{i}.txt"
        with open(filename, 'w') as f:
            f.write(content)
