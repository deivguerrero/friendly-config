from distutils.core import setup
LATEST = '0.0.4'

setup(
  name='friendly-config',
  version=LATEST,
  description='Simple wrapper for yaml files',
  url='https://github.com/deivguerrero/friendly-config.git',
  author='David Guerrero Morales',
  author_email='deivguerrero@gmail.com',
  license='MIT',
  packages=[
    'mconfig',
    ],
  zip_safe=False,
  install_requires=[
    'PyYAML==3.12',
    ],
  download_url='https://github.com/deivguerrero/friendly-config/tarball/{}'.format(LATEST),
  keywords='configuration config yaml yml',
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Topic :: Utilities',
  ],
)
