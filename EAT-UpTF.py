#!/usr/bin/python

import sys
import scipy.stats as st
from statsmodels.stats.multitest import multipletests as mt
import argparse

########################### argument parser #######################################################################
parser  = argparse.ArgumentParser(description="Enrichment Analysis Tool for Upstream Transcription Factor of a gene set (EAT-UpTF) : conduct enrichment analysis of upstream transcription factor for a gene set of interest.")
parser.add_argument('--cistrome', help='database file of cistrome', default='interaction_DAPseq.txt', type=argparse.FileType('r'))
parser.add_argument('--gene_group', help='file containing group of genes (new line delimited)', type=argparse.FileType('r'))
parser.add_argument('--num_ref_genes','-N', help='No. of total genes in reference genome, default=27206 for Arabidopsis thaliana', default=27206.0, type=float)
parser.add_argument('--model', help='statistical model: HG=hypergeometric test, BN=binomial test, default=HG', default='HG', type=str)
parser.add_argument('--post_hoc', help='post hoc analysis: bonferroni=Bonferroni family-wise error rate correction, fdr_bh=Benjamini & Hochberg False Discover Rate correction, default=fdr_bh', default='fdr_bh', type=str)
parser.add_argument('--alpha', help='alpha in post hoc analysis, default:0.05', default=0.05, type=float)
parser.add_argument('--output', help='output file name', default='EAT-UpTF.output', type=argparse.FileType('w'))
parser.add_argument('--alias', help='gene alias file, default=NA', default='NA', type=str)
args = parser.parse_args()

########################## module for TF annotation ###############################################################
def alias_anno(opened_file_list):
    alias   = {}
    for gene in opened_file_list:
        gene_cell   = gene.strip().split('\t')
        if len(gene_cell)>2:
            ids = gene_cell[0]
            sym = gene_cell[1]
            func    = gene_cell[2]
        else:
            ids = gene_cell[0]
            sym = gene_cell[1]
            func    = 'NA'
        if ids in alias.keys():
            alias[ids][0].append(sym)
            alias[ids][1].append(func)
        else:
            alias[ids]  = [[sym],[func]]
    return alias

######################### MAIN SCRIPT PERFORMING ENRICHMENT ANALYSIS ###############################################

cis_dict  = {}
cis   = args.cistrome.readlines()                                   #### READ CISTROME DATABASE
gene_list   = [x.strip() for x in args.gene_group.readlines()]      #### READ LIST OF GOIs

n   = float(len(gene_list))                                         #### NO. OF GOIs
N   = args.num_ref_genes                                            #### NO. OF TOTAL GENES IN REFERENCE GENOME

for i in cis:
    cell    = i.strip().split()
    tf  = cell[0]
    target  = cell[1]

    if tf in cis_dict.keys():
        cis_dict[tf].append(target)
    else:
        cis_dict[tf]   = [target]

information_dict    = {}
id_list = []
p_value_list    = []
adjusted_p_value_list   = []

####################### CALCULATE STATISTICAL SIGNIFICANCE #########################################################
for j in cis_dict.keys():
    x   = len(list(set(cis_dict[j])))                               #### NO. OF TARGET GENES FOR SPECIFIC TF IN REFERENCE GENOME
    y   = len(set(gene_list).intersection(set(cis_dict[j])))        #### NO. OF TARGET GENES FOR SPECIFIC TF IN GOIs
    expected = (x/N)                                                #### RATIO IN WHOLE REFERENCE GENOME (EXPECTED)
    if args.model   == 'BN':                                        #### STATISTICAL METHOD SELECTION
        p_value = st.binom_test(y,n,expected)
    else:
        p_value = st.hypergeom.sf(y-1,N,x,n)

    information_dict[j.strip()] = [str(y),str(int(n)),str(y/n),str(x),str(int(N)),str(expected),str(p_value)]
    id_list.append(j.strip())
    p_value_list.append(p_value)

adjusted_p_value_list = mt(p_value_list, alpha=args.alpha, method=args.post_hoc)    #### ADJUSTED P-VALUE CALCULATION

output  = args.output

if args.alias   == 'NA':                                            #### PRINT OUT RESULTS (WITHOUT TF ANNOTATION)
    output.write('TF (AGI)'+'\t'+ 'x' +'\t'+ 'n' +'\t'+ 'observed (ratio)' +'\t'+ 'X' +'\t'+ 'N' +'\t'+ 'expected (ratio)' +'\t'+ 'p-value' +'\t'+ 'q-value' +'\n')
    for k in range(len(id_list)):
        output.write(id_list[k] +'\t'+ '\t'.join(information_dict[id_list[k]]) +'\t'+ str(adjusted_p_value_list[1][k])+'\n')
else:                                                               #### PRINT OUT RESULTS (ALONG WITH TF ANNOTATION)
    alias_dict  = alias_anno(open(args.alias,'r').readlines())
    output.write('TF (AGI)'+'\t'+ 'x' +'\t'+ 'n' +'\t'+ 'observed (ratio)' +'\t'+ 'X' +'\t'+ 'N' +'\t'+ 'expected (ratio)' +'\t'+ 'p-value' +'\t'+ 'q-value' +'\t'+ 'gene symbol' +'\t'+ 'gene name' +'\n')
    for k in range(len(id_list)):
        try:
            output.write(id_list[k] +'\t'+ '\t'.join(information_dict[id_list[k]]) +'\t'+ str(adjusted_p_value_list[1][k])+'\t'+ ', '.join(list(set(alias_dict[id_list[k]][0]))) +'\t'+ ', '.join(list(set(alias_dict[id_list[k]][1]))) +'\n')
        except KeyError:
            output.write(id_list[k] +'\t'+ '\t'.join(information_dict[id_list[k]]) +'\t'+ str(adjusted_p_value_list[1][k])+'\t'+ ' ' +'\t'+ ' ' +'\n')
