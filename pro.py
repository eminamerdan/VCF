import sys
import re

List = ["synonymous_SNV","nonsynonymous_SNV","nonframeshift_insertion", "frameshift_insertion","stopgain","stoploss","frameshift_deletion","nonframeshift_deletion"]

ListFun = ["nonsynonymous_SNV","nonframeshift_insertion", "frameshift_insertion","stopgain","stoploss","frameshift_deletion","nonframeshift_deletion"]

MUT = []

def parse_vcf(vcf_file):
    with open(vcf_file, 'r') as vcf_f:
        for line in vcf_f:
            check_up_line=True
            if line[0] != '#':
                v=line.rstrip().split('\t')
                #print line,v
                if len(v)<11:
                    print >> sys.stderr,'WARNING:',line
                CHROM = v[0]
                POS = v[1]
                ID = v[2]
                REF = v[3]
                ALT = v[4]
                info_field_line = v[7]
                info_field_line_array = info_field_line.split(";")
                dict_info = {}
                for i in info_field_line_array:
                    if "=" in i:
                        key = i.split("=")[0]
                        value = i.split("=")[1]
                        dict_info[key]=value
                        my_GeneRefGene = dict_info.get('Gene.refGene','')
                        my_ExonicFuncRefGene = dict_info.get('ExonicFunc.refGene','')
                        my_AAChangeRefGene = dict_info.get('AAChange.refGene','')
                        my_gnomAD2 = dict_info.get('gnomAD_genome_ALL','')
                        my_ExAC2 = dict_info.get('ExAC_ALL','')
                        my_1000g2 = dict_info.get('1000g2015aug_all','')
                
                if my_ExonicFuncRefGene == "." or my_AAChangeRefGene == ".":
                    check_up_line=False
                    continue
                if my_ExonicFuncRefGene == "" or my_AAChangeRefGene == "":
                    check_up_line=False
                    continue
                if my_ExonicFuncRefGene == "unknown" or my_AAChangeRefGene == "UNKNOWN":
                    check_up_line=False
                    continue
                
                if my_AAChangeRefGene != ".":
                    my_AAChangeRefGene = my_AAChangeRefGene.replace(my_AAChangeRefGene, my_AAChangeRefGene.split(":")[-1]).replace("p.", "")
                
                if len(my_GeneRefGene.split(","))>1:
                    my_GeneRefGene = my_GeneRefGene.replace(my_GeneRefGene, my_GeneRefGene.split(",")[0])
                
                if my_gnomAD2 == "." or my_gnomAD2 == "":
                    my_gnomAD2 = 0
                if my_ExAC2 == "." or my_ExAC2 == "":
                    my_ExAC2 = 0
                if my_1000g2 == "." or my_1000g2 == "":
                    my_1000g2 = 0

                my_gnomAD = float(my_gnomAD2)
                my_ExAC = float(my_ExAC2)
                my_1000g = float(my_1000g2)
                A=[my_gnomAD,my_ExAC,my_1000g]

                
                format_line=v[8]
                format= format_line.split(":")
                normal_line = v[9]
                normal = normal_line.split(":")
                tumor_line = v[10]
                tumor = tumor_line.split(":")
                GT1 = normal [0]
                DP1 = normal [2]
                RD1 = float(normal[3])
                AD1 = float(normal[4])
                GT2 = tumor [0]
                DP2 = tumor [2]
                RD2 = float(tumor[3])
                AD2 = float(tumor[4])
                
                if GT1 == "0/0" and GT2 == "0/1" or GT2 == "1/0":
                    MUT = "somatic"
                else:
                    MUT = "germline"
                
                if my_ExonicFuncRefGene in List:
                    max (A)
                    depth=RD1+AD1
                    ratio= RD1/(RD1+AD1)
            
                    depth2=RD2+AD2
                    ratio2=RD2/(RD2+AD2)
                    
                if max(A) <= 0.005 and depth >= 10 and ratio >= 0.05 and depth2 >= 10 and ratio2 >= 0.05:
                    print (CHROM),(POS),(REF),(ALT),(my_GeneRefGene), my_AAChangeRefGene, (my_ExonicFuncRefGene), max(A), depth, ratio, depth2, ratio2, MUT, GT1, GT2




if __name__ == "__main__":
    vcf=sys.argv[1]
    parse_vcf(vcf)
