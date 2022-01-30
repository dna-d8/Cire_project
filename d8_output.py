import pandas as pd
import mopy as mo


def curtailment(data_folder_name, start_limit=180, reduction=20, end_limit=0):
    common_files_folder = mo.path.join(mo.output_path, data_folder_name, "common", "files")
    individual_folder = mo.path.join(mo.output_path, data_folder_name, "individual")
    pypsa_out_path = mo.path.join(mo.output_path, data_folder_name, "pypsa_out")

    # input file
    gen_p_max_pu = pd.read_csv(mo.path.join(mo.input_path, data_folder_name, "generators-p_max_pu.csv"), index_col="name", parse_dates=True)
    total_curtailments = pd.DataFrame(index=gen_p_max_pu.columns)

    co2_limit = start_limit
    while co2_limit >= end_limit:
        cur = pd.DataFrame(index=gen_p_max_pu.index)

        # read from folder
        gens = pd.read_csv(mo.path.join(pypsa_out_path, str(co2_limit), "generators.csv"), index_col="name", parse_dates=True)
        electricity = pd.read_csv(mo.path.join(individual_folder, str(co2_limit),  "electricity.csv"), index_col="name", parse_dates=True)

        for i in gen_p_max_pu.columns:
            cur = mo.hor(cur, ((gen_p_max_pu.loc[:, i] * gens.loc[i, "p_nom_opt"]) - electricity.loc[:, i]))

        # save individual curtailment
        cur.to_csv(mo.path.join(individual_folder, str(co2_limit)
                                , "curtailments.csv"))

        # dataframe of total curtailments
        total_curtailments[co2_limit] = cur.sum(axis=0)

        # save total curtailments
        total_curtailments.to_csv(mo.path.join(common_files_folder, "total_curtailments.csv"))
        co2_limit = co2_limit - reduction


if __name__ == "__main__":
    curtailment("fi_4.0")