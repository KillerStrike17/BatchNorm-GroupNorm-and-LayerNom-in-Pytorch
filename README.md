# BatchNorm,GroupNorm and LayerNom in Pytorch

DeepLib library structure is taken from [Link](https://github.com/parrotletml/era_session_seven/tree/main/mnist)

CIFAR10 Dataset:

![Dataset](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/dataset.png?raw=true)

## Comparision

BatchNormalization works well on Images as compared to LayerNorm and Group Norm. BatchNorm reaches 70% accuracy in 5 Epochs in less parameters, LayerNorm reaches maximum of 68.33% where as Group Norm Reaches maximum of 73.11% and Batch Norm reaches 79.58%.

## BatchNormalization

### Model Config:

![Assets/Batch Norm Model.png](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/Batch%20Norm%20Model.png?raw=true)

Parameters: 31,642

### Graphs

![BatchNorm Curves](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/curves%20batchnorm.png?raw=true)

### Misclassified Images

![Misclassified Images](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/misclassified%20batchnorm.png?raw=true)

## LayerNormalization

### Model Config:

![Assets/Layer Norm Model.png](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/Layer%20Norm%20Model.png?raw=true)

Parameters: 49,090

### Graphs

![layerNorm Cruves](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/curves%20layernorm.png?raw=true)

### Misclassified Images

![Misclassified Images](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/misclassified%20layernorm.png?raw=true)

## GroupNormalization

### Model Config:

![Assets/Group Norm Model.png](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/Batch%20Norm%20Model.png?raw=true)

Parameters: 49,090

### Graphs

![GroupNorm Cruves](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/curves%20groupnorm.png?raw=true)

### Misclassified Images

![Misclassified Images](https://github.com/KillerStrike17/BatchNorm-GroupNorm-and-LayerNom-in-Pytorch/blob/main/Assets/misclassified%20groupnorm.png?raw=true)
