import deeplabcut

config_path = r'C:\Users\Angel\Desktop\EstimAI-Mena-2023-07-06\config.yaml'
# video_path = r'C:\Users\Angel\Desktop\Prueba con ADFE\GrupoTCRata6Fase3PM2_R.mp4'
video_path = r'D:\EstiAI_\4_JOINTS\0Iteration\1 SEC\ADFE_1-00-85_2-00-60 - 2SEC.mp4'


# deeplabcut.analyze_videos(config_path, video_path, videotype='mp4', shuffle=1, trainingsetindex=0, gputouse=0, save_as_csv=True, destfolder=None)
#
# deeplabcut.filterpredictions(config_path, video_path, shuffle=1, trainingsetindex=0, filtertype='arima', p_bound=0.01, ARdegree=3, MAdegree=1, alpha=0.01)
# #
# deeplabcut.plot_trajectories(config_path, video_path, videotype='mp4', shuffle=1, trainingsetindex=0, filtered=True , displayedbodyparts='all', showfigures=True)
# #
# deeplabcut.create_labeled_video(config_path, video_path, save_frames = True)
# #
deeplabcut.analyzeskeleton(config_path, video_path, videotype='mp4', shuffle=1, trainingsetindex=0, save_as_csv=True, destfolder=None)