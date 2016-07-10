#!/bin/bash
export LD_LIBRARY_PATH=/home/$(whoami)/Dropbox/dataENF/blmg/blpapi_cpp_3.8.18.1/Linux

if [[ $# -eq 0 ]]
then
      echo "arg 1 : securityList"
      exit
else
    securityList=$1
fi

OUTPUTFOLDER=$(date +'%Y%m%d')
if [[ ! -d $OUTPUTFOLDER ]]
then
    mkdir $OUTPUTFOLDER
fi

while IFS='' read -r line || [[ -n "$line" ]]; do
    if [[ -n $line ]]
    then
        echo $line
        python bbgDownloadIntradayBar.py -s"$line" > $OUTPUTFOLDER/"$(echo $line | awk '{print $1}')".txt
    fi
done < "$securityList"
