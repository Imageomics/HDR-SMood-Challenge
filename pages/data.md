# Beetles as Sentinel Taxa: Data

This challenge uses images and metadata associated with [carabid beetle](https://en.wikipedia.org/wiki/Ground_beetle) specimens collected by the [National Ecological Observatory Network (NEON)](https://www.neonscience.org/) for the "Ground beetles sampled from pitfall traps" data product (DP1.10022.001, [RELEASE-2025](https://doi.org/10.48443/cd21-q875)) to predict drought conditions at the location and time of sampling. 

For this challenge, drought was characterized for each beetle sampling event using values of the Standardized Precipitation Evapotranspiration Index (SPEI) retrieved from the [GRIDMET Drought image collection](https://developers.google.com/earth-engine/datasets/catalog/GRIDMET_DROUGHT#description) (see [Abatzoglou (2011)](https://doi.org/10.1002/joc.3413).

All data are licensed under <<get NEON preferred license infromation from Christine>>.

## General Overview of Inputs and Expected Outputs

**Model inputs** will be a flat metadata table (csv format) where each row is a metadata record for a specimen image. Multiple images will be associated with a sampling `event_id`, where a "sampleing event" corresponds with a location (NEON Site ID) and the date on which the beetle specimens were collected. Thus, multiple input records (multiple images of beetle specimens) will be used to predict a single SPEI value at a given site on a given date. Note that `event_id`s will be anonymized in the test dataset, but the metadata will include `site_id` and `collect_date` in the training data. 

**What to predict:** The SPEI metrics represent cumulative drought conditions over a time window. For this challenge, participants will submit predictions for SPEI metrics representing three different time scales: 
- `spei_30d` is drought conditions calculated from data for the 30 day window preceding sample collection
- `spei_1y` is the drought condition calculated from the year preceding sample collection
- `spei_2y` is the drought condition calculated from the two years preceding sample collection

**The submission file** will be a long-format flat table (csv file format) with a prediction for each `spei_30d`, `spei_1y`, and `spei_2y` for each `event_id`. Predictions will include a measure of uncertainty, so each prediction will include `mu` (mean) and `sigma` (standard deviation). See the example submission below for more details. 

## Instructions to Download Training Data

<<needs updating for beetle ml process, once we have it developed>>

First, install the downloader in your virtual environment:
```bash
pip install git+https://github.com/Imageomics/cautious-robot
```
Then download <<link to training data csv>> and run: 
```bash
cautious-robot -i <path/to/beetle_ml_train.csv> -o <path/to/images> -s hybrid_stat -v md5
```

This will create subfolders ...
<<are we going to provide a download of the images, or just a metadata file with image URIs?>>




## Additional Information About the CSV File

Following the above steps, participants will obtain a csv metadata file with `image_uri`s linking to the specimen images. Each record (row) is metadata for a single specimen image. The training dataset will include all the fields described in the schema below. The test dataset will only include `event_id` (anonymized), `domain_id`, `scientific_name`, and `image_uri`.

<<We can update this as appropriate if we are going to add metadata about the image, like image quality flags etc. Also, I'm unclear on whether we're going to provide a download of the image files to participants, or just give them a table with image_uris>>

### Data Fields
| fieldName | description | dataType | relatedTerms |
|---|---|---|---|
| event_id | An (anonymized) identifier for the set of information associated with the event, which includes information about the place and time of the event | string | [DWC_v2009-04-24:eventID](http://rs.tdwg.org/dwc/terms/history/index.htm#eventID-2009-04-24)
| collect_date | Date of the collection event | dateTime | [DWC_v2009-04-24:eventDate](http://rs.tdwg.org/dwc/terms/history/index.htm#eventDate-2009-04-24)
| domain_id | Unique identifier of the NEON domain | string | [DWC_v2009-04-24:locationID](http://rs.tdwg.org/dwc/terms/history/index.htm#locationID-2009-04-24)
| site_id | NEON site code | string | [DWC_v2009-04-24:locationID](http://rs.tdwg.org/dwc/terms/history/index.htm#locationID-2009-04-24)
| scientific_name | Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined | string | [DWC_v2009-04-24:scientificName](http://tdwg.github.io/dwc/terms/history/index.htm#scientificName-2009-09-21)
| image_id | Unique identifier for image | string  | |
| image_uri | Location of image media resource (link to image) | string | |
| spei_30d | Target variable: SPEI calculated over a short timescale (1 month), reflecting short-term moisture conditions. | real | |
| spei_1y | Target variable: SPEI calculated over a medium timescale (1 year), reflecting seasonal precipitation patterns. | real | |
| spei_2y | Target variable: SPEI calculated over a long timescale (2 years), reflecting long-term hydrological conditions. | real | |


## Submission Samples

Participants can download sample submissions with the baseline algorithms (`DinoV2` and `BioCLIP` based) from the "Files" tab.
