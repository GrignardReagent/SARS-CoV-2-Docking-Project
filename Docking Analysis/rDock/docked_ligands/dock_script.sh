#!/bin/bash

for dir in */
do
	cd $dir
	lig=${dir%/}
	printf "Start docking for ligand $lig."
	printf "\n"
	rbdock -r def.prm -p dock.prm -n 10 -i $lig.sdf -o docking_out4 > docking_out4.log
	printf "Docking for ligand $lig complete."
	printf "\n\n"
	cd ..
done
