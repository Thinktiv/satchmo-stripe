from setuptools import setup, find_packages

VERSION = (1, 0, 2)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='satchmo-stripe',
    version=__version__,
    description='Stripe Integration with Satchmo',
    long_description=open('README.md').read(),
    author='Sahil Kalra',
    author_email='sahil.kalra@joshworkz.com',
    url='https://github.com/Thinktiv/satchmo-stripe',
    download_url='https://github.com/Thinktiv/satchmo-stripe/downloads',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "stripe==1.9.5",
        "Django>=1.4.2",
        "Satchmo==0.9.3",
        "South==0.8.2"
    ],
)
