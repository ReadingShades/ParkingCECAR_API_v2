"""Constant file for the detector_utils module
"""
# colors for visualization
COLORS = [
    [0.000, 0.447, 0.741],
    [0.850, 0.325, 0.098],
    [0.929, 0.694, 0.125],
    [0.494, 0.184, 0.556],
    [0.466, 0.674, 0.188],
    [0.301, 0.745, 0.933],
]

# Proven HuggingFace models
MODELS = [
        "nickmuchi/yolos-small-finetuned-license-plate-detection",
        "nickmuchi/detr-resnet50-license-plate-detection",
        "nickmuchi/yolos-small-rego-plates-detection",
    ]

# Default test model
DEFAULT_MODEL = "nickmuchi/yolos-small-finetuned-license-plate-detection"