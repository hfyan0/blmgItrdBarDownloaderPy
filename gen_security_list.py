#!/usr/bin/env python3
from datetime import datetime,date,timedelta

fut_sym_list = [("BO" ,"Comdty"), ("CHW","Index"), ("CHY","Curncy"), ("CL" ,"Comdty"), ("EC" ,"Curncy"), ("ES" ,"Index"), ("FCY","Index"), ("GC" ,"Comdty"), ("HC" ,"Index"), ("HG" ,"Comdty"), ("HI" ,"Index"), ("IFB","Index"), ("IH" ,"Index"), ("INO","Index"), ("JPW","Index"), ("JY" ,"Curncy"), ("MRO","Index"), ("NG" ,"Comdty"), ("NI" ,"Index"), ("NK" ,"Index"), ("NO" ,"Index"), ("NQ" ,"Index"), ("QZ" ,"Index"), ("S " ,"Comdty"), ("SI" ,"Comdty"), ("SSI","Index"), ("TMI","Index"), ("TP" ,"Index"), ("TW" ,"Index"), ("XUC","Curncy"), ("XU" ,"Index"), ("YM" ,"Index")]
index_list = ["HSI Index", "HSCEI Index", "VHSI Index", "SHASHR Index", "SHCOMP Index", "SHSZ300 Index"]
mth_code_dict = { 1 : 'F', 2 : 'G', 3 : 'H', 4 : 'J', 5 : 'K', 6 : 'M', 7 : 'N', 8 : 'Q', 9 : 'U', 10: 'V', 11: 'X', 12: 'Z' }


dt_list = []
dt = date.today()-timedelta(days=30)
while dt < date.today()+timedelta(days=90):
    dt_list.append(dt)
    dt = dt+timedelta(days=1)

fut_code_list = sorted(list(set([ str(mth_code_dict[int(x.month)]) + str(x.year)[-1] for x in dt_list ])))

blmg_fut_sym_list = map(lambda x: map(lambda f: x[0]+f+" "+x[1], fut_code_list), fut_sym_list)
blmg_fut_sym_list = [j for i in blmg_fut_sym_list for j in i]

print ('\n'.join(blmg_fut_sym_list+index_list))
