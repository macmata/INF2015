import argparse
import logging

from builder import Quote
from builder.reader.json import JsonReader

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

driver, car, contrat = JsonReader(input_file).get_data()
q = Quote(car, driver, contrat)
q.build_quote()

result = {
    'assurable': q.assurable,
    'montant_annuel': q.montant_annuel,
    'mensualite': q.montant_mensuel
    }
print(result)
