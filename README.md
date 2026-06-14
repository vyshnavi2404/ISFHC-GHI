# ISFHC-GHI

## Hybrid Gait-Based Human Identification Using Modified U-Net and Score-Level Fusion

This repository provides the supplementary implementation package associated with the research work:

**"Hybrid Gait-Based Human Identification Using Modified U-Net and Score-Level Fusion"**

The proposed ISFHC-GHI framework integrates adaptive preprocessing, enhanced gait silhouette segmentation, multi-feature extraction, hybrid classification, and improved score-level fusion to achieve robust gait-based human identification.

---

## Framework Overview

The proposed framework consists of the following major stages:

```text
Input Gait Video
        |
        v
Video-to-Frame Conversion
        |
        v
AdLOG-WF Preprocessing
        |
        v
Modified U-Net Segmentation
        |
        v
Hierarchy of Skeleton Features
        |
        v
Multitexton Features
        |
        v
Color Features
        |
        v
Unified Feature Representation
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
Final Human Identification
```

---

## Repository Structure

```text
ISFHC-GHI/
│
├── preprocessing/
│   ├── adlog_wf.py
│   └── image_enhancement.py
│
├── segmentation/
│   ├── munet.py
│   └── attention_block.py
│
├── feature_extraction/
│   ├── hos_features.py
│   ├── multitexton.py
│   └── color_features.py
│
├── classification/
│   ├── linknet_classifier.py
│   ├── squeezenet_classifier.py
│   └── score_fusion.py
│
├── config/
│   └── experiment_config.yaml
│
├── datasets/
│   └── dataset_preparation.md
│
├── docs/
│   ├── workflow.md
│   ├── architecture.md
│   └── supplementary_material.md
│
├── examples/
│   └── sample_execution.ipynb
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Major Components

### AdLOG-WF Preprocessing

The Adaptive LOG-Based Wiener Filtering (AdLOG-WF) module performs image enhancement prior to segmentation. The module combines Gaussian smoothing, Laplacian edge enhancement, adaptive variance estimation, and nonlinear intensity updating to suppress noise while preserving gait-related structural information.

### Modified U-Net Segmentation

The Modified U-Net architecture extracts accurate gait silhouettes from preprocessed frames. The model incorporates attention mechanisms, skip connections, and encoder-decoder learning to improve segmentation quality under varying gait conditions.

### Multi-Feature Extraction

Three complementary feature categories are extracted:

* Hierarchy of Skeleton (HOS) Features
* Multitexton Features
* Color Features

The extracted features capture structural, textural, and appearance-based gait characteristics.

### Hybrid Classification

The framework employs:

* LinkNet Classifier
* SqueezeNet Classifier

to independently evaluate the extracted feature representation.

### Improved Score-Level Fusion

Classifier outputs are integrated using the Improved Score-Level Fusion (ISF) strategy based on score normalization and adaptive weighting mechanisms to generate the final identification decision.

---

## Datasets

The framework was evaluated using:

* CASIA-A
* CASIA-B
* OU-ISIR

Researchers are requested to obtain these datasets directly from their respective official providers and comply with all associated usage policies.

---

## Experimental Environment

| Parameter               | Specification        |
| ----------------------- | -------------------- |
| Programming Language    | Python 3.7+          |
| Processor               | Intel Core i3-1115G4 |
| Memory                  | 8 GB RAM             |
| Operating System        | Windows/Linux        |
| Deep Learning Framework | TensorFlow / Keras   |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/vyshnavi2404/ISFHC-GHI.git
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the framework:

```bash
python main.py
```

---

## Reproducibility

This repository is intended to support reproducibility of the proposed ISFHC-GHI framework by providing representative implementation workflows, architectural descriptions, preprocessing modules, feature extraction routines, classification modules, score-fusion procedures, configuration files, and supplementary documentation.

---

## Citation

If you use this repository in your research, please cite:

```text
Hybrid Gait-Based Human Identification Using Modified U-Net and Score-Level Fusion
SN Computer Science
```

---

## License

This project is distributed under the MIT License.

---

## Contact

For implementation-related questions and academic correspondence, please contact the corresponding author of the manuscript.
