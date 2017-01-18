Input data
==========

AVHRR GAC
---------

The input AVHRR data we process here is the AVHRR Global Area Coverage files prepared by Climate Monitoring SAF.
The data is provided at MET by the OSI SAF group and can be found at :code:`GACDIR=/lustre/storeA/project/fou/hi/normap2/gacrepr_v2/pps_v2`

Here is an example of the information provided for one swath:

.. code-block:: bash

   S_NWC_CT_noaa19_99999_20151115T2114571Z_20151115T2257416Z.h5
   S_NWC_CMAprob_noaa19_99999_20151115T2114571Z_20151115T2257416Z.h5
   S_NWC_CMA_noaa19_99999_20151115T2114571Z_20151115T2257416Z.h5
   S_NWC_sunsatangles_noaa19_99999_20151115T2114571Z_20151115T2257416Z.h5
   S_NWC_avhrr_noaa19_99999_20151115T2114571Z_20151115T2257416Z.h5

- The :code:`avhrr` file contains the actual measurements, six channels (5 measuring at a time).
- The :code:`sunsatangles` file contain information about the sun elevation and the sensor zenith angle
- The :code:`CMA` file contains cloud mask
- The :code:`CMAprob` file contains probabilities of the surface pixel being covered by cloud
- The :code:`CT` file contains the cloud types


Output data
===========

Each of the processing steps (resampling, calculation of coefficients, SIC computation, temporal aggregation) produces output files stored in the filesystem.
On PPI at MET Norway they can be found at:

.. code-block:: bash
   $ls /lustre/storeB/project/metkl/ice-arc/data$

   resampled-avhrr-gac-gacv2-4k #---- resampled original data
   sic-avhrr-gacv2-4k #-------------- SIC retrievals
   stats-gacv2-4k #------------------ binned files (daily and monthly)
   vis06-coeffs-gacv2-10k #---------- reflectance coefficients needed for the SIC retrieval

Ancillary data
==============

.. code-block:: bash
   $ ls codeshop/compute_sic/resources -1

   extent_mask_10k.npz
   extent_mask_4k.npz
   land_mask_10k.npz
   land_mask_4k.npz
   land_mask.npz
   LandOceanLakeMask_nh_ease2-250.nc

We use the same land mask and sea ice concentration extent mask as in the OSI SAF PMW sea ice concentration records. Details on the files can be found in the attributes of the :code:`LandOceanLakeMask_nh_ease2-250.nc` file.

The projections used in this project are placed in the area definition file which is used by the :code:`pyresample` module. 

.. code-block:: bash
   /lustre/storeB/users/mikhaili/icearc-avhrr-sic/codeshop/compute_sic/areas.cfg

.. code-block::
   REGION: nsidc_stere_south_10k {
       NAME: NSIDC Polar Stereographic South
       PCS_ID: nsidc_stere_south_10k
       PCS_DEF: proj=stere, lat_0=-90, lat_ts=-70, lon_0=0, k=1, x_0=0, y_0=0, a=6378273, b=6356889.449, units=m
       XSIZE: 790
       YSIZE: 830
       AREA_EXTENT: (-3950000.000,-3950000.000, 3950000.000, 4350000.000)
   };

   REGION: nsidc_stere_north_4k {
       NAME: NSIDC Polar Stereographic North
       PCS_ID: nsidc_stere_north_10k
       PCS_DEF: proj=stere, lat_0=90, lat_ts=70, lon_0=-45, k=1, x_0=0, y_0=0, a=6378273, b=6356889.449, units=m
       XSIZE: 1900
       YSIZE: 2800
       AREA_EXTENT: (-3850000.0, -5350000.0, 3750000.0, 5850000.0)
   };

