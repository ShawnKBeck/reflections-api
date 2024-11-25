import csv

def build_db():
    data = dict()
    with open("static/DailyReflections.csv", "r") as f:
        csv_reader = csv.reader(f)
        for id, month, day, title, reading, source, thought in csv_reader:
            if id == "Id":
                continue

            # Initialize entry
            entry = {
                "id": id,
                "date": f"{month} {day}",
                "title": title,
                "reading": reading,
                "source": source,
                "thought": thought,
            }

            # Add to database structure
            if month not in data:
                data[month] = {}
            data[month][day] = entry

    return data