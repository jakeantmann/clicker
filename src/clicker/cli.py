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
    allowed_names = ["snap", "crackle", "pop"]
    
    analysis_names = allowed_names if analysis_names is None else analysis_names
    
    for name in analysis_names:
        if name in allowed_names:
            logger.info("Performing analysis \"{name}\"".format(name=name))
            time.sleep(3)
            logger.info("Analysis \"{name}\" successfully performed.".format(name=name))
        else:
            logger.warning("There is no analysis called {name}".format(name=name))

def output(output_names):
    allowed_names = ["snap", "crackle", "pop"]
    
    output_names = allowed_names if output_names is None else output_names
    
    for name in output_names:
        if name in allowed_names:
            logger.info("Building output \"{name}\"".format(name=name))
            time.sleep(3)
            logger.info("Output \"{name}\" successfully built".format(name=name))
        else:
            logger.warning("There is no output called {name}".format(name=name))

@click.group()
@click.version_option()
def main():
    """CLI for etl."""

@main.command("etl", help="Perform ETL")
@click.option("-e", "--extract", "perform_extract", default=True, type=bool, help="Perform extraction")
@click.option("-t", "--transform", "perform_transform", default=True, type=bool, help="Perform transformation")
@click.option("-l", "--load", "perform_load", default=True, type=bool, help="Perform load")
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
    help="Names of specific analyses to perform. Input multiple options with \"-i option_1 -i option_2\" etc",
)
def main_analysis(analysis_names):
    analysis(analysis_names)
    return True

@main.command("output", help="Build output reports")
@click.option(
    "-i", "--input", "output_names", default=None, type=str, multiple=True,
    help="Names of specific output reports to build. Input multiple options with \"-i option_1 -i option_2\" etc",
)
def main_output(output_names):
    output(output_names)
    return True
