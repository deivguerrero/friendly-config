from distutils.core import setup
setup(
  name = 'friendly-config',
  version = '0.0.2',
  author = 'David Guerrero Morales',
  author_email = 'deivguerrero@gmail.com',
  description='Simple wrapper for yaml files',
  license= 'MIT',
  packages=['config'],
  install_requires=['PyYAML==3.12'],
  url='https://github.com/deivguerrero/friendly-config.git',
  download_url='https://github.com/deivguerrero/friendly-config/tarball/0.0.2',
  keywords=['configuration', 'yaml'],
  classifiers = [
      'Development Status :: 0.0.2 - Alpha',
      'License :: MIT License',
      'Programming Language :: Python :: 3.6.4',
      'Topic :: Utilities'
  ],
)
