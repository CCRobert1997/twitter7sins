. ./openrc.sh

sleep 20

#ping check all instances (also add the keys)
ANSIBLE_HOST_KEY_CHECKING=False ansible all -i hosts -m ping

#For all instances, mount volumn and install basic packages
ansible-playbook -i hosts playbook/basic.yml

#For db instances, install couchdb cluster
ansible-playbook -i hosts playbook/couchdb.yml

#For db instances, install and run harvester
ansible-playbook -i hosts playbook/harvester.yml

#For web instances, install and run webserver
ansible-playbook -i hosts playbook/webserver.yml