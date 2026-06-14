# Workflow Diagram

```text
Input Video
      |
      v
Video to Frame Conversion
      |
      v
AdLOG-WF Preprocessing
      |
      v
Modified U-Net Segmentation
      |
      v
HOS Features
      |
      v
Multitexton Features
      |
      v
Color Features
      |
      v
Unified Feature Vector
      |
      v
LinkNet Classification
      |
      v
SqueezeNet Classification
      |
      v
Improved Score-Level Fusion
      |
      v
Human Identification
