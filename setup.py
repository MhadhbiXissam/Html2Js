from setuptools import setup, find_packages


setup(
    name='Html2Js',
    version='1.0',
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

)