#!/bin/bash
clear 

echo -n "Masukkan angka :"
read angka

if [ $angka -gt 70 ]
then
  echo " $angka adalah pertahankan"
elif [ $angka -lt 70 ]
then
  echo " $angka adalah jangan keseringan main"
elif [ $angka == 70 ]
then
  echo " $angka adalah harus lebih baik lagi"
else
  echo " $angka tidak sesuai"
fi
