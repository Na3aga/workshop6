import plotly.offline as pl
from plotly import tools
import plotly.graph_objs as go
from model import get_dataset
from collections import Counter

dataset = get_dataset(220000)
income_groups = set(dataset.keys())


def reg_incgroups_number():
    inc_and_regions = {'$0 to <$10,000':{},'$10,000-<$20,000':{},'$20,000-<$30,000':{},'$30,000-<$40,000':{},'$40,000-<$50,000':{},'$50,000+':{}}


    for i in list(dataset.keys()):
        '''
        fill income groups dictionary with values like...
        {'Economic Development Region' : int(Number of Households)}
        '''
        counties = Counter()
        for j in list(dataset[i].keys()):
            for m in list(dataset[i][j].keys()):
                counties[j] +=len(dataset[i][j][m])
        inc_and_regions[i] = dict((k[0],k[1]) for k in counties.most_common(3))



    x=list(inc_and_regions.keys())


    trace0 = go.Bar(
        name='First by number of households',
        x=x,
        y=[list(i.values())[0] for i in list(inc_and_regions.values())],
        text=[list(i.keys())[0] for i in list(inc_and_regions.values())],
        textposition='auto',
        marker=dict(
            color='rgb(49,130,189)'
        )
    )
    trace1 = go.Bar(
        name='Second by number of households',
        x=x,
        y=[list(i.values())[1] for i in list(inc_and_regions.values())],
        text=[list(i.keys())[1] for i in list(inc_and_regions.values())],
        
        textposition='auto',
        marker=dict(
            color='rgb(204,204,204)',
        )
    )
    trace2 = go.Bar(
        name='Thirth by number of households',
        x=x,
        y=[list(i.values())[2] for i in list(inc_and_regions.values())],
        text=[list(i.keys())[2] for i in list(inc_and_regions.values())],
        textposition='auto',
        marker=dict(
            color='rgb(158, 64, 147)',
        )
    )


    # data = [trace0, trace1,trace2]

    inc_and_children = {'$0 to <$10,000':{},'$10,000-<$20,000':{},'$20,000-<$30,000':{},'$30,000-<$40,000':{},'$40,000-<$50,000':{},'$50,000+':{}}

    for i in list(dataset.keys()):
        '''
        fill income groups dictionary with values like...
        {'Have Children' : int(Number of Households)}
        '''
        counties = Counter()
        for j in list(dataset[i].keys()):
            for m in list(dataset[i][j].keys()):
                for hh in dataset[i][j][m]: 
                    kids = hh['HhChildren']
                    counties[kids] +=1
        inc_and_children[i] = dict((k[0],k[1]) for k in counties.most_common(2))

    x=list(inc_and_children.keys())

    trace_no = go.Bar(
        name='one+ child',
        x=x,
        y=[list(i.values())[0] for i in list(inc_and_children.values())],
        text=[list(i.keys())[0] for i in list(inc_and_children.values())],
        textposition='auto',
        marker=dict(
            color='rgb(49,130,189)'
        )
    )
    trace_yes = go.Bar(
        name='No children',
        x=x,
        y=[list(i.values())[1] for i in list(inc_and_children.values())],
        text=[list(i.keys())[1] for i in list(inc_and_children.values())],

        textposition='auto',
        marker=dict(
            color='rgb(204,204,204)',
        )
    )

   
    # layout = go.Layout(title='number of households with/out kis by income groups',
    #                     titlefont={'size': 32, 'color': 'blue'}
  

    # layout = go.Layout(title='number of households in cities by income groups',
    #                     titlefont={'size': 32, 'color': 'blue'}
    #                 )

    fig = tools.make_subplots(rows=2,cols=1)
    fig.append_trace(trace0,1,1)  
    fig.append_trace(trace1,1,1)  
    fig.append_trace(trace2,1,1)  
    fig.append_trace(trace_yes,2,1)  
    fig.append_trace(trace_no,2,1)   
    pl.plot(fig, filename='reg_incgroups_number.html')
    return


# PLOT NUMBER 2

def races_incomes():
    inc_and_races = {'$0 to <$10,000':{},'$10,000-<$20,000':{},'$20,000-<$30,000':{},'$30,000-<$40,000':{},'$40,000-<$50,000':{},'$50,000+':{}}

    for a in list(dataset.keys()):
        '''
        fill income groups dictionary with values like...
        {'Race/Ethnicity' : int(number of households)}
        '''
        races = Counter()
        for b in list(dataset[a].keys()):
            for c in list(dataset[a][b].keys()):
                for d in dataset[a][b][c]:
                    races[d['Race']] +=1
        inc_and_races[a] = dict((k[0],k[1]) for k in races.most_common(10))



    def create_pie(dictionary, name='',domain = False,hoverinfo="label+percent+name",hole = .4):
        result = dict()
        result["type"] = "pie"
        result["name"] = str(name)
        result["hoverinfo"] = hoverinfo
        result["hole"] = hole
        if domain != False:
            result["domain"] = domain
        result["values"] = list(dictionary.values())
        result["labels"] = list(dictionary.keys())

        return result


    def create_domains(dictionary):
        result = dict()
        number = len(dictionary)
        size = round(1.0 / number, 3) - 0.04
        step = size  + 0.04 
        x1,x2 = 0.0,size
        for i in list(dictionary.keys()):
            result[i] = {'x':[x1,x2]}
            x1 += step
            x2 += step 

        return result
        
    domains = create_domains(inc_and_races)

    data = [create_pie(inc_and_races[d],d,domain = domains[d] ,hole=0.2 ) for d in list(inc_and_races.keys())]

    fig = {
        "data": data,
        "layout": {
            "title":"Race/Ethnicity percantage in income groups",
            "titlefont":{
                "size": 32,
                "color": "green"
            }
        }
    }

    pl.plot(fig, filename = "racesincomes.html")

    return
        

reg_incgroups_number()
races_incomes()