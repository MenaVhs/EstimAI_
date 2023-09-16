import deeplabcut

config_path = r'C:\Users\mena_\Desktop\Child-Caregiver-Teresa-2023-09-12\config.yaml'

# To edit configurations
# edits = {'colormap': 'Paired',
#          'individuals': ['child', 'caregiver'],
#          'skeleton': [['headCenter', 'handRight'], ['headCenter', 'handLeft'], ['headCenter', 'eyebrowsBTW']]}

# To save edits in config.yaml
# deeplabcut.auxiliaryfunctions.edit_config(config_path, edits)

# To extrac frames
# deeplabcut.extract_frames(config_path, mode='automatic', algo='kmeans', cluster_step=10, userfeedback=False, crop=True)

# deeplabcut.generate_training_dataset.frame_extraction.extract_frames(config_path, mode='automatic', algo='kmeans',
#                                                                      crop=False, userfeedback=True, cluster_step=5,
#                                                                      cluster_resizewidth=30, cluster_color=True)

# To open Napari GUI
# deeplabcut.label_frames(config_path)

# Check Annotated Frames
# deeplabcut.check_labels(config_path, visualizeindividuals=True)

# Create the Training Dataset
# the skeleton defined in the config.yaml / default AUGMENTATION = imgaug
# deeplabcut.create_multianimaltraining_dataset(config_path, paf_graph='config')

# To train the network
# deeplabcut.pose_estimation_tensorflow.training.train_network(config_path, shuffle=1, trainingsetindex=0, max_snapshots_to_keep=5, displayiters=1000, saveiters=1000, maxiters=200000, gputouse=0, autotune=True, allow_growth=True)
# deeplabcut.train_network(config_path, shuffle=1, trainingsetindex=0, gputouse=0, max_snapshots_to_keep=5, autotune=False, displayiters=100, saveiters=15000, maxiters=20000, allow_growth=True)

# To evaluate de network
# deeplabcut.evaluate_network(config_path, plotting=True)