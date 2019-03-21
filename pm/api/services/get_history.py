import csv
import requests
import pandas as pd

url = "https://www.netfonds.no/quotes/paperhistory.php?paper=NANO.OSE&csv_format=csv"

response = requests.get(url).text

pd.read_csv(response, encoding="ISO-8859-1", delimiter=",")

reader = csv.reader(response.splitlines(), delimiter=',')

for row in reader:
    print('\t'.join(row))