import argparse

parser = argparse.ArgumentParser(description='Noise Maker')

parser.add_argument('--src', type=str,
                    help='name or path of source images.')
parser.add_argument('--dst', type=str,
                    help='path of destination.')

parser.add_argument('--method', type=str,
                    help='method of noising. {salt_and_pepper, gaussian}')
parser.add_argument('--p', type=float, default=0.05,
                    help='probability of salt and pepper noise.')
parser.add_argument('--var', type=float, default=10/255.,
                    help='variance of gaussian noise.')

args = parser.parse_args()
