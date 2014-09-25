
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv '-Dimporttsv.separator=,' -Dimporttsv.columns=HBASE_ROW_KEY,info:first_name,info:last_name,info:email,info:freq_wt,info:acct_created,info:last_login,info:zipcode,info:birth_year,info:gender,info:active,info:ip_address user_info msd/users_10K


