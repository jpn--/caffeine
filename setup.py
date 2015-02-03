from setuptools import setup

setup(
  name = 'caffeine',
  py_modules = ['caffeine'],
  version = '0.2',
  description = 'A tool to keep Mac OS X from sleeping',
  author = 'Jeffrey Newman',
  author_email = 'jeff@newman.me',
  url = 'https://github.com/jpn--/caffeine', 
  download_url = 'https://github.com/jpn--/caffeine', 
		  license = 'MIT',
		  classifiers = [
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Operating System :: MacOS :: MacOS X',
		  ],
  install_requires=["pyobjc-core >= 3.0.4",],
)