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

def parser_to_csv(path_to_csv):
    """creates csv file."""
    rows_to_write = []
    with open(path_to_csv) as f:
        reader = csv.reader(f)
        start_index = 1
        for row in reader:
            if row[0].isdigit():
                rows_to_write.append([f" {start_index}-{start_index + int(row[0])-1}", *row[1:]])
                start_index += int(row[0])
            else:
                print(row, "EI OLE DIGIT")
    with open('loterii-2017-uus.csv', mode="w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(rows_to_write)
    return True