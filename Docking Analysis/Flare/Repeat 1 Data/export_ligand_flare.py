# ***STEP 1 in Flare select and export all desired ligands into ONE sdf file using the GUI*** 
# If the code does not work, you can select manually and export your desired ligands into one sdf file using the GUI
from cresset import flare
import os

project = flare.main_window().project
ligands = project.ligands

os.chdir('/Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/Flare/Repeat 1 Data')
# Write ALL the ligands into an sdf file
flare.write_file('site1_ligands.sdf',ligands)

# ***The loop does not work***
# for l in ligands: 
# 	if l.title.endswith('_D'):
# 		name = l.title.strip('_D')
# 		flare.write_file(name+'.pdb',l)

# ***STEP 2 in Pymol WITH "site1_ligands.sdf" OPENED***
# This is an internal function of Pymol that exports the indivisual states in the sdf into separate pdf files
multifilesave /Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/Flare/Repeat 4 Data/Site1/{}-{title}.pdb, state = 0 #state = 0 means 'all states'

# Sometimes, states are accidentally saved as untitled. 
# If this happens, there are 2 available options:
# 1. Drag the desired ligand from Flare into Pymol and export as a pdb file, rename it properly
# 2. Rename the desired ligand in Pymol before exporting: 
# click on 'Properties' --> Select the desired state --> Find 'Label' --> Double clcik to change the name on 'Label'


# ***STEP 3 on a command line*** 
# This will run on shell script, so may not work on a Windows command line
# Make directories for the ligands
mkdir docked_ligands
cd docked_ligands
mkdir Forsythoside_E Lopinavir DAR Disulfiram Diammonium Baicalein Baicalin Wogonin Wogonoside VTRRT NHC
for dir in */
do
	printf "Start making $dir folder."
	printf "\n"
	cd $dir
	mkdir -p Site1/With_Water Site1/Without_Water Site2/With_Water Site2/Without_Water Site3d/With_Water Site3d/Without_Water Site3m/With_Water Site3m/Without_Water
	printf "Finished making $dir folder."
	printf "\n\n"
	cd ..
done

# The following codes move and rename your pdb files into the folders you just created for each ligand
# moving site 1 ligands with water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site1/ 
for file in W_Site1_*_D.pdb
do
	ligand=${file//W_Site1_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site1/With_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 1 ligands without water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site1/
for file in Site1_*_D.pdb
do
	ligand=${file//Site1_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site1/Without_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 2 ligands with water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site2/
for file in W_Site2_*_D.pdb
do
	ligand=${file//W_Site2_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site2/With_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 2 ligands without water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site2/
for file in Site2_*_D.pdb
do
	ligand=${file//Site2_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site2/Without_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 3d ligands with water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site3d/
for file in W_Site3d_*_D.pdb
do
	ligand=${file//W_Site3d_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site3d/With_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 3d ligands without water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site3d/
for file in Site3d_*_D.pdb
do
	ligand=${file//Site3d_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site3d/Without_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 3m ligands with water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site3m/
for file in W_Site3m_*_D.pdb
do
	ligand=${file//W_Site3m_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site3m/With_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

# moving site 3m ligands without water, change: the directory for each repeat, name of the pdb file, the renamed file (line starting with mv)
cd /Users/ianyang/Desktop/University\ of\ Edinburgh/Third\ Year/EUYSRA/Docking\ Analysis/Flare/Repeat\ 4\ Data/Site3m/
for file in Site3m_*_D.pdb
do
	ligand=${file//Site3m_}
	ligand=${ligand//_D.pdb}
	printf "Start moving $ligand to new folder"
	printf "\n"
	mv $file ../docked_ligands/$ligand/Site3m/Without_Water/rpt4.pdb
	printf 'Finished moving $ligand'
	printf '\n\n'
done

