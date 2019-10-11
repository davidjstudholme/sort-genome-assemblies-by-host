for i in */*rna_from_genomic.fna.gz ; do echo $i; rm "$i"; done
for i in */*cds_from_genomic.fna.gz ; do echo $i; rm "$i"; done
for i in */*_from_genomic*; do echo $i; rm "$i"; done
for i in */*.gz; do echo $i; gunzip "$i"; done


