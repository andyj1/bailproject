### The Bail Project: Ontology and more structured, uniform analysis

#### *Available Datasets (City, State)*
> East Baton Rouge, Louisiana (55534 after preprocessing)
- 9616 cases with empty bond information
- 215090 cases with zero bond information

> Wayne, Michigan (7047 after preprocessing)
- 46756 cases with empty bond information
- 145170 cases with zero bond information

> Washington, Arkansas (8741 after preprocessing)
- 11 cases with empty bond information
- 41208 cases with zero bond information

> New York City, New York (1550 after preprocessing)
- 48054 cases with other(non-numeric, e.g. remanded, sentenced) bond information
- 356 cases with zero bond information

#### Packages
> run ```python pip install -r requirements.txt ``` to install all packages

#### Analysis
- The distribution of race and gender for each state (where available) is observed
- For Louisiana, time spent in jail and bail bond amount relationship is observed; for other states, the date of arrest remains unclear (though booking date is available).
- For 

#### Ontology
- Each state charge description (statute) is classified (manually and/or automatically) into the BJS code and BJS Broad Category, which contains five different groups (shown below)
> Viloent, Drug, Property, Public Order, Other
- Plots: frequency of each BJS broad category for each state, particularly for those with bail bonds < \$5,000 because The Bail Project focuses on and assists with groups with such amounts.

#### Constraints
- Due to the nature of web-scraped data, the data is not exhaustive and has a number of factors that lead to final preprocessed data of much lower size. 
- Data preprocessing is performed such that (1) unncessary columns are removed, (2) empty and zero bail bond amounts are removed and (3) rows are sorted by Name or ID by ascending order, without NaN entries. Note that duplicates (across all columns) are not dropped because doing so significantly reduces the size of available data. For Michigan, only the bail bond amount is extracted from the bond information column (which has everything combined into one)
