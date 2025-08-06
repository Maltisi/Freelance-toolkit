import json, os, datetime

LOG_FILE = 'data/time_log.json'

def load_entries():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as file:
        return json.load(file)

def save_entry(project, start_time, end_time):
    entry = {
        'project': project,
        'start': start_time.isoformat(),
        'end': end_time.isoformat(),
        'duration': str(end_time - start_time)
    }
    entries = load_entries()
    entries.append(entry)
    with open(LOG_FILE, 'w') as file:
        json.dump(entries, file, indent=4)

def track_time():
    project = input('Enter project name: ')
    print('Tracking started. Press Enter to stop.')
    start_time = datetime.datetime.now()
    input()
    end_time = datetime.datetime.now()
    save_entry(project, start_time, end_time)
    print(f'Time logged for project "{project}"')
import json
import os

def view_logs():
    log_file = os.path.join("data", "time_log.json")

    if not os.path.exists(log_file):
        print("No time logs found.")
        return

    with open(log_file, "r") as file:
        logs = json.load(file)

    if not logs:
        print("No time logs recorded.")
        return

    print("\n=== Time Logs ===")
    for i, entry in enumerate(logs, start=1):
        print(f"\nLog {i}:")
        print(f"Project: {entry['project']}")
        print(f"Start: {entry['start']}")
        print(f"End: {entry['end']}")
        print(f"Duration: {entry['duration']}")
