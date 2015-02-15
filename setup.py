import os

from setuptools import setup

ANGULAR_VERSIONS = ['1.2', '1.3', '1.4']
ANGULAR_PATHS = ['%s/*.*', '%s/i18n/*.*', '%s/i18n/ngLocale/*.*']


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "django-angular-static",
    version = "20150215",
    url = 'https://github.com/Alkemic/django-angular-static',
    license = 'MIT',
    description = "AngularJS (1.2, 1.3, 1.4) static files collection for Django",
    long_description = read('README.md'),

    author = 'Daniel Czuba',
    author_email = 'dc@danielczuba.pl',

    packages = ['angular'],
    package_data={'angular': [
        'static/angular/%s' % (dir % version) 
        for version in ANGULAR_VERSIONS 
        for dir in ANGULAR_PATHS
    ]},
    include_package_data=True,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
