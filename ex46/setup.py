try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get ai at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'instal_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': ['bin/mathh.py'],
    'name': 'ex46'
}

setup(**config)
