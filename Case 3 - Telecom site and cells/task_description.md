# Problem solving challenge - Telecom site and cells case
The following case scenario is an example of the kind of problems we need to approach and solve in our daily work. 

The idea is that you read through the description and provide a potential solution based on your interpretation of the problem. 
Sample table records are provided along with this file.


## Background
In the mobile telephone network, there are lots of devices that need to work together to give the customer a pleasant experience. Examples of those devices is a customer’s cell phone and network cells which the phone connects to. There are cells of different technology gsm (2g), umts (3g) and lte (4g). Cells are grouped into physical locations called sites. One site has at least one cell and can be composed of any mix of cells in different technologies. At Telia we receive a snapshot of this cell/site data every day for all the countries.

Each cell of a technology can operates on different frequency bands. For gsm there are 900 and 1800 MHZ, umts has 900 and 2100 MHZ and lte has 700, 800, 2600, 1800 and 2100 MHZ.

We are given below 4 tables and sample table records are provided in the ‘Archive’ folder.
1) gsm
2) lte
3) site
4) umts

## Task
Your task is to write SQL statements for below queries. The data has 2 parts. The first part is the cell data (gsm.csv, umts.csv and lte.csv) and the second one is the site data (site.csv). The data, as mentioned before, is organised by day. Your task is to create one data set for all cells and enrich each cell with information from the site. All cells that cannot be assigned a site should be dropped.

The calculated values should be the following:

1. How many cells per technology are there on each site. The column name should be as follows: site_$TECHNOLOGY_cnt

> Example: for a site S there are 2 cells gsm, 3 cells umts and 0 cells lte. <br>
> The result should be site_Ite_cnt: 0, site_umts_cnt: 3, site_gsm_cnt: 2

2. Calculate number of cells per frequency band on a particular site

> Example: for a site S there is 2 cell gsm with 900MHZ, one cell umts 2100MHZ and one cell lte with 1800MHZ. <br>
> The result should be: <br>
> frequency_band_G900_by_site: 1 cells, frequency_band_U2100_by_site: 1, frequency_band_L1800_by_site: 1, frequency_band_L2100_by_site: 0 (and so on)

