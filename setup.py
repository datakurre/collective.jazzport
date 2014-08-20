from setuptools import setup, find_packages


setup(
    name='collective.jazzport',
    version='0.1.0',
    description='A yet another Zip exporter for Plone content',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Plone :: 4.3',
    ],
    keywords='',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    url='https://source.kopla.jyu.fi/code/plone-packages/collective.jazzport',
    license='EUPL',
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
        'Products.CMFPlone',
        'futures',
        'plone.app.registry',
        'plone.app.vocabularies',
        'plone.registry',
        'plone.supermodel',
        'requests',
        'zope.component',
        'zope.interface',
        'zope.i18nmessageid',
        'zope.schema',
        # -*- Extra requirements: -*-
    ],
    extras_require={'test': [
        'unittest2',
        'plone.app.testing',
        'plone.app.robotframework',
    ]},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
