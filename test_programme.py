#Set up parameter
dir_path = "E:/python/"
num_of_task = 5
main_dir_name = "Els"
test_dir_name = "Tast Task"
sample_dir_name = "Sample"
result_dir_name = "Result"
report_dir_name = "Report"
main_path = dir_path+main_dir_name
test_dir_path = main_path+"/"+test_dir_name


#開始建立資料夾
#Make Main Dir
import os 
if os.path.exists(main_path):
    pass
else:
    os.mkdir(main_dir_name)

#Make sub dir and sub sub dir
for x in range(1,num_of_task+1,1):
    sub_path = test_dir_path+str(x)
    sample_dir_path = sub_path+"/"+sample_dir_name
    result_dir_path = sub_path+"/"+result_dir_name
    report_dir_path = sub_path+"/"+report_dir_name
    os.mkdir(sub_path)
    os.mkdir(sample_dir_path)
    os.mkdir(result_dir_path)
    os.mkdir(report_dir_path)

