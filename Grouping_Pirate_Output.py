# -----------------------------------------------------------------------------------------------
# 
#
#
# Jonathan Holmes
#
# Permission to use, copy, modify, and/or distribute this software or any part thereof for any
# purpose with or without fee is hereby granted provided that:
#     (1) the original author is credited appropriately in the source code
#         and any accompanying documentation
# and (2) that this requirement is included in any redistribution.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.
#
# E-mail: jh795@leicester.ac.uk
# ------------------------------------------------------------------------------------------------
# 
#
# This script should rely on no libraries outside of the default python libraries and as such should
# require no additional installation. To run the programme navigate to the direcotry containing your
# input file then run the programme as follows:
#
# 			python3 Grouping_Pirate_Output.py
#
# 
#
# ------------------------------------------------------------------------------------------------



# Required Libraries
import os
import shutil
 
# Created functions
def extract_PV_information(A):
	Fasta = open(A).read().split(">")[1:]

	PV_IDS = []
	Rep_seq = ""

	for seq in Fasta:
		for r in Repeats:
			if r in seq:	
				PV_IDS.append(seq[:seq.index("\n")])
				Rep_seq = r

	return [PV_IDS, Rep_seq]

"""
This code moves each g0 number generated by Pirate into indiviual folders containing the aa and nucleotide sequences split by the presence or absence of a given repeat tract

input - Pirate alignment folder

output - folder containing split sequences

"""

Target = "/scratch/spectre/j/jh795/Phasome_Exp/Pirate_Output/feature_sequences"
Output = "Sequences_from_Pirate"


## Creates all searched for repeats
Repeat_Units = ["A","T","G","C","AT","CT"]
Minimum_Lengths = [10,10,7,7,6,6] 

Repeats = []
for i in range(0,len(Repeat_Units)):
	Repeats.append(Repeat_Units[i]*Minimum_Lengths[i])


## Loops through all files in Pirate Output
for file in os.listdir(Target):	
	if "nucleotide" in file:
		#print(file)
		ID = file.replace(".nucleotide.fasta","")
		nucleotide = ID + ".nucleotide.fasta"
		protein = ID + ".aa.fasta"

		PV_IDS = extract_PV_information(Target + "/" + nucleotide)


		if len(PV_IDS[0]) != 0:

			os.mkdir(Output + "/" + ID)
			PV_nucl = []
			non_PV_nucl = []
			PV_aa = []
			non_PV_aa = []	
		
			for seq in open(Target + "/" + nucleotide).read().split(">")[1:]:
				if seq[:seq.index("\n")] in PV_IDS[0]:
					PV_nucl.append(seq)
				else:
					non_PV_nucl.append(seq)

			for seq in open(Target + "/" + protein).read().split(">")[1:]:
				if seq[:seq.index("\n")] in PV_IDS[0]:
					PV_aa.append(seq)
				else:
					non_PV_aa.append(seq)
				
			if len(non_PV_nucl) != 0:
				os.mkdir(Output + "/" + ID + "/NO_PV_nucleotide")	
				os.mkdir(Output + "/" + ID + "/NO_PV_AA")
				output_file_non_PV_nucl = open(Output + "/" + ID + "/NO_PV_nucleotide" + "/" + ID + ".nucleotide.fasta","w")	
				output_file_non_PV_aa = open(Output + "/" + ID + "/NO_PV_AA" + "/" + ID + ".AA.fasta","w")
				output_file_non_PV_nucl.write(">" + ">".join(non_PV_nucl))
				output_file_non_PV_aa.write(">" + ">".join(non_PV_aa))
				output_file_non_PV_nucl.close()


			os.mkdir(Output + "/" + ID + "/PV_nucleotide_" + PV_IDS[1])	
			os.mkdir(Output + "/" + ID + "/PV_AA_" + PV_IDS[1])
			output_file_PV_nucl = open(Output + "/" + ID + "/PV_nucleotide_" + PV_IDS[1] + "/" + ID + ".nucleotide.fasta","w")
			output_file_PV_aa = open(Output + "/" + ID + "/PV_AA_" + PV_IDS[1] + "/" + ID + ".AA.fasta","w")
			output_file_PV_nucl.write(">" + ">".join(PV_nucl))
			output_file_PV_aa.write(">" + ">".join(PV_aa))			
			output_file_PV_nucl.close()
			output_file_PV_aa.close()




		if len(PV_IDS[0]) == 0:
			os.mkdir(Output + "/" + ID)	
			os.mkdir(Output + "/" + ID + "/NO_PV_AA")
			os.mkdir(Output + "/" + ID + "/NO_PV_nucleotide")
			shutil.copy(Target + "/" + nucleotide, Output + "/" + ID + "/NO_PV_nucleotide/" + nucleotide)
			shutil.copy(Target + "/" + protein, Output + "/" + ID + "/NO_PV_AA/" + protein)

			

























