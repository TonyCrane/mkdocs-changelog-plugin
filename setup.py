import os
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path) as file:
        content = file.read()
    return content if content else 'no content read'


setup(
    name='mkdocs-changelog-plugin',
    version='0.1.3',
    author='TonyCrane',
    author_email='me@tonycrane.cc',
    description='A MkDocs plugin that create changelog in a page',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs python markdown changelog',
    url='https://github.com/TonyCrane/mkdocs-changelog-plugin',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    entry_points={
        'mkdocs.plugins': [
            'changelog = mkdocs_changelog_plugin.plugin:ChangelogPlugin'
        ]
    },
    include_package_data=True,
    package_data={
        'mkdocs_changelog_plugin': [
            'templates/*.html',
            'css/*.css',
        ]
    }
)
