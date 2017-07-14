#!/bin/bash
export LD_LIBRARY_PATH=/home/$(whoami)/Dropbox/dataENF/blmg/blpapi_cpp_3.8.18.1/Linux

if [[ $# -eq 0 ]]
then
      echo "arg 1 : securityList"
      exit
else
    securityList=$1
fi

OUTPUTFOLDER=$(date +'%Y%m%d')"_GMT"
if [[ ! -d $OUTPUTFOLDER ]]
then
    mkdir $OUTPUTFOLDER
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    if [[ -n $line ]]
    then
        echo $line
        ADJ="false"
        # ADJ="true"
        python bbgDownloadIntradayBar.py -s"$line" --adjusted $ADJ > $OUTPUTFOLDER/"$(echo $line | awk '{print $1}')".csv
    fi
done < "$securityList"
