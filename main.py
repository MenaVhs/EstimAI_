# -*- coding: utf-8 -*-
# Use with DEEPLABCUT interpreter

# Distance conditions for experiment
joint = 'Spine'
condition = 0
unit = 'cm'  # or m
event_time = 0  # sec
video_path = r'C:\Users\Angel\Desktop\PRUEBAS con videos externos\Shoenfeld\Grupo2r5s15_10fps_Recortado.mp4'

# DeepLabCut data
config_path = r'C:\Users\Angel\Desktop\EstimAI-Mena-2023-07-06\config.yaml'
shuffle = 1
gputouse = 0
videotype = 'mp4'
save_as_csv_DeepLabCut = True
destfolder_DeepLabCut_documents = None  # if "None", automatically DeepLabCut saves files in the same video path
                                        # Or you can write a path like: r'C:\path\...\directory'

# Analyze a video with DeepLabCut
analyze_videos = False
filter_predictions = True
plot_trajectories = True
analyze_skeleton = False
create_labeled_video = False


if __name__ == "__main__":
    import exe

    __author__ = 'MenaVhs'
    exe.execution()
