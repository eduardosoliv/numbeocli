import bs4

class Parser:
    def __init__(self, content):
        self.__soup = bs4.BeautifulSoup(content, "lxml")

    def indices_diff(self):
        indices = []
        indices_table = self.__soup.find("table", {"class" : "table_indices_diff"})

        if indices_table is not None:
            for row in indices_table.findAll('tr'):
                tds = row.findAll('td')
                if len(tds) > 0:
                    text = tds[0].getText().strip()
                    category = text[0:text.index(' in ')]
                    diff_type = 'higher' if text.find('lower') == -1 else 'lower'
                    text = text[0:text.index('%')][::-1]
                    percentage = text[0:text.index(' ')][::-1]
                    indices.append({
                        'category': category,
                        'diff_type': diff_type,
                        'percentage': float(percentage),
                    })

        return indices
