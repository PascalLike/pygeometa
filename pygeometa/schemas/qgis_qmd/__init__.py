# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution # is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2023 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import ast
import logging
import os

from lxml import etree
from owslib.iso import CI_OnlineResource, CI_ResponsibleParty, MD_Metadata

from pygeometa.schemas.base import BaseOutputSchema

LOGGER = logging.getLogger(__name__)
THISDIR = os.path.dirname(os.path.realpath(__file__))


class QMDSchema(BaseOutputSchema):
    """QGIS QMD output schema"""

    def __init__(self):
        """
        Initialize object

        :returns: pygeometa.schemas.base.BaseOutputSchema
        """

        super().__init__('qmd', 'xml', THISDIR)

    def import_(self, metadata: str) -> dict:
        """
        Import metadata into MCF

        :param metadata: string of metadata content

        :returns: `dict` of MCF content
        """

        mcf = {
            'mcf': {
                'version': '1.0',
            },
            'metadata': {},
            'identification': {},
            'contact': {},
            'distribution': {}
        }

        LOGGER.debug('Parsing QMD metadata')

        LOGGER.debug('Setting metadata')

        LOGGER.debug('Setting language')

        LOGGER.debug('Setting identification')

        LOGGER.debug('Setting contacts')

        LOGGER.debug('Setting distribution')

        return mcf

