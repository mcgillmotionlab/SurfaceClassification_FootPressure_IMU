README


# Pipeline for Preprocessing, Model Training, and Deployment


The following instructions are for the notebooks regarding the study using the Honda data. 
The working environment is found at 

code > Code from Honda Development > ...


### Step 1: Initial Data Processing

These notebooks are accessible within Folder 1.
Run Notebook 1a
- Ensure the data path points to the original folder containing all raw data.
- This notebook loads and organizes the data for further processing.

Run Notebook 1b
This step merges and creates datasets separately for:
- IMU sensors
- Insole sensors
The output datasets will be used for segmentation in the next step.

### Step 2: Choose a Segmentation Method

Depending on your segmentation approach, select the appropriate folder:
- Folder 2 → Contains Insole Based Gait Cycle Segmentations
- Folder 3 → Contains Random Sampled Sliding Window Segmentations
Make sure to choose the folder that aligns with your analysis goals.

### Step 3: Process Segmentation

Once a segmentation method is selected, process the data using the corresponding segmentation notebooks:

For insole segmentation:
- Run Notebook 2a → Processes segmentation for IMU datasets
- Run Notebook 2b → Processes segmentation for Insole datasets

For random sampled segmentation:
- Run Notebook 3a → Processes segmentation for IMU datasets
- Run Notebook 3b → Processes segmentation for Insole datasets


### Step 4: Train the Models

Navigate to the Model Notebooks section.
Run the notebooks to train the various model combinations used in the study.
Fine-tune and validate models as needed before deployment.
