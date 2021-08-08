#/bash
# a bash script to setup the environment for the project

# install pip3 and virtualenv
sudo apt-get install python3-pip -y

# create the virutual environment in the project root
pip3 install virtualenv
virtualenv -p python3 GTFS_2021

# activate the virtual environment
source GTFS_2021/bin/activate

# install packages you will need
pip3 install -r setup/requirements.txt