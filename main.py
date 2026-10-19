# Dependencies
import csv
import io
import openpyxl

def main(input):
	# Abbreviations: wb - Workbook, ws - Worksheet
    
	# Use BytesIO to convert the input bytes string to an in-memory bytes object
	# so that openpyxl can read it as if it were an Excel file.
	# See: https://docs.python.org/3/library/io.html#io.BytesIO
	wb = openpyxl.load_workbook(io.BytesIO(input['template_bytes']))

	ws = wb[input['sheet_name']]

	# Use StringIO to convert the CSV string to an in-memory stream
	# so that csv.reader can iterate over it as if it were a file.
	# See: https://docs.python.org/3/library/io.html#io.StringIO
	reader = csv.reader(io.StringIO(input['csv_string']))

	# Skip header row
	next(reader)

	# enumerate(reader, start=6) yields (row_idx, csv_row) tuples where csv_row is a list of strings.
	# enumerate(csv_row, start=1) yields (col_idx, value) tuples from that list.
	# Together they provide the row and column coordinates for each cell.
	# See: https://docs.python.org/3/library/functions.html#enumerate
	for row_idx, csv_row in enumerate(reader, start=6):
		for col_idx, value in enumerate(csv_row, start=1):
			ws.cell(row=row_idx, column=col_idx, value=value)

	# Write the workbook to an in-memory bytes object.
	# seek(0) resets the stream position to the beginning so that read() returns all bytes.
	# See: https://docs.python.org/3/library/io.html#io.RawIOBase.seek
	output = io.BytesIO()
	wb.save(output)
	output.seek(0)
	return {'filled_template': output.read()}
