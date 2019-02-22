# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013, 2014, 2015, 2016 CERN.
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

"""PDF previewer based on pdf.js."""

from __future__ import absolute_import, print_function

from flask import render_template

from ..proxies import current_previewer

previewable_extensions = ['pdf', 'pdfa']


def can_preview(file):
    """Check if file can be previewed."""
    return file.has_extensions('.pdf', '.pdfa')


def preview(file):
    """Preview file."""
    return render_template(
        'invenio_previewer/pdfjs.html',
        file=file,
        html_tags='dir="ltr" mozdisallowselectionprint moznomarginboxes',
        css_bundles=['pdfjs_css.css'],
        js_bundles=current_previewer.js_bundles + [
            'pdfjs_js.js',
            'fullscreen_js.js'
        ]
    )
