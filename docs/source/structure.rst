=================
Project structure
=================

.. code-block:: bash

   .
   ├── ansible #-------------------------- Deployment playbooks
   ├── codeshop
   │   ├── behave.ini #------------------- Integration tests configuration
   │   └── compute_sic #------------------ Directory where processing scripts reside
   │       ├── areas.cfg #---------------- File with area definitions
   │       ├── calc_coeff.py #------------ Calculate montly coefficients for tie points selection
   │       ├── compute_sic.py #----------- Process resampled AVHRR files and compute SIC
   │       ├── README.md
   │       ├── resample_gac.py #---------- Resample swath data to NSIDC grid
   │       └── resources 
   │           └── land_mask.npz #-------- Landmask extracted from OSI SAF data
   ├── docs #----------------------------- Documentation
   ├── env
   │   └── lustre-env.sh #---------------- Environment configuration file
   ├── features #------------------------- Integration tests
   ├── notebooks #------------------------ Post-processing and analysis notebooks
   │   ├── compare_osisaf_gac.ipynb
   │   ├── modis_analysis.ipynb
   │   └── trend_analysis.ipynb
   ├── README
   ├── scripts
   │   ├── calc_coeff.sh #---------------- Batch job to process one month of data
   │   ├── compute_sic.sh #--------------- Batch job to process one month of data
   │   ├── process_batch.sh #------------- Batch job to process one month of data
   │   └── resample_gac.sh #-------------- Batch job to process one month of data
   ├── sge
   │   ├── list.2008.txt #---------------- List of all available satellites for that year
   │   ├── run-sge.sh #------------------- Script for submitting SGE jobs
   │   ├── single_sat_list.1982.txt #----- what satellite to use for that year
   │   └── total-list.1982-2008.txt #----- complete list of satellites/years
   └── Vagrantfile

.
