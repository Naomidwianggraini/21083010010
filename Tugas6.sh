#!/bin/bash

declare -a arrayIPSMahasiswa

printf "Jumlah Input :"
read n

for ((i=0; i<n; i=i+1))
do
    read arrayIPSMahasiswa[$i]
done

for ((i=0; i<n; i=i+1))
do
    let IPS=IPS+arrayIPSMahasiswa[i]
done

printf "\nIPS mhs : %i / %i\n" $IPS $n

let IPK=IPS/n
printf "IPK mhs : %i\n" $IPK
