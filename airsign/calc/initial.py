import pathlib
import airsign.mission.exreader

mission_input_folder = pathlib.Path.cwd() / 'input' / 'missions'
filename = 'missions.xlsx'
path_to_mission_file = pathlib.Path(mission_input_folder, filename)

mission_workbook = airsign.mission.exreader.load_mission_file(path_to_mission_file)

missions = airsign.mission.exreader.create_missions(mission_workbook)

airsign.mission.exreader.load_segments(mission_workbook, missions)
