# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier (Camptocamp)
#    Author: Vincent Renaville
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Timesheet Fullfill Wizard',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'description': '''
Add a wizard into timesheet allowing people to complete a long period of
time with the given values. This is mainly useful to handle a long period of
time like holidays.

Known limitation:
- Will complete all day between dates
    ''',
    'author': "Camptocamp,Odoo Community Association",
    'website': 'http://camptocamp.com',
    'depends': ['hr_timesheet_sheet',
                'project',
                ],
    'data': ['wizard/timesheet_fulfill_view.xml',
             ],
    'demo': [],
    'test': ['test/timesheet_fulfill.yml',
             ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
