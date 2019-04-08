# Kaveh Tehrani
# Small script for overnight backups to my remote drives.

import argparse
import os
import datetime
import shutil
import distutils.dir_util


def copy_directory(str_origin: str, str_destination: str, b_compress: bool = True) -> str:
    str_outpath = os.path.join(str_destination, datetime.datetime.now().strftime('%Y%m%d %H%M%S'))

    if b_compress:
        str_outpath = shutil.make_archive(str_outpath, 'zip', str_origin)
    else:
        distutils.dir_util.copy_tree(str_origin, str_outpath)

    return str_outpath


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--origin', help='original folder to copy')
    parser.add_argument('-d', '--destination', help='destination for backup')
    parser.add_argument('-c', '--compress', help='compress to copy as is')
    parser.set_defaults(compress=True)

    args = vars(parser.parse_args())
    print(args)

    str_outpath = copy_directory(args['origin'], args['destination'], args['compress'])

    print(f'Successfully copied {str_outpath} to {str_outpath}')
