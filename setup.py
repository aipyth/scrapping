import setuptools

setuptools.setup(
    name='scrapping',
    version='0.1.dev',
    author='Ivan Zhytkevych',
    author_email='ipython10@gmail.com',
    description='Simple multitoolable web scrapper',

    packages=setuptools.find_packages(),
    install_requires=['user-agent>=0.1.9', 'requests>=2.22.0', 'lxml>=4.3.4', 'bs4'],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
