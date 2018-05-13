import re
from setuptools import setup, find_packages, Extension

def get_version(project_name):
    regex = re.compile(r"^__version__ = '(\d+\.\d+\.\d+)'$")
    with open(f"{project_name}/__init__.py") as f:
        for line in f:
            m = regex.match(line)
            if m is not None:
                return m.groups(1)[0]

class About(object):
    NAME='string_distance'
    VERSION=get_version(NAME)
    AUTHOR='blester125'
    EMAIL=f'{AUTHOR}@gmail.com'
    URL=f'https://github.com/{AUTHOR}/{NAME}'
    DL_URL=f'{URL}/archive/{VERSION}.tar.gz'
    LICENSE='MIT'


ext_modules = [
    Extension(
        "string_distance.minimum_edit_distance",
        ["string_distance/minimum_edit_distance.pyx"]
    ),
    Extension(
        "string_distance.maximum_edit_distance",
        ["string_distance/maximum_edit_distance.pyx"]
    ),
    Extension(
        "string_distance.edit_distance",
        ["string_distance/edit_distance.pyx"],
    ),
    Extension(
        "string_distance.float_minimum_edit_distance",
        ["string_distance/float_minimum_edit_distance.pyx"]
    ),
    Extension(
        "string_distance.float_edit_distance",
        ["string_distance/float_edit_distance.pyx"]
    ),
    Extension(
        "string_distance.sequence_distance",
        ["string_distance/sequence_distance.pyx"]
    ),
    Extension(
        "string_distance.token_distance",
        ["string_distance/token_distance.pyx"]
    ),
]


setup(
    name=About.NAME,
    version=About.VERSION,
    description="Minimum Edit Distance",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author=About.AUTHOR,
    author_email=About.EMAIL,
    url=About.URL,
    download_url=About.DL_URL,
    license=About.LICENSE,
    packages=find_packages(),
    package_data={
        'string_distance': [
            'README.md',
            'string_distance/cost.pxd',
            'string_distance/edit_distance.c',
            'string_distance/minimum_edit_distance.c',
            'string_distance/minimum_edit_distance.pxd',
            'string_distance/maximum_edit_distance.c',
            'string_distance/maximum_edit_distance.pxd',
            'string_distance/float_cost.pxd',
            'string_distance/float_edit_distance.c',
            'string_distance/float_minimum_edit_distance.c',
            'string_distance/float_minimum_edit_distance.pxd',
            'string_distance/sequence_distance.c'
            'string_distance/sequence_distance.pxd',
            'string_distance/token_distance.c'
        ],
    },
    include_package_data=True,
    install_requires=[
        'cython',
    ],
    setup_requires=[
        'cython',
    ],
    extra_requires={
        'test': ['pytest'],
    },
    keywords=[],
    ext_modules=ext_modules
)
