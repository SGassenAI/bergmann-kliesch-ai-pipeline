"""
Minimal inference workflow for automated Bergmann-Kliesch Score assessment.

This script documents the intended order of the inference pipeline used in the manuscript.
It is provided for research transparency. Patient-level images, annotations, model weights,
and derived outputs are not included in this repository.

Before use, adapt config_template.yaml to local paths and provide trained model weights.
"""

from pathlib import Path
import yaml


def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def main(config_path):
    config = load_config(config_path)

    output_dir = Path(config["paths"]["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Automated Bergmann-Kliesch Score inference pipeline")
    print("--------------------------------------------------")
    print("This minimal public script documents the pipeline order.")
    print("No patient data or model weights are included.")

    print("\nPipeline steps:")
    print("1. Export HE and OCT3/4 regions of interest from whole-slide images")
    print("2. Generate tissue masks")
    print("3. Extract HE patches and OCT3/4 tiles")
    print("4. Run HE tubule segmentation model")
    print("5. Run OCT3/4 spermatid detection model")
    print("6. Post-process tubule masks and spermatid detections")
    print("7. Register paired HE and OCT3/4 whole-slide images")
    print("8. Project spermatid detections into HE coordinates")
    print("9. Assign spermatid detections to individual seminiferous tubules")
    print("10. Calculate Bergmann-Kliesch Score")

    print("\nConfigured output directory:")
    print(output_dir)

    print("\nNote:")
    print("The full inference implementation requires local whole-slide images,")
    print("trained model weights, and institutional preprocessing paths.")


if __name__ == "__main__":
    main("configs/config_template.yaml")
