from setuptools import setup, find_packages

setup(
    name='codegate-sandbox',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'python-dotenv==0.19.1',
    ],
)
