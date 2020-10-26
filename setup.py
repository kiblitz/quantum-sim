
from setuptools import find_packages, setup

setup(
  name='quantSim',
  packages=find_packages(include=['quantSim']),
  version='0.1.0',
  description='Quantum computing simulator',
  license='MIT',
  install_requires=['typing'],
)
