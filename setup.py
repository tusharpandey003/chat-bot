from setuptools import find_packages, setup


setup(
    name='Medical chatbot',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version<"3.10"',
    ],
)
