from setuptools import setup, find_packages

setup(
    name='dazbo_commons',
    version='0.1.0',
    author='Darren Lester',
    author_email='derailed.dash@gmail.com',
    description='Handy utility code, such as coloured logging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/derailed-dash/dazbo_python_commons',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Development Status :: 4 - Beta', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
    install_requires=[
        # list of required packages
    ],
    extras_require={
        'dev': [
            'pytest>=5.4',
            'check-manifest',
            'twine',
        ],
    },
)
