from setuptools import setup, find_packages


setup(name='klondike',
      version='1.0',
      description='klondike for XP',
      packages=find_packages(),
      test_suites="nose.collector",
      test_dependencies=['nose']
      )
