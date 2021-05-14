#!/bin/bash

export ARUBA_SRC=`pwd`
upcase_image_type=$(echo $1 | tr '[a-z]' '[A-Z]') 
if [ x$1 != x ]
then
    echo "env set for $upcase_image_type buid"
    export $upcase_image_type=y
else
    echo "Error:missed image type,please input it"
fi
if [ x$2 != x ]
then
    echo "set LABELID to be $2"
    export LABELID=$2
fi
if [ x$3 != x ]
then
    echo "set peforce client to be $3"
    export P4CLIENT=$3
fi
export |grep P4CLIENT
export |grep ARUBA_SRC
export |grep LABELID
if [ x$1 != x ]
then
    export |grep $upcase_image_type
else
    echo "Error:missed image type,please input it"
fi

