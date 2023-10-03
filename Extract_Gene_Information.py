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
# 			python3 Extract_Gene_Information.py
#
# 
#
# ------------------------------------------------------------------------------------------------


### Code aims to extract the gene information namely the gene name for later reference in PCA or gene identity/evolution study. 

# In built functions
def replace(a):
	b = []
	for i in a:
		if len(i) != 0:
			b.append("1")
		else:
			b.append("0")
	return b


## This is the path to the phasomeIT index.html file which is found in the summary tracts directory
target = "...path to files..../summary_tracts/groups/index.html"

## isolating output gene table..
File = open(target).read().split("PV Gene groups")[1].split('href="Not in group.html')[0].split("<tr><td>")


## removing header
Header = File[0].split("</th><th>")[6:]

Isolate_List = []


for element in Header:
	Isolate_List.append(element[element.index('">')+2:element.index('</a>')])

Gene_List = []

for line in File[1:-1]:
	Line = line.split("</td><td>")[:6]
	Gene_List.append(Line[1])




Matrix = []


## Extracting gene information --- any modifications to the type of genes you want to extract should be done by changing the condition of the if statement
Matrix = []
for line in File[1:-1]:
      Line = line.split("</td><td>")[6:]
      Gene = []
      for pos in Line:
            ID = []
            isolate = pos.split("</div>")
            for i in isolate:
                  if "#00b000" in i:
                  #if "background-color" not in i and "L_" in i:                                      #### This means empty cell... - to change background colour change the "#00" if statement... i think #ffa000 is orange and #00b00 should be green so to do any hits just remove and add if "L_" in i
                        ID.append(i.split(">")[-2].replace("</a",""))
            ID.append("")
	    ## here the first gene family of a specific cell is extracted - this can be changed to extract any gene family e.g. last.
            Gene.append(ID[0])
      Matrix.append(Gene)


## the matrix contain the first green hit for each isolate for each gene group..


## This output is a presence absence matrix 
output_file = open("Presence_Absence_Matrix.tsv","w")

output_Header = []
for i in Header:
	output_Header.append(i[i.index('">') + 2:i.index("</a>")])


output_file.write("Isolate\t" + "\t".join(Gene_List) + "\n")

## Changes gene ids to 1 and 0 for presence absence
check = []
for i in range(0,len(output_Header)):	
	Line = []
	for line in Matrix:
		Line.append(line[i])
	end = [output_Header[i]] + replace(Line)

	output_file.write("\t".join(end) + "\n") 
	check.append(end)
output_file.close()



## This output is a gene list table... see phasoemit gene group column.. 
print(Matrix)
print(Gene_List)
print(Isolate_List)

output_file = open("Gene_groups.tsv","w")


output_file.write("\t".join(["GeneGroups/Isolates"] + Isolate_List) + "\n")


for i in range(0,len(Gene_List)):
	output_file.write("\t".join([Gene_List[i]] + Matrix[i]) + "\n")


output_file.close()














