import deeplabcut
import main

config_path = main.config_path
video_path = main.video_path

shuffle_ = main.shuffle
gputouse_ = main.gputouse
videotype = main.videotype
save_as_csv_ = main.save_as_csv_DeepLabCut
destfolder_ = main.destfolder_DeepLabCut_documents

analyze_videos = main.analyze_videos
filter_predictions = main.filter_predictions
plot_trajectories = main.plot_trajectories
create_labeled_video = main.create_labeled_video
save_frames_ = main.save_frames
analyze_skeleton = main.analyze_skeleton


def execution():
    if analyze_videos: deeplabcut.analyze_videos(config_path, video_path, videotype, shuffle=shuffle_,
                                                 trainingsetindex=0, gputouse=gputouse_, save_as_csv=save_as_csv_,
                                                 destfolder=destfolder_)

    if filter_predictions: deeplabcut.filterpredictions(config_path, video_path, shuffle=shuffle_, trainingsetindex=0,
                                                        filtertype='arima', p_bound=0.01, ARdegree=3, MAdegree=1,
                                                        alpha=0.01)

    if plot_trajectories: deeplabcut.plot_trajectories(config_path, video_path, videotype=videotype, shuffle=shuffle_,
                                                       trainingsetindex=0, filtered=True, displayedbodyparts='all',
                                                       showfigures=True)

    if create_labeled_video: deeplabcut.create_labeled_video(config_path, video_path, save_frames=save_frames_)

    if analyze_skeleton: deeplabcut.analyzeskeleton(config_path, video_path, videotype=videotype, shuffle=shuffle_,
                                                    trainingsetindex=0, save_as_csv=save_as_csv_,
                                                    destfolder=destfolder_)
