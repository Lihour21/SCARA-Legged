# SCARA-Legged

![legged-scara](https://github.com/Lihour21/SCARA-Legged/assets/108794757/f1c086ff-2316-49a5-81a9-436ade85545b)


Nowadays, parallel robots are used popularly in industry because of its flexibility, high rigidity and high loading capacity. However, in contrast of those benefits, they still exist main drawbacks as small workspace interrupted by singularity zones. This project attempts to study how a parallel robot based on 5-bar linkage works. In quadruped robot locomotion using parallel mechanisms, researchers have used equal link lengths as legs for walking. However, force requirements are not the same in the forward and return strokes. Major issues include conceiving a 5-bar linkage, designing a 2-DOF parallel robot through workspace synthesis, singularity analysis and structure design, implementing a prototype and control system. System operation as well as experimental results validate this approach. 

MATLAB's visualization capabilities allow you to create 2D or 3D animations of the five-bar parallel robot's motion. You can plot the trajectories, visualize joint angles, velocities, and forces, and observe the robot's behavior in real-time. This visual feedback aids in understanding the robot's kinematics and dynamics and supports debugging, analysis, and presentation of results.
In the Matlab-Simulink/SimulationParallel folder you will find all files related and used for Matlab/Simulink model of the robot. The original approach was to train optimize the controller gains through simulation with this model but be advised that it took one hour of computing to simulate 1 second of robot movement. https://youtu.be/-mN-EzNc1tQ?si=2JMFAL4tGZeSrtJu


