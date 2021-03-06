import argparse
import logging.config
import logging
import json
import sys
import os
import inspect
import json

from builder.quote import Quotes
from builder.reader.json_reader import JsonReader
from builder.rules import vehicules
from builder.stats import Stats

stats = Stats('stats.sqlite')

logging.config.fileConfig('config.ini')

parser = argparse.ArgumentParser(description= \
        'Calculate a an insurance quote for luxury car.')
parser.add_argument(
    'input',  type=str, nargs='?',
    help='Input file to read the quote information.'
)
parser.add_argument(
    'output', metavar='output', type=str, nargs='?',
    help='Output file to write the quote to.'
)
parser.add_argument(
    '-L', type=argparse.FileType('w'), help='Show the list of vehicues',
    metavar='outfile'
)
parser.add_argument(
    '-S', type=argparse.FileType('w'), help='Returns some statistics',
    metavar='outfile'
)

args = parser.parse_args()
if args.L:
    json_data = json.dumps(vehicules.return_list_of_vehicules(), indent=4)
    args.L.write(json_data)
    args.L.close()
    exit(0)

if args.S:
    json_data = json.dumps(stats.return_all_stats(), indent=4)
    args.S.write(json_data)
    args.S.close()
    exit(0)

input_file = args.input
output_file = args.output

logging.debug('Calculating quote from %s' % input_file)
driver, cars, motos, contrat = JsonReader(input_file).get_data()
q = Quotes(cars + motos, driver, contrat)
stats.insert_from_quotes(q)
result = {
    'assurable': q.assurable,
    'montant_annuel': q.yearly_amount,
    'mensualite': q.monthly_amount
    }
logging.debug("Resultat : %s" % result)

with open(output_file, 'w') as f:
    f.write(json.dumps(result))
