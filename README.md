# Automated Bergmann-Kliesch Score Assessment in Testicular Biopsies

This repository contains the source code for the AI-based whole-slide image analysis pipeline described in the manuscript:

Automated Bergmann-Kliesch Score Assessment in Testicular Biopsies Using Artificial Intelligence-Based Whole-Slide Image Analysis: A Retrospective Monocentric Development and Validation Study

## Overview

The pipeline performs automated Bergmann-Kliesch Score assessment from paired haematoxylin-eosin and OCT3/4-stained whole-slide images of testicular biopsies.

The workflow includes:

1. ROI extraction from whole-slide images
2. Tissue mask generation
3. Patch and tile extraction
4. HE-based seminiferous tubule segmentation
5. OCT3/4-based elongated spermatid detection
6. Post-processing of segmentation masks
7. Multimodal HE/OCT3/4 image registration
8. Projection of spermatid detections into HE coordinates
9. Tubule-level assignment of spermatid detections
10. Automated Bergmann-Kliesch Score calculation

## Intended use

This code is provided for research transparency and reproducibility.

It is not intended for clinical use without external validation, local quality control, and regulatory assessment.

## Data availability

The source code is publicly available in this repository.

Trained model weights and the datasets used and/or analyzed during the study are available from the corresponding author on reasonable request, subject to institutional and data protection requirements.

No patient-level image data, annotations, model weights, or derived patient-specific outputs are included in this repository.

## Requirements

The pipeline was developed in Python 3.8.10 using fastai, PyTorch, SimpleITK, scikit-image, OpenSlide, Shapely, NumPy, pandas, OpenCV, Pillow, matplotlib, and tqdm.

Exact package versions are listed in requirements.txt.

## Repository structure

src/bergmann_pipeline/   Core reusable pipeline code
scripts/                 Executable pipeline scripts
configs/                 Example configuration templates
docs/                    Documentation
notebooks/               Optional cleaned example notebooks

## Citation

If you use this code, please cite the associated manuscript.

## License

See LICENSE.
