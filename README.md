# Trade Canada

## An interactive Power BI dashboard to get a basic overview of Canada's trade with its major trading partners.

### The dashboard consists of 4 sections:
1. Overview: It shows an overview of Canada's trade with the world, like the export and import amounts and different ratios pertaining to its trade.
2. Provincial: Indicates the proportion of trade by provinces with respect to rest of Canada, top imports and exports by Canadian provinces and the export and import amounts between 1997 and 2025.
3. Partners: Shows year-on-year changes in trade between Canada and its major trading partners between 1997 and 2025 and other relevant information in a visually interactive format.
4. Resources: Useful to indentify Canada's dependence on certain countries for trading selected resources.



### Data Source: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210017501



### How to do it yourself:
Step 1: Download the date from the above source.  
Step 2: Store the downloaded file in the same location as the python files.  
Step 3: Run process.py. It cleans and structures the data and removes unwanted columns.  
Step 4: Load the data in Power BI. You can use the same csv. You can use inserter.py to insert the data in PostgreSQL, and then load the data from there.  
Step 5: Explore the visualization.



### Technology used: Python, Power BI, DAX


## Work Samples

### Page 1
The first page of the dashboard (Overview) shows basic global level KPIs

![page 1 base_001](https://github.com/user-attachments/assets/aacb3ff1-221c-492a-8034-6e3d9315f21c)



### Page 2
The second page (Provincial) shows unfiltered province wise trade proportion, YoY change in imports, exports, and trade.

![page 2 base_001](https://github.com/user-attachments/assets/589f8243-99e2-44c0-9a4d-fa5e1cc251f8)


Selecting a province and year slicer (extreme top) in the slicer changes the charts accordingly.

![page 2 province filtered_001](https://github.com/user-attachments/assets/64162e2f-9516-4a5d-8329-2905db7a027a)

![page 2 province and date filtered_001](https://github.com/user-attachments/assets/63d67528-e42a-484a-846a-38cec9a8c07f)



### Page 3
The third page (Trading Partners) shows unfiltered YoY change in imports, exports, and trade as well as exports and import line chart.

![page 3 base_001](https://github.com/user-attachments/assets/c0eb50dd-726b-4e2f-997a-4cff1a977bdf)


Selecting a trading partner and year slicer (extreme top) in the slicer changes the charts accordingly.

![page 3 country filtered_001](https://github.com/user-attachments/assets/9846335f-c8f6-43cb-a223-85474aee83be)

![page 3 country and date filtered_001](https://github.com/user-attachments/assets/e0f6ec46-a120-48f2-8b5f-eb1a97702482)



### Page 4
The fourth page (Resources) shows unfiltered resource's contribution to trade and export and import line chart for all the resources combined.

![page 4 base_001](https://github.com/user-attachments/assets/980ce64d-5e61-4931-9fd1-bb5b8117c8dd)


Selecting a resource and year slicer (extreme top) in the slicer changes the charts accordingly.

![page 4 resource filtered_001](https://github.com/user-attachments/assets/96113291-0115-4dc5-b3b6-054f62a0b608)


![page 4 resource and date filtered_001](https://github.com/user-attachments/assets/8892d1c5-5cf3-407e-ac63-3f1eb30e335f)


