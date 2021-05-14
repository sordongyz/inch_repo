#!/bin/bash


PLATFORM_ALL="ARRAN ARDMORE TALISKER SPRINGBANK OCTOMORE X4 GLENLIVET MASTERSON KILCHOMAN AULTMORE GLENMORANGIE PORFIDIO GRAPPA MILAGRO";
unset BUILD_LIST;

for word in $PLATFORM_ALL;
       do 
           export|grep $word >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "Platform: $word "
           fi
        done
           export|grep "FAT_AP" >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "Type:IAP"
           else
                   echo "Type:AOS"
           fi
           echo "P4CLIENT:$P4CLIENT"
		   echo "ARUBA_SRC:$ARUBA_SRC"
		   echo "LABELID:$LABELID"
           export|grep "REGULATORY_TESTING" >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "REGULATORY_TESTING:YES"
           else
                   echo "REGULATORY_TESTING:NO"
           fi
           export|grep "ARUBA_MAKE_VERBOSE" >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "ARUBA_MAKE_VERBOSE:YES"
           else

                   echo "ARUBA_MAKE_VERBOSE:NO"
           fi
           export|grep "MANUFACTURING_BUILD" >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                  echo "MANUFACTURING_BUILD:YES"
          else 
                  echo "MANUFACTURING_BUILD:NO"
           fi
           export|grep "OEM" >/dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "OEM BUILD:YES"
           fi
           
           export |grep "USE_FAKE_SHA1_SIGNATURE" > /dev/null 2>&1;
           if [ $? -eq 0 ];
           then
                   echo "FAKE_SIGNATURE"
           fi
           
           
                   
