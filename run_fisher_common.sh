#!/bin/bash
#SBATCH --account=IscrC_LUAD-MUT
#SBATCH --export=ALL
#SBATCH --nodes=1                    # 1 node
#SBATCH --time=16:00:00                # time limits
#SBATCH --error=fisherC.err            # standard error file
#SBATCH --output=fisherC.out           # standard output file
#SBATCH --mem=100G                    # memory size
#SBATCH -p bdw_usr_prod

#./myscript
/marconi/home/userexternal/emerdan0/scratch/fisher_common.sh