import csv
import json
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
def show_data():
  hotspots = []
  with open('puntos-wi-fi-publicos.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')    
    for row in spamreader:
      hotspots.append({
        'lugar': row[0], 
        'lon': row[1], 
        'lat': row[2], 
        'barrio': row[3], 
        'comuna': row[4], 
        'categoria': row[5], 
        'domicilio': row[6]
      });
  return render_template('mapa.html', data=hotspots)

if __name__ == '__main__':
  app.run()