#!/bin/sh


source /cvmfs/sft.cern.ch/lcg/views/dev4/latest/x86_64-slc6-gcc7-opt/setup.sh
rm -rf build;mkdir build;cd build; cmake.. ;make

echo "Done"
