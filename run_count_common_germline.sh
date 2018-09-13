#!/bin/bash
#SBATCH --account=IscrC_LUAD-MUT
#SBATCH --export=ALL
#SBATCH --nodes=1                    # 1 node
#SBATCH --time=16:00:00                # time limits
#SBATCH --error=commonG.err            # standard error file
#SBATCH --output=commonG.out           # standard output file
#SBATCH --mem=64G                    # memory size
#SBATCH -p bdw_usr_prod

#./myscript
/marconi/home/userexternal/emerdan0/scratch/count_common_germline.sh