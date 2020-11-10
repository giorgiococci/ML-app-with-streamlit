# -*- coding: utf-8 -*-
import os
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv

'''
@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
'''

basedir = os.path.abspath("src/data")
logging.basicConfig(
    filename=os.path.join(basedir, "app.log"),
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def debug_path():
    # Configure basepath and define dataset path (debug only)
    BASEPATH = os.path.abspath("data/raw")
    DATASET = "diabetes.csv"

    dataset_path = os.path.join(BASEPATH, DATASET)
    logging.debug(f"Dataset path: {dataset_path}")

    return dataset_path