import xlrd
import commands
import sys

#The following var need to be set accoring the workspace setting
AOS_SRC="fcs8800"
DEST_DIR="opensource"
SHEET_NAME_COL = 1
SHEET_VERSION_COL = 3

reload(sys)
sys.setdefaultencoding('utf8')
STR_CON='-'
cp_failed_list=""
find_failed_dict=dict()
sucessed_dict= dict()

workbook = xlrd.open_workbook(sys.argv[1])
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

#The work sheet name should be changed accoring to the actual spreadsheet
worksheet1 = workbook.sheet_by_name(u'AOS 8.6 components')

"""
worksheet1 = workbook.sheets()[0]
worksheet1 = workbook.sheet_by_index(0)
for worksheet_name in worksheets:
worksheet = workbook.sheet_by_name(worksheet_name)
"""

print "Sort opensource pakage begin"
"""
num_rows = worksheet1.nrows
for curr_row in range(1):
	row = worksheet1.row_values(curr_row)
	print 'row%s is %s' %(curr_row,row)
	num_cols = worksheet1.ncols
	for curr_col in range(3):
		col = worksheet1.col_values(curr_col)
		print 'col%s is %s' %(curr_col,col)
		for rown in range(1):
			for coln in range(1):
				cell = worksheet1.cell_value(rown,coln)
				print cell
"""

row = 1
print("total num is %d" %worksheet1.nrows)
while row < worksheet1.nrows:
	name = worksheet1.cell_value(row,SHEET_NAME_COL)
	ver = worksheet1.cell_value(row,SHEET_VERSION_COL)
	#print("name string is %s" %name)
	#print("ver string is %s" %ver)
	if ver != '':
		ver_split= str(ver).split(', ')
		name_split = str(name).split('-')
		i=0
		while i < ver_split.__len__():
		#while i < 1:
			str_opensource_prj =  str(name_split[0]) + STR_CON + str(ver_split[i])
			print "==================="
			print str(row) + ":" + str_opensource_prj
			find_cmd = "find "  + AOS_SRC  + " -name " + str_opensource_prj + " -type d"
			print find_cmd
			#os.system(find_cmd)
			find_res,find_out = commands.getstatusoutput(find_cmd)
			if find_out != "" :
				#find_outprint "find " + str(str_opensource_prj) + '@' + str(find_out)
				cp_res,cp_out = commands.getstatusoutput("cp -aprf " + str(find_out) + " " + str(DEST_DIR));
				if cp_res != 0:
					print "cp " + str(find_out) + " Failed"
					cp_failed_list += str(str_opensource_prj) + ' '
				else:
					sucessed_dict[row] = str_opensource_prj
			else:
				print "find " + str(str_opensource_prj) + " Failed"
				find_failed_dict[row]=str_opensource_prj
			i+=1
	else:
		str_opensource_prj = name
		print "==================="
		print str(row) + ":" + str_opensource_prj
		find_cmd = "find "  + AOS_SRC  + " -name " + str_opensource_prj + " -type d"
		#print find_cmd
		#find_cmdos.system(find_cmd)
		find_res,find_out = commands.getstatusoutput(find_cmd)
		if find_out != "" :
			#print "find " + str(str_opensource_prj) + '@' + str(find_out)
			cp_res,cp_out = commands.getstatusoutput("cp -aprf " + str(find_out) + " " + str(DEST_DIR));
			if cp_res != 0:
				print "cp " + str(find_out) + " Failed"
				cp_failed_list += str(str_opensource_prj) + ' '
		else:
			print "find " + str(str_opensource_prj) + " Failed"
			find_failed_dict[row]=str_opensource_prj
	row += 1;
print "==================="
print "Failed items:"
print find_failed_dict
#for key in find_failed_dict.keys():
#	print str(key) + ": " + str(find_failed_dict[key])
print"retrying failed itms:"
for row,value in find_failed_dict.items():
	name = worksheet1.cell_value(row,1)
	str_opensource_prj = name + "*"
	find_cmd = "find " + AOS_SRC + " " + "-name " + str_opensource_prj + " -type d"
	print find_cmd
	find_res, find_out = commands.getstatusoutput(find_cmd)
	if find_out != "":
		print find_out
		cp_res,cp_out = commands.getstatusoutput("cp -aprf " + str(find_out) + " " + str(DEST_DIR));
		if cp_res != 0:
			print "cp " + str(find_out) + " Failed"
			cp_failed_list += str(str_opensource_prj) + ' '
print  "cp failed:" + str(cp_failed_list)
print sucessed_dict
print "Sort end"

