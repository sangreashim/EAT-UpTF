
![EAT-UpTF](https://user-images.githubusercontent.com/38829486/76416622-bf348080-63de-11ea-9fb0-b6bcb443d3f1.jpg)


# EAT-UpTF
Enrichment Analysis Tool for Upstream Transcription Factor of a gene set (EAT-UpTF) : conduct enrichment analysis of upstream transcription factor for a gene set of interest.

Currently, EAT-UpTF officially provide database only for Arabidopsis thaliana.

# Prerequisite
python3 (>= 3.6.8)

SciPy (>= 1.4.1)

Statsmodels (>= 0.11.1)

# Synopsis

<b>Upstream TF enrichment analysis:</b>

python3 EAT-UpTF.py --cistrome DAP_seq_default.txt --gene_group test_set_LHY_ChIPseq.txt --model HG --post_hoc fdr_bh --alpha 0.05 --alias gene_aliases_20140331.txt


<b>Transcriptional regulatory network:</b>

python3 network.py --cistrome DAP_seq_default.txt --gene_group test_set_LHY_ChIPseq.txt --TFs TFs.txt > TRN.txt

# Parameters for EAT-UpTF

  --cistrome file         
  database file of cistrome
  
  --gene_group file       
  file containing group of genes (new line delimited)
  
  --num_ref_genes int     
  No. of total genes in reference genome, 
  default=27206 for Arabidopsis thaliana
  
  --model str             
  statistical model: 
  HG=hypergeometric test, 
  BN=binomial test, 
  default=HG
  
  --post_hoc str          
  post hoc analysis: 
  bonferroni=Bonferroni family-wise error rate correction, 
  fdr_bh=Benjamini & Hochberg False Discover Rate correction, 
  default=fdr_bh
  
  --alpha float: 0<=x<=1  
  alpha in post hoc analysis, 
  default:0.05
  
  --output file           
  output file name
  
  --alias file           
  gene alias file, 
  default=NA,
  gene_aliases_20140331.txt file can be downloaded from TAIR webpage


# Trnascriptional regulatory network construction

  --cistrome 
  database file of cistrome 
  
  --gene_group 
  file containing group of genes (new line delimited)
  
  --TFs 
  file containing group of TFs (new line delimited AGI ID)
  
  <b>Subject output file (eg. TRN.txt) to cytoscape for construction of TRN.</b>
  
  
  # How to customize database
  
  EAT-UpTF conducts TF enrichment analysis based on the experimentally validated interaction between specific TF and its target genes. Interaction between TF and its targets (identified by ChIP-/DAP-seq) can be added manually as following example.
  
  <b>1. Annotate ChIP-/DAP-seq peaks based on the genome annotation for species of interest. </b>
  
	<b>command line: bedtools closest -a Athaliana_167_TAIR10.gene.bed (genome_annotation_BED_file) -b TF_A.narrowPeak (ChIP-/DAP-seq_peak_BED_file) -D a > TF_A.narrowPeak.annotation </b>

Example of TF_A.narrowPeak.annotation
	
	chr1    3631    5899    AT1G01010       .       +       chr1    20916   21117   1:21016 146     .       34.3    0.00    20.56   100     15018
	chr1    5928    8737    AT1G01020       .       -       chr1    20916   21117   1:21016 146     .       34.3    0.00    20.56   100     -12180
	chr1    11649   13714   AT1G01030       .       -       chr1    20916   21117   1:21016 146     .       34.3    0.00    20.56   100     -7203
	chr1    23146   31227   AT1G01040       .       +       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     -1912
	chr1    31170   33153   AT1G01050       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     9936
	chr1    33379   37871   AT1G01060       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     12145
	chr1    38752   40944   AT1G01070       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     17518
	chr1    44677   44787   AT1G01073       .       +       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     -23443
	chr1    45296   47019   AT1G01080       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     24062
	chr1    47485   49286   AT1G01090       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     26251
	chr1    50075   51199   AT1G01100       .       -       chr1    21034   21235   1:21134 113     .       9.7     0.00    2.07    100     28841


  <b>2. To annotate genes for ChIP-/DAP-seq peaks considering 1000 bp upstream and 500 bp downstream regions, following command needed. </b>
	
Output file contains gene IDs (fourth column) and distance from gene to peak in last column (17th column). To select genes carrying TF peaks within 1000 bp upstream and 500 bp downstream, following command line needed.
  

	command line: awk '$17<=500 && $17>=-1000' TF_A.narrowPeak.annotation | awk '$8!=-1 && $8!=-1' | cut -f 4 | sort -u | sed 's/$/\tAT5G65130 (TF_gene_ID)/' | paste - - | cut -f 2,3 > TF_A.narrowPeak.u1000_d500.annotation </b>



TF_A.narrowPeak.u1000_d500.annotation file contains TF and target gene ID for first and second columns, respectively. The two columns must be delimited by <b>TAB</b>.

--------------------------- TF_A.narrowPeak.u1000_d500.annotation --------------------------

GENE_ID_of_TF_A   AT1G01453

GENE_ID_of_TF_A   AT1G01471

GENE_ID_of_TF_A   AT1G01540

GENE_ID_of_TF_A   AT1G01800

GENE_ID_of_TF_A   AT1G01930

GENE_ID_of_TF_A   AT1G01980

GENE_ID_of_TF_A   AT1G02100

GENE_ID_of_TF_A   AT1G02160

GENE_ID_of_TF_A   AT1G02180

GENE_ID_of_TF_A   AT1G02370

GENE_ID_of_TF_A   AT1G02410

GENE_ID_of_TF_A   AT1G02710


  3. Conduct step1 and 2 for other TFs (B, C, D, ...........................).



  4. Concatenate all annotation files into one txt file.
  
  
  cat *.narrowPeak.u1000_d500.annotation > ALL_TFs.narrowPeak.u1000_d500.annotation
  
  
  5. Use ALL_TFs.narrowPeak.u1000_d500.annotation for --cistrome argument.
  

  For other species, interaction database can be manually constructed as described above.
