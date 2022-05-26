from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='Html2js',
    version='1.4',
    license='MIT',
    author="Mhadhbi Issam",
    author_email='mhadhbixissam@gmail.com ',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/MhadhbiXissam/Html2Js',
    keywords='convert html to javascript code ( JSX like )',
    install_requires=[
          'beautifulsoup4','lxml'
      ],
    long_description=long_description,
    long_description_content_type='text/markdown'

)
