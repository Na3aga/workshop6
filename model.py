# County / County Group,Households with Elderly,Households with Children,Economic Development Region,
# Income Groups,Percent of Poverty Level,Low-to-Moderate Income (LMI) Group,Household Type,Non-elderly Disabled Indicator,
# Race / Ethnicity,Linguistic Isolation,Housing Unit Type,Owner-Renter Status,Main Heating Fuel Type,
# Home Energy Payment Method,Housing Vintage,LMI Study Region,LMI Population Segment,Mortgage Indicator,
# Time in Home,Education Level,Head of Household Age,Household Weight
import pandas as pd
import csv
import plotly.offline as pl
import plotly.graph_objs as go
from functools import reduce

def get_dataset(stop=100):
    dataset = dict() 
    with open("nyserda.csv",'r') as f:
        f.readline()
        reader = csv.reader(f)
        count = 0
        for i in reader:
            [
                County, HhElderly, HhChildren, EcoDevRegion,
                IncGroups, PercPovertyLvl, LMIgroup, HhType,
                NonEldeDisIndic, Race, LingIsol, HousUnitType,
                OwnerStatus, MHFuelType, HEPayMethod, HousVintage, 
                LMIstudyRegion, LMIpopSegment, MortgageIndic, TimeInHome,
                EduLvl,HeadOfHhAge,HhWeight
            ] = [q for q in i] 
            if IncGroups not in dataset:
                dataset[IncGroups] = {EcoDevRegion:{County:
                [{
                    'HhElderly': HhElderly, 
                    'HhChildren': HhChildren,
                    'PercPovertyLvl': PercPovertyLvl,
                    'LMIgroup': LMIgroup,
                    'HhType': HhType,
                    'NonEldeDisIndic':NonEldeDisIndic,
                    'Race': Race,
                    'LingIsol': LingIsol,
                    'HousUnitType': HousUnitType,
                    'OwnerStatus': OwnerStatus,
                    'MHFuelType': MHFuelType,
                    'HEPayMethod': HEPayMethod,
                    'HousVintage': HousVintage,
                    'LMIstudyRegion': LMIstudyRegion,
                    'LMIpopSegment': LMIpopSegment,
                    'MortgageIndic': MortgageIndic,
                    'TimeInHome': TimeInHome,
                    'EduLvl': EduLvl,
                    'HeadOfHhAge': HeadOfHhAge,
                    'HhWeight': HhWeight
                    }]}}
            else:
                if EcoDevRegion not in dataset[IncGroups]:
                    dataset[IncGroups][EcoDevRegion] = {County:
                    [{
                        'HhElderly': HhElderly, 
                        'HhChildren': HhChildren,
                        'PercPovertyLvl': PercPovertyLvl,
                        'LMIgroup': LMIgroup,
                        'HhType': HhType,
                        'NonEldeDisIndic':NonEldeDisIndic,
                        'Race': Race,
                        'LingIsol': LingIsol,
                        'HousUnitType': HousUnitType,
                        'OwnerStatus': OwnerStatus,
                        'MHFuelType': MHFuelType,
                        'HEPayMethod': HEPayMethod,
                        'HousVintage': HousVintage,
                        'LMIstudyRegion': LMIstudyRegion,
                        'LMIpopSegment': LMIpopSegment,
                        'MortgageIndic': MortgageIndic,
                        'TimeInHome': TimeInHome,
                        'EduLvl': EduLvl,
                        'HeadOfHhAge': HeadOfHhAge,
                        'HhWeight': HhWeight
                    }]}
                else: 
                    if County not in dataset[IncGroups][EcoDevRegion]:
                        dataset[IncGroups][EcoDevRegion][County] = [{
                            'HhElderly': HhElderly,
                            'HhChildren': HhChildren,
                            'PercPovertyLvl': PercPovertyLvl,
                            'LMIgroup': LMIgroup,
                            'HhType': HhType,
                            'NonEldeDisIndic':NonEldeDisIndic,
                            'Race': Race,
                            'LingIsol': LingIsol,
                            'HousUnitType': HousUnitType,
                            'OwnerStatus': OwnerStatus,
                            'MHFuelType': MHFuelType,
                            'LMIstudyRegion': LMIstudyRegion,
                            'LMIpopSegment': LMIpopSegment,
                            'MortgageIndic': MortgageIndic,
                            'TimeInHome': TimeInHome,
                            'EduLvl': EduLvl,
                            'HeadOfHhAge': HeadOfHhAge,
                            'HhWeight': HhWeight
                            }] 
                    else: 
                        dataset[IncGroups][EcoDevRegion][County].append(
                            {
                            'HhElderly': HhElderly, 
                            'HhChildren': HhChildren,
                            'PercPovertyLvl': PercPovertyLvl,
                            'LMIgroup': LMIgroup,
                            'HhType': HhType,
                            'NonEldeDisIndic':NonEldeDisIndic,
                            'Race': Race,
                            'LingIsol': LingIsol,
                            'HousUnitType': HousUnitType,
                            'OwnerStatus': OwnerStatus,
                            'MHFuelType': MHFuelType,
                            'HEPayMethod': HEPayMethod,
                            'HousVintage': HousVintage,
                            'LMIstudyRegion': LMIstudyRegion,
                            'LMIpopSegment': LMIpopSegment,
                            'MortgageIndic': MortgageIndic,
                            'TimeInHome': TimeInHome,
                            'EduLvl': EduLvl,
                            'HeadOfHhAge': HeadOfHhAge,
                            'HhWeight': HhWeight
                        })
            count+=1
            if count==stop:
                return dataset

    return dataset

# data = get_dataset()

# count = 0
# for i in list(data.values()):
#     for q in list(i.values()):
#         for j in list(q.values()):
#             print(j)
#             count+=len(j)
            

# print(count)
# print(get_dataset())

# Вивести стовпчикову діаграму: по ОХ на кожну групу дохідності по три стовпчики які відповідають регіонам,
# по ОУ кількість сімей з таким доходом.
dataset = get_dataset(22000)
# income_groups = set(dataset.keys())

inc_regions = {'$0 to <$10,000':{},'$10,000-<$20,000':{},'$20,000-<$30,000':{},'$30,000-<$40,000':{},'$40,000-<$50,000':{},'$50,000+':{}}
for i in set(dataset.keys()):
    inc_regions[i] = dict((k,sum(len(dataset[i][k][q]) for q in list(dataset[i][k].keys()))) for k in list(dataset[i].keys())[:3])

# num_of_house_holds = {}
# for k,v in inc_regions:
    

print(inc_regions)


import plotly.plotly as py
import plotly.graph_objs as go


x=list(inc_regions.keys())
# print(x,'\n\n',
#     [list(i.values())[0] for i in list(inc_regions.values())],'\n\n',
#     [list(list(inc_regions.values())[0].keys())]
# )

trace0 = go.Bar(
    x=x,
    y=[list(i.values())[0] for i in list(inc_regions.values())],
    text=[list(i.keys())[0] for i in list(inc_regions.values())],
    textposition='auto',
    marker=dict(
        color='rgb(49,130,189)'
    )
)
trace1 = go.Bar(
    x=x,
    y=[list(i.values())[1] for i in list(inc_regions.values())],
    text=[list(i.keys())[1] for i in list(inc_regions.values())],
    textposition='auto',
    marker=dict(
        color='rgb(204,204,204)',
    )
)
trace2 = go.Bar(
    x=x,
    y=[list(i.values())[2] for i in list(inc_regions.values())],
    text=[list(i.keys())[2] for i in list(inc_regions.values())],
    textposition='auto',
    marker=dict(
        color='rgb(158, 64, 147)',
    )
)


data = [trace0, trace1,trace2]
layout = go.Layout(
    xaxis=dict(tickangle=-45),
    barmode='group',
)

# fig = go.Figure(data=data, layout=layout)
pl.plot(data, filename='reg_incgroups_number.html')

