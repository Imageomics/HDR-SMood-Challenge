# Beetles as Sentinel Taxa: Predicting drought conditions from NEON specimen imagery
### Brought to you by Imageomics Institute and NEON as part of the 2025 HDR ML Challenge

## Introduction 

Climate change is increasing the frequency and severity of drought events globally, posing significant threats to ecosystems, agriculture, water resources, and human societies ([IPCC, 2022](https://www.ipcc.ch/report/ar6/wg2/)). Effective monitoring and prediction of drought conditions are crucial for mitigation and adaptation strategies. While traditional drought monitoring relies on meteorological and hydrological data, ecological indicators can provide complementary insights into ecologically significant on-the-ground impacts of water stress.

Insects, particularly ground beetles (Coleoptera: Carabidae), are well-established bioindicators due to their sensitivity to environmental changes (including moisture availability), high diversity, and relative ease of sampling ([Lövei and Sunderland 1996](https://doi.org/10.1146/annurev.en.41.010196.001311); [Rainio & Niemelä, 2003](https://doi.org/10.1023/A:1022412617568)). This widespread beetle family has been used to evaluate changes in landscape and local environmental conditions following natural and anthropogenic disturbances, including climate change ([Muller-Kroehling et al. 2014](https://www.zobodat.at/pdf/Angewandte-Carabidologie_10_0097-0100.pdf); [Qiu et al. 2023](https://doi.org/10.1111/geb.13670)) and drought ([Weiss et al. 2024a](https://doi.org/10.1007/s10980-024-01920-1),[b](https://doi.org/10.1111/ecog.07020)). While responses to these disturbances can be captured by changes in their abundance and composition, morphological and ecological traits are increasingly used to characterize communities because they give insight into why species respond to change ([Cadotte et al. 2015](https://doi.org/10.1016/j.tree.2015.07.001); [Fountain-Jones et al. 2015](https://doi.org/10.1111/een.12158); [Moretti et al. 2017](https://doi.org/10.1111/1365-2435.12776)).

The [National Ecological Observatory Network (NEON)](https://www.neonscience.org/) provides unprecedented, standardized ecological data across the United States, including systematic collections of carabid beetles ([DP1.10022.001](https://data.neonscience.org/data-products/DP1.10022.001)) from diverse terrestrial ecosystems ([Thorpe et al., 2016]( https://doi.org/10.1002/ecs2.1627)). These collections, housed in the [NEON Biorepository](https://biorepo.neonscience.org), include high-resolution images of individual specimens. This challenge leverages this unique resource to explore a novel approach to environmental monitoring.

## Setup Overview
The goal of this challenge is to predict the drought status at a location on a specific date based on images of carabid beetle specimens collected at the location on that date. This will be an out-of-sample challenge because training data will be assembled from one set of locations, with test data coming from a different set of locations. All locations will be NEON sites.

This challenge will provide insight about how well carabid beetles can serve as indicator taxa to understand local drought conditions. It will also help ecologists better understand how inter- and intra-specific variation in carabid traits correspond with local environmental conditions, and over what time scales. We expect trait variations among specimens can be detected in the imagery and linked to drought metrics using AI/ML models. If these models perform better than benchmark models (e.g., historical mean drought condition at a site for the given day-of-year, or models using only metadata), it suggests there is ecologically relevant information that can be extracted from specimen images and linked to environmental data.

### Algorithm requirement
Participants are tasked with predicting the Standardized Precipitation Evapotranspiration Index (SPEI) metric, which represents cumulative drought conditions over a specified time window. For this challenge, participants will be provided with images of beetle specimens collected at a particular location during a sampling event. Based on these images, they must predict values of the SPEI metric for three time windows:

- `spei_30d`: drought condition calculated from data for the 30 day window preceding sample collection.
- `spei_1y`: drought condition calculated from the year preceding sample collection.
- `spei_2y`: drought condition calculated from the two years preceding sample collection.

### Training data
The training data comprises images from beetle specimens and a metadata file that indicates the location and date each specimen was collected, its scientific name, and the values of the three SPEI metrics at the sampling location on the collection date. 

### Test data
Test data will include images of beetle specimens and limited metadata. The metadata file will indicate an anonymized sampling `eventId` associated with each specimen, along with the specimen's scientific name and the anonymized eco-climatic domain of the collection site (but not the site ID or location). The collection date and the SPEI values will not be provided in the test dataset.

## Timeline

This ML Challenge starts on August 13, 2025, and will run through October 31, 2025. Be sure to resubmit your preferred model from the development phase by October 31, 2025 at 11:59pm [AOE](https://www.timeanddate.com/time/zones/aoe); it will then be run on the final test sets. Only one submission will be run against the test sets to determine your final score in the challenge.


This challenge was generated based on the [Imageomics/HDR-anomaly-challenge](https://github.com/Imageomics/HDR-anomaly-challenge), which used the [CodaBench Iris Sample Bundle](https://github.com/codalab/competition-examples/tree/master/codabench/iris/bundle); full formatting and challenge design process can be found in the [challenge repo on GitHub](https://github.com/Imageomics/HDR-SMood-Challenge).
