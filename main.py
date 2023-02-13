from datetime import datetime
from datetime import date

import numpy as np
import pandas as pd
import streamlit as st
st.title('برنامج القراءت')
if st.button('احصل على برنامجك اليومي'):
    Names = ['ام كوثر', ' نهال', 'مينة', 'ام مصعب', ' سعيدة', '  نجاة', 'سمية', 'أسماء', 'ام بسمة', ' حنان', 'وصال',
             'ملاك', 'ام سلمى', 'نادية', 'علي', 'عبد المجيد', 'وجدان', ' أكرم', '  شمس', 'إجلال', 'عبد الله', 'لطيفة',
             'ام سهام', 'حبيبة', 'مريم', 'يوسفية', 'جليلة', 'بوشته'
                                                            '  محمد', 'كبيرة']
    ahzab = ["1/2", "3/4", "5/6", "7/8", "9/10", "11/12", "13/14", "15/16", "17/18", "19/20", "21/22", "23/24", "25/26",
             "27/28", "29/30", "31/32", "33/34", "35/36", "37/38", "39/40", "41/42", "43/44", "45/46", "47/48", "49/50",
             "51/52", "53/54", "55/56", "57/58", "59/60"]
    mon_dictionnaire = np.load('coran_df.npy', allow_pickle='TRUE').item()
    mon_new_dictionnaire = {"تاريخ": datetime.now().date()}
    for i in Names:
        index = ahzab.index(mon_dictionnaire[i])
        if index == 28:
            index = 0
        else:
            index = ahzab.index(mon_dictionnaire[i]) + 1
        mon_new_dictionnaire[i] = ahzab[index]

    mon_dictionnaire = mon_new_dictionnaire
    np.save('coran_df.npy', mon_dictionnaire)
    mon_dictionnaire.pop("تاريخ",None)
    st.write(mon_dictionnaire)