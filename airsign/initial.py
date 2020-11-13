import pathlib, 


mission_input_folder = pathlib.Path.cwd() / 'airsign' / 'input' / 'missions'
filename = 'missions.xlsx'
path_to_mission_file = pathlib.Path(mission_input_folder,filename)

mission_list = exreader.scan_mission_file(path_to_mission_file)

for mission in mission_list:
    exreader.create_mission_from_sheet(path_to_mission_file,mission,mission_list)
