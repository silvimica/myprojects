from jinja2 import Environment, FileSystemLoader
import pandas as pd


env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('dag_template.py')

input = pd.read_excel('input.xlsx')
input = input.to_dict('r')[0]

# Render template
output_from_parsed_template = template.render(from_=input['from_'], 
                                              to_=input['to_'], 
                                              conn_from=input['conn_id_from'], 
                                              conn_to=input['conn_id_to'], 
                                              schema_from=input['schema_from'],
                                              schema_to = input['schema_to'],
                                              tables_to=input['tables_to'],
                                              tables_from=input['tables_from'],
                                              schedule=input['schedule'], 
                                              dag_id=input['dag_id'], 
                                              owner=input['owner'], 
                                              start_date = input['start_time'], 
                                              truncate_table = input['truncate_table'])

# Save results
with open("{}.py".format(input['dag_id']), "w", encoding='utf8') as f:
    f.write(output_from_parsed_template)