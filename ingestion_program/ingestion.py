#!/usr/bin/env python
# Copied description and defaults from codabench/iris/bundle/ingestion_program/ingestion.py

# Usage: python ingestion.py input_dir output_dir ingestion_program_dir submission_program_dir

# AS A PARTICIPANT, DO NOT MODIFY THIS CODE.
#
# This is the "ingestion program" written by the organizers.
# This program also runs on the challenge platform to test your code.
#
# ALL INFORMATION, SOFTWARE, DOCUMENTATION, AND DATA ARE PROVIDED "AS-IS".
# ISABELLE GUYON, CHALEARN, AND/OR OTHER ORGANIZERS OR CODE AUTHORS DISCLAIM
# ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY PARTICULAR PURPOSE, AND THE
# WARRANTY OF NON-INFRIGEMENT OF ANY THIRD PARTY'S INTELLECTUAL PROPERTY RIGHTS.
# IN NO EVENT SHALL ISABELLE GUYON AND/OR OTHER ORGANIZERS BE LIABLE FOR ANY SPECIAL,
# INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF SOFTWARE, DOCUMENTS, MATERIALS,
# PUBLICATIONS, OR INFORMATION MADE AVAILABLE FOR THE CHALLENGE.
#
# Main contributors: Isabelle Guyon and Arthur Pesah, March-October 2014
# Lukasz Romaszko April 2015
# Originally inspired by code code: Ben Hamner, Kaggle, March 2013
# Modified by Ivan Judson and Christophe Poulain, Microsoft, December 2013
# Last modifications Isabelle Guyon, October 2017

# ===== Begin Imageomics modifications =====
import os
import re
from sys import argv, path, executable, exit
import subprocess
import time
from datetime import datetime, timezone
from packaging.version import Version, InvalidVersion
import pandas as pd
import csv

def install_from_whitelist(req_file, program_dir):
    whitelist = open(os.path.join(program_dir,"whitelist.txt"), 'r').readlines()
    whitelist = [i.rstrip('\n') for i in whitelist]

    for package in open(req_file, 'r').readlines():
        package = package.rstrip('\n')
        package_version = package.split("==")
        if len(package_version) > 2:
            # invalid format, don't use
            print(f"requested package {package} has invalid format, will install latest version (of {package_version[0]}) if allowed")
            package = package_version[0]
        elif len(package_version) == 2:
            version_str = package_version[1]
            try:
                 Version(version_str)
            except InvalidVersion:
                 exit(f"requested package {package} has invalid version, please check that {version_str} is the correct version of {package_version[0]}.")

        if package_version[0] in whitelist:
            # package must be in whitelist, so format check unnecessary
            subprocess.check_call([executable, "-m", "pip", "install", package])
            print(f"{package_version[0]} installed")
        else:
            exit(f"{package_version[0]} is not an allowed package. Please contact the organizers on GitHub to request acceptance of the package.")

def is_image_extension(path):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    return os.path.splitext(path)[-1].lower() in image_extensions

def process_prediction(prediction, event_id):
    """
    Check if the score is valid.
    If the score is not valid, throw exception and exit; else return the formatted score.
    """
    VAR_KEYS = {'SPEI_30d', 'SPEI_1y', 'SPEI_2y'}
    PARAM_KEYS = {'mu', 'sigma'}
    if isinstance(prediction, dict) and len(prediction) == len(VAR_KEYS) and VAR_KEYS == prediction.keys():
        pred_output = []
        for var in VAR_KEYS:
            param_pred = prediction[var]
            if isinstance(param_pred, dict) and len(param_pred) == len(PARAM_KEYS) and PARAM_KEYS == param_pred.keys():
                for param in PARAM_KEYS:
                    if isinstance(param_pred[param], float):
                        final_pred = round(param_pred[param], 4)
                        pred_output.append([event_id, var, param, final_pred])
                    else:
                        exit(f"Invalid prediction format. Prediction values should be floats.")
            else:
                exit(f"Invalid prediction format. Mean and std keys for each SPEI should be {PARAM_KEYS}.")
        return pred_output
    else:
        exit(f"Invalid prediction format. SPEI keys should be {VAR_KEYS}.")
    

if __name__ == "__main__":
    
    print("We're running ingestion")

    # Get the current UTC time
    current_time_utc = datetime.now(timezone.utc)
    # Print the timestamp in UTC
    print("Current UTC Time:", current_time_utc.strftime('%Y-%m-%d %H:%M:%S'))

    ### INPUT/OUTPUT: Get input and output directory names
    input_dir = os.path.abspath(argv[1])
    output_dir = os.path.abspath(argv[2])
    program_dir = os.path.abspath(argv[3])
    submission_dir = os.path.abspath(argv[4])
    
    print("Using input_dir: " + input_dir)
    print("Using output_dir: " + output_dir)
    print("Using program_dir: " + program_dir)
    print("Using submission_dir: " + submission_dir)

    path.append(program_dir) # In order to access libraries from our own code
    path.append(submission_dir) # In order to access libraries of the user

    start = time.time()
    requirements_file = os.path.join(submission_dir, "requirements.txt")
    if os.path.isfile(requirements_file):
        install_from_whitelist(requirements_file, program_dir)
    end = time.time()

    elapsed = time.strftime("%H:%M:%S", time.gmtime(end - start))

    print(f"pip handling packages takes {elapsed}.")

    # Import remaining packages
    from PIL import Image
    from tqdm import tqdm

    from model import Model
    

    print("model imported")
    submit_model = Model()
    submit_model.load()

    if hasattr(submit_model, "device"):
        print(f"model running on device: {submit_model.device}")
    
    # Load metadata
    metadata = pd.read_csv(os.path.join(input_dir, "input.csv"), dtype={"relative_img_loc": str, "colorpicker_path": str, "scalebar_path": str, "scientificName": str, "domainID": int, "eventID": int})
    # Group metadata by event_id
    grouped_metadata = metadata.groupby('eventID')
    with open(os.path.join(output_dir, "predictions.csv"), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["eventID","variable","parameter","prediction"])
        start = time.time()
        for event_id, group in tqdm(grouped_metadata, total=len(grouped_metadata)):
            event = []
            for row in group.itertuples(index=False):
                relative_img_filepath = os.path.join(input_dir, row.relative_img_loc)
                relative_img = Image.open(relative_img_filepath)
                colorpicker_img_filepath = os.path.join(input_dir, row.colorpicker_path)
                colorpicker_img = Image.open(colorpicker_img_filepath)
                scalebar_img_filepath = os.path.join(input_dir, row.scalebar_path)
                scalebar_img = Image.open(scalebar_img_filepath)
                # 'domainID','scientificName','relative_img_loc','colorpicker_path','scalebar_path'
                event.append({'relative_img':relative_img, 'colorpicker_img': colorpicker_img, 'scalebar_img': scalebar_img, 'scientificName': row.scientificName, 'domainID':row.domainID})
            prediction = submit_model.predict(event)
            pred_output = process_prediction(prediction, event_id)
            writer.writerows(pred_output)

        end = time.time()
        elapsed = time.strftime("%H:%M:%S", time.gmtime(end - start))

        print(f"model inference takes {elapsed}.")