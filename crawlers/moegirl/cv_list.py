import json

from lib.data.convert import class_to_json
from lib.data.indices import PageIndex
from lib.path import indices_root
from lib.sites import wikipedia_ja, moegirl


def crawl(category):
    target_fp = indices_root / f'{category}.txt'
    site = moegirl()
    with open(target_fp, 'w') as f:
        for p in site.categories[category]:
            title = p.name
            if title.startswith("Category:"):
                continue
            print(category, title)
            item = PageIndex(title=title, source=site.host)
            json.dump(class_to_json(item), f)
            f.write("\n")

def main():
    # crawl('声优')
    # crawl('VOCALOID声音提供者')
    crawl('虚拟UP主')

if __name__ == '__main__':
    main()
