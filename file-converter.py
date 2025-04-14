import sys
import markdown

while True:
	args = sys.argv
	command = args[1]
	input_file = args[2]
	output_file = args[3]
	if len(args) == 4 and command == 'markdown' and input_file.endswith('md') and output_file.endswith('html'):
		with open(input_file) as f:
			content = f.read()
			html_content = markdown.markdown(content)
		with open(output_file, 'w') as f:
			f.write(html_content)
		sys.stdout.buffer.write(b"done.\n")
		sys.stdout.flush()
		break
	else:
		sys.stdout.buffer.write(b"Invalid input. Try again.\n")
		sys.stdout.flush()
		sys.exit(1)
