import pathlib
import airsign.mission.exreader

mission_input_folder = pathlib.Path.cwd() / 'input' / 'missions'
filename = 'missions.xlsx'
path_to_mission_file = pathlib.Path(mission_input_folder, filename)

mission_list = airsign.mission.exreader.scan_mission_file(path_to_mission_file)

for mission in mission_list:
    airsign.mission.exreader.create_mission_from_sheet(path_to_mission_file, mission, mission_list)
