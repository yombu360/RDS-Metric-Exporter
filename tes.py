import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--config_file", help="increase output verbosity",
                    action="store")
args = parser.parse_args()

print(args.config_file)

