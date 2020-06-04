%% Prepare
close all;
clear all;
clc;
addpath(genpath('./'));

%% Load Map
map = load_map('maps/map_maze.txt', 0.2, 0.2, 0.25);
start = {[0,1,0]};
stop = {[9,1,9]};
nquad = length(start);

%% Planning
disp('Planning ...');
for qn = 1:nquad
    tic
    path{qn} = astar(map, start{qn}, stop{qn});
    toc
end
% if nquad == 1
%        plot_path(map, path{1});
% end


%% Additional init script
init_script;

%% Run trajectory
[trajectory,traj_time,end_condition] = test_trajectory(start, stop, map, path, true); % with visualization
