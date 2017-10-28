from setuptools import setup

setup(
    name="Cobra",
    version="0.1.0",
    description="Python event library.",
    author='TechneLogos',
    maintainer='Roy Stewart',
    maintainer_email='roythomasstewart@gmail.com',
    url='https://github.com/TechneLogos/PyEvents',
    license='GPL3.0',
    packages=["cobra"],
    long_description=open("docs/README.md").read(),
    classifiers=[
        #'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)