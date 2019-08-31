from setuptools import setup

requires = ['selenium']

setup(
    name='pairs_footprints_for_like',
    version='1.0',
    py_modules={'pairs_footprints_for_like'},
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'pairs_footprints_for_like = pairs_footprints_for_like:main',
        ],
    },
    license='BSD',
    author='mao2009',
    description='paris leave footprints fro like from me',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
