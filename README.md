# Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data

The repository contains the python code required to reproduce the results from our work together with a link and details related to the ECUPrint Aligned dataset. Steps to run all the provided code are detailed below.

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

The dataset linked in this repository represents the aligned and filtered input used by the Promoter-Censor algorithm proposed in our paper: Constraint-Guided Clustering for Identifying In-Vehicle Electronic Control Units from Voltage Data. 

<img width="6000" height="3062" alt="image" src="https://github.com/user-attachments/assets/7d774436-ed46-4fca-b7aa-57deca9008cc" />

**Motivation**: The original ECUPrint dataset was created by our group three years ago for statistical analysis of ECU voltage samples, where slight misalignments or incomplete entries had only a limited impact. However, for machine-learning classifier benchmarking, we later observed that these inconsistencies led to distorted performance estimates. To address this issue, we sanitized the dataset by aligning and filtering the samples to ensure that the reported results reflect classifier performance rather than data irregularities.

Briefly, the modifications compared to the ECUPrint dataset are the following:

- All bits from the 10 vehicles are aligned (the Python script used for alignment is also available)
- Samples are cut to exactly 1600 time-steps for passenger cars and 2500 time-steps for the heavy-duty vehicle
- Acknowledgement bits are removed because they do not come from the ECU that is the sender of the ID
- Incomplete bits lacking the falling edge were discarded to ensure dataset consistency

As a consequence the following IDs were removed the ECUPrint Aligned Dataset: 0x370 (Corsa), 0x511 (Duster), 0x4DE (Logan), 0x3A9, 0x43C, 0x171 (Ecosport), 0x428 (ix35) and 1 bit was removed for IDs 0x294, 0x19B (Civic). The sanitized dataset retains 175,378 samples from the original 181,874 samples of the ECUPrint dataset.

**Result**: The Ground Truth resulting from the new metholdology is slightly different from the original ECUPrint paper and is available in this [pdf](https://www.aut.upt.ro/~bgroza/projects/ecuprint-aligned/ecu_scan_gt.pdf).

**Independent corroboration**: We also verified the number of ECUs in the Ford vehicles with a diagnostic tool (FORScan v2.3.65) together with the electrical wiring diagrams and it matches the number of ECUs that we identified using Constraint-Guided Clustering. Documents used for determination of electrical wiring diagrams are:

- [Module Communication Diagram from Cardiagn - Ford Fiesta](https://cardiagn.com/2017-2020-ford-fiesta-all-engines-electrical-wiring-diagrams/)
- [Module Communication Diagram from Cardiagn - Ford Ecosport](https://cardiagn.com/ford-ecosport-2017-2022-service-and-repair-manual/)
- [Module Communication Diagram from Cardiagn - Ford Kuga](https://cardiagn.com/2019-ford-kuga-eu-ekke-wiring-diagrams-module-communication-network/)

#### Data links ####

File | Download | Notes
--- | :---------: | :----
**ECUPrint_Aligned.zip** | [link1 (University website)](http://localhost) <br /> [link2 (OneDrive)](https://1drv.ms/u/c/eab50b86f61a55f8/Ecyc_vTq6c1ArUZWDtkwfKcBQRwu3CvS3NjIqD9V-0yFNA?e=eqe2Sg) | Aligned ECUPrint CAN voltage samples, allocated per Vehicle, ECU and ID

More details related to the bit aligning concept, applied filters and insights related to the dataset structure and file contents are described below.

### Data pre-processing ###

ECUPrint raw voltage data was collected from 10 vehicles, ranging from small cars to SUVs and a heavy-duty vehicle with a Pico Scope 5000 Series.

**Sample Alignment and Trimming** - For each frame carrying a specific ID the ECUPrint dataset contains isolated dominant bits, i.e., a transition from recessive to dominant state and back. In the original files from the ECUPrint dataset, the rising edges and falling edges from each dominant bit are not aligned at the same index, as shown in the images below for the samples corresponding to ID 4F1 from the Hyundai i20 (left image) and to ID 04EF0021 from the John Deere tractor (right image).

<p>
<img alt="image" src="https://github.com/user-attachments/assets/75f58730-348d-418b-9814-a1d4a5fc1db0" width="49%" /> 
<img  alt="image" src="https://github.com/user-attachments/assets/05e6c156-cef8-429c-9e21-a8189906602d" width="49%" />
</p>

We aligned the bits for each ID at the same index, which led to a different number of time-steps per file out of which we preserve only 1600 time-steps for passenger cars and 2500 time-steps for the heavy-duty vehicle. An examples of the newly aligned bits is shown in the images below. They correspond to ID 4F1 from the Hyundai i20 (left image) and to ID 04EF0021 from the John Deere tractor (right image).

<p>
<img alt="image" src="https://github.com/user-attachments/assets/d09b7c46-c076-460b-bc50-fd4301fafac4" width="49%" />
<img alt="image" src="https://github.com/user-attachments/assets/86ce5c36-4505-4de7-aa3a-c4d933c6a7e6" width="49%" />
</p>

**Removal of ACK Bits** - Analyzing the bits from the ECUPrint dataset, we have found some acknowledgement bits instead of genuine dominant bits that were removed from the alignment process and are not part of the ECUPrint Aligned Dataset. An example is shown for one of the Honda Civic files that had different samples for ID 19B compared to all other files that had the right samples.

<p>
<img alt="image" src="https://github.com/user-attachments/assets/ee0c4277-6878-42bc-9cad-3c6314222680" width="49%"/>
</p>

**Removal of Non-Isolated Bits** - For some IDs, the ECUPrint dataset does not contain single isolated dominant bits. The voltage samples for those bits had a continuous plateau level while for isolated bits, the file ends with the samples of the falling edge. These IDs were removed from the alignment process and are not part of the ECUPrint Aligned Dataset. An example is shown for ID 511 from the Dacia Duster that had different samples compared to all other IDs from the same ECU.

<p>
<img width="613" height="433" alt="image" src="https://github.com/user-attachments/assets/c883792b-93bc-45a5-a1eb-10bdb43caf42" />
</p>

**Establishment of a New ECU Allocation** - Based on the newer analysis of the voltage samples for all of the IDs, we found that there is a different number of ECUs for some vehicles compared to the determination from ECUPrint. There are two additional ECUs determined for the Ford Kuga and 1 additional ECU determined for the Ford Fiesta and Ford Ecosport while there is 1 ECU less for the Hyundai i20. This is also due to the use of some voltage bits that were left as "Unclassified" in the original ECUPrint dataset and were not grouped with a particular ECU since the clock skew could not be determined for those IDs based on the collected frames. The updated ECU allocation from the ECUPrint Aligned dataset provides the newly determined ground truth allocation of IDs to ECUs to the best of our knowledge.

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

The dataset is structured as described below. We provide the raw CAN voltage samples measured with the PicoScope with a sample interval of 2 nanoseconds (sample rate was set to 500 MS/s). CAN voltages are collected for 10 cars (175,378 sampled bits) with ECU allocation. Data is allocated to specific ECUs based on the analysis in our work. Note that this distribution is to the best we could ascertain based on our analysis, we do not claim this separation to be absolute.  

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

B. Groza, P. Iosif and L. Popa, "Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data". [pdf](https://www.aut.upt.ro/~bgroza/Papers/ecu_scan.pdf)

```
@article{groza26constraint,
title={Constraint-Guided Clustering for Identifying in-Vehicle Electronic Control Units from Voltage Data},
author={Groza, Bogdan and Iosif, Patricia and Popa, Lucian},
conference={},
year={2026},
publisher={}
}
```

## Contacts
* lucian.popa [at] aut.upt.ro
* bogdan.groza [at] upt.ro
