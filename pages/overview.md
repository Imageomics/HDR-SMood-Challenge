# Beetles as Sentinel Taxa: Predicting drought conditions from NEON specimen imagery
### Brought to you by Imageomics Institute as part of the 2025 HDR ML Challenge


## Introduction 

Climate change is increasing the frequency and severity of drought events globally, posing significant threats to ecosystems, agriculture, water resources, and human societies ([IPCC, 2022](https://www.ipcc.ch/report/ar6/wg2/)). Effective monitoring and prediction of drought conditions are crucial for mitigation and adaptation strategies. While traditional drought monitoring relies on meteorological and hydrological data, ecological indicators can provide complementary insights into ecologically significant on-the-ground impacts of water stress.

Insects, particularly ground beetles (Coleoptera: Carabidae), are well-established bioindicators due to their sensitivity to environmental changes (including moisture availability), high diversity, and relative ease of sampling ([Lövei and Sunderland 1996](https://doi.org/10.1146/annurev.en.41.010196.001311); [Rainio & Niemelä, 2003](https://doi.org/10.1023/A:1022412617568)). This widespread beetle family has been used to evaluate changes in landscape and local environmental conditions following natural and anthropogenic disturbances, including climate change ([Muller-Kroehling et al. 2014](https://www.zobodat.at/pdf/Angewandte-Carabidologie_10_0097-0100.pdf); [Qiu et al. 2023](https://doi.org/10.1111/geb.13670)) and drought (Weiss et al. 2024a,b). While responses to these disturbances can be captured by changes in their abundance and composition, morphological and ecological traits are increasingly used to characterize communities because they give insight into why species respond to change ([Cadotte et al. 2015](https://doi.org/10.1016/j.tree.2015.07.001); [Fountain-Jones et al. 2015](https://doi.org/10.1111/een.12158); [Moretti et al. 2017](https://doi.org/10.1111/1365-2435.12776)).

The National Ecological Observatory Network (NEON) provides unprecedented, standardized ecological data across the United States, including systematic collections of carabid beetles from diverse terrestrial ecosystems ([Thorpe et al., 2016]( https://doi.org/10.1002/ecs2.1627)). These collections, housed in the NEON Biorepository, include high-resolution images of individual specimens. This challenge leverages this unique resource to explore a novel approach to environmental monitoring.



## Setup Overview
This challenge is designed to simulate a real-world biological scenario. Suppose a biologist studies a particular butterfly Species A with many subspecies. One day, the biologist finds that a subset of the images collected looks slightly abnormal in their visual appearance. The biologist does not recognize the pattern as belonging to any of the subspecies on which their research is focused. After investigation, the biologist finds that these unusual samples are hybrids produced by different subspecies of Species A. Realizing that they may encounter other hybrids in future collections of images, the biologist seeks an anomaly detection algorithm to automatically identify (unseen) hybrid cases.

### Algorithm requirement
The developed anomaly detection algorithm needs to output an anomaly score (a real number) for each test image. The higher the score is, the more likely the image is an anomaly (i.e., hybrid).

### Training data
The training data comprises images from all the Species A subspecies and the most common hybrid. The most common* hybrid refers to a specific combination of the parent subspecies that has the most images. This hybrid is called the signal hybrid; other hybrids are called the non-signal hybrids.    

### Test data
We consider two sets of images in the test set:
- One from Species A, comprising images from all the Species A subspecies, the signal hybrid, and the non-signal hybrids.
- One from a mimicking Species B, comprising images from two subspecies of Species B and their hybrid. The two subspecies of Species B are the ones mimicking the parent subspecies of the signal hybrid of Species A.

## Timeline

This ML Challenge starts on September 11th, 2024, and will run through January 17th, 2025. Be sure to resubmit your preferred model from the development phase by January 17th at 11:59pm [AOE](https://www.timeanddate.com/time/zones/aoe); it will then be run on the final test sets. Only one submission will be run against the test sets to determine your final score in the challenge.


\*  Note that these hybrids are just the most common within this particular dataset, not necessarily in general.

**References and credits:** [Zenodo citations](https://github.com/Imageomics/HDR-anomaly-challenge/blob/main/butterfly_anomaly.bib).<br />
This challenge was generated based on the [CodaBench Iris Sample Bundle](https://github.com/codalab/competition-examples/tree/master/codabench/iris/bundle); full formatting and challenge design process can be found in the [challenge repo on GitHub](https://github.com/Imageomics/HDR-anomaly-challenge).
