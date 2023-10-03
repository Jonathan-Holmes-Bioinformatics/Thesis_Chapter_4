seqfile = /scratch/spectre/j/jh795/Phasome_Exp/Sequences_from_Pirate/g00199/NO_PV_nucleotide/g00199_trimmed.nucleotide.fasta      * sequence data filename
treefile = /scratch/spectre/j/jh795/Phasome_Exp/Sequences_from_Pirate/g00199/NO_PV_nucleotide/RAxML_bestTree.g00199.nwk     * tree structure file name
outfile = /scratch/spectre/j/jh795/Phasome_Exp/Sequences_from_Pirate/g00199/NO_PV_nucleotide/g00199_PAML_Ouput_2.txt * main result file name

seqtype = 1  * 1:codons; 2:AAs; 3:codons-->AAs
noisy = 1
verbose = 0
model = 0    * models for codons: 0
             *  0:one, 1:b, 2:2 or more dN/dS ratios for branches   

NSsites = 2   * 0:one w;1:neutral;2:selection; 3:discrete;4:freqs;
                * 5:gamma;6:2gamma;7:beta;8:beta&w;9:beta&gamma;
                * 10:beta&gamma+1; 11:beta&normal>1; 12:0&2normal>1;
                * 13:3normal>0

fix_blength = -1  * 0: ignore, -1: random, 1: initial, 2: fixed

cleandata = 0
