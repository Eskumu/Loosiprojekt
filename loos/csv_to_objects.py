"""Parse csv to sql objects."""

from .models import Prize, Ticket
import csv

def parser(path_to_csv):
    """
    Parse csv to sql objects.
    
    Works if sql table is empty at first.
    open terminal
    cd to Loosiprojekt
    
    delete old database
    python manage.py flush
    
    open manage.py in shell
    python manage.py shell
    
    from loos.csv_to_objects import parser
    parser('filename.csv')
    """
    #TODO: add instructions to clean sql table here.
    #TODO: make this function work with previous sql table
    with open(path_to_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            obj, created = Prize.objects.get_or_create(prize_text=row[1],prize_description=row[2])
            if created and row[0].isdigit():
                for _ in range(int(row[0])):
                    Ticket.objects.create(prize=obj)
            else:
                print(row, "Something is wrong with the format.")
    return True