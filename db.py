import csv
import pprint 
from datetime import date

def build_db():
    data = dict()
    with open("static/DailyReflections.csv", "r") as f:
        csv_reader = csv.reader(f)
        for id, month, day, title, reading, source, thought in csv_reader:
            if id == "Id":
                continue

            if not month in data:
                data[month] = dict()
            
            if not day in data[month]:
                data[month][day] = dict()


            try:
                the_date = date(int(date.today().year), int(month), int(day)).strftime("%B %-d")
            except ValueError:
                the_date = "February 29"

            data[month][day] = {
                "id": id,
                "title": title,
                "reading": reading,
                "source": source,
                "thought": thought,
                "date": the_date
            }

    return data

pp = pprint.PrettyPrinter(depth=3, width=1000)
db = build_db()
pp.pprint(db)


def read_csv(month=None, day=None):
    """
    helper method which reads from "the database".

    Accepts optional month and day for a specific
    """
    with open("static/DailyReflections.csv", "r") as f:
        csv_reader = csv.reader(f)
        
        since = date.today() - date(2022, 1, 1) 
        if month:
            since = date(2022, month, day) - date(2022, 1, 1) # TODO: make curr month
        
        row = list(csv_reader)[since.days % 365] 
        
        the_date = date(2022, month=int(row[1]), day=int(row[2])).strftime("%B %-d")
        data = {
            "title": row[3],
            "reading": row[4],
            "citation": row[5],
            "content": row[6],
            "date": the_date
        }
        return data