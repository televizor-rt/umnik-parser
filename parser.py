import re

import requests
from bs4 import BeautifulSoup
import csv

USER_AGENT = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}


def write_res(res):
    with open('dataframe.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(res)


def parse(link, container_selector, question_selector, answer_selector):
    response = requests.get(link, headers=USER_AGENT)
    soup = BeautifulSoup(response.content, "html.parser")
    if container_selector:
        container = soup.select(container_selector)
        for elem in container:
            question = elem.select(question_selector)
            if not question:
                continue
            question = question[0].getText().strip()
            question = re.sub("^\s+|\n|\r|\s+$", '', question)
            answer = elem.select(answer_selector)[0].getText().strip()
            answer = re.sub("^\s+|\n|\r|\s+$", '', answer)
            write_res([question, answer, link])
    else:
        questions = soup.select(question_selector)
        answers = soup.select(answer_selector)
        for i in range(len(questions)):
            question = questions[i].getText().strip()
            question = re.sub("^\s+|\n|\r|\s+$", '', question)
            answer = answers[i].getText().strip()
            answer = re.sub("^\s+|\n|\r|\s+$", '', answer)
            write_res([question, answer, link])
    print('OK')


if __name__ == '__main__':
    parse(
        'https://www.topsecret.com.ru/ru-RU/faq',
        '.panel-default',
        '.panel-heading',
        '.panel-collapse'

    )
    parse(
        'https://zarina.ru/help/',
        '.faqAccordion__section-item',
        '.faqAccordion__section-itemQuestion',
        '.faqAccordion__section-itemAnswer'

    )
    parse(
        'https://skinbutik.ru/faq/',
        '[itemprop="mainEntity"]',
        '[itemprop="name"]',
        '[itemprop="acceptedAnswer"]'
    )
    parse(
        'https://dtmskin.com/about/faq/',
        '.b-expand__item',
        '.b-expand__header',
        '.b-expand__content'
    )
    parse(
        'https://spasiboshop.org/about/faq/',
        '.questions li',
        '.quest',
        '.answ'
    )
    parse(
        'https://shop.atributika.ru/pomoshch/',
        '.b-accordion__item',
        '.b-accordion__title',
        '.b-accordion__content'
    )
    parse(
        'https://www.baldinini-shop.com/ru_ru/faq/',
        '.faq-item',
        '.question',
        '.answer'
    )
    parse(
        'https://befree.ru/faq',
        False,
        '.Faq__Question-sc-1o73cmu-4',
        '.Faq__Answer-sc-1o73cmu-5',
    )
    parse(
        'https://logosait.ru/articles/ecomm-faq',
        '.predl li',
        'h5',
        'p'
    )
    parse(
        'https://sell.aliexpress.com/ru/__pc/join-aliexpress-faq.htm',
        '.seller-ru-faq__item',
        '.seller-ru-faq__question',
        '.seller-ru-faq__answer'
    )
    parse(
        'https://multivarka.pro/about/faq/',
        '.faq-item',
        '.faq-item-question',
        '.faq-item-answer-block'
    )
    parse(
        'https://metallprofil.ru/shop/pokupatelyam/faq/',
        False,
        '.accordion__header',
        '.accordion__content'
    )


