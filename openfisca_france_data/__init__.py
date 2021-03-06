# -*- coding: utf-8 -*-


# Law-to-Code -- Extract formulas & parameters from laws
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2013 OpenFisca Team
# https://github.com/openfisca/LawToCode
#
# This file is part of Law-to-Code.
#
# Law-to-Code is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Law-to-Code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os


AGGREGATES_DEFAULT_VARS = [
    'cotsoc_noncontrib',
    'csg',
    'crds',
    'irpp',
    'ppe',
    'ppe_brute',
    'af',
    'af_base',
    'af_majo',
    'af_forf',
    'cf',
    'paje_base',
    'paje_nais',
    'paje_clca',
    'paje_clmg',
    'ars',
    'aeeh',
    'asf',
    'aspa',
    'aah',
    'caah',
    'rsa',
    'rsa_act',
    'aefa',
    'api',
    'majo_rsa',
    'psa',
    'logt',
    'alf',
    'als',
    'apl',
    ]
    # ajouter csgd pour le calcul des agrégats erfs
    # ajouter rmi pour le calcul des agrégats erfs
COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))
FILTERING_VARS = ["champm"]
PLUGINS_DIR = os.path.join(COUNTRY_DIR, 'plugins')
WEIGHT = "wprm"
WEIGHT_INI = "wprm_init"


def preproc_inputs(self, datatable):
    """Preprocess inputs table: country specific manipulations

    Parameters
    ----------
    datatable : a DataTable object
                the DataTable containing the input variables of the model

    """
    try:
        datatable.propagate_to_members(WEIGHT, 'ind')
    #    datatable.propagate_to_members('rfr_n_2', 'ind')
    #    datatable.propagate_to_members('nbptr_n_2', 'ind')
    except:
        pass