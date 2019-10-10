import re
import subprocess

class biosample:
    def __init__(self, title, host, sample_name, accession):
        self.host = host
        self.title = title
        self.sample_name = sample_name
        self.accession = accession
        
def parse_biosample(filepath):
    bs_title = ''
    bs_host = ''
    bs_accession = ''
    bs_sample_name = ''
    biosamples = []
    
    with open(filepath) as fp:
        for line in fp:
                
            p1 = re.compile('^\d+\:(.*)')
            match = p1.search(line)
            if match:
                
                ### This is the end of the previous BioSample, so print a summary of it
                #print bs_accession + ',' + bs_host + ',' + bs_sample_name + ',' + bs_title 
                bs = biosample(bs_title, bs_host, bs_sample_name, bs_accession)
                biosamples.append(bs)
                
                ### This is the beginning of a new BioSample entry
                bs_title = match.group(1).rstrip()

            p2 = re.compile('.*host="(.*)"')
            match = p2.search(line)
            if match:
                bs_host = match.group(1).rstrip()

            p3 = re.compile('.*sample name=(.*)')
            match = p3.search(line)
            if match:
                ### This is the sample name line
                bs_sample_name = match.group(1).rstrip()
            
            p4 = re.compile('BioSample: ([\w\d]+)')
            match = p4.search(line)
            if match:
                ### This is the accession line
                bs_accession = match.group(1).rstrip()

    return(biosamples)

class assembly:
    def __init__(self, assembly_accession, bioproject, biosample, wgs_master, refseq_category,
                 taxid, species_taxid, organism_name, infraspecific_name, isolate,
                 version_status, assembly_level, release_type, genome_rep, seq_rel_date,
                 asm_name, submitter, gbrs_paired_asm, paired_asm_comp, ftp_path):
        self.assembly_accession = assembly_accession
        self.bioproject = bioproject
        self.biosample = biosample
        self.wgs_master = wgs_master
        self.refseq_category = refseq_category
        self.taxid = taxid
        self.species_taxid = species_taxid
        self.organism_name = organism_name
        self.infraspecific_name = infraspecific_name
        self.isolate = isolate
        self.version_status = version_status
        self.assembly_level = assembly_level
        self.release_type = release_type
        self.genome_rep = genome_rep
        self.seq_rel_date = seq_rel_date
        self.asm_name = asm_name
        self.submitter = submitter
        self.gbrs_paired_asm = gbrs_paired_asm
        self.paired_asm_comp = paired_asm_comp
        self.ftp_path = ftp_path

def parse_assembly(filepath):
    assemblies = []
    with open(filepath) as fp:
        for line in fp:
            p1 = re.compile('\A\#')
            if p1.search(line):
                pass
            else:
                values = re.split('\t', line.rstrip())
                ass = assembly(*values[:20])
                assemblies.append(ass)
    return (assemblies)

### Parse the BioSamples file            
biosamples = parse_biosample('biosample_result.txt')

### Parse the assemblies file
assemblies = parse_assembly('assembly_summary.txt')

### Print the header line
print( 'biosample' + "\t" +
       'assembly_accession' + "\t" +
       'host' + "\t" +
       'bioproject' + "\t" +
       'infraspecific_name' + "\t" +
       'version_status' + "\t" +
       'genome_rep' + "\t" +
       'ftp_path'
)

### Now map assemblies to BioSamples
for bs in biosamples:
    #print bs.accession
    for ass in assemblies:
        #print ass.biosample
        if ass.biosample == bs.accession:
            print( bs.accession + "\t" +
                   ass.assembly_accession + "\t" +
                   bs.host + "\t" +
                   ass.bioproject + "\t" +
                   ass.infraspecific_name + "\t" +
                   ass.assembly_level + "\t" +
                   ass.version_status + "\t" +
                   ass.ftp_path
            )

            if ass.version_status == 'latest':
                print subprocess.call(["wget", "--no-clobber", '-P' + bs.host, ass.ftp_path + '/*genomic.fna.gz'])
                print subprocess.call(["wget", "--no-clobber", '-P' + bs.host, ass.ftp_path + '/*genomic.gbff.gz'])
            
    
