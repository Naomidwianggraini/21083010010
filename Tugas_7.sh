#!/bin/bash

#mendeklarasikan fungsi
function panjang {
    echo "Masukan Panjang : "
    read panjang
}
function lebar {
    echo "Masukan Lebar : "
    read lebar
}
function luas {
     let luas=$panjang*$lebar
     echo -e "Luas Persegi : \n$luas"
}

#memanggil fungsi
panjang 
lebar
luas
