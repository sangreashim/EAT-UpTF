
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

python3 EAT-UpTF.py --cistrome interaction_DAPseq.txt --gene_group test_set_LHY_ChIPseq.txt --model HG --post_hoc fdr_bh --alpha 0.05 --alias gene_aliases_20140331.txt


<b>Transcriptional regulatory network:</b>

python3 network.py --cistrome interaction_DAPseq.txt --gene_group test_set_LHY_ChIPseq.txt --TFs TFs.txt > TRN.txt

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
