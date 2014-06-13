# XCAssets Bundle Image Exporter

Short script for exporting images in .xcassets bundles to individual image files.

Particularly helpful since the current Xcode 6 Beta doesn't work with image bundles on iOS7

http://stackoverflow.com/questions/24063937/running-an-ios7-project-under-xcode-6-image-assets-dont-show-up
http://stackoverflow.com/questions/24063778/images-not-showing-in-ios-7-1-with-xcode-6-swift

## Usage

    usage: export_xcassets.py [-h] [-l] source destination

    positional arguments:
      source           Source .xcassets bundle directory to export
      destination      Destination directory to save images from the xcassets
                       bundle
    optional arguments:
      -h, --help       show this help message and exit
      -l, --lowercase  All output filenames are lowercase