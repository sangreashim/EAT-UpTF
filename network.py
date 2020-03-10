#!/usr/bin/python

import sys
import scipy.stats as st
import argparse
import os
parser  = argparse.ArgumentParser(description="Module to create transcriptional regulatory network")
parser.add_argument('--cistrome', help='database file of cistrome', type=argparse.FileType('r'))
parser.add_argument('--gene_group', help='file containing group of genes', type=argparse.FileType('r'))
parser.add_argument('--TFs', help='file containing gene IDs (AGI) of transcription factors of interest', type=argparse.FileType('r'))
parser.add_argument('--output', help='output file name', default='cisEGG.output', type=argparse.FileType('w'))
args = parser.parse_args()

cistrome_dic    = {}
for x in args.cistrome.readlines():
    cell    = x.strip().split()
    tf_id   = cell[0]
    target_id   = cell[1]
    if tf_id not in cistrome_dic.keys():
        cistrome_dic[tf_id] = [target_id]
    else:
        cistrome_dic[tf_id].append(target_id)

gene_set   = set([x.strip() for x in args.gene_group.readlines()])
gene_stack  = []
print('Source'+'\t'+'InteractionType'+'\t'+'Target'+'\t'+'Val')
for tf in [x.strip() for x in args.TFs.readlines()]:
    target_set = set(cistrome_dic[tf])
    intersection_list    = list(gene_set.intersection(target_set))
    gene_stack += intersection_list
    for target in intersection_list:
        print(tf +'\t'+ 'pd' +'\t'+ target +'\t'+ 'True')

for off_target in list(gene_set-set(gene_stack)):
        print(off_target)

    



