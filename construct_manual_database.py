import sys
import os

tfID_fileName_list  = open(sys.argv[1],'r').readlines()
genome_annotation_file  = sys.argv[2]
upstream = sys.argv[3]
downstream  = sys.argv[4]
gene_ID_column  = sys.argv[5]
distance_column = sys.argv[6]
peak_left   = sys.argv[7]

for x in tfID_fileName_list:
    cell    = x.strip().split()
    tfID    = cell[0].strip()
    fileName    = cell[1].strip()
    os.system("bedtools closest -a "+ genome_annotation_file +" -b "+ fileName +" -D a > "+ fileName +".annotation ; awk '$"+ distance_column +"<="+ downstream +" && $"+ distance_column +">=-"+ upstream +"' "+ fileName +".annotation | awk '$"+ peak_left +"!=-1' | cut -f "+ gene_ID_column +" | sort -u | sed 's/$/\t"+ tfID +"/' | paste - - | cut -f 2,3 > "+ fileName +".u1000_d500.annotation")

