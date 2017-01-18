ICE-ARC project where AVHRR GAC records are used to derive
sea ice concentration (SIC) in the Arctic Region.

The AVHRR based SIC retrievals are used to validate the SIC values derived from the passive microwave satellite observations

This project is modular, where different methodologies can be used to derive sea ice concentration values.

"features" folder contains actual recipes for processing the data
and for selecting the methodologies

"tests" is just regression unit tests

To run behaviour test suit do:
    ansible-playbook -i ansible/hosts ansible/playbook.yml --limit='local' --tags='tests' --extra-vars='base_dir=/path/to/project'
Where 'local' is an alias of your local machine, defined in the 'ansible/hosts' file

Read documentation [here](docs/source/quickstart.rst)
