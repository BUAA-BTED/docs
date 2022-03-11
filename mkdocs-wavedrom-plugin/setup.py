from setuptools import setup, find_packages


setup(
    name='mkdocs-wavedrom-plugin',
    version='0.1.0',
    python_requires='>=3.6',
    install_requires=['mkdocs>=1', 'beautifulsoup4>=4.6.3'],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'markdownwavedrom=markdownwavedrom.plugin:MarkdownWavedromPlugin'
        ]
    }
)
