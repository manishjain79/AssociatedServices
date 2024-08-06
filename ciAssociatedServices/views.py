from pathlib import Path
from django.shortcuts import render
import pandas as pd

xls_filename = './ciAssociatedServices/static/ciAssociatedServices/appfiles/TM_CIs_Associated_Service.xlsx'



def generate_html(dataframe: pd.DataFrame):
    '''get the table HTML from the dataframe'''
    tableid = 'table'
    table_html = dataframe.to_html(justify="center", table_id=tableid, header=True, render_links=True, classes=['fs-5', 'text-start', 'fst-italic'], index=False)
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    {table_html}
    """
    # return the html
    return html


def get_data(xlsfile: str, xlssheet: str, filtercolumnname: str, filterstring: str):
    '''
    This function reads an excel sheet and filter the contents from a filtercolumnname with filterstring.
    Once we have the dataframe with filtered table, we insert the output with HTML elements that can show this dataframe as table on web page.
    '''
    df = pd.read_excel(xlsfile ,sheet_name=xlssheet)
    if filterstring == 'ALL':
        df_filtered = df
    else:
        df_filtered = df[df[filtercolumnname].isin([filterstring.upper()])]
    generated_filtered_df_as_html = generate_html(df_filtered)
    # df_tma = df[df['GC'].isin(['TMA'])]
    # df_tmis = df[df['GC'].isin(['TMIS'])]
    # df_tmls = df[df['GC'].isin(['TMLS'])]
    # df_tmlth = df[df['GC'].isin(['TMLTH'])]
    # df_tmsth = df[df['GC'].isin(['TMSTH'])]
    # df_tmiv = df[df['GC'].isin(['TMIV'])]
    # df_tmlm = df[df['GC'].isin(['TMLM'])]
    # df_tmim = df[df['GC'].isin(['TMIM'])]
    # df_tmi = df[df['GC'].isin(['TMI'])]
    # df_tmli = df[df['GC'].isin(['TMLI'])]
    # tmahtml = generate_html(df_tma)
    # tmishtml = generate_html(df_tmis)
    # tmlshtml = generate_html(df_tmls)
    # tmlthhtml = generate_html(df_tmlth)
    # tmsthhtml = generate_html(df_tmsth)
    # tmivhtml = generate_html(df_tmiv)
    # tmlmhtml = generate_html(df_tmlm)
    # tmimhtml = generate_html(df_tmim)
    # tmihtml = generate_html(df_tmi)
    # tmlihtml = generate_html(df_tmli)
    # print(df_tma)
    return generated_filtered_df_as_html


def gethtmltemplate(cli_xlsfile, cli_xlssheet, cli_columnToFilter, cli_gcname):
    '''
    This is a wrapper function to get_data so that we can dynamically pass information when calling this.
    '''
    filtered_html = get_data(xlsfile=cli_xlsfile, xlssheet=cli_xlssheet, filtercolumnname=cli_columnToFilter, filterstring=cli_gcname)
    return filtered_html


# Create your views here.
def home(request):
    '''
    This function gets executed upon calling for any gcname.
    '''
    context = {
        'data_table': gethtmltemplate(xls_filename,'CIs_Asscoiated Service Offering','GC', 'ALL'),
        'title': 'Home' }
    return render(request, 'ciAssociatedServices/gc.html', context)

# Create your views here.
def GCDetails(request, gcname):
    '''
    This function gets executed upon calling for any gcname.
    '''
    context = {
        'data_table': gethtmltemplate(xls_filename,'CIs_Asscoiated Service Offering','GC', gcname),
        'title': 'Home',
         'currentselection': gcname }
    return render(request, 'ciAssociatedServices/gc.html', context)
