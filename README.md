# Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data

We show that clustering, i.e., unsupervised learning, of voltage characteristics, is in fact more challenging when done on a larger pool of electronic control units as several out-of-the-box clustering methods and metrics will fail to determine the correct number of clusters when exerted over a large dataset. An overview of the voltage dataset distribution using PCA-2 (Principal Component Analysis) is shown below.

<p align="center">
<img width="640" height="480" alt="PCA2_Cluster_Overview" src="https://github.com/user-attachments/assets/70e42d39-bb90-4eab-8383-fb19d8d8305c" />
</p>

To overcome this issue, we propose a new methodology that takes advantage of domain-specific constraints, which guide the search toward the correct number
of electronic control units in a car, or even in a larger pool of units from several cars. We introduce two new metrics: correctness, which measures the success ratio with respect to the constraints, and divergence, which measures the consistency of the clustering, and show that they provide a strong indication for the optimal number of clusters.

<p align="center">
<img width="7905" height="2380" alt="clustering_procedure_bis_bis" src="https://github.com/user-attachments/assets/123e3bfa-bd30-4ea8-a8a9-9575eb65d4b4" />
</p>

In this specific context, both metrics prove to be more reliable than the widely used Silhouette score, Davies-Bouldin and Calinski-Harabasz indexes. We successfully test our methodology on the largest dataset available today for in-vehicle voltage characteristics and discover new insights regarding the number of devices. In this repository we share only a part of the entire dataset, for two passenger vehicles, due to file size constraints.

# Repository 
The repository contains the python code required to reproduce the results from our work on the provided dataset voltage samples (Honda Civic, Dacia Duster). Steps to run all the provided code are detailed below.

### Prerequisites
To run the code, ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Jupyter Notebook](https://jupyter.org/)
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)

### Code
Once all prerequisites are installed, the following variables from the python code need to be customized:
- <b>data_path</b> <- set to your location following the example with the provided path
- <b>scaling</b> <- set to 0 (without) or 1 (with) for choosing without/with rescaling of voltage data that supports clustering improvements
- <b>nrows</b> <- set to 1600 (passenger cars) or 2400 (heavy industry vehicle) for chossing between number of data samples/file for passenger cars or the heavy industry vehicle

Then, all section from the notebook need to be run in order to get the results that are presented in our work.

### Dataset

To allow artificial intelligence algorithms to properly use the ECUPrint raw voltage data for CAN fingerprinting evaluation, we have refined this raw data, since the ECUPrint analysis was done using statistical features only (bit time, plateau time, mean voltage, maximum voltage), without any machine learning approach. Our intention to use the raw voltage data from the original dataset led to some challenges that we have encountered. Based on evaluation of the raw voltage samples for each ID, we have decided to align samples on the rising edge and limit the number of samples to 1600 for passenger cars and 2500 samples for the tractor. 

The updated dataset is called ECUPrint_Aligned, publicly available as archive file (.zip format) on the University website or OneDrive to everyone that endeavors to use it for ECU fingerprinting research topics.

#### Data links ####

File | Download | Notes
--- | :---------: | :----
**ECUPrint_Aligned.zip** | [link1 (University website)](http://localhost) <br /> [link2 (OneDrive)](https://1drv.ms/u/c/eab50b86f61a55f8/Ecyc_vTq6c1ArUZWDtkwfKcBQRwu3CvS3NjIqD9V-0yFNA?e=eqe2Sg) | Aligned ECUPrint CAN voltage samples, allocated per Vehicle, ECU and ID

More details related to the bit aligning concept, applied filters and insights related to the dataset structure and file contents are described below.

#### Concept ####

ECUPrint raw voltage data was collected from 10 vehicles, ranging from small cars to SUVs and a heavy-duty vehicle with a Pico Scope 5000 Series.

#### A - Raw Voltage data samples - ECUPrint ####

For each frame carrying a specific ID we have collected samples for an isolated dominant bit, i.e., a transition a transition from recessive to dominant state and back. In the original files from the ECUPrint dataset, the rising edges and falling edges from each dominant bit are not aligned at the same index. That is also why there is a variation of the index when the plateau state of the dominant bit is reached, as shown in the images below for the samples corresponding to ID 4F1 from Hyundai i20 (left image) and to ID 04EF0021 from the John Deere tractor data (right image).

<p>
<img alt="image" src="https://github.com/user-attachments/assets/75f58730-348d-418b-9814-a1d4a5fc1db0" width="49%" /> 
<img  alt="image" src="https://github.com/user-attachments/assets/05e6c156-cef8-429c-9e21-a8189906602d" width="49%" />
</p>

#### B - Raw Voltage data samples - ECU Aligned ####

<b> B.1 - Bit Alignment and File Content Harmonization </b> - We decided to align the bits for each ID at the same index, which led to a different number of samples per file. That is why, based on our analysis we decided to preserve only 1600 samples for passenger cars and 2500 samples for the tractor in order to have a common raw data structure and file content. Examples of aligned bit samples are shown in the images below. They correspond to ID 4F1 from Hyundai i20 (left image) and to ID 04EF0021 from the John Deere tractor data (right image).

<p>
<img alt="image" src="https://github.com/user-attachments/assets/d09b7c46-c076-460b-bc50-fd4301fafac4" width="49%" />
<img alt="image" src="https://github.com/user-attachments/assets/86ce5c36-4505-4de7-aa3a-c4d933c6a7e6" width="49%" />
</p>

<b> B.2 - Removal of Outliers (ACK Bits) </b> - Analyzing the bits from the ECUPrint dataset, we have found some outliers (acknowledge bits instead of genuine dominant bits) that were removed from the alignment process and are not part of the ECU Aligned (Datasets). An example is shown for one of the Honda Civic files that had different samples for ID 19B compared to all other files that had the right samples.

<p>
<img alt="image" src="https://github.com/user-attachments/assets/ee0c4277-6878-42bc-9cad-3c6314222680" width="49%"/>
</p>

<b> B.3 - Removal of Outliers (Non-Isolated Bits) </b> - For some IDs, the ECUPrint dataset does not contain single isolated dominant bits. The voltage samples for those bits had a continuous plateau level while for isolated bits, the file ends with the samples of the falling edge. These IDs were removed from the alignment process and are not part of the ECUPrint Aligned Dataset. An example is shown for ID 511 from the Dacia Duster that had different samples compared to all other IDs from the same ECU.

<p>
<img width="613" height="433" alt="image" src="https://github.com/user-attachments/assets/c883792b-93bc-45a5-a1eb-10bdb43caf42" />
</p>

<b>B.4 - Establishment of a New ECU Allocation </b> - Based on deep analysis of the voltage samples for all of the IDs, we found that there is a different number of ECUs for some vehicles compared to the determination from ECUPrint. There are two additional ECUs determined for the Ford Kuga and 1 additional ECU determined for the Ford Fiesta and Ford Ecosport while there is 1 ECU less for the Hyundai i20. This is also influenced by the usage of "Unclassified" voltage bits from ECUPrint dataset which were not grouped with a particular ECU since clock skew could not be determined for those IDs based on the collected frames. The updated ECU allocation from the ECU Aligned datasets provides the newly determined ground truth allocation of IDs to ECUs to the best of our knowledge.

Number | Vehicle | Model year | No. of IDs | No. of identified ECUs | Voltage bits 
---- | :------: | :-------: | :--------: | :--------: | :--------:
(i) | Honda Civic | 2012-2017 | 43 | 6 | 14,567
(ii) | Opel Corsa | 2006-2014 | 28 | 4 | 9,131
(iii) | Hyundai i20 | 2014-2020 | 40 | 6 | 17,767
(iv) | John Deere Tractor | 2010-2018 | 39 | 3 | 4,021
(v) | Dacia Duster | 2010-2017 | 11 | 3 | 8,942
(vi) | Dacia Logan | 2012-2019 | 45 | 6 | 31,297
(vii) | Hyundai ix35 | 2009-2015 | 26 | 6 | 19,856
(viii) | Ford Fiesta | 2017-2020 | 47 | 7 | 21,729
(ix) | Ford Kuga | 2013-2019 | 70 | 11 | 28,024
(x) | Ford Ecosport | 2018-2021 | 85 | 5 | 20,044
**Total** | **-** | **-** | **432** | **57** | **175,378**

#### Dataset Content ####

The dataset is structured as described below. We provide the raw CAN voltage samples measured with the PicoScope with a sample interval of 2 nanoseconds (sample rate was set to 500 MS/s). The dataset was collected after vehicle startup (cold engine) and is available as CAN voltages collected for 10 cars (175,378 sampled bits) with ECU allocation. Data is allocated to specific ECUs based on the analysis in our work. Note that this distribution is to the best we could ascertain based on our analysis, we do not claim this separation to be absolute.  

<b> Folder structure </b> 

**CAN voltage samples with ECU allocation** \
| \
|------ DUSTER \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|------ LOGAN \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|------ ECOSPORT \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|------ FIESTA \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU7\
|------ KUGA \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU7\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU8\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU9\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU10\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU11\
|------ CIVIC \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|------ I20 \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|------ IX35 \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU5\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU6\
|------ JOHNDEERE \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|------ CORSA \
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU1\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU2\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU3\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|----ECU4

Voltage data is stored in csv format and has some metadata included before the raw voltage samples. The metadata contains the following information in the first rows from each file:   

ID (hexadecimal)], \
[ID (decimal)], \
[DLC (decimal)], \
[Timestamp, Channel 1 (CANH), Channel 2 (CANL)], \
[Measurement unit],

The metadata is followed by the actual raw voltage samples:

[Voltage data (1600 samples/file for cars and 2500 samples/file for the John Deere tractor)].

### Publication ###

Feel free to use our dataset for research purposes by giving credit to our paper below.

B. Groza, P. Iosif and L. Popa, "Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data", The 40th Annual AAAI Conference on Artificial Intelligence, 2026. [pdf](https://www.aut.upt.ro/~bgroza/Papers/ecu_scan.pdf)

```
@article{popa2022ecuprint,
title={Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data},
author={Groza, Bogdan and Iosif, Patricia and Popa, Lucian},
conference={The 40th Annual AAAI Conference on Artificial Intelligence},
year={2026},
publisher={AAAI}
}
```

## Contacts
* lucian.popa [at] aut.upt.ro
* bogdan.groza [at] upt.ro
