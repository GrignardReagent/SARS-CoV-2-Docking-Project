# This code writes docking scores from flare into a csv file
from cresset import flare
import csv

project = flare.main_window().project

with open('/Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/docking_scores_site1.csv', 'w') as score_file:

    wr = csv.writer(score_file, dialect='excel')
    title_row = ['lig_name', 'LF Rank Score', 'LF dG', 'LF VSscore','LF LE']
    wr.writerow(title_row)
    for l in project.ligands:
        if l.title.endswith('_D'):
            name = l.title.strip('_D')
            row = []
            row.append(name)
            row.append(l.properties['LF Rank Score'])
            row.append(l.properties['LF dG'])
            row.append(l.properties['LF VSscore'])
            row.append(l.properties['LF LE'])
            wr.writerow(row)


