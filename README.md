# SortGenomeAssembliesByHost
Download bacterial genome assemblies and sort into folders according to BioProject 'host' field

## The problem I want to solve:
I wanted to mine for some patterns in *Staphylococcus aureus* genome sequences that associate with the host from which the bacteria were isolated.
The URLs for each genome assembly are available in this file: https://ftp.ncbi.nih.gov/genomes/genbank/bacteria/Staphylococcus_aureus/assembly_summary.txt.
This file does not contain metadata such as host of isolation. However, this file does specify a BioSample for each Assembly and that metadata is held in the BioProject. We can download this metadata as an XML file from the NCBI's FTP site. Or we can download a simple flatfile from the NCBI's web interface.

So, the stepts that this script performs are:
* Parse Assembly summary file
* Parse BioProject summary file
* Map Assemblies to BioProjects
* Infer host for each assembly
* Download each assembly into a directory whose name indicates the host



