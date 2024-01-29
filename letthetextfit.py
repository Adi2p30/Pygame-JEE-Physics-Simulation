def split_long_text_lines(is_or_was_a_long_text):
    width_of_would_be_surface, _ = font.size(is_or_was_a_long_text)

    if width_of_would_be_surface > limit_pixel_width:
        text_split = is_or_was_a_long_text.split(' ')
        new_shorter_but_could_be_long_text = ' '.join(text_split[:-1])
        #print(new_shorter_but_could_be_long_text)
        the_right_amount_of_text = split_long_text_lines(new_shorter_but_could_be_long_text)
        return the_right_amount_of_text
    return is_or_was_a_long_text

lines_that_fit = []
while a_paragraph:
    perfect_line_after_split = split_long_text_lines(a_paragraph)
    lines_that_fit.append(perfect_line_after_split)
    a_paragraph = a_paragraph.replace(perfect_line_after_split, '')
print(lines_that_fit)

text_surfaces_from_split = []
for line in lines_that_fit:
    text_surfaces_from_split.append(font.render(line, True, 'white'))
return text_surfaces_from_split