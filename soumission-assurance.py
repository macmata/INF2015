import argparse

from builder import Quote,load

parser = argparse.ArgumentParser(description='Calculate a an insurance quote \
    for luxury car.')
parser.add_argument('input', metavar='input', type=str, nargs=1,
                   help='Input file to read the quote information/')
parser.add_argument('output', metavar='output', type=str, nargs=1,
                   help='Output file to write the quote to.')

args = parser.parse_args()

input_file = args.input[0]
output_file = args.output[0]

car,driver = load.extract_data_all(input_file)
q = Quote(car, driver)
q.build_quote()

print (q.montant)
