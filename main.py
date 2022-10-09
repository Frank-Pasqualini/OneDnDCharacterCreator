"""
Main file for this program.
"""

import argparse
import logging
import os
import pkgutil
import sys

import mergedeep

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARNING"))


def load_all_content_files(directory: str, packages: list[str]) -> list:
    """
    Loads in a list of python modules to process. Used for variable imports
    :param directory: The directory to scan for content files
    :type directory: str
    :param packages: The list of content files to scan
    :type packages: str
    :return: A list of usable python modules
    :rtype: list
    """

    package_importers = {}
    for importer, package_name, _ in pkgutil.iter_modules([directory]):
        package_importers[package_name] = importer

    for package in packages:
        try:
            importer = package_importers[package]
            full_package_name = f"{directory}.{package})"
            if full_package_name not in sys.modules:
                module = importer.find_module(package).load_module(package)
                yield module
        except KeyError as exc:
            logging.error("Cannot find file %s.py in directory %s",
                          package, directory)
            raise ImportError(
                f"Cannot find file {package}.py in directory {directory}") from exc


def main(characters: list[str], sources: list[str]):
    """
    Main function.
    """

    logging.info(
        "Generating sheets for characters %s using sources %s", characters, sources)

    content = {}
    for source in load_all_content_files("sources", sources):
        try:
            mergedeep.merge(content, source.CONTENT)
        except AttributeError as exc:
            logging.error(
                "%s has not correctly implemented the CONTENT dictionary", source)
            raise AttributeError(
                f"{source} has not correctly implemented the CONTENT dictionary") from exc

    for character in load_all_content_files("characters", characters):
        try:
            finished_character = character.create(content)
            finished_character.write_character_sheet(
                f"output/{finished_character.get_name()}.pdf")
        except AttributeError as exc:
            logging.error(
                "%s has not correctly implemented a create() method", character)
            raise AttributeError(
                f"{character} has not correctly implemented a create() method") from exc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a list of characters with the OneD&D rules and content "
                                                 "supplied by the sources.")

    parser.add_argument("characters", type=str, nargs="+",
                        help="A list of character python files to generate sheets for.")
    parser.add_argument("--sources", type=str, nargs="+",
                        help="A list of source python files to load content from. Order matters, as some sources "
                             "override other sources.", default=["srd", "odnd1", "odnd2"])

    args = parser.parse_args()
    main(**vars(args))
