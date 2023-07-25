#!/usr/bin/env python3
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='social_collage',
    version='0.9.3',
    packages=['social_collage'],
    description='Create image collages in social networks style',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/meequz/social_collage',
    author='Mikhail Varantsou',
    license='MIT',
    author_email='meequz@gmail.com',
    install_requires=['pillow'],
    keywords='collage ',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)
