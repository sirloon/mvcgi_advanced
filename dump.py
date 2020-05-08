import os

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

from biothings.utils.common import uncompressall

import biothings.hub.dataload.dumper


class MvcgiDumper(biothings.hub.dataload.dumper.LastModifiedHTTPDumper):

    SRC_NAME = "mvcgi_advanced"
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    SCHEDULE = None
    UNCOMPRESS = True
    SRC_URLS = [
        'https://www.cancergenomeinterpreter.org/data/cgi_biomarkers_latest.zip'
    ]
    __metadata__ = {
        "src_meta": {
            'license_url': 'https://www.cancergenomeinterpreter.org/faq#q11c',
            'licence': 'CC BY-NC 4.0',
            'url': 'https://www.cancergenomeinterpreter.org'
        }
    }

    def post_dump(self, *args, **kwargs):
        if self.__class__.UNCOMPRESS:
            self.logger.info("Uncompress all archive files in '%s'" %
                             self.new_data_folder)
            uncompressall(self.new_data_folder)
