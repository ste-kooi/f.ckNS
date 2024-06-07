import csv
import sys
import os

# Add the path to the classes folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from model import Model

def output(model: Model):
    """
    This function generates an output file in csv format.
    It takes values from a model
    
    """

    # Initiate data list of lists with a header
    data = [['train', 'stations']]

    
    # get all routes from the model
    for route in model.routes.values():
        stations = [station.name for station in route.stations]
        # Format the list to omit quotation marks
        stations_str = f"[{', '.join(stations)}]" 
        data.append([f'train_{route.train_id}', stations_str])
  

    # footer of the table contains the score of the model
    data.append(['score', model.calculate_score()])

    # write data to CSV file
    filename = "output/model_output.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data has been written to {filename}")

def test_output():
    test = Model("Holland")
    # Route 1
    test.add_route(test.stations['Beverwijk'], 1)
    test.routes[1].add_station(test.stations['Castricum'])
    test.routes[1].add_station(test.stations['Alkmaar'])
    test.routes[1].add_station(test.stations['Hoorn'])
    test.routes[1].add_station(test.stations['Zaandam'])

    # Route 2
    test.add_route(test.stations['Amsterdam Sloterdijk'], 2)
    test.routes[2].add_station(test.stations['Amsterdam Centraal'])
    test.routes[2].add_station(test.stations['Amsterdam Amstel'])
    test.routes[2].add_station(test.stations['Amsterdam Zuid'])
    test.routes[2].add_station(test.stations['Schiphol Airport'])

    # Route 3
    test.add_route(test.stations['Rotterdam Alexander'], 3)
    test.routes[3].add_station(test.stations['Gouda'])
    test.routes[3].add_station(test.stations['Alphen a/d Rijn'])
    test.routes[3].add_station(test.stations['Leiden Centraal'])
    test.routes[3].add_station(test.stations['Schiphol Airport'])
    test.routes[3].add_station(test.stations['Amsterdam Zuid'])



    output(test)

if __name__ == "__main__":
    test_output()