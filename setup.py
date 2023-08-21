from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in prismss_addon/__init__.py
from prismss_addon import __version__ as version

setup(
	name="prismss_addon",
	version=version,
	description="Prismss Addon",
	author="InshaSiS Techonologies",
	author_email="support@inshasis.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
