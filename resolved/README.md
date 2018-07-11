In this folder we have the main code for the resolved Analysis



It is made of 3 files:
1) ```resolved-recon.cpp``` : the file where the actual analysis take place.
2) ```utils.h``` : the file where classes and utility functions used in the "resolved-recon.cpp" are defined and specified.
3) ```Cutflow.h```: the file where the structure for the Cutflow is determined.


I suggest to have the latest ROOT version running ( at the moment of writing ROOT 6.14) otherwise there might be some issues where with the RDataframes production or when reading the output file.

**MAIN SETTINGS**

The output file is called ```pheno_resolved.root``` and the name can be specified at the end of the ```resolved-recon.cpp``` file with ```std::string output_filename = "pheno_resolved.root";```.

The input file is defined in the initialisation of the RDataframe in the main function as :

```RDataFrame frame("Delphes", "/data/atlas/atlasdata/micheli/4b/Events/run_02/tag_1_delphes_events.root");```

** TO COMPILE AND RUN THE CODE**

You will need CMake running on your machine. Then

```
rm -rf build; mkdir build; cd build
```

We made the folder ```build``` where CMake will output the ```pheno_resolved.root``` file. 
In the ```build`` folder type,
```
cmake ..; make
```

If it compiles without error then you should be able to run

```
./resolved-recon
```
This will generate the output file ```pheno_resolved.root``` in the ```build``` folder.