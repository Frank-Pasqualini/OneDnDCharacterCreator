import argparse
import logging
import pkgutil
import sys

import mergedeep

# ENABLE DEBUG LOG FOR NOW
logging.basicConfig(level=logging.DEBUG)


def load_all_content_files(directory: str, packages: list[str]):
    """Takes a list of filenames and attempts to load."""

    package_importers = {}
    for importer, package_name, _ in pkgutil.iter_modules([directory]):
        package_importers[package_name] = importer

    for package in packages:
        importer = package_importers[package]
        full_package_name = f"{directory}.{package})"
        if full_package_name not in sys.modules:
            module = importer.find_module(package).load_module(package)
            yield module


def main(characters, sources):
    logging.info(
        "Generating sheets for characters %s using sources %s", characters, sources)

    content = {}
    for source in load_all_content_files("sources", sources):
        mergedeep.merge(content, source.CONTENT)

    for character in load_all_content_files("characters", characters):
        finished_character = character.create(content)
        finished_character.write_character_sheet(
            f"output/{finished_character.get_name()}.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a list of characters with the OneD&D rules and content "
                                                 "supplied by the sources.")

    parser.add_argument('characters', type=str, nargs='+',
                        help='A list of character python files to generate sheets for.')
    parser.add_argument('--sources', type=str, nargs='+', help='A list of source python files to load content from.',
                        default=["srd", "odnd1", "odnd2"])

    args = parser.parse_args()
    main(args.characters, args.sources)
