# -*- coding: utf-8 -*-
# Use with DEEPLABCUT interpreter

# Distance conditions for experiment
Activate_Distance_condition = True

joint = 'Spine'
condition = 100
unit = 'cm'  # or m
event_time = 3  # sec

# Video to analyze
video_path = r'C:\Users\...\Shoenfeld\Grupo2r5s15_10fps_Recortado.mp4'

# DeepLabCut data
config_path = r'C:\Users\...\EstimAI-Mena-2023-07-06\config.yaml'
shuffle = 1
gputouse = 0
videotype = 'mp4'
save_as_csv_DeepLabCut = True
destfolder_DeepLabCut_documents = None  # if "None", automatically DeepLabCut saves files in the same video path
                                        # or you can write a path like: r'C:\path\...\directory'

# Analyze a video with DeepLabCut
analyze_videos = True
filter_predictions = False
plot_trajectories = False
analyze_skeleton = False # it is recommended that when executing this command, it should be in individual.

# Create Labeled videos
create_labeled_video = False
save_frames = True


if __name__ == "__main__":
    import exe

    __author__ = 'MenaVhs'
    exe.execution()
