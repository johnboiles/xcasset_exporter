#!/usr/bin/env python

""" Script to export images from an .xcassets bundle
"""

import argparse
import os
import fnmatch
import json
import shutil


def export_asset_bundle(source, destination, lowercase=False):
    """Loops through all assets in the .xcassets bundle at source and copies all images to destination."""
    # TODO: App icons have a separate extension (.appiconset). They would also require additional logic to name
    #  correctly. Skipping those for now.
    for imageset in fnmatch.filter(os.listdir(source), '*.imageset'):
        print "Processing %s" % imageset
        # Load JSON
        imagesset_path = os.path.join(source, imageset)
        json_path = os.path.join(imagesset_path, 'Contents.json')
        imageset_json = json.load(open(json_path))
        for image in imageset_json['images']:
            imageset_name = imageset.split('.imageset')[0]
            if 'filename' in image:
                filename = image['filename']
                _, extension = os.path.splitext(filename)
                output_filename = imageset_name
                if image['scale'] == '2x':
                    output_filename += '@2x'
                output_filename += '%s' % extension
                if lowercase:
                    output_filename = output_filename.lower()
                source_path = os.path.join(imagesset_path, filename)
                destination_path = os.path.join(destination, output_filename)
                print "Copying %s to %s" % (source_path, destination_path)
                shutil.copyfile(source_path, destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Exports all images in an .xcassets bundle to the destination directory. Output files are named based on the image name in the .xcassets bundle.')
    parser.add_argument("source", help="Source .xcassets bundle directory to export")
    parser.add_argument("destination", help="Destination directory to save images from the xcassets bundle")
    parser.add_argument('-l', '--lowercase', help='All output filenames are lowercase', action='store_true')

    args = parser.parse_args()

    export_asset_bundle(args.source, args.destination, lowercase=args.lowercase)
