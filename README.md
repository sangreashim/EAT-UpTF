
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
  
  
  # How to customize database
  
  EAT-UpTF conducts TF enrichment analysis based on the experimentally validated interaction between specific TF and its target genes. Interaction between TF and its targets (identified by ChIP-/DAP-seq) can be added manually as following example. The fisrt and second columns represent TF and target genes, respectively. The two columns must be delimited by <b>TAB</b>.


AT5G60130       AT1G01010

AT5G60130       AT1G01030

AT5G60130       AT1G01040

AT5G60130       AT1G01070

AT5G60130       AT1G01073

AT5G60130       AT1G01110

AT5G60130       AT1G01120

AT5G60130       AT1G01140

....

AT3G28920       AT5G67350

AT3G28920       AT5G67360

AT3G28920       AT5G67370

AT3G28920       AT5G67390

AT3G28920       AT5G67411

AT3G28920       AT5G67420

AT3G28920       AT5G67430

AT3G28920       AT5G67455

AT3G28920       AT5G67460


  For other species, interaction database can be manually constructed as described above.
