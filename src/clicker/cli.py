import logging
import sys
import time

import click

__all__ = [
    "main",
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_analysis_list():
    return ["snap", "crackle", "pop"]

def get_output_list():
    return ["stop", "drop", "roll"]    

def extract():
    logger.info("Extracting...")
    time.sleep(5)
    logger.info("Extraction complete")

def transform():
    logger.info("Transforming...")
    time.sleep(5)
    logger.info("Transformation complete")

def load():
    logger.info("Loading...")
    time.sleep(5)
    logger.info("Load complete")
    
def analysis(analysis_names):
    analysis_list = get_analysis_list()
    
    analysis_names = analysis_list if len(analysis_names) == 0 else analysis_names
    analysis_names = list(set(analysis_names))
    
    print("The following analysis methods will be implemented:")
    print("\n".join([" - {name}".format(name=name) for name in analysis_names]))

    for name in analysis_names:
        if name in analysis_list:
            logger.info("Performing analysis \"{name}\"...".format(name=name))
            time.sleep(3)
            logger.info("Analysis \"{name}\" successfully performed.".format(name=name))
        else:
            logger.warning("There is no analysis called {name}. Skipping.".format(name=name))
    logger.info("Analysis complete")

def output(output_names):
    output_list = get_output_list()
    
    output_names = output_list if len(output_names) == 0 else output_names
    output_names = list(set(output_names))
    
    print("The following output reports will be built:")
    print("\n".join([" - {name}".format(name=name) for name in output_names]))
    
    for name in output_names:
        if name in output_list:
            logger.info("Building output \"{name}\"...".format(name=name))
            time.sleep(3)
            logger.info("Output \"{name}\" successfully built".format(name=name))
        else:
            logger.warning("There is no output called {name}. Skipping".format(name=name))
    logger.info("Output report building complete")

@click.group()
@click.version_option()
def main():
    """CLI for mock data analysis project"""

@main.command("analysis_list", help="Show list of names of allowed analysis methods")
def main_get_analysis_list():
    print("Available analysis methods:")
    output = [" - \"{entry}\"".format(entry=entry) for entry in get_analysis_list()]
    print("\n".join(output))

@main.command("output_list", help="Show list of names of allowed output reports")
def main_get_output_list():
    print("Available output reports:")
    output = [" - \"{entry}\"".format(entry=entry) for entry in get_output_list()]
    print("\n".join(output))


@main.command("etl", help="Perform ETL")
@click.option("-e", "--extract", "perform_extract", default=True, type=bool, help="Perform data extraction")
@click.option("-t", "--transform", "perform_transform", default=True, type=bool, help="Perform data transformation")
@click.option("-l", "--load", "perform_load", default=True, type=bool, help="Perform data load")
def main_etl(perform_extract, perform_transform, perform_load):
    if perform_extract:
        extract()
    if perform_transform:
        transform()
    if perform_load:
        load()
    return True
    
@main.command("analysis", help="Perform analysis")
@click.option(
    "-i", "--input", "analysis_names", default=None, type=str, multiple=True,
    help="Names of specific analysis methods to perform. Input multiple options with \"-i option_1 -i option_2\" etc. Not using this option will run all available analysis methods",
)
def main_analysis(analysis_names):
    analysis(analysis_names)
    return True

@main.command("output", help="Build output reports")
@click.option(
    "-i", "--input", "output_names", default=None, type=str, multiple=True,
    help="Names of specific output reports to build. Input multiple options with \"-i option_1 -i option_2\" etc. Not using this option will build all available outputs",
)
def main_output(output_names):
    output(output_names)
    return True
