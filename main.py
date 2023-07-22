# -*- coding: utf-8 -*-
# Use with DEEPLABCUT interpreter

# Distance conditions for experiment
joint = 'Spine'
condition = 100
unit = 'cm'  # or m
event_time = 3  # sec
video_path = r'C:\path\to\the\video\for\analyze\video.mp4'

# DeepLabCut data
config_path = r'C:\path\to\DLC-project-2023-07-06\config.yaml'
shuffle = 1
gputouse = 0
videotype = 'mp4'
save_as_csv_DeepLabCut = True
destfolder_DeepLabCut_documents = None  # if "None", automatically DeepLabCut saves files in the same video path
                                        # Or you can write a path like: r'C:\path\...\directory'

# Analyze a video with DeepLabCut
analyze_videos = True
filter_predictions = False
plot_trajectories = False
create_labeled_video = False
analyze_skeleton = False

if __name__ == "__main__":
    import exe

    __author__ = 'MenaVhs'
    exe.execution()
