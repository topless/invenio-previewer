# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""JS/CSS bundles for Previewer."""

from __future__ import absolute_import, print_function

from flask_webpackext import WebpackBundle

previewer = WebpackBundle(
    __name__,
    'assets',
    entry={
        'previewer_app': './js/invenio_previewer/app.js',
        'previewer_theme': './scss/invenio_previewer/theme.scss',
    },
    dependencies={
        'jquery': '~3.3.1',
        "bootstrap": '~3.3.6',
        "font-awesome": '~4.5.0',
        'd3': '^3.5.17',
        'flightjs': '~1.5.1',
        'pdfjs-dist': '1.4.192',
        'prismjs': '1.4.1'
    }
)
