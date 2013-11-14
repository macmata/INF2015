import argparse
import logging.config
import logging
import json
import sys
import os
import inspect

from builder.quote import Quotes
from builder.reader.json_reader import JsonReader
from builder.rules import vehicules

logging.config.fileConfig('config.ini')

if sys.argv[1] == '-L' and len(sys.argv) == 3:
    vehicule_list = vehicules.show_list()
    with open(sys.argv[2], 'w') as f:
        f.write(vehicule_list)
    exit(1)


parser = argparse.ArgumentParser(description= \
        'Calculate a an insurance quote for luxury car.')
parser.add_argument(
    'input',  type=str, nargs=1,
    help='Input file to read the quote information/'
)
parser.add_argument(
    'output', metavar='output', type=str, nargs=1,
    help='Output file to write the quote to.'
)
args = parser.parse_args()

input_file = args.input[0]
output_file = args.output[0]

logging.debug('Calculating quote from %s' % input_file)
driver, cars, motos, contrat = JsonReader(input_file).get_data()
q = Quotes(cars + motos, driver, contrat)
result = {
    'assurable': q.assurable,
    'montant_annuel': q.yearly_amount,
    'mensualite': q.monthly_amount
    }
logging.debug("Resultat : %s" % result)

with open(output_file, 'w') as f:
    f.write(json.dumps(result))
