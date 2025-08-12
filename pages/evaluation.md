# Beetles as Sentinel Taxa: Evaluation
This challenge is an out-of-sample prediction challenge. The goal is to predict the drought status at a location on a specific date based on images of carabid beetle specimens collected at the location on that date. This will be an out-of-sample challenge because training data will be assembled from one site of locations, and test data will be assembled from a different set of locations. All locations will be NEON sites.

This challenge will provide insight about how well carabid beetles can serve as an indicator taxa to understand local drought conditions. This challenge will help ecologists better understand how inter- and intra-specific variation in carabid traits correspond with local environmental conditions, and over what time scales. We expect trait variations among specimens can be detected in the imagery and linked to drought metrics using AI/ML models. If these models perform better than benchmark models (e.g., historical mean drought condition at a site for the given day-of-year, or models using only metadata), it suggests there is ecologically relevant trait information that can be extracted from specimen images and linked to environmental data. 

**What to predict:** The Standardized Precipitation Evapotranspiration Index (SPEI) metric represents cumulative drought conditions over a time window. For this challenge, participants will submit predictions for SPEI metrics for specific sampling events, where the SPEI values were calculated using three different time windows preceeding the sampleing event to represent three different temporal scales over which different types of ecological processes may be affected: 
- `spei_30d` is the drought condition calculated from data for the 30 day window preceding sample collection.
- `spei_1y` is the drought condition calculated from the year preceding sample collection.
- `spei_2y` is the drought condition calculated from the two years preceding sample collection.

**The submission file** will be a long-format flat table (csv file format) with a prediction for each `spei_30d`, `spei_1y`, and `spei_2y` for each `event_id`. Predictions will include a measure of uncertainty, so each prediction will include `mu` (mean) and `sigma` (standard devation). See the example submissoin below for more details. 

## The Test Dataset
This test data set comprises:
- An image collection of carabid beetle specimens.
- A metadata table

### Data Fields in the Metadata Table
| fieldName | description | dataType | relatedTerms |
|---|---|---|---|
| event_id | An (anonymized) identifier for the set of information associated with the event, which includes information about the place and time of the event | string | [DWC_v2009-04-24:eventID](http://rs.tdwg.org/dwc/terms/history/index.htm#eventID-2009-04-24)
| domain_id | Unique identifier of the NEON domain | string | [DWC_v2009-04-24:locationID](http://rs.tdwg.org/dwc/terms/history/index.htm#locationID-2009-04-24)
| scientific_name | Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined | string | [DWC_v2009-04-24:scientificName](http://tdwg.github.io/dwc/terms/history/index.htm#scientificName-2009-09-21)
| image_id | Unique identifier for image | string  | |
| image_uri | Location of image media resource (link to image) | string | |

## Evaluation Phases
There are 2 phases. Each test data set is split into a development set and a final test set (the challenge dataset).  
1. **Development phase:**
	* The provided training data contains:
		- Images of carabid beetle specimens from various species, collection sites, and dates.
		- A metadata CSV including SPEI values corresponding with each of the `eventId`s in the training dataset. 
	* The goal is to develop an algorithm to predict each of the three SPEI values for an `eventId` given the images of beetles collected during that sampling event.
	* Upload your model: feedback will be provided on the development set until the end of the challenge; one submission is allowed per day.
		1. CRPS values (see below for more details) will be returned for all predictions (you can calculate the scores yourself, but we will provide a scoring dashboard as well) 
	* Participants may submit _one_ score on the development sets to be displayed on the leaderboard. This score can be removed and replaced with a newer or better score as they choose.
2. **Final phase:**
	* This phase will start automatically at the end of the challenge.
 	* Be sure to submit your preferred algorithm as a final submission before the end of the challenge, as this will be the model run on the test data for final scores.
	* Each participant's last submission will be evaluated on the final test set and scores will be posted to the leaderboard. 

## Evaluation metric

This competition allows you to submit your developed algorithm, which will be run on the development and the final test dataset through CodaBench.

Your algorithm needs to generate three SPEI predictions (`spei_30d`, `spei_1y`, and `spei_2y`) for each `event_id` when given a collection of images of specimens collected during a given sampling `event_id`. 

Each prediction will be scored using the continuous rank probability score (CRPS), which provides a metric to evaluate both the accuracy and precision of a prediction when compared against an observed datapoint ([Gneiting and Raftery 2007](https://doi.org/10.1198/016214506000001437)). Here we use the convention where 0 is the best possible score, and CRPS values increase as prediction accuracy and precision decrease. This approach has been used successfully in forecasting challenges like the [NEON Ecological Forecasting Challenge](https://projects.ecoforecast.org/neon4cast-ci/) organized by the [Ecological Forecasting Initiative (EFI)](https://ecoforecast.org/) (see the documentation [here](https://projects.ecoforecast.org/neon4cast-docs/Evaluation.html)). Submissions to this challenge will be scored using the [`score4cast` R package](https://github.com/eco4cast/score4cast) developed by EFI. 

The CRPS values for a submission will be averaged across `eventId`s to produce an overall score, where the winning submission will have the lowest overall score. For the challenge, we will also post a leaderboard with sub-categories for each SPEI time scale (30 days, 1 year, 2 years). There will also be an extra-challenging "novel eco-domain" category, where beetle images and metadata from sampling events from an eco-domain that was not included in the training dataset will be provided as input as a true out-of-sample challenge. 

