#!/bin/bash

info_memoire=$(free -m | grep Mem)
memoire_total=$(echo $info_memoire | awk '{print $2}')
memoire_utilise=$(echo $info_memoire | awk '{print $3}')
memoire_libre=$(echo $info_memoire | awk '{print $4}')
echo -e "memoire_total:$memoire_total'Mo \nmemoire_utilise:$memoire_utilise'Mo \nmemoire_libre:$memoire_libre'Mo"
