import deeplabcut
import main

config_path = main.config_path
video_path = main.video_path

shuffle_ = main.shuffle
gputouse_ = main.gputouse
videotype = main.videotype
save_as_csv_ = main.save_as_csv_DeepLabCut
destfolder_ = main.destfolder_DeepLabCut_documents

deeplabcut.analyze_videos(config_path, video_path, videotype, shuffle=shuffle_, trainingsetindex=0, gputouse=gputouse_, save_as_csv=save_as_csv_, destfolder=destfolder_)


# get_project_feature(joint, condition, unit, event_time)


# deeplabcut.filterpredictions(config_path, video_path, shuffle=1, trainingsetindex=0, filtertype='arima', p_bound=0.01, ARdegree=3, MAdegree=1, alpha=0.01)
# #
# deeplabcut.plot_trajectories(config_path, video_path, videotype='mp4', shuffle=1, trainingsetindex=0, filtered=True , displayedbodyparts='all', showfigures=True)
# #
# deeplabcut.create_labeled_video(config_path, video_path, save_frames = True)
# #
# deeplabcut.analyzeskeleton(config_path, video_path, videotype='mp4', shuffle=1, trainingsetindex=0, save_as_csv=True, destfolder=None)