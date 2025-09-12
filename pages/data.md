# Beetles as Sentinel Taxa: Data

This challenge uses images and metadata associated with [carabid beetle](https://en.wikipedia.org/wiki/Ground_beetle) specimens collected by the [National Ecological Observatory Network (NEON)](https://www.neonscience.org/) for the "Ground beetles sampled from pitfall traps" data product (DP1.10022.001, [RELEASE-2025](https://doi.org/10.48443/cd21-q875)) to predict drought conditions at the location and time of sampling. 

For this challenge, drought was characterized for each beetle sampling event using values of the Standardized Precipitation Evapotranspiration Index (SPEI) retrieved from the [GRIDMET Drought image collection](https://developers.google.com/earth-engine/datasets/catalog/GRIDMET_DROUGHT#description) (see [Abatzoglou (2011)](https://doi.org/10.1002/joc.3413)).

All data are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## General Overview of Inputs and Expected Outputs

**Model inputs** will be a flat metadata table (CSV format) where each row is a metadata record for a specimen image. Multiple images will be associated with a sampling `eventID`, where a "sampling event" corresponds with a location (NEON Site ID) and the date on which the beetle specimens were collected. Thus, multiple input records (multiple images of beetle specimens) will be used to predict a single SPEI value at a given site on a given date. Note that `eventID`s will be anonymized in the test dataset, but the metadata will include `siteID` and `collectDate` in the training data. 

**What to predict:** The SPEI metrics represent cumulative drought conditions over a time window. For this challenge, participants will submit predictions for SPEI metrics representing three different time scales: 
- `SPEI_30d` is the drought condition calculated from data for the 30 day window preceding sample collection.
- `SPEI_1y` is the drought condition calculated from the year preceding sample collection.
- `SPEI_2y` is the drought condition calculated from the two years preceding sample collection.

**The submission file** will be a zip file containing the model weights, `model.py`, and `requirements.txt`. The `model.py` should contain a `Model` class with the methods `load` (to setup and load the model) and `predict` that takes a list of Python dictionaries as input. The list of dictionaries contains information for a single collection event. The dictionaries will contain the following keys:

`relative_img`: the `PIL.Image` of the beetle

`colorpicker_img`: the `PIL.Image` of the color calibration card

`scalebar_img`: the `PIL.Image` of the scalebar

`scientificName`: (str) the scientific name of the give beetle

`domainID`: (int) the domain ID (anonymized) where the beetle was collected

The `predict` method should return a dictionary containing keys for each `SPEI_30d`, `SPEI_1y`, and `SPEI_2y`. Predictions will include a measure of uncertainty, so each prediction will include `mu` (mean) and `sigma` (standard deviation). The output will look like:
```
{
    "SPEI_30d": {
        "mu" : 1.2,
        "sigma" : 0.1,
    },
    "SPEI_1y": {
        "mu" : -0.3,
        "sigma" : 0.7,
    },
    "SPEI_2y": {
        "mu" : 2.2,
        "sigma" : 0.3,
    },
}
```


See the example submissions at https://github.com/Imageomics/HDR-SMood-Challenge-sample for more details. 

## Instructions to Download Training Data

The challenge training data is available on Hugging Face, from [imageomics/sentinel-beetles](https://huggingface.co/datasets/imageomics/sentinel-beetles). Please follow the directions provided in the dataset card to access the data, and open a [discussion](https://huggingface.co/datasets/imageomics/sentinel-beetles/discussions) if you encounter any issues. Note that the data will not be made available until the official launch of the challenge.


## Additional Information About the CSV File

The CSV metadata file (included in the [Hugging Face repository](https://huggingface.co/datasets/imageomics/sentinel-beetles/)) has `relative_img_loc`s linking to the specimen images. Each record (row) is metadata for a single specimen image. The training dataset will include all the fields described in the schema below. The validation and challenge (test) datasets will only include `eventID` (anonymized), `domainID` (anonymized), `scientificName`, and `relative_img_loc`.

See [Data Fields](#data-fields), below, or the [dataset](https://huggingface.co/datasets/imageomics/sentinel-beetles/), itself, for more information on these terms.


### Data Fields
| fieldName | description | dataType | relatedTerms |
|---|---|---|---|
| eventID | An (anonymized) identifier for the set of information associated with the event, which includes information about the place and time of the event | string | [DWC_v2009-04-24:eventID](http://rs.tdwg.org/dwc/terms/history/index.htm#eventID-2009-04-24)
| collectDate | Date of the collection event | dateTime | [DWC_v2009-04-24:eventDate](http://rs.tdwg.org/dwc/terms/history/index.htm#eventDate-2009-04-24)
| domainID | Unique identifier (anonymized) of the NEON domain | string | [DWC_v2009-04-24:locationID](http://rs.tdwg.org/dwc/terms/history/index.htm#locationID-2009-04-24)
| siteID | NEON site code (anonymized) | string | [DWC_v2009-04-24:locationID](http://rs.tdwg.org/dwc/terms/history/index.htm#locationID-2009-04-24)
| scientificName | Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined | string | [DWC_v2009-04-24:scientificName](http://tdwg.github.io/dwc/terms/history/index.htm#scientificName-2009-09-21)
| public_id | Unique identifier for image | string  | |
| relative_img_loc | Beetle image location within the beetle images folder (flattened_images) | string | |
| colorpicker_path | Color card image location within the color card and scale images folder (color_and_scale_images) | string | |
| scalebar_path | Scale image location within the color card and scale images folder (color_and_scale_images) | string | |
| SPEI_30d | Target variable: SPEI calculated over a short timescale (1 month), reflecting short-term moisture conditions. | real | |
| SPEI_1y | Target variable: SPEI calculated over a medium timescale (1 year), reflecting seasonal precipitation patterns. | real | |
| SPEI_2y | Target variable: SPEI calculated over a long timescale (2 years), reflecting long-term hydrological conditions. | real | |


## Submission Samples

Participants can download sample submissions with the baseline algorithms (`DinoV2` and `BioCLIPV2` based) from the "Files" tab.
