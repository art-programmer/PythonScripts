import glob
import os
import numpy as np

filenames = os.listdir('evaluations/new_vis_floornet/')
sample_ids = [filename.replace('auto3d-', '').replace('.ply.npy', '') for filename in filenames]

method_statistics = []
info_types = ['wall', 'edge', 'room', 'relation']
info_order = [0, 1, 3, 2]
for folder in ['evaluations/new_vis_floornet', 'evaluations/new_vis_heuristics', 'evaluations/new_vis_no_inter', 'evaluations/new_vis_round_2']:
    all_statistics = []
    for sample_id in sample_ids:
        if 'floornet' in folder:
            statistics = np.load(folder + '/auto3d-' + sample_id + '.ply.npy')
            statistics = np.array([[statistics['statistics'][info_type][1], statistics['statistics'][info_type][2]] for info_type in info_order])            
        else:
            statistics = np.load(folder + '/auto3d-' + sample_id + '.npy')[()]
            statistics = np.array([[float(statistics[info_type][0]) / max(statistics[info_type][1], 1), float(statistics[info_type][0]) / max(statistics[info_type][2], 1)] for info_type in info_types])
            pass
        all_statistics.append(statistics)        
        continue
    all_statistics = np.stack(all_statistics, axis=0)
    method_statistics.append(all_statistics)
    continue

method_image_names = []
for method in ['hsv', 'real_gt', 'floornet', 'floorplan_heuristics', 'floorplan_no_inter', 'floorplan_round_2']:
    method_image_names.append(['all_images/' + str(index) + '_' + method + '.png' for index in range(94)])
    continue

indices = range(6)
string = """
\\begin{table*}[t]
\\centering
\\footnotesize
\\setlength\\tabcolsep{0.3pt}
\caption{More qualitative results.}
  \\begin{tabular}{cc|cccc}
\hline
\multirow{2}{*}{Point Cloud} & \multirow{2}{*}{Ground Truth} & \multirow{2}{*}{FloorNet} & Ours \\newline (w/o E_{data}, E_{consis}) & Ours \\newline (w/o E_{consis}) & \multirow{2}{*}{Ours} \\\\
 &  &  & (w/o E_{data}, E_{consis}) & (w/o E_{consis}) & \\\\
\hline
"""
for index in indices:
    for method_index in range(6):
        string += '\\includegraphics[width=0.15\\textwidth]{figures/' + method_image_names[method_index][index] + '}'
        if method_index < 5:
            string += ' & '
        else:
            string += ' \\\\\n'
            pass
        continue
    string += ' & & '
    for method_index, method_name in enumerate(['Corner', 'Edge', 'Room', 'Room++']):
        statistics = method_statistics[method_index][index]
        for number in statistics[:2]:
            string += '%0.1f/%0.1f, '%(number[0] * 100, number[1] * 100)
            continue
        if method_index < 3:
            string += '& '
        else:
            string += '\\\\\n'
            pass
        continue
    string += ' & & '
    for method_index, method_name in enumerate(['Corner', 'Edge', 'Room', 'Room++']):
        statistics = method_statistics[method_index][index]
        for number in statistics[2:4]:
            string += '%0.1f/%0.1f, '%(number[0] * 100, number[1] * 100)
            continue
        if method_index < 3:
            string += '& '
        else:
            string += '\\\\\n'
            pass
        continue
    continue
string += """
\hline
\end{tabular}
\end{table*}
"""

print(string)
