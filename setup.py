from setuptools import setup, find_packages

setup(
    name='examplepip',
    version='1.0.1',
    description='example for practice',
    author='The Python Packaging Authority',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages('examplepip'),
    install_requires=['Flask-SQLAlchemy==2.2'],
    python_requires='>=2.6, <3',
)
