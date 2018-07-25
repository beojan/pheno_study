##Python script to Split HEPMC files ONCE and FOR ALL
#we split the hepmc file in 100 small files
numb_events=10000
with open("/data/atlas/atlasdata2/DiHiggsSharedSamples/high-stats-unboosted/SHERPA_QCD_4b.hepmc") as infile:
	events = 0
	for line in infile:
		if events == 0 :
			final= open("4b_split0.hepmc","w+")
			final.write("HepMC::Version 2.06.08\n")
        		final.write("HepMC::IO_GenEvent-START_EVENT_LISTING")
    		if line.startswith("HepMC::Version 2.06.08"):
			continue
   		if line.startswith("HepMC::IO_GenEvent-START_EVENT_LISTING"):
			continue
    		if line.startswith("E"):
			events+=1
    		if events% numb_events==0 and events !=0 :
			final.write("HepMC::IO_GenEvent-END_EVENT_LISTING")
			final.close()
			file_count = events/numb_events
        		final= open("4b_split%d.hepmc" % file_count,"w+")
			final.write("HepMC::Version 2.06.08\n")
        		final.write("HepMC::IO_GenEvent-START_EVENT_LISTING")
    		print "Writing to", final.name
    		final.write(line)	
    		if line.startswith("H"):
			final.close()
        		break

infile.close()
