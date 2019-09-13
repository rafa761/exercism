import re


def format_strong(text):
    return text.group(1) + '<strong>' + \
           text.group(2) + '</strong>' + text.group(3)


def format_italic(text):
    return text.group(1) + '<em>' + text.group(2) + \
           '</em>' + text.group(3)


def format_header(text):
    match_header = re.match('(^#{1,6}) (.*)', text)
    len_header = len(match_header.groups()[0])
    return f'<h{len_header}>' + match_header.groups()[1] + f'</h{len_header}>'


def parse_markdown(markdown=str):
    # Changed to splitlines method
    lines = markdown.splitlines()
    res = ''
    in_list = False

    for line in lines:

        # Simplified Identify Header
        if re.match('(^#{1,6}) (.*)', line):
            line = format_header(line)

        match_asterisk = re.match(r'\* (.*)', line)
        if match_asterisk:
            if not in_list:
                in_list = True
                text = match_asterisk.group(1)

                # Simplified check for strong
                check_strong = re.match('(.*)__(.*)__(.*)', text)
                if check_strong:
                    text = format_strong(check_strong)

                # Simplified check for italic
                check_italic = re.match('(.*)_(.*)_(.*)', text)
                if check_italic:
                    text = format_italic(check_italic)

                line = '<ul><li>' + text + '</li>'

            else:
                is_italic = False
                text = match_asterisk.group(1)

                # Simplified check for strong
                check_strong = re.match('(.*)__(.*)__(.*)', text)
                if check_strong:
                    text = format_strong(check_strong)

                # Simplified check for italic
                check_italic = re.match('(.*)_(.*)_(.*)', text)
                if check_italic:
                    text = format_italic(check_italic)

                line = '<li>' + text + '</li>'
        else:
            if in_list:
                line = '</ul>+i'
                in_list = False

        match_special_char = re.match('<h|<ul|<p|<li', line)
        if not match_special_char:
            line = '<p>' + line + '</p>'

        check_strong = re.match('(.*)__(.*)__(.*)', line)
        if check_strong:
            line = format_strong(check_strong)

        check_italic = re.match('(.*)_(.*)_(.*)', line)
        if check_italic:
            line = format_italic(check_italic)

        res += line
    if in_list:
        res += '</ul>'
    return res
