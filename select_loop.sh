#!/bin/bash

select minuman in teh kopi air jus susu gaada
do
  case $minuman in
    teh|kopi|air|semua)
      echo "Maaf, habis"
      ;;
      gaada)
        break
      ;;
      *) echo "Tidak ada di daftar menu"
      ;;
  esac
done
