def do_twise(f, arg):
	f(arg)
	f(arg)

def print_onece(arg):
	print(arg)

#do_twise(print_onece, "spam")

def do_four(f, arg):
	do_twise(f, arg)
	do_twise(f, arg)

#do_four(print_onece, "spam!")

do_twise(print_onece, "spam!!")
do_twise(print_onece, "spam!!!")