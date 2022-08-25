# Requisito 12
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_tag, search_by_category
from tech_news.analyzer.ratings import top_5_categories, top_5_news
import sys


def check_if_option_is_valid(option):
    range_options = range(0, 8)
    if(not option.isnumeric() or int(option) not in range_options):
        print("Opção inválida", file=sys.stderr)
        return 'error'
    else:
        return


def option_0():
    number = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(number)


def option_1():
    title = input("Digite o título:")
    return search_by_title(title)


def option_2():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def option_3():
    tag = input("Digite a tag:")
    return search_by_tag(tag)


def option_4():
    category = input("Digite a categoria:")
    return search_by_category(category)


def analyzer_menu():
    """Seu código deve vir aqui"""
    input_messages = [
        'Selecione uma das opções a seguir:\n',
        '0 - Popular o banco com notícias;\n',
        '1 - Buscar notícias por título;\n',
        '2 - Buscar notícias por data;\n',
        '3 - Buscar notícias por tag;\n',
        '4 - Buscar notícias por categoria;\n',
        '5 - Listar top 5 notícias;\n',
        '6 - Listar top 5 categorias;\n',
        '7 - Sair.'
    ]

    options = {
        '0': option_0,
        '1': option_1,
        '2': option_2,
        '3': option_3,
        '4': option_4,
        '5': top_5_news,
        '6': top_5_categories,
    }

    while True:
        selection = input(" ".join(input_messages))

        check_option = check_if_option_is_valid(selection)
        if check_option:
            return check_option
        if selection == '7':
            print('Encerrando script')
            break
        else:
            return options[selection]()
