# SortGenomeAssembliesByHost
Download bacterial genome assemblies and sort into folders according to BioProject 'host' field

## The problem I want to solve:
I wanted to mine for some patterns in *Staphylococcus aureus* genome sequences that associate with the host from which the bacteria were isolated.
The URLs for each genome assembly are available in this file: https://ftp.ncbi.nih.gov/genomes/genbank/bacteria/Staphylococcus_aureus/assembly_summary.txt.
This file does not contain metadata such as host of isolation. However, this file does specify a BioSample for each Assembly and that metadata is held in the BioProject. We can download this metadata as an XML file from the NCBI's FTP site. Or we can download a simple flatfile from the NCBI's web interface.

So, the steps that this script performs are:
* Parse Assembly summary file
* Parse BioProject summary file
* Map Assemblies to BioProjects
* Infer host for each assembly
* Download each assembly into a directory whose name indicates the host

## Usage

```python ./parse_biosample_txt.py > assemblies-and-bioprojects.csv```

The script expects to find two input files in the working directory: ```biosample_result.txt``` and ```assembly_summary.txt```.
The first of these can be generated using the "Send to file" function on the NCBI's BioProject we page. For example: at https://www.ncbi.nlm.nih.gov/biosample/?term=Staphylococcus+aureus, click on "Send to file" and select "Text (full)" as the Format.  
The latter can be downloaded from the NCBI's FTP site, e.g. https://ftp.ncbi.nih.gov/genomes/genbank/bacteria/Staphylococcus_aureus/assembly_summary.txt

As well as generating a tab-delimited table listing assemblies and some of their associated BioSample metadata, the script also uses wget to download the assembly data from NCBI:

```
$ ls

Animal                          Chicken (Hen)               Human (neonate)               pheasant
assemblies-and-bioprojects.csv  cow                         kangaroo                      pig
assembly_summary.txt            Cow                         laboratory mouse              Pig
Avian (bird)                    cow with bovine mastitis    Lamb                          pigs
biosample_result.txt            dog                         macaque                       Rabbit
biosample_result.txt~           environmental               Meleagris gallopavo           Rattus
blank vole                      Equus caballus              missing                       ribbon fish
Bos taurus                      Equus ferus caballus        Mus musculus C3H              Rodentia
Bos taurus (cow)                feline                      NA                            sheep
bovine                          Felis catus                 not applicable                Sheep
Bovine                          field vole                  Not applicable                Sheep (Ewe)
canine                          Gallus gallus               not available                 Sus scrofa
Canis lupus familiaris          Globicephala macrorhynchus  not available: not collected  Sus scrofa domesticus
Capra pyrenaica                 Gyps fulvus                 Oryctolagus cuniculus         swine
Caprine                         Hen                         Ovine                         Swine
cat                             Homo sapiens                Ovis aries                    unknown
Cat                             Homo sapiens newborn        parse_biosample_txt.py
cattle                          horse                       parse_biosample_txt.py~
Cervus elaphus                  Human (Infant)              partridge
```

It is necessary to gunzip the downloaded files, which are downloaded as .fna.gz and .gbff.gz files.


