from textwrap import TextWrapper

# initialize TextWrapper with 40 character width

wrapper = TextWrapper(
 initial_indent="  ", subsequent_indent="  ", drop_whitespace=False, width=40
)

def PrintWrapper(text):
    line_list = wrapper.wrap(text)
    for line in line_list:
        print(line)