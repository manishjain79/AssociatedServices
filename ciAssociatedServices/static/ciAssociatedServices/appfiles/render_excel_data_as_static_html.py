import pandas as pd
import sys


template_path = './templates/ciAssociatedServices/'

def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    tableid = 'table'
    table_html = dataframe.to_html(justify="center", table_id=tableid, header=True)
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    {table_html}
    """
    # return the html
    return html


def write_html(generated_html, html_templatefile_output):
    with open(html_templatefile_output, "w") as html_template:
        html_template.write(generated_html)
    return html_templatefile_output


def get_data(xlsfile: str, xlssheet: str, filtercolumnname: str, filterstring: str):
    df = pd.read_excel(xlsfile ,sheet_name=xlssheet)
    if filterstring == 'ALL':
        df_filtered = df
    else:
        df_filtered = df[df[filtercolumnname].isin([filterstring.upper()])]
    generated_filtered_df_as_html = generate_html(df_filtered)
    df_tma = df[df['GC'].isin(['TMA'])]
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
    # cli_xlsfile= sys.argv[1]
    # cli_xlssheet= sys.argv[2]
    # cli_columnToFilter= sys.argv[3]
    # cli_gcname= sys.argv[4]
    # df = pd.read_excel(xls_filename,sheet_name='Sheet1')
    # html = generate_html(df)
    # indexhtml = write_html(generated_html=html, html_templatefile_output='./templates/index.html')
    # open_html(indexhtml)
    filtered_html = get_data(xlsfile=cli_xlsfile, xlssheet=cli_xlssheet, filtercolumnname=cli_columnToFilter, filterstring=cli_gcname)
    # write_html(filtered_html, html_templatefile_output=f'{template_path}/{cli_gcname}.html')
    return filtered_html

if __name__ == "__main__":
    pass
