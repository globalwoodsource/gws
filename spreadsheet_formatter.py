from xlutils.copy import copy
from xlrd import open_workbook
import xlwt
import sys

def expand_image_col(filename):
	img_prefix = "DSCN"
	img_ext = ".jpg"

	rb = open_workbook(filename,formatting_info=True)
	r_sheet = rb.sheet_by_index(0)
	wb = copy(rb)
	w_sheet = wb.get_sheet(0)
	
	# find image col
	for col in range(0,r_sheet.ncols):
		if r_sheet.cell(0,col).value == "Images":
			img_col = col
			break

	for row in range(1,r_sheet.nrows):
		s = r_sheet.cell(row,img_col).value.split('-')
		img_range = [int(v) for v in s if v != '']
		if len(img_range) == 1:
			w_sheet.write(row,img_col+i,img_prefix+repr(img_range[0])+img_ext)
		elif len(img_range) > 1:
			if img_range[1] < img_range[0]:
				print "BAD: Invalid image range for row "+repr(row+1)+"."
			for i,img_n in enumerate(range(img_range[0],img_range[1]+1)):
				w_sheet.write(row,img_col+i,img_prefix+repr(img_n)+img_ext)
	
	wb.save(filename[:-4]+'-out.xls')
	print "YAY: Output written to "+filename[:-4]+'-out.xls'


if __name__ == "__main__":
	expand_image_col(sys.argv[1])
