==========
Quickstart
==========

Assuming the work is being done on the Post Processing Infrastructure (PPI), these are the steps necessary to do the processing:

Get repository:

.. code-block:: bash

   git clone https://github.com/metno/icearc-avhrr-sic

Install dependencies assuming you have rights to write into the python package folder (e.g. you use virtualenv [and you should]):

.. code-block:: bash

   cd icearc-avhrr-sic
   pip install -r requirements.txt

.. important::
    NB: On PPI systems you need to load some software modules that may not be available by default, e.g.: fyba, hdf, netcdf

.. code:: bash

    module load fyba hdf netcdf

Source environment variable:

.. code:: bash

   source ./env/lustre.env

First the analysis is based on the resampled data. That allows to save a massive amount of processing time at later stages.
Also, the reflectance data is corrected here for the sun elevation.

Make sure you check two parameters in the :code:`run-sge.sh` file:

.. code:: bash

    PREFIX='10k'
    #$ -t 200505-200509

:code:`PREFIX` variable tells what ID to prepend to output directories, so different versions of the product can be created. Edit the :code:`-t` flag value to select which dates to process. It can be either a range or a list of months.

The jobs array is implemented in such way that processing is split by months, each computing node is processing a single month of data at a time.

Submit resampling job to SGE
----------------------------

.. code:: bash

    qsub ../sge/run-sge.sh ./scripts/resample-gac.sh

The analysis is based on the knowledge of AVHRR Channel 1 reflectance distribution, therefore we need to collect statistics first.

Submit coefficients computation job to SGE
------------------------------------------

.. code:: bash

    qsub ./sge/run-sge.sh ./scripts/resample-gac.sh

Monthly aggregation
-----------------------------

Once the coefficients are available, it's possible to compute sea ice concentration in the same manner:

.. code:: bash

    qsub ./sge/run-sge.sh ./scripts/compute-cdo.sh

