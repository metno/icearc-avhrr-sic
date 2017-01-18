==========
How to run
==========

Before executing any commands, make sure to source the environment configuration file which includes the workspace description (mainly path ot various directories).

.. code-block:: bash

   $ source ./env/lustre-env.sh

To make the processing system flexible and adaptable to differnt workspaces we have three levels of processing types:
 * Process single files (single swath/satellite)
 * Process monthly files (single month/single or multiple satellites)
 * Batch processing on Sun Grid Engine (multiple months or years and multiple satellites)


The first two methods are meant to be run interactively while the last on is optimized of the MET PPI infrastructure and relies on the Sun Grid Engine

Process single swath
--------------------

To process a single NOAA18 swath, do:

.. code-block:: bash

   python ./codeshop/compute_sic/resample_gac.py --input-file <swath_filepath>
							    --output-dir=<output_directory>
							    --sensor=avhrr_noaa18 
							    -a <path-to-dir-with-areas>/areas.cfg

The same is for the other scripts :code:`calc_coeff.py`, :code:`compute_sic.py`. For the list of arguments or optional parameters use :code:`-h` option.
However for convenience purposes it's better to use shell wrapper scripts, like :code:`./resample_gac.sh` which is a wrapper for the :code:`resample_gac.py`, the invocation command being:

Process one month of data
-------------------------

.. code-block:: bash

   ./scripts/resample_gac.sh noaa18 200808

Where `200808` is the the month to be process indicated in `%Y%m` format.
For submitting the jobs to Sun Grid Engine (SGE), do:

.. code-block:: bash

   qsub ./sge/run-sge.sh ./scripts/resample_gac.sh

Notice that the wrapper script :code:`resample_gac.sh` is passed as an argument to :code:`run-sge.sh`. The latter contains information necessary for the SGE to submit and spawn jobs. It will parse the contents of the files that contain satellites names, e.g. :code:`./sge/single_sat_list.2008.txt` and provide parameters required by SGE to launch the job.
