#!/bin/bash


if [ -n "${1}" ]; then
   case ${1} in 
      new)
         screen -list
         echo -n "Please enter the name of the new screen: "
         read SCREEN_NAME
         export SCREEN_NAME
         screen -l -h 100000 -S ${SCREEN_NAME}
      ;;
      *)
         export SCREEN_NAME="${1}"
         screen -r ${1}
      ;;
   esac
else
   which=`screen -list |grep Detached|head -1|awk '{print $1}' |sed -e 's/ //g'`
   if [ -n "${which}" ]  ; then
          echo "Attaching to ${which}"
          screen -r ${which}
   else
      screen -list
      echo -n "Please enter the name of the new screen: "
      read SCREEN_NAME
      export SCREEN_NAME
      screen -l -h 100000 -S ${SCREEN_NAME}
   fi
fi
name of the new screen: "
      read SCREEN_NAME
      export SCREEN_NAME
      screen -l -h 100000 -S ${SCREEN_NAME}
   fi
fi
