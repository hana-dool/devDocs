#!/usr/bin/env python3
# pip install coloredlogs verboselogs

import os
import coloredlogs, logging, verboselogs

#logger = logging.getLogger(__name__)
logger = verboselogs.VerboseLogger(__name__)    # add logger.success

log_path = 'train.log'

def main():
    # Write main code here
    pass


if __name__ == '__main__':
    """
    Initialise with NOTSET level and null device, and add stream handler separately.
    This way, the root logging level is NOTSET (log all), and we can customise each handler's behaviour.
    If we set the level during the initialisation, it will affect to ALL streams, so the file stream cannot be more verbose (lower level) than the console stream.
    """
    #logging.basicConfig(format='', level=logging.NOTSET, stream=open(os.devnull, 'w'))
    coloredlogs.install(fmt='', level=logging.NOTSET, stream=open(os.devnull, 'w'))

    # Different module different logging level
    #logging.getLogger('slowfast.utils.checkpoint').setLevel(logging.WARNING)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format  = coloredlogs.ColoredFormatter('%(name)s: %(lineno)4d - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)

    f_handler = logging.FileHandler(log_path)
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s - %(name)s: %(lineno)4d - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    root_logger = logging.getLogger()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(f_handler)

    try:
        main()
    except Exception:
        logger.exception("Exception occurred")