#! /bin/bash

nodes=$(openstack baremetal node list -c UUID -f value)
for node in $nodes
do
    openstack baremetal node delete ${node}
done

networks=$(openstack network list -c ID -f value)
for network in $networks
do
    openstack network delete ${network}
done
