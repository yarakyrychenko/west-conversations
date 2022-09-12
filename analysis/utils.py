from convokit import Corpus, Coordination, TextCleaner, PolitenessStrategies
from scipy.stats import ttest_ind_from_stats
import numpy as np, pandas as pd, seaborn as sns, os, matplotlib.pyplot as plt, matplotlib.patches as mpatches


# helper function to plot two coordination scores against each other as a chart,
#   on aggregate and by coordination marker
# a is a tuple (speakers, targets)
# b is a tuple (speakers, targets)
def make_chart(a_scores, b_scores, a_description, b_description, a_color="lightskyblue", b_color="plum"):
    # get scores by marker and on aggregate
    a_score_by_marker = a_scores["marker_agg2"]
    a_agg1, a_agg2, a_agg3 = a_scores["agg1"], a_scores["agg2"], a_scores["agg3"]
    b_score_by_marker = b_scores["marker_agg2"]
    b_agg1, b_agg2, b_agg3 = b_scores["agg1"], b_scores["agg2"], b_scores["agg3"]

    # the rest plots this data as a double bar graph
    a_data_points = sorted(a_score_by_marker.items())
    b_data_points = sorted(b_score_by_marker.items())
    a_data_points, b_data_points = zip(*sorted(zip(a_data_points, b_data_points),
        key=lambda x: x[0][1], reverse=True))
    labels, a_data_points = zip(*a_data_points)
    _, b_data_points = zip(*b_data_points)

    labels = ["aggregate 1", "aggregate 2", "aggregate 3"] + list(labels)
    a_data_points = [a_agg1, a_agg2, a_agg3] + list(a_data_points)
    b_data_points = [b_agg1, b_agg2, b_agg3] + list(b_data_points)

    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(len(a_data_points)) + 0.35)
    ax.set_xticklabels(labels, rotation="vertical")

    ax.bar(np.arange(len(a_data_points)), a_data_points, 0.35, color=a_color)
    ax.bar(np.arange(len(b_data_points)) + 0.35, b_data_points, 0.35, color=b_color)

    b_patch = mpatches.Patch(color=a_color,
                             label=a_description + " (total: " +
                             str(a_scores["count_agg1"]) + ", " +
                             str(a_scores["count_agg2"]) + ", " + 
                             str(a_scores["count_agg3"]) +  ")")
    g_patch = mpatches.Patch(color=b_color,
                             label=b_description + " (total: "  +
                             str(b_scores["count_agg1"]) + ", " +
                             str(b_scores["count_agg2"]) + ", " + 
                             str(b_scores["count_agg3"]) + ")")
    plt.legend(handles=[b_patch, g_patch])

    filename = str(a_description) + " vs " + str(b_description) + ".png"
    #plt.savefig(filename, bbox_inches="tight")
    print('Created chart "' + filename + '"')




def make_interaction_chart(a_scores, b_scores, c_scores, d_scores, a_description, b_description, c_description, d_description,
                            a_color="lightskyblue", b_color="plum"):
    # get scores by marker and on aggregate
    a_score_by_marker = a_scores["marker_agg2"]
    a_agg1, a_agg2, a_agg3 = a_scores["agg1"], a_scores["agg2"], a_scores["agg3"]
    b_score_by_marker = b_scores["marker_agg2"]
    b_agg1, b_agg2, b_agg3 = b_scores["agg1"], b_scores["agg2"], b_scores["agg3"]
    
    c_score_by_marker = c_scores["marker_agg2"]
    c_agg1, c_agg2, c_agg3 = c_scores["agg1"], c_scores["agg2"], c_scores["agg3"]
    d_score_by_marker = d_scores["marker_agg2"]
    d_agg1, d_agg2, d_agg3 = d_scores["agg1"], d_scores["agg2"], d_scores["agg3"]


    #labels = ["aggregate 1", "aggregate 2", "aggregate 3"] + list(labels)
    #a_data_points = [a_agg1, a_agg2, a_agg3] + list(a_data_points)
    #b_data_points = [b_agg1, b_agg2, b_agg3] + list(b_data_points)

    data_points = [a_agg3,b_agg3,c_agg3,d_agg3]
    labels = [a_description, b_description, c_description, d_description]

    plt.bar(labels, data_points,color = ['r','b','r','b'])
    print("(total: " + 
                             str(a_scores["count_agg3"]) + ", " +
                             str(b_scores["count_agg3"]) + ", " +
                             str(c_scores["count_agg3"]) + ", " +
                             str(d_scores["count_agg3"]) +  ")")

    filename = str(a_description) + " vs " + str(b_description) + ".png"
    #plt.savefig(filename, bbox_inches="tight")
    print('Created chart "' + filename + '"')

CoordinationWordCategories = ["article", "auxverb", "conj", "adverb",
"ppron", "ipron", "preps", "quant"]

def get_stats(coord_oobj):
    from statistics import stdev
    from collections import defaultdict
    
    a1_scores_by_marker = defaultdict(list)
    scores_by_marker = defaultdict(list)
    for speaker, scores in coord_oobj.items():
        for cat, score in scores.items():
            scores_by_marker[cat].append(score)
            if len(scores) == len(CoordinationWordCategories):
                a1_scores_by_marker[cat].append(score)
    do_agg2 = False
    if len(scores_by_marker) == len(CoordinationWordCategories):
        do_agg2 = True
        avg_score_by_marker = {cat: sum(scores) / len(scores)
                               for cat, scores in scores_by_marker.items()}
    agg1s, agg2s, agg3s = [], [], []
    for speaker, scoredict in coord_oobj.items():
        scores = list(scoredict.values())
        if len(scores) >= 1:
            avg = sum(scores) / len(scores)
            agg3s.append(avg)
            if len(scores) == len(CoordinationWordCategories):
                agg1s.append(avg)
            if do_agg2:
                for cat in avg_score_by_marker:
                    if cat not in scoredict:
                        scores.append(avg_score_by_marker[cat])
                agg2s.append(sum(scores) / len(scores))
    agg1 = sum(agg1s) / len(agg1s) if agg1s else None
    agg2 = sum(agg2s) / len(agg2s) if agg2s else None
    agg3 = sum(agg3s) / len(agg3s) if agg3s else None

    a1_avg_by_marker = {cat: sum(scores) / len(scores)
                            for cat, scores in a1_scores_by_marker.items()}
    avg_by_marker = {cat: sum(scores) / len(scores)
                         for cat, scores in scores_by_marker.items()}
    
    aggs = [agg1s, agg2s, agg3s]
    
    agg = [agg1, agg2, agg3]

    stds = [stdev(agge) for agge in aggs]
    nums = [len(agge)   for agge in aggs]

    return agg, stds, nums


def ttest_print_all_results(a_m, a_st, a_num, b_m, b_st, b_num):
    results = []
    for i in range(len(a_m)):
        res = ttest_ind_from_stats(a_m[i], a_st[i], a_num[i], b_m[i], b_st[i], b_num[i])
        print("Aggragate "+str(i))
        print("Mean \t STD \t Total Number")
        print(round(a_m[i],4), round(a_st[i],4), a_num[i],sep="\t")
        print(round(b_m[i],4), round(b_st[i],4), b_num[i],sep="\t")
        print(res)
        results.append(res)
        print("\n")