import pandas as pd
from django.db import transaction
from pcndodger.analytics.models import DataSet,PcnDataSetDetail
data_sets = DataSet.objects.all()
for endpoint in data_sets:
    df=pd.read_json('https://opendata.camden.gov.uk/resource/2ckv-3acu.json?$limit=3000000')

    df2 = df.drop(columns=[':@computed_region_6i9a_26nj', ':@computed_region_hxwp_gyfc'])
    df2['data_set'] = endpoint
    df2.head()
df2.shape


PcnDataSetDetail.objects.all().delete()
for item in df2.to_dict('records'):
    print(row.socrata_id)
    row = PcnDataSetDetail(**item)
    row.save()
