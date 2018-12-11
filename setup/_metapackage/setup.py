import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-hr-timesheet",
    description="Meta package for oca-hr-timesheet Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-hr_timesheet_role',
        'odoo12-addon-hr_timesheet_sheet',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
