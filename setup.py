#!/usr/bin/env python
from setuptools import setup
import os


# Utility function to read README.md file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name="django-membersuite-auth",
      version="0.1",
      description="Django Authentication By MemberSuite",
      author=("Association for the Advancement of Sustainability in "
              "Higher Education"),
      author_email="webdev@aashe.org",
      url="https://github.com/AASHE/django-membersuite-auth",
      long_description=read("README.md"),
      packages=[
          "django_membersuite_auth",
          "django_membersuite_auth.migrations",
          "django_membersuite_auth.templates"
      ],
      classifiers=[
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Framework :: Django"
      ],
      include_package_data=True,
      install_requires=["django",
                        "future",
                        "python-membersuite-api-client"],
      dependency_links=["https://github.com/AASHE/"
                        "python-membersuite-api-client.git#"
                        "egg=python-membersuite-api-client.egg"])
