#! /usr/bin/env python
# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import logging
from openfisca_france_data.surveys import Survey, SurveyCollection

log = logging.getLogger(__name__)


def build_empty_eipp_survey_collection(years= None):

    if years is None:
        log.error("A list of years to process is needed")

    base_eipp_survey_collection = SurveyCollection(name = "eipp")
    base_eipp_survey_collection.set_config_files_directory()
    input_data_directory = base_eipp_survey_collection.config.get('data', 'input_directory')
    output_data_directory = base_eipp_survey_collection.config.get('data', 'output_directory')

    tables = ["base"]
    eipp_tables = dict()
    for year in [2011,2012]:
        for table in tables:
            eipp_tables[table] = {
                "stata_file": os.path.join(
                    os.path.dirname(input_data_directory),
                    "fichiers_eipp",
                    "{}_{}.dta".format(table, year),
                    ),
                "year": year,
                }

        survey_name = u"eipp_{}".format(year)
        hdf5_file_path = os.path.join(
            os.path.dirname(output_data_directory),
            u"{}{}".format(survey_name, u".h5")
            )
        survey = Survey(
            name = survey_name,
            hdf5_file_path = hdf5_file_path
            )
        for table, table_kwargs in eipp_tables.iteritems():
            survey.insert_table(name = table, **table_kwargs)
        surveys = base_eipp_survey_collection.surveys
        surveys[survey_name] = survey
    return base_eipp_survey_collection


if __name__ == '__main__':
    import logging
    import sys
    import datetime
    start_time = datetime.datetime.now()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    eipp_survey_collection = build_empty_eipp_survey_collection(
        years = [2011,2012],
        )
    eipp_survey_collection.fill_hdf_from_stata(surveys_name = ["eipp_2011"])
    eipp_survey_collection.fill_hdf_from_stata(surveys_name = ["eipp_2012"])
    eipp_survey_collection.dump(collection = u"eipp")
    log.info("The program have been executed in {}".format( datetime.datetime.now()-start_time))
    
    