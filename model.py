# County / County Group,Households with Elderly,Households with Children,Economic Development Region,
# Income Groups,Percent of Poverty Level,Low-to-Moderate Income (LMI) Group,Household Type,Non-elderly Disabled Indicator,
# Race / Ethnicity,Linguistic Isolation,Housing Unit Type,Owner-Renter Status,Main Heating Fuel Type,
# Home Energy Payment Method,Housing Vintage,LMI Study Region,LMI Population Segment,Mortgage Indicator,
# Time in Home,Education Level,Head of Household Age,Household Weight
import pandas as pd
import csv

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


