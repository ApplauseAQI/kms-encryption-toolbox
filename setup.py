from setuptools import find_packages
from setuptools import setup

setup(
    name='kms-encryption-toolbox',
    version='0.0.1',
    url='https://github.com/ApplauseOSS/kms-encryption-toolbox',
    license='Applause',
    description='Encryption toolbox to be used with the Amazon Key Management Service for securing your deployment secrets. It encapsulates the aws-encryption-sdk package to expose cmdline actions.',
    author='Applause',
    author_email='architecture@applause.com',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
        'aws-encryption-sdk>=1.2.0',
        'click>=6.6',
        'attrs>=16.3.0,<17.0.0'
    ],
    entry_points={
        "console_scripts": [
            "kms-encryption = kmsencryption.__main__:main",
        ]
    },
    scripts=["kmsencryption/scripts/decrypt-and-start.sh"]
)
