import nbformat
from nbclient import NotebookClient
from pathlib import Path

def run_notebook(input_path, output_path=None):
    with open(input_path) as f:
        nb = nbformat.read(f, as_version=4)

    client = NotebookClient(nb, timeout=-1, kernel_name="python3")
    client.execute()

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

def run_all_notebooks(notebooks, output_dir="executed_notebooks"):
    out = Path(output_dir)
    out.mkdir(exist_ok=True)

    for nb in notebooks:
        nb = Path(nb)
        print(f"Running {nb}...")
        run_notebook(nb, out / nb.name)
        print(f"Finished {nb} \n")

if __name__ == "__main__":
    notebooks = [
        "00_check_file_length_and_merge.ipynb",
        "01_add_global_to_local_orientation.ipynb",
        "02_detect_gait_annotations.ipynb",
        "03_deep_learning_prep_data.ipynb",
        "04_calculate_combine_statistical_features.ipynb",
        "05_clean_up.ipynb",
        "06_xgb_statistical.ipynb",
        "07_deep_learning_model.ipynb",
    ]
    run_all_notebooks(notebooks)