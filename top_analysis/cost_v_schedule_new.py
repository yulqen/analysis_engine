"""
New code for cost v schedule matrix
"""

from analysis_engine.data import (
    Master,
    get_project_information,
    get_master_data, CostData,
    MilestoneData, cost_v_schedule_chart,
    root_path
)

m = Master(get_master_data(), get_project_information())
costs = CostData(m, m.current_projects)
milestones = MilestoneData(m, m.current_projects)
milestones.calculate_schedule_changes()
wb = cost_v_schedule_chart(milestones, costs)
wb.save(root_path / "output/costs_schedule_matrix.xlsx")

#  handling for projects that have greater than 100 movement
