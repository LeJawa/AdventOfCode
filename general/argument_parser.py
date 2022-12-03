import argparse

def get_config():
    parser = argparse.ArgumentParser(description="Day 1 script",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--no-output", action="store_true", help="Don't show output")
    args = parser.parse_args()
    config = vars(args)
    return config