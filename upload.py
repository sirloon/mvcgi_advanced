import os

import biothings, config
biothings.config_for_app(config)

import biothings.hub.dataload.uploader

# when code is exported, import becomes relative
try:
    from mvcgi.parser import load_data as parser_func
except ImportError:
    from .parser import load_data as parser_func


class MvcgiUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    name = "mvcgi"
    __metadata__ = {
        "src_meta": {
            'license_url': 'https://www.cancergenomeinterpreter.org/faq#q11c',
            'licence': 'CC BY-NC 4.0',
            'url': 'https://www.cancergenomeinterpreter.org'
        }
    }
    idconverter = None
    storage_class = biothings.hub.dataload.storage.IgnoreDuplicatedStorage

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return parser_func(data_folder)
