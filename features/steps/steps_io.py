from behave import *
import os
import yaml
from pypps_reader import NwcSafPpsData
import numpy
import netCDF4

@given(u'the project deployed using Ansible')
def step_impl(context):
    # check there is an Ansible directory
    assert context.ansible_basedir
    assert context.playbook_path


@then(u'there should be a playbook sitting in the Ansible directory')
def step_impl(context):
    # Check there is a readable playbook in the Ansible directory
    assert context.playbook[0]['vars']['test_date']


@when(u'data storage is avaiable')
def step_impl(context):
    assert context.ansible_basedir
    assert context.playbook
    assert os.path.exists(context.local_gac_dir)

@then(u'it contains NOAA GAC satellite data')
def step_impl(context):
    # form year from test date
    year = context.test_date.strftime('%Y')
    date = context.test_date.strftime('%Y%m%d')
    data_dir = os.path.join(context.local_gac_dir, year, date)
    assert os.path.exists(data_dir)
    context.data_dir = data_dir

    # list data directory contents and check whether it contains all
    # necessary information
    file_list = os.listdir(data_dir)
    assert file_list is not None

    angles = filter(lambda x: 'sunsatangles' in x, file_list)
    cloudtypes = filter(lambda x: 'cloudtype' in x, file_list)
    avhrr = filter(lambda x: 'avhrr' in x, file_list)
    cloudmask = filter(lambda x: 'cloudmask' in x, file_list)

    context.avhrr_file_list = avhrr

    assert all([angles, cloudmask, cloudtypes, avhrr])


@then(u'the AVHRR data can be read using pypps_reader')
def step_impl(context):

    avhrr_data_file = os.path.join(context.data_dir, context.avhrr_file_list[0])
    avhrr_data_ch1 = NwcSafPpsData(avhrr_data_file).image1.data
    # make sure the data is for the same date as the test_date
    # XXX ugly fugly
    assert context.test_date.strftime('%Y%m%d') == NwcSafPpsData(avhrr_data_file)._what['time_slot'].strftime('%Y%m%d')
    assert isinstance(avhrr_data_ch1, numpy.ndarray)

@then(u'the OSI SAF data can be read')
def step_impl(context):
    sic_data_path = context.sic_data_path
    sic_file_list = os.listdir(sic_data_path)
    sic_data = netCDF4.Dataset(os.path.join(sic_data_path, sic_file_list[0]))
    assert isinstance(sic_data.variables['ice_conc'][:], numpy.ndarray)

@given(u'the playbook contains SIC data path and is not empty')
def step_impl(context):
    context.sic_data_path = context.local_sic_dir
    assert os.path.exists(context.sic_data_path)
    assert any(os.listdir(context.sic_data_path))
