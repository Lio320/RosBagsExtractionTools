# ROSBAGs Extraction Tool

This Python package is a command-line tool to extract data from ROS bag files. It allows you to specify topics and save extrected data in an organized directory strucutre.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Lio320/RosBagsExtractionTools.git
    cd rosbag_image_extractor
    ```

1.1 **Create a virtual environment (OPTIONAL):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install using pip:**
    ```bash
    pip install .
    ```

## Usage

Once installed, you can use the `extract` command from your terminal to extract images.

**Basic Command Structure:**

```bash
python3 extract.py -s <path_to_rosbag_file> -t <list of topics to extract>
```