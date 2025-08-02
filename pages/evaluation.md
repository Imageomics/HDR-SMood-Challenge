# Beetles as Sentinel Taxa: Evaluation
This challenge is an out-of-sample prediction challenge. The goal is to predict the drought status at a location on a specific date based on images of carabid beetle specimens collected at the location on that date. This will be an out-of-sample challenge because training data will be assembled from one site of locations, and test data will assembled from a different set of locations. All locations will be NEON sites.

This challenge will provide insight about how well carabid beetles can serve as an indicator taxa to understand local drought conditions. This challenge will help ecologists better understand how inter- and intra-specific variation in carabid traits correspond with local environmental conditions, and over what time scales. We expect trait variations among specimens can be detected in the imagery and linked to drought metrics using AI/ML models. If these models perform better than benchmark models (e.g., historical mean drought condition at a site for the given day-of-year, or models using only metadata), it suggests there is ecologically relevant information that can be extracted from specimen images and linked to environmental data. 

## The Test Dataset
This test data set comprises:
- An image collection of carabid beelte specimens.
- A metadata table

The goal of the challenge is to use a collection of images of carabid beetles collected during a sampling event (specimens collected at a given location on a given date) to predict the drought conditions at that site. 




## Evaluation Phases
There are 2 phases. Each test data set is split into a development set and a final test set.  
1. **Development phase:**
	* The provided training data contains:
		- Images of all Species A subspecies: these images are considered "normal" (not anomaly) cases.
		- A signal set comprising the most common hybrid: these images are considered anomaly cases.*
	* The goal is to develop an algorithm to detect hybrid instances (the anomaly cases).
	* Upload your model: feedback will be provided on the development set until the end of the challenge; one submission is allowed per day.
		1. Detect signal and non-signal hybrid subspecies of Species A. 
		2. Detect subspecies hybrids among the mimic Species B (Species B subspecies are mimics of the Species A signal hybrid parent subspecies).
	* Participants may submit _one_ score on the development sets to be displayed on the leaderboard. This score can be removed and replaced with a newer or better score as they choose.
2. **Final phase:**
	* This phase will start automatically at the end of the challenge.
 	* Be sure to submit your preferred algorithm as a final submission before the end of the challenge, as this will be the model run on the test data for final scores.
	* Each participant's last submission will be evaluated on the final test set and scores will be posted to the leaderboard. 

## Evaluation metric

This competition allows you to submit your developed algorithm, which will be run on the development and the final test dataset through CodaBench.

Your algorithm needs to generate three SPEI predictions for each `event_id`, where each `event_id` will have a collection of several images of carabid beetle specimens that were collected at that location on that date: 

Each prediction will be scored using the Continuous Rank Probability Score (CRPS)

The submissions are evaluated based on two metrics:
- The true positive rate (TPR) at the true negative rate (TNR) = 95%: the recall of hybrid cases, with a score threshold set to recognizing non-hybrid cases with 95% accuracy.
- PRC AUC


\*  Note that these hybrids are just the most common within this particular dataset, not necessarily in general.
