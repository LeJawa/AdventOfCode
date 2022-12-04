import argparse

def get_config_from_individual_day():
    parser = argparse.ArgumentParser(description="Individual day script",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--no-output", action="store_true", help="Don't show output")
    args = parser.parse_args()
    config = vars(args)
    return config


def get_config_for_new_days_generation():
    parser = argparse.ArgumentParser(description="Generate new days. Default is current year and one additional day up to 25.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-y", "--year", help="Year in which to generate day")
    parser.add_argument("-d", "--days", help="Days to generate")
    args = parser.parse_args()
    config = vars(args)
    return config