# Dataset Preparation

## Overview

The proposed ISFHC-GHI framework was evaluated using publicly available benchmark gait recognition datasets. The datasets were selected due to their widespread use in gait analysis research and their ability to provide diverse walking conditions, viewpoints, and subject variations.

The following datasets were utilized during experimental evaluation:

* CASIA-A
* CASIA-B
* OU-ISIR

Researchers are requested to obtain the datasets directly from their respective official sources and comply with all applicable licensing and usage policies.

---

## Data Preparation Procedure

The raw gait video sequences undergo a sequence of preprocessing operations before being supplied to the proposed framework.

### Step 1: Video Acquisition

Gait sequences are collected from the selected benchmark datasets. Each sequence contains walking patterns captured under different viewpoints and environmental conditions.

### Step 2: Video-to-Frame Conversion

Each gait sequence is decomposed into individual image frames to facilitate frame-level processing and silhouette extraction.

### Step 3: Frame Normalization

The extracted frames are resized and normalized to maintain consistency across different datasets and acquisition conditions.

### Step 4: AdLOG-WF Preprocessing

The Adaptive LOG-Based Wiener Filtering (AdLOG-WF) module is applied to reduce noise while preserving gait-related structural information. The preprocessing stage improves image quality and supports more accurate segmentation.

### Step 5: Gait Silhouette Segmentation

The preprocessed frames are supplied to the Modified U-Net segmentation model. The network generates foreground gait silhouettes by separating the walking subject from the background environment.

### Step 6: Feature Extraction

Three complementary categories of features are extracted from the segmented silhouettes:

* Hierarchy of Skeleton (HOS) Features
* Multitexton Features
* Color Features

The extracted features capture structural, textural, and appearance-based gait characteristics.

### Step 7: Feature Representation

The extracted features are combined to form a unified feature vector that serves as the input for the classification stage.

### Step 8: Dataset Partitioning

The prepared feature representations are divided into training and testing subsets.

Training–Testing Split:

```text
Training Data : 70%
Testing Data  : 30%
```

### Step 9: Classification and Evaluation

The training data are supplied to LinkNet and SqueezeNet classifiers. The resulting classification scores are integrated using the Improved Score-Level Fusion (ISF) strategy to generate the final identification results.

---

## Evaluation Metrics

The performance of the proposed framework is evaluated using:

* Accuracy
* Precision
* Recall
* Specificity
* F-Measure
* Matthews Correlation Coefficient (MCC)
* Negative Predictive Value (NPV)
* False Positive Rate (FPR)
* False Negative Rate (FNR)

---

## Reproducibility Notes

The dataset preparation procedure described in this document summarizes the workflow followed during experimental evaluation of the ISFHC-GHI framework. Researchers may adapt the preparation pipeline according to their dataset characteristics while preserving the overall processing sequence described in the manuscript.
