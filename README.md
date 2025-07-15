# Harnessing the Data Revolution (HDR) Scientific Mood (Modeling out of Distribution) ML Challenge
Repository for [Imageomics' CodaBench challenge]() as part of the broader [HDR Scientific Mood ML Challenge](https://www.nsfhdr.org/mlchallenge-y2).

We use the same base container as the challenges from the three other HDR Institutes; it is available [Coming Soon](). There are options to use packages not included in this container as long as they are in the [pre-approved list](ingestion_program/whitelist.txt); if your solution requires a package not listed there, please open an [issue](https://github.com/Imageomics/HDR-SMood-challenge/issues) to request it (provided it is not already requested by someone else).

For more details on participating in the challenge, please see the pages in the [CodaBench challenge]() itself.

### To-Do

This repo is still under development as we construct the Y2 SMood Challenge: Beetles as Sentinel Taxa.
- Update [pages/](pages) to describe Beetle Challenge.
- Add metadata and image baselines.
- Update ingestion and scoring programs for the format of this challenge (multiple images used for prediction).
- Files may have the training CSV or other training data information--not to be added until start of challenge.
- Input and Reference data will not be added until after challenge ends (maintained in private repo until then).

## Full Bundle Structure

```
baselines/
    XX_code_submission/
        # Zip the contents of this folder to submit this baseline to the challenge on CodaBench
        clf.pkl
        metadata
        model.py
        requirements.txt
competition.yaml
files/
    ????
Imageomics_logo_butterfly.png
ingestion_program/
    ingestion.py
    metadata.yaml
    whitelist.txt
input_data/
    # Images used for testing submitted models (images must be zipped together directly under input_data, not within a subfolder (`val.zip`, `test.zip`)
pages/
    # These will be all the optional tabs under "Get Started" on the challenge page. They are used to describe the challenge for participants
    data.md
    evaluation.md
    overview.md
    starting_kit.md
    terms.md
reference_data/
    # Labels for the images in input_data/. Can be .txt, .csv, etc.
scoring_program/
    metadata.yaml
    score_combined.py
```

### Notes on Structure

- The base container specified in the `competition.yaml` must have the requirements for the ingestion and scoring programs. These can be manually imported through a `requirements.txt`, but then each of these files will need to do so at the beginning. It is better to install these requirements in the base container and allow for participants to include a requirements file with their model's needed programs.
  - Example: For this challenge, our container must have (at minimum) `pillow`, `pandas`, and `tqdm`. The base container used for this competition will be provided.
  - Any requirements used by participants must be on the approved whitelist (or participants must reach out to request their addition) for security purposes.
- Scores must be saved to a `score.json` file where the keys detailed in the `Leaderboard` section of the `competition.yaml` are give as the keys for the scores.
- This full collection of files and folders is zipped as-is to upload the bundle to CodaBench.
- `run.sh` is a bash script to simulate the scoring process used for the Leaderboard on your local machine. This works by first building the docker container, and then running the bash script within the virtual environment. The script will
  -  Create a folder `/ref` for the CSV ground truth file and a folder `/res` for the generated prediction txt file.
  -  Run `ingestion_program/ingestion.py` to get the predictions from your model and output the predictions to the txt file.
  -  Run `scoring_program/score_combined.py` to evaluate the predictions by comparing to the ground truth. The final scores are then written to a JSON file.
- To test with `run.sh`, you should provide your own curated validation dataset (e.g. subsampling from train split) including images and a simulated ground truth file.
