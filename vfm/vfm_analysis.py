"""
Compiles VfM analysis. Places into output file an excel file with data.

This programme takes the project data from the following keys:
- state when code finalised.
In the output workbook the initial tabs contain a raw print out of this data for each
project. The final tab contains a 'count' as required for analysis.
What is the analysis trying to achieve... need from user(s).

Command line options
analysis_engine run vfm analysis. Default is current and latest quarter, all projects.
flags.
- quarters. specify the quarters to be analysed
- groups. specify particular groups e.g. business case stage, dft group
- project. specify a particular project or group of projects.

"""
from data_mgmt.data import (
    Master,
    root_path,
    get_project_information,
    get_master_data,
    VfMData,
    vfm_into_excel
)


def compile_vfm_analysis(m: Master,
                         **kwargs):
    vfm = VfMData(m)
    # current and last quarter set as default
    if kwargs == {}:
        current_quarter = str(m.master_data[0].quarter)
        last_quarter = str(m.master_data[1].quarter)
        quarter_list = [current_quarter, last_quarter]
        vfm.get_dictionary()
        vfm.get_count()
    if "quarters" in kwargs.keys():
        quarter_list = kwargs["quarters"]
        vfm.get_dictionary()
        vfm.get_count()
    if "group" in kwargs.keys():
        vfm.get_dictionary(group=kwargs["group"])
        vfm.get_count()
    if "stage" in kwargs.keys():
        vfm.get_dictionary(stage=kwargs["stage"])
        vfm.get_count()

    wb = vfm_into_excel(vfm, quarter_list)
    wb.save(root_path / "output/vfm.xlsx")


mst = Master(get_master_data(), get_project_information())
# compile_vfm_analysis(mst, stage="FBC", quarters=["Q4 18/19", "Q3 19/20", "Q2 20/21"])


