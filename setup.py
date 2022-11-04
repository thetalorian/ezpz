from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ezpz',
    version="0.1",
    description='Easy Pan and Zoom',
    long_description=readme(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Image Processing :: Archival',
    ],
    keywords='tkinter canvas drag drop pan zoom',
    url='https://github.com/thetalorian/ezpz',
    author='Samuel Plum',
    author_email='splum@taloria.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'tk',
    ],
    #package_data={'': ['images/*']},
    #include_package_data=True,
    zip_safe=False)