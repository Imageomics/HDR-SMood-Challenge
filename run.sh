#!/bin/bash
: <<'END_COMMENT'
1. Set Up the Environment:
        1.1 Pull the Docker image:
        docker pull ytchou97/hdr-image:latest

        1.2 Run the container:
            a) If use a GPU:
            docker run -it --gpus device=0 -v [repo_path]:/codabench [image_id] /bin/bash
            b) If only use CPU:
            docker run -it -v [repo_path]:/codabench [image_id] /bin/bash

2. Edit and Then Run the Script
    cd codabench
    chmod +x run.sh
    ./run.sh

END_COMMENT

# predict;evaluate
task_type=";evaluate" 

task_folder="validation"

# Get the predictions
if [[ "$task_type" == *"predict"* ]]; then
    input_dir="input_data/$task_folder" # This is the directory you put the images in.
    output_dir="sample_result_submission/$task_folder/res" # The prediction file will output to this directory.
    program_dir="ingestion_program"
    submission_dir="baselines/dummy_code_submission"
    python3 ingestion_program/ingestion.py $input_dir $output_dir $program_dir $submission_dir
fi

# Score the predictions
if [[ "$task_type" == *"evaluate"* ]]; then
    input_dir="sample_result_submission/$task_folder"
    output_dir="sample_result_submission/$task_folder"
    Rscript scoring_program/score.R $input_dir $output_dir
fi