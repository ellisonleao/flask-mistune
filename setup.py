# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='Flask-Mistune',
    version='0.1.1',
    url='https://github.com/ellisonleao/flask-mistune/',
    license='MIT',
    author=u'Ellison Leão',
    author_email='ellisonleao@gmail.com',
    description=u'A interface between the Flask web framework and the Mistune'
    u' Markdown parser.',
    zip_safe=False,
    packages=find_packages(),
    py_modules=['flask_mistune'],
    install_requires=[
        'Flask>=0.7',
        'mistune',
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
