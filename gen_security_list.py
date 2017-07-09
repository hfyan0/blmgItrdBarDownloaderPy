#!/usr/bin/env python3
from datetime import datetime,date,timedelta

fut_sym_list = [("BO" ,"Comdty"), ("CHW","Index"), ("CHY","Curncy"), ("CL" ,"Comdty"), ("EC" ,"Curncy"), ("ES" ,"Index"), ("FCY","Index"), ("GC" ,"Comdty"), ("HC" ,"Index"), ("HG" ,"Comdty"), ("HI" ,"Index"), ("IFB","Index"), ("IH" ,"Index"), ("INO","Index"), ("JPW","Index"), ("JY" ,"Curncy"), ("MRO","Index"), ("NG" ,"Comdty"), ("NI" ,"Index"), ("NK" ,"Index"), ("NO" ,"Index"), ("NQ" ,"Index"), ("QZ" ,"Index"), ("S " ,"Comdty"), ("SI" ,"Comdty"), ("SSI","Index"), ("TMI","Index"), ("TP" ,"Index"), ("TW" ,"Index"), ("XUC","Curncy"), ("XU" ,"Index"), ("YM" ,"Index")]
index_list = ["HSI Index", "HSCEI Index", "VHSI Index", "SHASHR Index", "SHCOMP Index", "SHSZ300 Index"]
mth_code_list = ['F','G','H','J','K','M','N','Q','U','V','X','Z']

dt_list = [date.today(), date.today()+timedelta(days=365)]
y_list = map(lambda x: str(x.year)[-1], dt_list)
fut_code_list = map(lambda y: map(lambda m: m+y, mth_code_list), y_list)
fut_code_list = [j for i in fut_code_list for j in i]
blmg_fut_sym_list = map(lambda x: map(lambda f: x[0]+f+" "+x[1], fut_code_list), fut_sym_list)
blmg_fut_sym_list = [j for i in blmg_fut_sym_list for j in i]

print ('\n'.join(blmg_fut_sym_list+index_list))
