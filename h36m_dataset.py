"""
This implementation assumes that the Human3.6M dataset is stored in a directory specified by data_path, with subdirectories for each subject and action, and H5 files containing the 3D pose data for each action. It loads the data for the specified subjects and actions using the H5Py library, and stores the data as a list of dictionaries, with each dictionary containing the subject, action, and pose data for a single frame.

The get_poses() method returns a list of individual Pose objects, each with a subject, action, and pose data. You can use this method to extract individual poses and generate pairs of poses for training the Siamese network.
"""
import os
import numpy as np
import h5py

class H36MDataset:
    def __init__(self, data_path='/path/to/h36m/dataset', subjects=['S1', 'S5', 'S6', 'S7', 'S8', 'S9', 'S11']):
        self.data_path = data_path
        self.subjects = subjects
        self.actions = ['Directions', 'Discussion', 'Eating', 'Greeting', 'Phoning', 'Photo', 'Posing', 'Purchases', 'Sitting', 'SittingDown', 'Smoking', 'Waiting', 'Walking', 'WalkDog', 'WalkTogether']
        
        # Load the data
        self.data = self._load_data()
    
    def _load_data(self):
        data = []
        for subject in self.subjects:
            for action in self.actions:
                filename = os.path.join(self.data_path, subject, 'MyPoseFeatures', 'D3_Positions_mono_universal', action + '.h5')
                with h5py.File(filename, 'r') as f:
                    positions = f['positions_3d'][()]
                    num_frames = positions.shape[0]
                    for i in range(num_frames):
                        data.append({'subject': subject, 'action': action, 'pose': positions[i]})
        return data
    
    def get_poses(self):
        poses = []
        for item in self.data:
            poses.append(Pose(item['subject'], item['action'], item['pose']))
        return poses

class Pose:
    def __init__(self, subject, action, pose):
        self.subject = subject
        self.action = action
        self.pose = pose
