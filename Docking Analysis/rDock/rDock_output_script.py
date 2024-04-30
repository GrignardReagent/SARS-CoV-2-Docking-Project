from cresset import flare 
import csv

project = flare.main_window().project

#This code writes rDock docking scores in a csv file

with open('/Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/rDock/rDock_site1_docking_score.csv', 'w') as score_file:

    wr = csv.writer(score_file, dialect='excel')
    title_row = ['lig_name', 'SCORE']
    wr.writerow(title_row)
    for l in project.ligands:
        name = l.title
        row = []
        row.append(name)
        row.append(l.properties['SCORE'])
        wr.writerow(row)

