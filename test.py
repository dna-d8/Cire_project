import pypsa
from os import path
import pandas as pd
import mopy as mo
import timeit

# ###read data
# input_folder_path = "/run/media/dixit/D8_HD/D/Study/SEM_2/Cire/moosces/input_folder/"
# results_folder = "/run/media/dixit/D8_HD/D/Study/SEM_2/Cire/moosces/output_folder/"
#
#
# cost = pd.DataFrame()
# clock = pd.DataFrame()
#
#
#
# # i = 78000000
# # 110000000
# # i = max_emission
# # print(max_emission)
# #####output =  566441431.4687587
#
#
# ##########################################################
# i = 166000000
# results_folder_name = "t2.1"
# dif = 30000000
# i_i = i
# ##########################################################
#
#
#
# results_folder_path = path.join(results_folder, (results_folder_name + "/"))
# input_folder = path.join(input_folder_path,(results_folder_name + "/"))
#
# ###network
# n = pypsa.Network()
# n.import_from_csv_folder(input_folder)
#
# while i > 5:
#     time_clock_start = timeit.default_timer()
#
#     # Global constrains
#     n.add("GlobalConstraint", "Co2_limit", type="primary_energy", carrier_attribute="co2_emissions", constant=i, sense="<=")
#
#     folder = str(int(i))
#
#     results_folder = path.join(results_folder_path, folder)
#
#     n.lopf(n.snapshots, solver_name="gurobi_direct")
#     n.export_to_csv_folder(results_folder)
#
#     n.mremove("GlobalConstraint", ["Co2_limit"])
#
#     # vis####################################################################################################
#
#     #######total energy#######
#     sums = pd.DataFrame()
#
#     sums = mo.ver(sums, n.generators_t.p.sum(axis=0), n.links_t.p0.sum(axis=0))
#     sums.columns = [str(round(int(i) / 10e5, 1)) + "M"]
#
#     if i == i_i:
#         total_energy = sums
#     else:
#         total_energy = mo.hor(total_energy, sums)
#     #######total energy#######
#
#     #######p_nom_opt#######
#     optimal = pd.DataFrame()
#
#     optimal = mo.ver(optimal, n.generators.loc[:, "p_nom_opt"], n.links.loc[:, "p_nom_opt"],
#                      n.stores.loc[:, "e_nom_opt"])
#     optimal.columns = [str(round(int(i) / 10e5, 1)) + "M"]
#
#     if i == i_i:
#         opt = optimal
#     else:
#         opt = mo.hor(opt, optimal)
#     ########p_nom_opt######
#
#     # vis####################################################################################################
#
#     # cost####################################################################################################
#
#     ###gen###
#     for j in n.generators_t.p.columns:
#         if n.generators.loc[j, "p_nom_opt"] - n.generators.loc[j, "p_nom"] > 0:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.generators.loc[j, "capital_cost"] * (
#                     n.generators.loc[j, "p_nom_opt"] - n.generators.loc[j, "p_nom"])
#         else:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0
#
#     ###links###
#     for j in n.links_t.p0.columns:
#         if n.links.loc[j, "p_nom_opt"] - n.links.loc[j, "p_nom"] > 0:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.links.loc[j, "capital_cost"] * (
#                     n.links.loc[j, "p_nom_opt"] - n.links.loc[j, "p_nom"])
#         else:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0
#
#     ###stores###
#     for j in n.stores_t.p.columns:
#         if n.stores.loc[j, "e_nom_opt"] - n.stores.loc[j, "e_nom"] > 0:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.stores.loc[j, "capital_cost"] * (
#                     n.stores.loc[j, "e_nom_opt"] - n.stores.loc[j, "e_nom"])
#         else:
#             cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0
#
#     # cost####################################################################################################
#
#     if n.generators.loc["support_gen_ele", "p_nom_opt"] != 0 or n.generators.loc[
#         "support_gen_heat", "p_nom_opt"] != 0 or n.generators.loc["support_gen_hydrogen", "p_nom_opt"] != 0:
#         print("Error support_gen")
#         i = 0
#
#     i = int(i) - dif
#     total_energy.index.name = "tech"
#     opt.index.name = "tech"
#     cost.index.name = "tech"
#     total_energy.to_csv(path.join(results_folder_path, "total_energy.csv"))
#     opt.to_csv(path.join(results_folder_path, "opt.csv"))
#     cost.to_csv(path.join(results_folder_path, "cost.csv"))
#     total_cost = cost.sum(axis=0)
#     total_cost.to_csv(path.join(results_folder_path, "total_cost.csv"))
#     time_clock_stop = timeit.default_timer()
#     clock.to_csv(path.join(results_folder_path, "time_clock.csv"))
#     execution_time = time_clock_stop - time_clock_start
#     clock.loc[str(round(int(i) / 10e5, 1)) + "M", "time in s"] = execution_time
#     # break


# x = pd.read_csv("/run/media/dixit/D8_HD/D/Study/SEM_2/Cire/moosces/output_folder/t2.1/166000000/loads-p.csv", index_col="time")
# print((x.lco[:,0]).max())


import pypsa
from os import path
# import os
import pandas as pd
import mopy as mo
import timeit

###read data
input_folder_path = "/run/media/dixit/D8_HD/D/Study/SEM_2/Cire/moosces/input_folder/"
results_folder = "/run/media/dixit/D8_HD/D/Study/SEM_2/Cire/moosces/output_folder/"


cost = pd.DataFrame()
clock = pd.DataFrame()



# i = 78000000
# 110000000
# i = max_emission
# print(max_emission)
#####output =  566441431.4687587


##########################################################
i = 166000000
results_folder_name = "t2.1"
dif = 30000000
i_i = i
##########################################################



results_folder_path = path.join(results_folder, (results_folder_name + "/"))
input_folder = path.join(input_folder_path, (results_folder_name + "/"))

###network
n = pypsa.Network()
n.import_from_csv_folder(input_folder)

while i > 5:
    time_clock_start = timeit.default_timer()

    # Global constrains
    n.add("GlobalConstraint", "Co2_limit", type="primary_energy", carrier_attribute="co2_emissions", constant=i, sense="<=")

    folder = str(int(i))

    results_folder = path.join(results_folder_path, folder)

    n.lopf(n.snapshots, solver_name="gurobi_direct")
    n.export_to_csv_folder(results_folder)

    n.mremove("GlobalConstraint", ["Co2_limit"])

    # vis####################################################################################################


    ########peak_values##############3
    # e_peak = pd.DataFrame()
    # h_peak = pd.DataFrame()
    #                                            "2030-01-01 00:00:00+01:00"
    # e_peak = mo.ver(e_peak, n.generators_t.loc["2030-01-26 06:00:00+01:00",:], n.links_t.loc["2030-01-26 06:00:00+01:00",:])
    # h_peak = mo.ver(h_peak, n.generators_t.loc["2030-11-28 17:00:00+01:00",:], n.links_t.loc["2030-11-28 17:00:00+01:00",:])
    #
    # e_peak.columns = [str(round(int(i) / 10e5, 1)) + "M"]
    # h_peak.columns = [str(round(int(i) / 10e5, 1)) + "M"]
    #
    # if i == i_i:
    #     heat_peak = h_peak
    #     elec_peak = e_peak
    # else:
    #     heat_peak = mo.hor(heat_peak, h_peak)
    #     elec_peak = mo.hor(elec_peak, e_peak)
    #
    # ########peak_values##############3

    #######total energy#######
    sums = pd.DataFrame()

    sums = mo.ver(sums, n.generators_t.p.sum(axis=0), n.links_t.p0.sum(axis=0))
    sums.columns = [str(round(int(i) / 10e5, 1)) + "M"]

    if i == i_i:
        total_energy = sums
    else:
        total_energy = mo.hor(total_energy, sums)
    #######total energy#######

    #######p_nom_opt#######
    optimal = pd.DataFrame()

    optimal = mo.ver(optimal, n.generators.loc[:, "p_nom_opt"], n.links.loc[:, "p_nom_opt"],
                     n.stores.loc[:, "e_nom_opt"])
    optimal.columns = [str(round(int(i) / 10e5, 1)) + "M"]

    if i == i_i:
        opt = optimal
    else:
        opt = mo.hor(opt, optimal)
    ########p_nom_opt######

    # vis####################################################################################################

    # cost####################################################################################################

    ###gen###
    for j in n.generators_t.p.columns:
        if n.generators.loc[j, "p_nom_opt"] - n.generators.loc[j, "p_nom"] > 0:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.generators.loc[j, "capital_cost"] * (
                    n.generators.loc[j, "p_nom_opt"] - n.generators.loc[j, "p_nom"])
        else:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0

    ###links###
    for j in n.links_t.p0.columns:
        if n.links.loc[j, "p_nom_opt"] - n.links.loc[j, "p_nom"] > 0:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.links.loc[j, "capital_cost"] * (
                    n.links.loc[j, "p_nom_opt"] - n.links.loc[j, "p_nom"])
        else:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0

    ###stores###
    for j in n.stores_t.p.columns:
        if n.stores.loc[j, "e_nom_opt"] - n.stores.loc[j, "e_nom"] > 0:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = n.stores.loc[j, "capital_cost"] * (
                    n.stores.loc[j, "e_nom_opt"] - n.stores.loc[j, "e_nom"])
        else:
            cost.loc[j, str(round(int(i) / 10e5, 1)) + "M"] = 0

    # cost####################################################################################################

    if n.generators.loc["support_gen_ele", "p_nom_opt"] != 0 or n.generators.loc[
        "support_gen_heat", "p_nom_opt"] != 0 or n.generators.loc["support_gen_hydrogen", "p_nom_opt"] != 0:
        print("Error support_gen")
        i = 0

    i = int(i) - dif

    total_energy.index.name = "tech"
    elec_peak.index.name = "tech"
    heat_peak.index.name = "tech"
    opt.index.name = "tech"
    cost.index.name = "tech"

    total_energy.to_csv(path.join(results_folder_path, "total_energy.csv"))
    elec_peak.to_csv(path.join(results_folder_path, "elec_peak.csv"))
    heat_peak.to_csv(path.join(results_folder_path, "heat_peak.csv"))
    opt.to_csv(path.join(results_folder_path, "opt.csv"))
    cost.to_csv(path.join(results_folder_path, "cost.csv"))
    total_cost = cost.sum(axis=0)
    total_cost.to_csv(path.join(results_folder_path, "total_cost.csv"))
    time_clock_stop = timeit.default_timer()
    clock.to_csv(path.join(results_folder_path, "time_clock.csv"))
    execution_time = time_clock_stop - time_clock_start
    clock.loc[str(round(int(i) / 10e5, 1)) + "M", "time in s"] = execution_time
    # break
