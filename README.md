This file is a part of DNN-DR (DIP® DIP DNN for Drug Repurposing)
The package is distributed under DNN-DR
Version 0.0.1

Copyright © 2020 Deep Intelligent Pharma.

Room 1608, Tower B T3, Wangjing SOHO, #1 Futong East Avenue,
Wangjing, Chaoyang District, Beijing, China

DNN-DR is a method to classify drugs to their therapeutic use based on transcriptomic data. DNN-DR has fully connected multilayer perception with 978 input nodes for gene expression and 163 input nodes for signaling pathways. The output nodes are 6 therapeutic use classes. 

The introduction of the codes supplied within this method is described hereafter.

The codes are written Python 3.6
packages from mlp, which can be obtained by the following links:

https://github.com/alvarouc/mlp/blob/master/mlp/model.py

The package was tested with the following configuration:

system: linux
python version: 3.6
sklearn : 0.20.0
keras : 2.2.4
pandas : 0.24.1
numpy : 1.15.0
logging : 0.5.1.2

1. data
   input_path_data.txt is a feature file.
   input_label.txt is the a label file.
   
2. example
   python example.py


Please cite the paper in any publication containing results acquired
using this method.
