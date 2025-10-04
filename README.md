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

In this specific context, both metrics prove to be more reliable than the widely used Silhouette score, Davies-Bouldin and Calinski-Harabasz indexes. We successfully test our methodology on the largest dataset available today for in-vehicle voltage characteristics and discover new insights regarding the number of devices. In this repository we share only a part of the entire dataset, due to file size constraints.

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

### Dataset
Extract the provided archive files (CIVIC.7z and DUSTER.7z) to a location of your choice to get the dataset voltage samples for Honda Civic and Dacia Duster.

### Code
Once all prerequisites are installed, the following variables from the python code need to be customized:
- <b>data_path</b> <- set to your location following the example with the provided path
- <b>scaling</b> <- set to 0 (without) or 1 (with) for choosing without/with rescaling of voltage data that supports clustering improvements
- <b>nrows</b> <- set to 1600 (passenger cars) or 2400 (heavy industry vehicle) for chossing between number of data samples/file for passenger cars or the heavy industry vehicle

Then, all section from the notebook need to be run in order to get the results that are presented in our work.



