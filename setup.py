from setuptools import setup

setup(
    name='EgoisticLily',
    version='0.0.1',
    packages=['egoisticlily', 'egoisticlily.modelmaker'],
    install_requires=["tensorflow>=2.0", "numpy", "marisa-trie"],
    url='',
    license='MIT',
    author='Hashimoto Masahiko',
    author_email='hashimom@geeko.jp',
    entry_points={
        "console_scripts": [
            "egoisticlily = egoisticlily.converter:main",
        ],
    },
    description=''
)
