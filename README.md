# quadrotor_trajectory_planning

### Run

Run `main.m` to start the program.

`traj_opt7.m` is key file to generate a trajectory. The current algorithm use a 7-order piecewise polynomial to generate a smooth trajectory. Constrains are listed below:

<img src="imgs/formula.png" alt="image" style="zoom:67%;" />

### Examples

![image](imgs/maze.gif)

![image](imgs/p1p3_map3_snap.gif)