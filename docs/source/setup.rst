=====
Setup
=====

Dependencies
============

NB: you can skip the system packages installation if you work on PPI

System packages (install with apt-get):

.. code-block:: bash

   python-tk

Before installing python packages it is recommended to create a Python virtual environment:

.. code-block:: bash

   # install Virtual Environment system wide, no need on PPI
   sudo apt-get install python-virtualenvironment

   # Create virtual environment called venv
   virtualenv venv    source venv/bin/activate # activate virtualenvironment

   # Upgrade pip, newest versions are able to bypass compiling packages locally
   # They install so called 'wheel' prebuilt packages
   pip install pip --upgrade

Python packages:

.. code-block:: bash

   numpy
   h5py
   matplotlib
   pyresample
   netCDF4
   scipy

Easiest way to install the dependencies is to:

.. code-block:: bash

   pip install -r ./codeshop/compute_sic/requirements.txt

