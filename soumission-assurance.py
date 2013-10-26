import argparse
import logging.config
import logging
import json

from builder.quote import Quote
from builder.reader.json import JsonReader

logging.config.fileConfig('config.ini')

parser = argparse.ArgumentParser(description='Calculate a an insurance quote \
    for luxury car.')
parser.add_argument(
    'input', metavar='input', type=str, nargs=1,
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

quotes = build_qu
q = Quote(cars[0], motos[0], driver, contrat)
q.build_quote()

result = {
    'assurable': q.assurable,
    'montant_annuel': q.montant_annuel,
    'mensualite': q.montant_mensuel
    }

logging.debug("Resultat : %s" % result)

with open(output_file, 'w') as f:
    f.write(json.dumps(result))
