import pandas as pd
import mopy as mo
import matplotlib.pyplot as plt
import numpy as np


# bar_colour = ["b", "g", "k", "m", "c", "r", "pink", "orange", "yellow"]
#
# # heat
heat_in = ["heat_pump", "heat_boiler_oil", "heat_boiler_gas", "heat_discharging"]
heat_out = ["heat_demand", "heat_charging"]
#
#
# # only ch and di
# heat_in = ["heat_discharging"]
# heat_out = ["heat_charging"]
#
# heat_colour = ["b-", "g--", "k:", "m+", "c--", "r:"]
#
# # hydrogen
hydrogen_in = ["electrolyser", "steam_reforming", "hydrogen_discharging"]
hydrogen_out = ["hydrogen_demand", "hydrogen_charging", "hydrogen_fuel_cell"]


# only ch and di
# hydrogen_in = ["hydrogen_discharging"]
# hydrogen_out = ["hydrogen_charging"]

# hydrogen_colour = ["b-", "g--", "k:", "m-", "c--", "r:"]
#
# # electricity
electricity_out = ['heat_pump', 'electrolyser', "", "electricity_demand", "battery_charging", "hydro_charging"]
electricity_in = ['biomass', 'hydropower', 'solar', 'wind_offshore', 'wind_onshore', 'lignite_coal', 'hard_coal', 'natural_gas', "oil", "battery_discharging", "hydro_discharging", "hydrogen_fuel_cell"]

colour_list = ["black", "gray", "darkgrey", "silver","red", "green", "blue", "sienna", "orchid", "fuchsia", "salmon", "tomato", "peru", "khaki", "plum", "purple", "violet", "pink", "yellow"]




# only ch and di
# electricity_in = ["hydro_discharging"]
# electricity_out = ["hydro_charging"]
# electricity_in = ["battery_discharging"]
# electricity_out = ["battery_charging"]
# electricity_colour = ["b-", "g--", "k:", "+m", "--c", ":r"]


opt_file = ['solar', 'wind_offshore', 'wind_onshore', 'steam_reforming', 'support_gen_ele', 'electrolyser', 'heat_pump', 'battery_storage', 'hydro_storage', 'hydrogen_storage', 'heat_storage', 'battery_charging', 'battery_discharging', 'hydro_charging', 'hydro_discharging', 'hydrogen_charging', 'hydrogen_discharging', 'heat_charging', 'heat_discharging']


def cum_sum_file(df, e_list):
    df_new = pd.DataFrame()

    for m in e_list:
        if m in df.columns:
            df_new = mo.hor(df_new, df.loc[:, m])

    df_new = df_new.cumsum(axis=1)
    return df_new


def file_hourly(in_folder_path, energy_file, e_list_in, e_list_out, out_file_name, out_folder_path, ele=False, time_step=False, time_slot=pd.date_range("2030-06-01", freq="H", periods=24, tz='Europe/Berlin')):
    c = 0
    df = pd.read_csv(mo.path.join(in_folder_path, energy_file), index_col="name", parse_dates=True)
    df_in = cum_sum_file(df, e_list_in)
    df_out = cum_sum_file(df, e_list_out)

    if time_step:
        for i in df_in.columns:
            if ele:
                plt.plot(time_slot, df_in.loc[time_slot, i], label=i)
            else:
                plt.plot(time_slot, df_in.loc[time_slot, i], heat_colour[c], label=i)
                c = c+1
        for j in df_out.columns:
            if ele:
                plt.plot(time_slot, df_out.loc[time_slot, j], label=j)
            else:
                plt.plot(time_slot, df_out.loc[time_slot, j], heat_colour[c], label=j)
                c = c+1
    else:
        for i in df_in.columns:
            if ele:
                plt.plot(df_in.index, df_in.loc[:, i], label=i)
            else:
                plt.plot(df_in.index, df_in.loc[:, i], heat_colour[c], label=i)
                c = c+1
        for j in df_out.columns:
            if ele:
                plt.plot(df_out.index, df_out.loc[:, j], label=j)
            else:
                plt.plot(df_out.index, df_out.loc[:, j], heat_colour[c], label=j)
                c = c+1

    plt.title(out_file_name)
    plt.xlabel("time in hours")
    plt.ylabel("energy in MWh")
    plt.legend(fontsize="x-small")
    plt.savefig(mo.path.join(out_folder_path, out_file_name + ".png"), dpi=600)
    plt.clf()
    # return


def cum_sum_file_total(df, e_list):
    df_new = pd.DataFrame(index=df.columns)

    for m in e_list:
        if m in df.index:
            df_new = mo.hor(df_new, df.loc[m, :])

    return df_new


def file_total(in_folder_path, energy_file_name, e_list_in, e_list_out, out_file_name, out_folder_path, ele=False):
    df = pd.read_csv(mo.path.join(in_folder_path, energy_file_name), index_col=0)

    c = 0

    df_in = cum_sum_file_total(df, e_list_in)
    df_out = cum_sum_file_total(df, e_list_out)

    X = np.arange(len(df_in.index))
    # lab = [df_in.columns[0]]
    plt.bar(X - 0.15, df_in.loc[:, df_in.columns[0]], width=.25, label=df_in.columns[0])
    for i in range(1, len(df_in.columns)):
        c = c+1
        plt.bar(X - 0.15, df_in.loc[:, df_in.columns[i]], color=colour_list[c], width=.25, bottom=(df_in.loc[:, df_in.columns[:i]]).sum(axis=1), label=df_in.columns[i])
        # lab.append(df_in.columns[i])

    X = np.arange(len(df_out.index))
    # lab = lab.append(df_out.columns[0])
    c = c+1
    plt.bar(X + 0.15, abs(df_out.loc[:, df_out.columns[0]]), width=.25, label=df_out.columns[0])
    for i in range(1, len(df_out.columns)):
        c = c+1
        plt.bar(X + 0.15, abs(abs(df_out.loc[:, df_out.columns[i]])), width=.25, bottom=abs((df_out.loc[:, df_out.columns[:i]]).sum(axis=1)), label=df_out.columns[i])
        # lab.append(df_out.columns[i])

    plt.title(out_file_name)
    plt.xlabel("CO2 limit in Mtons")
    plt.ylabel("annual energy in MWh")
    plt.xticks(np.arange(len(df_in.index)), df_in.index, rotation="vertical")
    plt.legend(fontsize="xx-small")
    plt.savefig(mo.path.join(out_folder_path, out_file_name + ".png"), dpi=600)
    plt.clf()
    # return


def vis(data_folder_name, line=False):
    if line:
        if mo.path.isdir(mo.path.join(mo.output_path, data_folder_name)):
            if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_bus")):
                mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_bus"))
            if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_bus")):
                mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_bus"))
            if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_bus")):
                mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_bus"))

            # Ch and Di
            if mo.path.isdir(mo.path.join(mo.output_path, data_folder_name)):
                if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_hydro_store")):
                    mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_hydro_store"))
                if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_store")):
                    mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_store"))
                if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_store")):
                    mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_store"))

            # if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_one_day")):
            #     mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "electricity_one_day"))
            # if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_one_day")):
            #     mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_one_day"))
            # if not mo.path.isdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_one_day")):
            #     mo.mkdir(mo.path.join(mo.output_path, data_folder_name, "results", "heat_one_day"))

            folder_list = mo.listdir(mo.path.join(mo.output_path, data_folder_name))
            folder_list.remove("results")
            for folder in folder_list:
                result_files_folder_path = mo.path.join(mo.path.join(mo.output_path, data_folder_name), folder, "results")

                file_hourly(result_files_folder_path, "electricity.csv", electricity_in, electricity_out, folder + "_electricity_bus", mo.path.join(mo.output_path, data_folder_name, "results", "electricity_hydro_store"), ele=True)
                file_hourly(result_files_folder_path, "heat.csv", heat_in, heat_out, folder + "_heat_bus", mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_store"))
                file_hourly(result_files_folder_path, "hydrogen.csv", hydrogen_in, hydrogen_out, folder + "_hydrogen_bus", mo.path.join(mo.output_path, data_folder_name, "results", "heat_store"))

                # entire year
                # file_hourly(result_files_folder_path, "electricity.csv", electricity_in, electricity_out, folder + "_electricity_bus", mo.path.join(mo.output_path, data_folder_name, "results", "electricity_one_day"), ele=True)
                # file_hourly(result_files_folder_path, "heat.csv", heat_in, heat_out, folder + "_heat_bus", mo.path.join(mo.output_path, data_folder_name, "results", "heat_one_day"))
                # file_hourly(result_files_folder_path, "hydrogen.csv", hydrogen_in, hydrogen_out, folder + "_hydrogen_bus", mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_one_day"))

                # one day
                # file_hourly(result_files_folder_path, "electricity.csv", electricity_in, electricity_out, folder + "_electricity", mo.path.join(mo.output_path, data_folder_name, "results", "electricity_bus"), ele=True, time_step=True, time_slot=pd.date_range("2030-06-01", freq="H", periods=24, tz='Europe/Berlin'))
                # file_hourly(result_files_folder_path, "heat.csv", heat_in, heat_out, folder + "_heat", mo.path.join(mo.output_path, data_folder_name, "results", "heat_bus"), time_step=True, time_slot=pd.date_range("2030-06-01", freq="H", periods=24, tz='Europe/Berlin'))
                file_hourly(result_files_folder_path, "hydrogen.csv", hydrogen_in, hydrogen_out, folder + "_hydrogen", mo.path.join(mo.output_path, data_folder_name, "results", "hydrogen_bus"), time_step=True, time_slot=pd.date_range("2030-06-01", freq="H", periods=24, tz='Europe/Berlin'))
        else:
            print("Error!!! output folder path dose not exits")
            return


if __name__ == "__main__":
    # vis("fi_3.0", line=True)