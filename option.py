import argparse

parser = argparse.ArgumentParser(description='Noise Maker')

parser.add_argument('--src', type=str,
                    help='name if single else path of source images')
parser.add_argument('--dst', type=str,
                    help='path of destination')

parser.add_argument('--method', type=str,
                    help='method of noising. salt_and_pepper, gaussian')

args = parser.parse_args()
